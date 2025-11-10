# PRD: AEO Assessment Tool - Production Version

## Overview
Enterprise-ready AEO assessment platform with lead capture, background processing, user accounts, and comprehensive analytics. Designed for embedding on marketing websites and generating qualified leads.

## Goals
- Capture qualified leads via valuable free assessments
- Scale to 100+ assessments/day
- Provide professional, shareable reports
- Track user engagement and conversion funnel
- Support multiple assessment types
- Build report history for returning users

## User Stories

### First-Time Visitor
1. Lands on assessment page
2. Enters company name + email
3. Receives confirmation email with tracking link
4. Gets notified when report is ready (3-5 min)
5. Views report, downloads PDF
6. Optionally creates account to save report

### Returning User
1. Logs in with email
2. Views assessment history
3. Runs new assessments
4. Compares reports over time
5. Exports data

### Admin/Marketing User
1. Accesses admin dashboard
2. Views lead funnel metrics
3. Sees popular companies assessed
4. Exports leads to CRM
5. Monitors system health

## Technical Stack

### Core
- **Framework:** FastAPI (Python 3.11+)
- **LLM Library:** pydantic-ai
- **Database:** PostgreSQL 15+
- **Cache/Queue:** Redis 7+
- **Task Queue:** Celery
- **Frontend:** HTMX + Tailwind CSS + Alpine.js
- **Template Engine:** Jinja2
- **Email:** SendGrid / Resend
- **Auth:** FastAPI-Users
- **ORM:** SQLAlchemy 2.0

### Infrastructure
- **App Server:** Gunicorn + Uvicorn workers
- **Queue Workers:** Celery workers (2-4 instances)
- **Storage:** S3-compatible for PDFs
- **Monitoring:** Sentry + Prometheus
- **Analytics:** PostHog / Plausible

## Architecture

```
┌─────────────────────┐
│   Browser / Web     │
└──────────┬──────────┘
           │
           ▼
┌──────────────────────────────────────────┐
│         Load Balancer / CDN              │
└──────────────────────────────────────────┘
           │
           ▼
┌──────────────────────────────────────────┐
│          FastAPI App Servers             │
│  ┌────────────────────────────────────┐  │
│  │  Web Routes                        │  │
│  │  - GET  /                          │  │
│  │  - POST /assess                    │  │
│  │  - GET  /report/{id}               │  │
│  │  - GET  /login, /signup            │  │
│  │  - GET  /dashboard                 │  │
│  │  - GET  /admin                     │  │
│  └────────────────────────────────────┘  │
└──────────────────────────────────────────┘
           │
           ├──────────────────┬─────────────────┐
           ▼                  ▼                 ▼
┌─────────────────┐  ┌──────────────┐  ┌──────────────┐
│   PostgreSQL    │  │    Redis     │  │   S3/Blob    │
│   - Users       │  │  - Sessions  │  │  - PDF files │
│   - Reports     │  │  - Job queue │  │  - Assets    │
│   - Assessments │  │  - Cache     │  └──────────────┘
└─────────────────┘  └──────┬───────┘
                            │
                            ▼
                   ┌──────────────────┐
                   │ Celery Workers   │
                   │ - Run LLM agents │
                   │ - Generate PDFs  │
                   │ - Send emails    │
                   └────────┬─────────┘
                            │
                            ▼
                   ┌──────────────────┐
                   │  LLM APIs        │
                   │  Email Service   │
                   └──────────────────┘
```

## Database Schema

