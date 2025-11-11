# AEO Assessment Tool

> Free AI Engine Optimization (AEO) assessments - See how AI engines like ChatGPT, Claude, Gemini, and Perplexity understand your company.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115.0-009688.svg)](https://fastapi.tiangolo.com)

## What is AEO?

**AEO (AI Engine Optimization)** is how companies ensure AI assistants like ChatGPT, Claude, Gemini, and Perplexity accurately understand, cite, and recommend them in answers.

As users shift from Google to AI for research, being visible *inside* AI-generated answers—with proper citations—is becoming critical for brand awareness, trust, and lead generation.

## What This Tool Does

This tool generates comprehensive AEO assessment reports that identify:

- ✅ **Current State**: What AI engines already know about your company
- 🚫 **Limitations**: Specific blockers preventing AI citations
- 💡 **Recommendations**: Concrete steps to improve AEO
- ⚠️ **Anti-patterns**: Harmful patterns to fix
- 📅 **Action Plan**: Prioritized 30-45 day roadmap
- 📈 **Success Metrics**: How to measure improvements

## Features

- **Multiple LLM Providers**: Gemini (default), OpenAI, Anthropic, Perplexity
- **Web Search Integration**: AI models research companies in real-time
- **Beautiful Reports**: Clean, professional HTML output
- **Zero Dependencies**: No database, queue, or Redis needed (MVP)
- **Easy Deployment**: Single Docker container or Python
- **Open Source**: Fork, customize, extend

## Quick Start

### Prerequisites

- Python 3.11+
- API key for at least one LLM provider (Gemini recommended)

### Installation

1. **Clone the repository**

```bash
git clone https://github.com/lestarr/AEO.git
cd AEO
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Configure environment**

```bash
cp .env.example .env
```

Edit `.env` and add your API key:

```env
ACTIVE_LLM_PROVIDER=gemini
GEMINI_API_KEY=your_actual_api_key_here
```

4. **Run the application**

```bash
uvicorn app.main:app --reload
```

5. **Open in browser**

Navigate to: http://localhost:8000

## Using Different LLM Providers

### Gemini (Default)

```env
ACTIVE_LLM_PROVIDER=gemini
GEMINI_API_KEY=your_key_here
GEMINI_MODEL=gemini-2.0-flash-exp
```

Get API key: https://makersuite.google.com/app/apikey

### OpenAI

```env
ACTIVE_LLM_PROVIDER=openai
OPENAI_API_KEY=your_key_here
OPENAI_MODEL=gpt-4o
```

Get API key: https://platform.openai.com/api-keys

For reasoning models:
```env
OPENAI_MODEL=o1-preview
```

### Anthropic Claude

```env
ACTIVE_LLM_PROVIDER=anthropic
ANTHROPIC_API_KEY=your_key_here
ANTHROPIC_MODEL=claude-3-7-sonnet-20250219
```

Get API key: https://console.anthropic.com/

### Perplexity

```env
ACTIVE_LLM_PROVIDER=perplexity
PERPLEXITY_API_KEY=your_key_here
PERPLEXITY_MODEL=sonar-pro
```

Get API key: https://www.perplexity.ai/settings/api

## Docker Deployment

### Build and run

```bash
docker build -t aeo-assessment .
docker run -p 8000:8000 --env-file .env aeo-assessment
```

### Using Docker Compose

Create `docker-compose.yml`:

```yaml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "8000:8000"
    env_file:
      - .env
    restart: unless-stopped
```

Run:

```bash
docker-compose up -d
```

## Deployment to Production

### Render

1. Fork this repository
2. Create new Web Service on [Render](https://render.com)
3. Connect your GitHub repo
4. Set environment variables in Render dashboard
5. Deploy!

### Railway

```bash
railway login
railway init
railway up
```

Add environment variables in Railway dashboard.

### Fly.io

```bash
fly launch
fly secrets set ACTIVE_LLM_PROVIDER=gemini
fly secrets set GEMINI_API_KEY=your_key
fly deploy
```

### Self-hosted VPS

```bash
# Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh

# Clone and run
git clone https://github.com/lestarr/AEO.git
cd AEO
cp .env.example .env
# Edit .env with your keys
docker-compose up -d
```

## Project Structure

```
AEO/
├── app/
│   ├── main.py              # FastAPI application
│   ├── config.py            # Configuration management
│   ├── agents/              # LLM agent implementations
│   │   ├── base.py          # Base agent interface
│   │   ├── gemini.py        # Gemini agent
│   │   ├── openai.py        # OpenAI agent
│   │   ├── anthropic.py     # Anthropic agent
│   │   └── perplexity.py    # Perplexity agent
│   └── templates/           # HTML templates
│       ├── base.html        # Base template
│       ├── index.html       # Landing page
│       └── report.html      # Assessment report
├── prompts/
│   └── aeo_narrative.txt    # Assessment prompt template
├── example_prompts/         # Additional prompt templates
├── requirements.txt         # Python dependencies
├── Dockerfile              # Docker configuration
├── .env.example            # Environment template
├── PRD_MVP.md             # MVP Product Requirements
├── PRD_PRODUCTION.md      # Production roadmap
└── README.md              # This file
```

## How It Works

1. **User Input**: Enter company name in web form
2. **LLM Research**: Selected AI model searches the web for company info
3. **Analysis**: Model evaluates entity presence, sourceability, gaps
4. **Report Generation**: Structured assessment with recommendations
5. **Display**: Clean HTML report with actionable insights

## API Endpoints

- `GET /` - Landing page / report display
- `POST /assess` - Generate assessment (form submit)
- `GET /health` - Health check
- `GET /reset` - Clear last assessment (testing)

## Configuration Options

All settings in `.env`:

| Variable | Options | Default | Description |
|----------|---------|---------|-------------|
| `ACTIVE_LLM_PROVIDER` | gemini, openai, anthropic, perplexity | gemini | Which LLM to use |
| `DEBUG` | true, false | false | Enable debug mode |
| `GEMINI_API_KEY` | string | - | Google AI API key |
| `OPENAI_API_KEY` | string | - | OpenAI API key |
| `ANTHROPIC_API_KEY` | string | - | Anthropic API key |
| `PERPLEXITY_API_KEY` | string | - | Perplexity API key |
| `*_MODEL` | string | see .env.example | Model identifier |

## Development

### Install dev dependencies

```bash
pip install -r requirements.txt
pip install pytest black ruff
```

### Run tests

```bash
pytest
```

### Format code

```bash
black app/
ruff check app/
```

### Local development

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## Roadmap

See [PRD_PRODUCTION.md](PRD_PRODUCTION.md) for the full production roadmap.

**Coming Soon:**
- ✅ Email capture for lead generation
- ✅ PostgreSQL database for report history
- ✅ Redis queue for background processing
- ✅ User accounts and dashboard
- ✅ PDF report export
- ✅ Admin panel with analytics
- ✅ Multiple assessment types (SEO, detailed AEO)
- ✅ API access

## Contributing

Contributions welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

- 📖 [Documentation](./PRD_MVP.md)
- 🐛 [Report Issues](https://github.com/lestarr/AEO/issues)
- 💬 [Discussions](https://github.com/lestarr/AEO/discussions)

## Acknowledgments

- Built with [FastAPI](https://fastapi.tiangolo.com)
- LLM orchestration with [pydantic-ai](https://github.com/pydantic/pydantic-ai)
- UI styling with [Tailwind CSS](https://tailwindcss.com)

## About

Created by [@lestarr](https://github.com/lestarr)

Part of the Modern Marketing toolkit for SEO + AEO optimization.

---

**⭐ Star this repo if you find it useful!**
