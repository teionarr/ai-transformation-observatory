# CODOS Competitive Observatory — scan configuration
#
# Band framing (the AI-transformation / agentic-deployment market):
#   Transformation Titans  → global consultancies & SIs (enterprise scale)
#   Forward Deployers      → AI-native transformation boutiques (Codos's band)
#   Agent Foundries        → horizontal agentic deployment platforms
#   Platform Gravity       → enterprise orchestration / infra you build on
#   Digital Labor          → AI employees / outcomes-as-a-service
#   Vertical Specialists   → function / industry-deep agents

# --- Scan settings ---
EXA_DAYS_BACK = 7          # weekly assurance sweep
EXA_NUM_RESULTS = 20
GEMINI_MODEL = "gemini-2.5-flash"

# Disambiguation context for the monthly site-finder: when a company's site can't
# be crawled, search for its real website and prefer the match in this space.
OBSERVATORY_TOPIC = "AI tools for company memory, knowledge, and transformation"

# Discovery scan — auto-detect new entrants not yet on the board
DISCOVERY_ENABLED = True
DISCOVERY_RELEVANCE_THRESHOLD = 60   # 0-100; Gemini relevance score to auto-add

# --- Bands (the six clusters of the AI-transformation market) ---
# "Other" is a catch-all for players that do not fit the six bands.
CATEGORIES = ["Transformation Titans", "Forward Deployers", "Agent Foundries", "Platform Gravity", "Digital Labor", "Vertical Specialists", "Other"]
STATUSES   = ["Incumbent", "Scaling", "Emerging", "Acquired"]