```sql
-- Users
CREATE TABLE users (
    id UUID PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    name VARCHAR(255),
    hashed_password VARCHAR(255),
    is_active BOOLEAN DEFAULT true,
    is_verified BOOLEAN DEFAULT false,
    created_at TIMESTAMP DEFAULT NOW(),
    last_login TIMESTAMP
);

-- Assessments
CREATE TABLE assessments (
    id UUID PRIMARY KEY,
    user_id UUID REFERENCES users(id),
    company_name VARCHAR(255) NOT NULL,
    company_website VARCHAR(500),
    status VARCHAR(50) NOT NULL, -- pending, processing, completed, failed
    llm_provider VARCHAR(50) NOT NULL, -- gemini, openai, anthropic, perplexity
    assessment_type VARCHAR(50) DEFAULT 'aeo_narrative',

    -- Results (JSONB for flexibility)
    result_data JSONB,

    -- Metadata
    ip_address INET,
    user_agent TEXT,
    processing_time_seconds INT,
    error_message TEXT,

    -- Files
    pdf_url VARCHAR(500),
    html_content TEXT,

    created_at TIMESTAMP DEFAULT NOW(),
    started_at TIMESTAMP,
    completed_at TIMESTAMP,

    INDEX idx_user_assessments (user_id, created_at DESC),
    INDEX idx_company (company_name),
    INDEX idx_status (status)
);

-- Email tracking
CREATE TABLE email_events (
    id UUID PRIMARY KEY,
    assessment_id UUID REFERENCES assessments(id),
    email VARCHAR(255) NOT NULL,
    event_type VARCHAR(50), -- sent, opened, clicked
    event_data JSONB,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Lead scoring
CREATE TABLE leads (
    id UUID PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    company_name VARCHAR(255),
    first_assessment_date TIMESTAMP,
    total_assessments INT DEFAULT 1,
    last_assessment_date TIMESTAMP,
    has_account BOOLEAN DEFAULT false,
    lead_score INT DEFAULT 0,
    source VARCHAR(100), -- website, github, linkedin
    utm_campaign VARCHAR(255),
    utm_source VARCHAR(255),
    utm_medium VARCHAR(255),
    created_at TIMESTAMP DEFAULT NOW(),

    INDEX idx_lead_score (lead_score DESC)
);
```

## Key Features

### 1. Enhanced Landing Page
- Hero section with value proposition
- "See how AI sees your company"
- Trust signals (reports generated, companies assessed)
- Sample report preview
- Form: Company Name + Email + (optional) Website URL
- GDPR-compliant consent checkbox
- reCAPTCHA integration

### 2. Email Capture & Verification
- **Pre-assessment:** Collect email before queuing
- Send verification code (optional) or magic link
- Store email + company in DB with pending status
- Allow guest assessments (email required for full report)

### 3. Background Processing
- POST /assess creates job in Redis queue
- Return job ID + polling endpoint
- Celery worker picks up job:
  1. Update status to "processing"
  2. Run LLM assessment (3-5 min)
  3. Generate HTML report
  4. Create PDF version
  5. Upload PDF to S3
  6. Send email notification with report link
  7. Update status to "completed"

### 4. Email Notifications
**Assessment Ready Email:**
```
Subject: Your AEO Assessment for [Company] is Ready

Hi there,

Your AI Engine Optimization assessment for [Company Name] is complete!

View Report: [Unique link]

Key Findings:
- [Teaser stat 1]
- [Teaser stat 2]
- [Teaser stat 3]

The full report includes:
✓ How AI engines currently see your company
✓ Specific gaps limiting your visibility
✓ 30-45 day action plan
✓ Success metrics and targets

[View Full Report Button]

Want to track your progress? Create an account to:
- Save your assessment history
- Run follow-up assessments
- Compare improvements over time

[Create Free Account]

Questions? Reply to this email.

Best,
[Your Name/Company]
```

### 5. Report Pages
- **Public URL:** `/report/{uuid}`
  - Accessible without login if you have link
  - Watermarked with generation date
  - Social sharing meta tags
- **User Dashboard:** See all reports
- **PDF Download:** Branded PDF with charts
- **Share Options:** Copy link, LinkedIn, Twitter

### 6. User Accounts (Optional)
- Email/password signup
- Magic link login
- OAuth (Google, GitHub) optional
- Dashboard showing:
  - Assessment history
  - Date + company + status
  - Download PDFs
  - Re-run assessments (rate limited)

