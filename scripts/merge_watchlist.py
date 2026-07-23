#!/usr/bin/env python3
"""Union-merge watchlist entries that landed on origin/main during the scan.

The scan rewrites data/watchlist.json wholesale (to reflect band/funding/status
overrides), so a user add committed mid-scan via api/add would be silently
dropped — and the later rebase would conflict. Run after `git fetch origin main`,
before committing.
"""
import json
import subprocess


def _load_local() -> list:
    try:
        with open("data/watchlist.json") as f:
            d = json.load(f)
            return d if isinstance(d, list) else []
    except Exception:
        return []


def _load_remote() -> list:
    try:
        raw = subprocess.run(
            ["git", "show", "origin/main:data/watchlist.json"],
            capture_output=True, text=True, check=True,
        ).stdout
        d = json.loads(raw)
        return d if isinstance(d, list) else []
    except Exception:
        return []


def main():
    local = _load_local()
    ids = {e.get("id") or e.get("url") for e in local}
    added = [e for e in _load_remote() if (e.get("id") or e.get("url")) not in ids]
    if added:
        with open("data/watchlist.json", "w") as f:
            json.dump(local + added, f, indent=2)
        print(f"[merge_watchlist] merged {len(added)} entr(ies) added mid-scan")
    else:
        print("[merge_watchlist] nothing to merge")


if __name__ == "__main__":
    main()