# --- Competitors (50 players + Codos anchor, from the competitive map) ---
# why = one-line rationale for why the player sits on the board (powers the "why tracked" popup)
COMPETITORS = [
    # ── Forward Deployers — AI-native transformation boutiques (Codos's band) ──
    {"id": "codos", "name": "Codos.ai", "url": "codos.ai", "category": "Forward Deployers", "crawl_paths": ["/", "/product"], "funding": "Stealth / pre-launch", "team": None, "status": "Emerging", "anchor": True,
     "why": "ANCHOR. 'The layer for AI-transformation' — diagnoses, installs and keeps a company evolving on its own, with agents deployed across functions and real outcomes in weeks. Straddles Forward Deployers + Agent Foundries: a continuous-optimization layer, not a one-time project."},
    # ── Transformation Titans — global consultancies & SIs ──
    {"id": "accenture", "name": "Accenture", "url": "accenture.com", "category": "Transformation Titans", "crawl_paths": ["/"], "funding": "Public · $3B Data&AI", "team": None, "status": "Incumbent",
     "why": "Incumbent SI; $3B committed to Data & AI scaling toward ~80k AI specialists; NVIDIA 'AI Refinery'; OpenAI Frontier Alliance. Owns the C-suite transformation relationship at enterprise scale."},
    {"id": "deloitte", "name": "Deloitte", "url": "deloitte.com", "category": "Transformation Titans", "crawl_paths": ["/"], "funding": "Private partnership", "team": None, "status": "Incumbent",
     "why": "Big-Four incumbent driving AI/agentic transformation via NVIDIA alliance and acquisitions; standardized a large workforce on Claude. Consulting-led, project-based economics."},
    {"id": "mckinsey", "name": "McKinsey QuantumBlack", "url": "mckinsey.com", "category": "Transformation Titans", "crawl_paths": ["/"], "funding": "~5,000 AI experts", "team": None, "status": "Incumbent",
     "why": "QuantumBlack AI arm (~5,000 experts); 'rewire the enterprise' with agentic workflows; Frontier Alliance + internal Lilli platform. Strategy-led transformation authority."},
    {"id": "bcgx", "name": "BCG X", "url": "bcg.com", "category": "Transformation Titans", "crawl_paths": ["/"], "funding": "~3,000 technologists", "team": None, "status": "Incumbent",
     "why": "BCG's build arm (~3,000 technologists); ~20% of BCG's $13.5B revenue is AI; OpenAI/Anthropic alliances. Strategy plus working prototypes at enterprise scale."},
    {"id": "bain", "name": "Bain (Vector)", "url": "bain.com", "category": "Transformation Titans", "crawl_paths": ["/"], "funding": "Private · ~18k upskilled", "team": None, "status": "Incumbent",
     "why": "Equipped its ~18,000-person team with AI; dedicated OpenAI Center of Excellence. Strategy-led, enterprise transformation budgets."},
    {"id": "ibmconsulting", "name": "IBM Consulting", "url": "ibm.com", "category": "Transformation Titans", "crawl_paths": ["/"], "funding": "~160k consultants", "team": None, "status": "Incumbent",
     "why": "~160,000 consultants with platform access; model-agnostic Consulting Assistants. Scale delivery of enterprise AI."},
    {"id": "ey", "name": "EY (EY.ai)", "url": "ey.com", "category": "Transformation Titans", "crawl_paths": ["/"], "funding": "~$1.4B EY.ai", "team": None, "status": "Incumbent",
     "why": "~$1.4B EY.ai investment; NVIDIA sovereign agentic platform; 50,000+ internal agents. Agentic transformation across service lines."},
    {"id": "pwc", "name": "PwC", "url": "pwc.com", "category": "Transformation Titans", "crawl_paths": ["/"], "funding": "Private", "team": None, "status": "Incumbent",
     "why": "'agent OS' + agentic managed services, outcomes-based; 200,000-seat ChatGPT Enterprise rollout. Closest Big-Four firm to outcome-priced agent delivery."},
    {"id": "kpmg", "name": "KPMG", "url": "kpmg.com", "category": "Transformation Titans", "crawl_paths": ["/"], "funding": "Multibillion MSFT", "team": None, "status": "Incumbent",
     "why": "Multibillion Microsoft cloud/AI spend; ISO 42001 governance claim; large Claude rollout. Governed enterprise AI transformation."},
    {"id": "capgemini", "name": "Capgemini", "url": "capgemini.com", "category": "Transformation Titans", "crawl_paths": ["/"], "funding": "€2B / 3 yrs", "team": None, "status": "Incumbent",
     "why": "€2B AI investment over three years; Google Cloud Partner of the Year; Frontier Alliance. AI-powered business transformation at scale."},
    {"id": "distyl", "name": "Distyl AI", "url": "distyl.ai", "category": "Forward Deployers", "crawl_paths": ["/"], "funding": "$175M Series B · $1.8B", "team": None, "status": "Scaling",
     "why": "DIRECT. $175M Series B at $1.8B (Sept 2025); 'SEAL Team Six of AI engineering' + Distillery platform; 'Distyl Scans' give an AI-readiness score/roadmap; $100M+ impact, production in weeks. Codos's closest, best-funded peer."},
    {"id": "tribe", "name": "Tribe AI", "url": "tribe.ai", "category": "Forward Deployers", "crawl_paths": ["/"], "funding": "Private · founded ~2019", "team": None, "status": "Scaling",
     "why": "DIRECT. Network of senior applied-AI practitioners, forward-deployed; takes companies to production in weeks; OpenAI/Anthropic founding partner."},
    {"id": "sand", "name": "Sand Technologies", "url": "sandtech.com", "category": "Forward Deployers", "crawl_paths": ["/"], "funding": "Scale-up · 7yr 2x", "team": None, "status": "Scaling",
     "why": "DIRECT. Global AI-native scale-up; seven years of 2x annual growth; enterprise AI + SandOS decision platform across utilities/insurance/healthcare/telecom."},
    {"id": "slalom", "name": "Slalom", "url": "slalom.com", "category": "Forward Deployers", "crawl_paths": ["/"], "funding": "Private", "team": None, "status": "Scaling",
     "why": "DIRECT. AI-readiness assessment to agent-driven workflows; 'AI as a platform of managed agents'; partners Google/Microsoft/Databricks/Salesforce."},
    {"id": "faculty", "name": "Faculty AI", "url": "faculty.ai", "category": "Forward Deployers", "crawl_paths": ["/"], "funding": "Private / VC", "team": None, "status": "Scaling",
     "why": "DIRECT. UK applied-AI / decision-intelligence firm deploying models and agents into operations across government and enterprise."},
    {"id": "neurons", "name": "Neurons Lab", "url": "neurons-lab.com", "category": "Forward Deployers", "crawl_paths": ["/"], "funding": "Boutique", "team": None, "status": "Emerging",
     "why": "DIRECT. Boutique agentic-AI consultancy (UK/Singapore) building agents for regulated BFSI; live in 8–12 weeks."},
    {"id": "devoteam", "name": "Devoteam", "url": "devoteam.com", "category": "Forward Deployers", "crawl_paths": ["/"], "funding": "Public · 11k+", "team": None, "status": "Incumbent",
     "why": "DIRECT. European AI services consultancy (11,000+); 'ADAPT' 4-week prototype program; agentic accelerators across Google/AWS/Microsoft/ServiceNow."},
    {"id": "mechorchard", "name": "Mechanical Orchard", "url": "mechanical-orchard.com", "category": "Forward Deployers", "crawl_paths": ["/"], "funding": "VC-backed", "team": None, "status": "Scaling",
     "why": "Adjacent–Direct. AI-native services modernizing legacy systems with agents ('Cursor for COBOL'); founder Rob Mee (ex-Pivotal)."},
    {"id": "webuildai", "name": "WeBuild-AI", "url": "webuild.ai", "category": "Forward Deployers", "crawl_paths": ["/"], "funding": "Early-stage", "team": None, "status": "Emerging",
     "why": "DIRECT. Early-stage AI-native consultancy embedding AI coding/automation, redesigning org structures and responsible-AI controls."},
    {"id": "multiverse", "name": "Multiverse", "url": "multiverse.io", "category": "Forward Deployers", "crawl_paths": ["/"], "funding": "$70M · $2.1B val", "team": None, "status": "Scaling",
     "why": "Adjacent. The 'AI adoption layer' via upskilling; $70M at $2.1B (May 2026); £2B+ tracked ROI. Bridges people to AI through skills, not deployed agents."},
    # ── Agent Foundries — horizontal agentic deployment platforms ──
    {"id": "sierra", "name": "Sierra", "url": "sierra.ai", "category": "Agent Foundries", "crawl_paths": ["/"], "funding": "$950M Series C · $15.8B", "team": None, "status": "Scaling",
     "why": "Direct–Adjacent. Bret Taylor / Clay Bavor; $950M Series C at $15.8B (May 2026), ~$150M ARR; managed, outcome-priced agents (~$1–2.50/resolution) expanding to 'Agent OS'."},
    {"id": "relevanceai", "name": "Relevance AI", "url": "relevanceai.com", "category": "Agent Foundries", "crawl_paths": ["/"], "funding": "$24M Series B", "team": None, "status": "Scaling",
     "why": "DIRECT. Build an 'AI workforce' / teams of agents, tool- and model-agnostic; 40,000 agents registered in a single month."},
    {"id": "lyzr", "name": "Lyzr", "url": "lyzr.ai", "category": "Agent Foundries", "crawl_paths": ["/"], "funding": "~$14.5M", "team": None, "status": "Emerging",
     "why": "DIRECT. Enterprise 'Agentic OS' for secure, governed agents across operations; ~$14.5M raised."},
    {"id": "lindy", "name": "Lindy", "url": "lindy.ai", "category": "Agent Foundries", "crawl_paths": ["/"], "funding": "VC-backed", "team": None, "status": "Emerging",
     "why": "Adjacent. No-code agent builder (Flo Crivello) for workflow/email/ops automation; SMB–mid-market."},
    {"id": "crewai", "name": "CrewAI", "url": "crewai.com", "category": "Agent Foundries", "crawl_paths": ["/"], "funding": "VC / OSS", "team": None, "status": "Emerging",
     "why": "Adjacent. Open-source multi-agent orchestration framework + enterprise studio; 1,200+ integrations; developer-led."},
    {"id": "beam", "name": "Beam AI", "url": "beam.ai", "category": "Agent Foundries", "crawl_paths": ["/"], "funding": "Early-stage", "team": None, "status": "Emerging",
     "why": "DIRECT. No-code agentic automation (Germany): 'upload your SOP, get a working agent'; live at F500, white-glove setup in weeks."},
    {"id": "stackai", "name": "Stack AI", "url": "stack-ai.com", "category": "Agent Foundries", "crawl_paths": ["/"], "funding": "YC / seed", "team": None, "status": "Emerging",
     "why": "Direct–Adjacent. YC no-code/low-code agent orchestration with on-prem option; democratizes agent building."},
    {"id": "knowlee", "name": "Knowlee", "url": "knowlee.ai", "category": "Agent Foundries", "crawl_paths": ["/"], "funding": "Early-stage", "team": None, "status": "Emerging",
     "why": "DIRECT. EU 'orchestration layer for agentic work' — agent-fleet dashboard, automation registry, multi-vertical."},
    {"id": "aily", "name": "Aily Labs", "url": "aily.com", "category": "Agent Foundries", "crawl_paths": ["/"], "funding": "~$80M", "team": None, "status": "Scaling",
     "why": "DIRECT. 'Super Agent' orchestrating 1,000+ agents for decision intelligence across finance/supply-chain/R&D; ~$80M raised; 1-day integration, P&L outcomes."},
    {"id": "writer", "name": "Writer", "url": "writer.com", "category": "Agent Foundries", "crawl_paths": ["/"], "funding": "~$1.9B val", "team": None, "status": "Scaling",
     "why": "Adjacent. Full-stack enterprise generative-AI platform with agents across functions; ~$1.9B valuation."},
    # ── Platform Gravity — enterprise orchestration / infra ──
    {"id": "agentforce", "name": "Salesforce Agentforce", "url": "salesforce.com", "category": "Platform Gravity", "crawl_paths": ["/"], "funding": "Public (Salesforce)", "team": None, "status": "Incumbent",
     "why": "Adjacent. CRM-native agents (Atlas engine), ~$2/conversation; deploy across service/sales/marketing. The platform enterprises may build on instead of buying a layer."},
    {"id": "copilotstudio", "name": "Microsoft Copilot Studio", "url": "microsoft.com", "category": "Platform Gravity", "crawl_paths": ["/"], "funding": "Public (Microsoft)", "team": None, "status": "Incumbent",
     "why": "Adjacent. Build agents across M365/Dataverse/Azure; $30/user Copilot + credit packs. Owns the enterprise desktop runtime."},
    {"id": "servicenow", "name": "ServiceNow AI Agents", "url": "servicenow.com", "category": "Platform Gravity", "crawl_paths": ["/"], "funding": "Public · bought Moveworks", "team": None, "status": "Incumbent",
     "why": "Adjacent. 'AI control tower', Autonomous Workforce, AI Agent Fabric/Orchestrator; acquired Moveworks ($2.85B). Workflow-platform gravity."},
    {"id": "googlecloud", "name": "Google Cloud (Vertex / delta)", "url": "cloud.google.com", "category": "Platform Gravity", "crawl_paths": ["/"], "funding": "Public (Google)", "team": None, "status": "Incumbent",
     "why": "Adjacent. Vertex AI Agent Builder + Google Cloud Consulting 'delta' team for agentic transformation."},
    {"id": "aws", "name": "AWS Bedrock AgentCore", "url": "aws.amazon.com", "category": "Platform Gravity", "crawl_paths": ["/"], "funding": "Public (Amazon)", "team": None, "status": "Incumbent",
     "why": "Adjacent. Fully-managed services to build/deploy/operate agents at scale, any framework or model."},
    {"id": "koreai", "name": "Kore.ai", "url": "kore.ai", "category": "Platform Gravity", "crawl_paths": ["/"], "funding": "VC-backed", "team": None, "status": "Scaling",
     "why": "Direct–Adjacent. Enterprise multi-agent orchestration across CX/EX/ops with on-prem and governance-first posture."},
    {"id": "c3ai", "name": "C3 AI", "url": "c3.ai", "category": "Platform Gravity", "crawl_paths": ["/"], "funding": "Public", "team": None, "status": "Incumbent",
     "why": "Adjacent. Public C3 Agentic AI Platform + turnkey enterprise apps for manufacturing/energy/financial services."},
    {"id": "glean", "name": "Glean", "url": "glean.com", "category": "Platform Gravity", "crawl_paths": ["/"], "funding": "$150M Series F · $400M+", "team": None, "status": "Scaling",
     "why": "Adjacent. Enterprise search + custom agents that act on context; $150M Series F (2025), $400M+ total."},
    {"id": "oracle", "name": "Oracle OCI Enterprise AI", "url": "oracle.com", "category": "Platform Gravity", "crawl_paths": ["/"], "funding": "Public", "team": None, "status": "Incumbent",
     "why": "Adjacent. OCI Enterprise AI — build/deploy production agents across ERP/HCM/CRM with governance and sovereign options."},
    {"id": "cognigy", "name": "Cognigy (NiCE)", "url": "cognigy.com", "category": "Platform Gravity", "crawl_paths": ["/"], "funding": "Acq. NiCE $955M", "team": None, "status": "Acquired",
     "why": "Adjacent. Enterprise conversational/agentic CX, voice gateway, on-prem; acquired by NiCE ($955M). Incremental upgrade vs rip-and-replace."},
    # ── Digital Labor — AI employees / outcomes-as-a-service ──
    {"id": "elevenx", "name": "11x", "url": "11x.ai", "category": "Digital Labor", "crawl_paths": ["/"], "funding": "~$74M (a16z)", "team": None, "status": "Scaling",
     "why": "Adjacent. 'Digital workers, human results' — Alice (SDR), Julian/Jordan (voice); ~$74M (a16z). (TechCrunch documented disputed traction claims.)"},
    {"id": "artisan", "name": "Artisan", "url": "artisan.co", "category": "Digital Labor", "crawl_paths": ["/"], "funding": "~$37M", "team": None, "status": "Emerging",
     "why": "Adjacent. 'Ava' AI BDR automating outbound; ~$37M raised, ~$5M ARR / ~250 customers (company-stated)."},
    {"id": "decagon", "name": "Decagon", "url": "decagon.ai", "category": "Digital Labor", "crawl_paths": ["/"], "funding": "$250M Series D · $4.5B", "team": None, "status": "Scaling",
     "why": "Adjacent. CX agents, $250M Series D at $4.5B (Jan 2026), ~$35M ARR, 80%+ deflection, outcome/conversation pricing."},
    {"id": "cognition", "name": "Cognition (Devin)", "url": "cognition.ai", "category": "Digital Labor", "crawl_paths": ["/"], "funding": "~$10.2B val", "team": None, "status": "Scaling",
     "why": "Adjacent. Devin, the autonomous AI software engineer; ~$10.2B (targeting ~$25B), ~$492M run-rate; acquired Windsurf; ACU usage pricing."},
    {"id": "moveworks", "name": "Moveworks (ServiceNow)", "url": "moveworks.com", "category": "Digital Labor", "crawl_paths": ["/"], "funding": "Acq. $2.85B", "team": None, "status": "Acquired",
     "why": "Adjacent. Employee-support AI assistant + Reasoning Engine across IT/HR/finance; ~5M users in ~18 months; acquired by ServiceNow ($2.85B)."},
    # ── Vertical Specialists — function / industry-deep agents ──
    {"id": "harvey", "name": "Harvey", "url": "harvey.ai", "category": "Vertical Specialists", "crawl_paths": ["/"], "funding": "$11B val · ~$1.22B", "team": None, "status": "Scaling",
     "why": "Adjacent. Legal AI agents for elite firms/enterprises; $11B valuation, ~$1.22B raised. Deep vertical moat competing for the legal-function budget."},
    {"id": "hippocratic", "name": "Hippocratic AI", "url": "hippocraticai.com", "category": "Vertical Specialists", "crawl_paths": ["/"], "funding": "~$404M · $1.6B val", "team": None, "status": "Scaling",
     "why": "Adjacent. Non-diagnostic healthcare voice agents with a physician safety board; ~$404M raised, ~$1.6B valuation; NVIDIA partner."},
    {"id": "cresta", "name": "Cresta", "url": "cresta.com", "category": "Vertical Specialists", "crawl_paths": ["/"], "funding": "VC-backed", "team": None, "status": "Scaling",
     "why": "Adjacent. Real-time contact-center intelligence running AI + human agents on dual tracks, learning from every call."},
    {"id": "fazeshift", "name": "Fazeshift", "url": "fazeshift.com", "category": "Vertical Specialists", "crawl_paths": ["/"], "funding": "$17M Series A", "team": None, "status": "Emerging",
     "why": "Adjacent. YC; AI agents automating accounts-receivable / order-to-cash as an 'intelligent control layer'; $17M Series A."},
    {"id": "eloquent", "name": "Eloquent AI", "url": "eloquent.ai", "category": "Vertical Specialists", "crawl_paths": ["/"], "funding": "$7.4M seed", "team": None, "status": "Emerging",
     "why": "Adjacent. YC 'AI operator' for regulated financial back-office (disputes, KYC, servicing); learns SOPs and drives apps without APIs; $7.4M seed."},
]