### 7. Admin Dashboard
**Metrics:**
- Total assessments (last 24h / 7d / 30d)
- New leads captured
- Conversion rate (email → account)
- Top companies assessed
- LLM provider usage & costs
- Average processing time
- Success/failure rates

**Lead Management:**
- Search/filter leads
- Export to CSV
- Mark as contacted
- Add notes
- CRM sync button (webhook)

**System Health:**
- Queue length
- Worker status
- API key quotas
- Error logs

### 8. Rate Limiting & Anti-Abuse
- **Anonymous:** 1 assessment per IP per 24h
- **With Email:** 2 assessments per 24h
- **Registered Users:** 5 assessments per 24h
- **Premium (future):** Unlimited

### 9. Analytics & Tracking
- Track user journey:
  - Landing → Form submission → Email open → Report view
- Heatmaps on reports (what sections read)
- UTM parameter tracking
- PostHog/GA4 integration

### 10. Multiple Assessment Types
- **AEO Narrative** (MVP default)
- **AEO Must Have** (detailed checklist)
- **SEO Must Have** (future)
- **Combined SEO+AEO** (future)

Users select type in form or URL param: `/?type=aeo_narrative`

## Configuration

```python
# config.py
class Settings(BaseSettings):
    # Database
    DATABASE_URL: str

    # Redis
    REDIS_URL: str

    # LLM Providers
    ACTIVE_LLM_PROVIDER: str = "gemini"
    GEMINI_API_KEY: str
    OPENAI_API_KEY: str
    ANTHROPIC_API_KEY: str
    PERPLEXITY_API_KEY: str

    # Email
    SENDGRID_API_KEY: str
    FROM_EMAIL: str

    # Storage
    S3_BUCKET: str
    S3_ACCESS_KEY: str
    S3_SECRET_KEY: str

    # Security
    SECRET_KEY: str
    RECAPTCHA_SECRET: str

    # Limits
    MAX_ASSESSMENTS_PER_IP_DAILY: int = 1
    MAX_ASSESSMENTS_PER_EMAIL_DAILY: int = 2

    # Features
    REQUIRE_EMAIL_VERIFICATION: bool = False
    ENABLE_USER_ACCOUNTS: bool = True

    class Config:
        env_file = ".env"
```

## File Structure

```
/
├── app/
│   ├── main.py
│   ├── config.py
│   ├── database.py
│   ├── models/
│   │   ├── user.py
│   │   ├── assessment.py
│   │   └── lead.py
│   ├── agents/
│   │   ├── base.py
│   │   ├── gemini.py
│   │   ├── openai.py
│   │   ├── anthropic.py
│   │   └── perplexity.py
│   ├── services/
│   │   ├── assessment_service.py
│   │   ├── email_service.py
│   │   ├── pdf_service.py
│   │   └── lead_service.py
│   ├── workers/
│   │   └── celery_app.py
│   ├── routers/
│   │   ├── public.py
│   │   ├── auth.py
│   │   ├── dashboard.py
│   │   └── admin.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── landing.html
│   │   ├── report.html
│   │   ├── dashboard.html
│   │   ├── admin.html
│   │   └── emails/
│   │       ├── assessment_ready.html
│   │       └── welcome.html
│   └── static/
│       ├── css/
│       ├── js/
│       └── images/
├── migrations/
│   └── alembic/
├── prompts/
│   ├── aeo_narrative.txt
│   ├── aeo_must_have.txt
│   └── seo_must_have.txt
├── tests/
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── celeryconfig.py
├── .env.example
├── README.md
├── PRD_MVP.md
└── PRD_PRODUCTION.md
```

## API Endpoints

### Public
- `GET /` - Landing page
- `POST /api/assess` - Submit assessment (requires email)
- `GET /api/assess/{id}` - Poll status
- `GET /report/{uuid}` - View report
- `GET /api/report/{uuid}/pdf` - Download PDF

