# PRD: AEO Assessment Tool - MVP

## Overview
Ultra-lightweight demo service that generates AEO (AI Engine Optimization) assessment reports for companies. Users input a company name, receive a comprehensive HTML report.

## Goals
- Create shareable demo for GitHub
- Generate leads through valuable free assessment
- Showcase AEO assessment methodology
- Minimal deployment complexity

## Non-Goals (MVP)
- User authentication
- Database storage
- Email delivery
- Queue system
- Multiple assessment types
- User-facing LLM selection

## User Story
1. User visits site
2. Enters company name in simple form
3. Clicks "Generate Assessment"
4. Sees loading screen (2-5 min)
5. Views comprehensive HTML report
6. Can copy/share URL (report in page)

## Technical Stack

### Core
- **Framework:** FastAPI (Python 3.11+)
- **LLM Library:** pydantic-ai
- **Frontend:** HTML + Tailwind CSS (CDN) + minimal vanilla JS
- **Template Engine:** Jinja2

### LLM Providers (Admin-configured)
- **Gemini** (default) - google-generativeai
- **OpenAI** - openai (use responses API)
- **Anthropic** - anthropic-sdk
- **Perplexity** - openai-compatible API

### Deployment
- Single Docker container OR
- Direct Python deployment (uvicorn)
- Environment variables for API keys
- No external dependencies (DB/Redis)

## Architecture

```
┌─────────────┐
│   Browser   │
└──────┬──────┘
       │ HTTP
       ▼
┌─────────────────────────────┐
│      FastAPI Server         │
│  ┌────────────────────────┐ │
│  │  Web Routes            │ │
│  │  - GET  /              │ │
│  │  - POST /assess        │ │
│  └────────────────────────┘ │
│  ┌────────────────────────┐ │
│  │  Assessment Engine     │ │
│  │  - Load prompts        │ │
│  │  - Execute via         │ │
│  │    pydantic-ai         │ │
│  │  - Format results      │ │
│  └────────────────────────┘ │
│  ┌────────────────────────┐ │
│  │  LLM Agents            │ │
│  │  - Gemini (default)    │ │
│  │  - OpenAI              │ │
│  │  - Anthropic           │ │
│  │  - Perplexity          │ │
│  └────────────────────────┘ │
└─────────────────────────────┘
       │
       ▼
┌─────────────────────────────┐
│    LLM Provider APIs        │
│  - Web search enabled       │
│  - Extended thinking        │
└─────────────────────────────┘
```

## File Structure

```
/
├── app/
│   ├── main.py                 # FastAPI app entry point
│   ├── config.py               # Settings & API keys
│   ├── agents/
│   │   ├── __init__.py
│   │   ├── base.py            # Base agent interface
│   │   ├── gemini.py          # Gemini agent
│   │   ├── openai.py          # OpenAI agent
│   │   ├── anthropic.py       # Anthropic agent
│   │   └── perplexity.py      # Perplexity agent
│   ├── assessment.py           # Core assessment logic
│   └── templates/
│       ├── index.html         # Landing page form
│       └── report.html        # Assessment report template
├── prompts/
│   └── aeo_narrative.txt      # Converted from prompt_AEO_report.md
├── requirements.txt
├── Dockerfile
├── .env.example
├── README.md
└── PRD_MVP.md
```

## Key Features

### 1. Landing Page
- Clean, professional design
- Single input field: "Company Name"
- Submit button: "Generate AEO Assessment"
- Brief explanation of what AEO is
- Example: "Try: Stripe" or "Try: IntraFind Software AG"
- Footer: GitHub link, your contact

### 2. Assessment Process
- Show loading indicator with estimated time
- Use SSE (Server-Sent Events) for progress updates:
  - "Researching company..."
  - "Analyzing entity presence..."
  - "Evaluating sourceability..."
  - "Generating recommendations..."
- Non-blocking (async FastAPI)

### 3. Report Display
- Rendered HTML with sections from prompt_AEO_report.md:
  - Snapshot: what the engines can already see
  - The catch: what limits inclusion
  - What "good" looks like
  - Anti-patterns to stop or fix
  - 30-45 day plan
  - How we'll measure success
- Clean typography
- Inline citations as links
- Copy report URL feature
- "Generate Another Assessment" button

### 4. Configuration
- `.env` file for API keys:
  ```
  ACTIVE_LLM_PROVIDER=gemini
  GEMINI_API_KEY=xxx
  OPENAI_API_KEY=xxx
  ANTHROPIC_API_KEY=xxx
  PERPLEXITY_API_KEY=xxx
  ```
- Admin can switch provider by changing env var

## Implementation Details

### Assessment Flow
1. User submits company name
2. Backend loads `prompts/aeo_narrative.txt`
3. Inject company name into prompt template
4. Select configured LLM provider
5. Execute with pydantic-ai:
   - Enable web search/browsing
   - Use thinking mode if available (OpenAI)
   - Stream response
6. Format response as HTML
7. Return rendered template

### LLM Agent Requirements
Each agent implements:
- `assess(company_name: str, prompt: str) -> AssessmentResult`
- Web search capability enabled
- Streaming support (optional for MVP)
- Error handling with fallback

### pydantic-ai Integration
```python
from pydantic_ai import Agent

class AssessmentResult(BaseModel):
    snapshot: str
    limitations: str
    recommendations: str
    anti_patterns: str
    action_plan: str
    metrics: str

agent = Agent(
    model='gemini-1.5-pro',
    system_prompt=load_prompt(),
    result_type=AssessmentResult
)

result = await agent.run(company_name)
```

## Success Metrics (Post-Launch)
- Assessments generated
- GitHub stars
- Inbound leads (via contact)
- Report shares (trackable via short URLs)

## Out of Scope (MVP)
- ❌ User accounts
- ❌ Assessment history
- ❌ Email capture
- ❌ PDF export
- ❌ Database
- ❌ Queue system
- ❌ Rate limiting (rely on hosting platform)
- ❌ SEO/Nice-to-Have assessments
- ❌ Custom report branding

## Deployment Guide

### Option 1: Docker
```bash
docker build -t aeo-assessment .
docker run -p 8000:8000 --env-file .env aeo-assessment
```

### Option 2: Direct Python
```bash
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

### Hosting Platforms (Free Tier)
- **Render** - Easy Docker deployment
- **Railway** - Git push to deploy
- **Fly.io** - Global edge deployment
- **Google Cloud Run** - Serverless containers

## Timeline
- Setup & structure: 30 min
- LLM agents implementation: 1-2 hours
- Frontend templates: 1 hour
- Testing & refinement: 1 hour
- **Total: 3-4 hours**

## Future Migration Path
See `PRD_PRODUCTION.md` for:
- Email capture & lead management
- Redis queue for background processing
- PostgreSQL for storage
- User accounts & history
- Analytics dashboard