# --- Exa search topics (AI-transformation / agentic-deployment intel) ---
SEARCH_TOPICS = [
    "AI transformation consulting agentic deployment platform funding 2026",
    "enterprise AI agents orchestration platform launch acquisition 2026",
    "outcomes-as-a-service digital labor AI agent per-outcome pricing",
    "AI-native services firm forward-deployed engineers production in weeks",
    "agentic AI enterprise adoption pilot to production GenAI ROI",
]

# Discovery topics — aimed at surfacing NEW entrants, not the tracked set
DISCOVERY_TOPICS = [
    "new AI transformation startup agentic deployment funding 2026",
    "stealth enterprise AI agent platform seed round",
    "AI services firm outcomes-based agents enterprise new company",
]

# --- Data sources (pipeline shown in the dashboard) ---
DATA_SOURCES = [
    {"id": "exa", "name": "Exa.ai", "kind": "neural search", "glyph": "hex"},
    {"id": "firecrawl", "name": "Firecrawl", "kind": "change-tracking scrape", "glyph": "flame"},
    {"id": "gemini", "name": "Gemini 2.5 Flash", "kind": "synthesis", "glyph": "diamond"},
    {"id": "web", "name": "Live Web (Google)", "kind": "grounded search", "glyph": "wave"},
]