### Authenticated
- `POST /auth/register`
- `POST /auth/login`
- `GET /auth/logout`
- `GET /dashboard` - User dashboard
- `GET /api/assessments` - List user's assessments

### Admin
- `GET /admin` - Admin dashboard
- `GET /api/admin/leads` - Export leads
- `GET /api/admin/metrics` - System metrics
- `POST /api/admin/config` - Update settings

## Deployment

### Docker Compose (Development)
```yaml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "8000:8000"
    env_file: .env
    depends_on:
      - postgres
      - redis
    volumes:
      - ./app:/app
    command: uvicorn app.main:app --reload --host 0.0.0.0

  worker:
    build: .
    env_file: .env
    depends_on:
      - postgres
      - redis
    command: celery -A app.workers.celery_app worker --loglevel=info

  postgres:
    image: postgres:15
    environment:
      POSTGRES_DB: aeo_assessment
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"

volumes:
  postgres_data:
```

### Production Hosting Options

**Option 1: Single VPS (Hetzner/DigitalOcean)**
- Docker Compose on VPS ($5-10/mo)
- Managed Postgres (Supabase/Neon) - Free tier
- Managed Redis (Upstash) - Free tier
- Cloudflare for CDN/SSL

**Option 2: Platform-as-a-Service**
- **App:** Render/Railway ($7-15/mo)
- **Workers:** Background worker instances
- **DB:** Built-in Postgres
- **Redis:** Built-in Redis

**Option 3: Cloud-Native (AWS/GCP)**
- App: Cloud Run / ECS
- DB: RDS / Cloud SQL
- Queue: ElastiCache Redis
- Storage: S3 / Cloud Storage
- Cost: ~$20-50/mo initially

## Migration Path from MVP

1. **Phase 1: Add Database**
   - Keep sync processing
   - Store assessments in Postgres
   - Add report history page

2. **Phase 2: Add Email Capture**
   - Require email for reports
   - Send notification emails
   - Track leads

3. **Phase 3: Add Background Queue**
   - Move to async processing
   - Add Redis + Celery
   - Improve UX with polling

4. **Phase 4: Add User Accounts**
   - Optional signup
   - Dashboard
   - Report history

5. **Phase 5: Add Admin Panel**
   - Lead management
   - Analytics
   - System monitoring

## Success Metrics

### Lead Generation
- **Target:** 50 qualified leads/month
- Email capture rate >70%
- Account creation rate >20%

### Engagement
- Report completion rate >85%
- PDF downloads >40%
- Repeat assessments >15%

### Technical
- 95% uptime
- <5 min processing time
- <2% error rate

### Business
- 10% lead → sales conversation
- $X attributed revenue
- XX GitHub stars

## Cost Estimation

### MVP (Free Tier)
- Hosting: $0 (Render/Railway free tier)
- LLM APIs: ~$0.10-0.50 per assessment
- **Total:** ~$5-25/mo (50 assessments)

### Production (100 assessments/day)
- Hosting: $20-50/mo
- Database: $10-25/mo
- Redis: $5-10/mo
- Email: $0-15/mo (SendGrid free: 100/day)
- LLM APIs: ~$300-500/mo (3,000 assessments)
- Storage: $5/mo
- **Total:** ~$340-615/mo

## Security Considerations
- Rate limiting per IP/email
- reCAPTCHA on form
- SQL injection prevention (SQLAlchemy ORM)
- XSS prevention (Jinja2 auto-escaping)
- CSRF tokens
- Secure password hashing (bcrypt)
- API key rotation
- GDPR compliance (data export/deletion)
- Email verification
- Report URL obfuscation (UUIDs)

## Future Enhancements
- White-label version for agencies
- API access for programmatic assessments
- Slack/Teams integration
- Comparative reports (company vs competitors)
- Historical tracking & trend analysis
- Premium tier with deeper analysis
- Multi-language support
- Custom branding for reports
