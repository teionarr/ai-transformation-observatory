import hashlib
import time
from datetime import datetime, timezone


class FirecrawlWorker:
    """Detects competitor site changes via Firecrawl change-tracking.

    Firecrawl stores page snapshots server-side (keyed by URL + markdown + tag),
    so change detection needs no local hash state. Each scrape returns a
    changeStatus (new/same/changed/removed) and, when changed, a git-diff.
    """

    DIFF_CHAR_LIMIT = 1500  # cap per-competitor diff fed to Gemini

    # Failures of the crawl infrastructure (billing, auth, throttling) — these say
    # nothing about whether the target site is alive, so they must not produce
    # crawl_status "error" (which the UI renders as the "site?" badge).
    # Account-level markers only — generic HTTP words ("unauthorized", "too many
    # requests") can come from the TARGET site being bot-walled, which is a real
    # site problem, not our infra.
    INFRA_ERROR_MARKERS = (
        "payment required", "credit", "quota", "billing", "rate limit",
        "invalid api key", "invalid token",
    )

    def __init__(self, api_key: str, tag: str = "weekly"):
        from firecrawl import FirecrawlApp
        self.app = FirecrawlApp(api_key=api_key)
        self.tag = tag
        self.call_count = 0  # real scrape calls this run (telemetry)
        self.infra_errors = 0  # scrapes that failed for infra reasons (credits/auth/429)

    def run(self, competitors: list[dict], keep_markdown: bool = False) -> list[dict]:
        results = []

        for comp in competitors:
            print(f"  [firecrawl] scanning {comp['url']}…")
            changed_pages = []
            diffs = []
            display_hash = "—"
            first_markdown = ""
            crawl_ok = False
            infra_fail = False

            for path in comp.get("crawl_paths", ["/", "/product"]):
                url = f"https://{comp['url']}{path}"
                page = self._scrape_page(url)
                if page == "infra":
                    infra_fail = True
                    continue
                if page is None:
                    continue
                crawl_ok = True
                if not first_markdown and page["markdown"]:
                    first_markdown = page["markdown"]

                if display_hash == "—" and page["markdown"]:
                    display_hash = self._display_hash(page["markdown"])

                if page["change_status"] == "changed":
                    changed_pages.append(path)
                    if page["diff_text"]:
                        diffs.append(f"# {path}\n{page['diff_text']}")

                time.sleep(2)  # rate limit: firecrawl free tier

            scanned_at = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M")
            combined_diff = "\n\n".join(diffs)[: self.DIFF_CHAR_LIMIT] if diffs else None

            row = {
                "id": comp["id"],
                "name": comp["name"],
                "url": comp["url"],
                "category": comp["category"],
                "status": comp.get("status", "Emerging"),
                "funding": comp.get("funding", "—"),
                "team": comp.get("team"),
                "why": comp.get("why"),
                "anchor": comp.get("anchor", False),
                "discovered": comp.get("discovered", False),
                "discovered_at": comp.get("discovered_at"),
                "discovery_relevance": comp.get("discovery_relevance"),
                "scanned": scanned_at,
                "hash": display_hash,
                "changed": len(changed_pages) > 0,
                "changed_pages": changed_pages,
                "diff": combined_diff,  # internal — consumed by Gemini, stripped before public snapshot
                "delta": None,          # filled by GeminiWorker
                # "skipped" = the crawl never really happened (credits/auth/429),
                # so we can't say anything about the site — main.py carries the
                # previous status forward for these rows.
                "crawl_status": "success" if crawl_ok else ("skipped" if infra_fail else "error"),
            }
            if keep_markdown:
                # internal — used by the site-finder to verify a guessed domain
                # actually belongs to the company; stripped before the snapshot
                row["_markdown"] = first_markdown[:5000]
            results.append(row)

        return results

    def _scrape_page(self, url: str) -> dict | None:
        self.call_count += 1
        try:
            result = self.app.scrape(
                url,
                formats=[
                    "markdown",
                    {"type": "changeTracking", "modes": ["git-diff"], "tag": self.tag},
                ],
                only_main_content=True,
                wait_for=2000,
            )
        except Exception as e:
            print(f"    [firecrawl] error on {url}: {e}")
            if any(m in str(e).lower() for m in self.INFRA_ERROR_MARKERS):
                self.infra_errors += 1
                return "infra"
            return None

        ct = self._attr(result, "changeTracking")
        diff = self._attr(ct, "diff")
        return {
            "markdown": self._attr(result, "markdown"),
            "change_status": self._attr(ct, "changeStatus"),
            "diff_text": self._attr(diff, "text"),
        }

    @staticmethod
    def _attr(obj, key, default=None):
        """Read a field whether the SDK returns objects or dicts."""
        if obj is None:
            return default
        if isinstance(obj, dict):
            return obj.get(key, default)
        return getattr(obj, key, default)

    @staticmethod
    def _display_hash(markdown: str) -> str:
        """Short content fingerprint — cosmetic only (the 'delta hash' column)."""
        return hashlib.sha256(markdown.encode("utf-8")).hexdigest()[:10]
