## Together: Elixpo Monorepo Project Index

A single, skimmable index for the projects in this monorepo. Jump into any section for details, or open each project’s own README for the full story.

### Quick navigation

| Project | What it is | Path |
|---|---|---|
| Elixpo monorepo overview | Vision, highlights, links | `/` |
| ElixpoAI Art Generator | Web-based AI art studio | `art.elixpo/` |
| Chat site and services | News, podcasts, weather flows | `chat.elixpo/` |
| Chrome Extension | Select text → transform to image | `elixpo-art-chrome-extension/` |
| Inkflow Workspace | Lightweight sketching app | `inkflow/` |
| Discord Bot (Jackey) | Generate/remix images in Discord | `jackey.elixpo/` |
| ML notebooks/workflows | Classifiers and generation | `kaggle_workflow/` |
| Search Agent | Web/YouTube search + synthesis API | `search.elixpo/` |
| Videolize Portfolio | Modern personal portfolio | `solanki.elixpo/` |

### Contents
- [Monorepo overview (root)](#monorepo-overview-root)
- [art.elixpo — ElixpoAI Art Generator](#artelixpo--elixpoai-art-generator)
- [chat.elixpo — Chat site and services](#chatelixpo--chat-site-and-services)
- [elixpo-art-chrome-extension — Chrome Extension](#elixpo-art-chrome-extension--chrome-extension)
- [inkflow — Inkflow Workspace](#inkflow--inkflow-workspace)
- [jackey.elixpo — Elixpo Discord Bot (Jackey)](#jackeyelixpo--elixpo-discord-bot-jackey)
- [kaggle_workflow — ML notebooks and workflows](#kaggle_workflow--ml-notebooks-and-workflows)
- [search.elixpo — Elixpo Search Agent](#searchelixpo--elixpo-search-agent)
- [solanki.elixpo — Videolize Personal Portfolio](#solankielixpo--videolize-personal-portfolio)

---

## Monorepo overview (root)

- Name: Elixpo-art
- Tagline: Your Engine for Personalized Synthetic Media

**Key highlights**
- 100% Open Source, free to use
- No signup or API keys required
- Simple embeds for images and text
- Used by open-source LLMs, bots, and communities
- Hacktoberfest 2024: Contributions welcomed (bug fixes, features, docs)

**Project overview**
AI-powered art generation platform with a robust backend and web UI, leveraging multiple ML models and algorithms to create artwork from user input.

**Core features**
- AI Art Generation (diverse styles)
- Image Enhancement and effects
- Prompt Enhancement tools
- Web UI for creation and editing
- Social media sharing
- Firebase integration (auth, storage, DB)
- Dataset tools for model training
- Server network for processing and delivery
- Server-side tracking of requests for LLM improvements

**Quick links**
- Gallery: [Elixpo Gallery](https://elixpoart.vercel.app/src/gallery)
  - Example image by ID: [Image 9pde71i621](https://elixpoart.vercel.app/src/gallery?id=9pde71i621)

<details>
<summary>Kaggle builds and datasets</summary>

- [Platform testing notebook](https://www.kaggle.com/code/circuitovertime/elixpo-ai-platform-testing-beta/edit/run/199734513)
- [Google Colab notebook](https://colab.research.google.com/drive/1jfJKeganPiY2i2T-vR_TlPQuMKEq8SC_?usp=sharing)
- [Prompts collection dataset](https://www.kaggle.com/datasets/circuitovertime/prompt-and-gibberish-for-ai-art-gen/data?select=prompts_collection.csv)
- [PromptPimp fine-tuning](https://www.kaggle.com/code/overtimecraftsclips/fine-tuning-of-elixpo-promptpimp)

</details>

- Chrome Extension: [Elixpo Art — Select Text and Transform to Picture](https://chromewebstore.google.com/detail/elixpo-art-select-text-an/hcjdeknbbbllfllddkbacfgehddpnhdh)
- Discord Bot invite: [Elixpo Discord Bot](https://discord.com/oauth2/authorize?client_id=1214916249222643752)
- Blog: [Elixpo Art Service analysis](https://elixpoart.vercel.app/src/blogs/elixpo_art)

**Supported by**
- LLMPlayground.net (Custom FLUX models hosting)
- Karma.YT (Social integrations)
- AWS Activate, Google Cloud for Startups, OVH Cloud (GPU credits)
- NVIDIA Inception (AI startup support)
- Azure (MS for Startups) — OpenAI credits
- Outlier Ventures (Accelerator)

**Vision**
- Open & Accessible
- Transparent & Ethical
- Community-Driven
- Interconnected ecosystem
- Evolving while remaining open

**License**
MIT License

[↑ Back to top](#together-elixpo-monorepo-project-index)

---

## art.elixpo — ElixpoAI Art Generator

- Description: Web-based AI art generator with backend services for image generation, enhancement, and prompt tooling.

**Features**
- AI art generation using advanced ML models
- Image enhancement effects
- Prompt enhancement for better outputs
- Web UI for creation and manipulation
- Social media sharing
- Firebase for auth, storage, and DB
- Dataset management tools
- Server network for efficient delivery

<details>
<summary>Install</summary>

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

</details>

<details>
<summary>Run</summary>

```bash
./server.sh
# then open http://localhost:5000
```

</details>

**License**
See project README for license notes.

[↑ Back to top](#together-elixpo-monorepo-project-index)

---

## chat.elixpo — Chat site and services

- README preview image present; for details, see code under `chat.elixpo/` (Node server, frontend, and Python helpers for news, podcasts, and weather flows).

[↑ Back to top](#together-elixpo-monorepo-project-index)

---

## elixpo-art-chrome-extension — Chrome Extension

- Name: Elixpo Art: Select Text and Transform to Picture
- Description: Converts selected text on any webpage into an AI-generated image via Elixpo services.

**Features**
- Text-to-image via AI
- Context-menu and selection based
- Customizable reload shortcut
- Firebase and Google API integration
- Prompt enhancement, styles (Chromatic, Anime, Landscape, Wpap, Pixel, Normal)
- Aspect ratios (1:1, 4:3, 16:9, 9:16)
- Custom instructions
- Image download and loading indicator
- Dynamic text feedback

**Install (unpacked)**
1. Open `chrome://extensions/`
2. Enable Developer mode
3. Load unpacked and select the extension directory

**Usage**
- Select text → right-click → Transform to Picture

**External APIs**
- `txtelixpo.vercel.app` for prompt refinement
- `imgelixpo.vercel.app` for image generation

**Dev links**
- Kaggle: [PromptPimp fine-tuning](https://www.kaggle.com/code/overtimecraftsclips/fine-tuning-of-elixpo-promptpimp)
- Hugging Face: [Elixpo/promptPimp](https://huggingface.co/Elixpo/promptPimp)

[c Back to top](#together-elixpo-monorepo-project-index)

---

## inkflow — Inkflow Workspace

- Description: Web app for intuitive digital art creation (sketching, shapes, color tools, save/export).

**Key features**
- Freehand drawing
- Shape tools
- Color and brush customization
- Undo/Redo
- Save and export

**Tech stack**
- HTML, CSS, JavaScript, Tailwind, Bootstrap, Git, Python

<details>
<summary>Getting started</summary>

```bash
git clone https://github.com/ez-vivek/Inkflow.git
cd Inkflow
# open index.html in a browser
```

</details>

**Collaboration**
- Thanks to contributors including backend/server support from Ayushman Bhattacharya

**License**
MIT

[↑ Back to top](#together-elixpo-monorepo-project-index)

---

## jackey.elixpo — Elixpo Discord Bot (Jackey)

- Description: Discord bot for generating and remixing AI images with slash commands, queuing, and permissions.

**Features**
- `/generate` images from prompts (count, AR, theme, model, seed, enhancement)
- `/remix` up to 3 images with a new prompt
- `/help` command
- Queue system, permission checks, download buttons
- Cache management and cleanup

<details>
<summary>Setup</summary>

```bash
git clone https://github.com/yourusername/elixpo-discord-bot.git
cd elixpo-discord-bot
npm install
```

Environment variables (`.env`):

```
DISCORD_TOKEN=...
CLIENT_ID=...
POLLINATIONS_TOKEN=... (optional)
```

Register slash commands:

```bash
node register_commands.js
```

Start bot:

```bash
node elixpo_discord_bot.js
```

</details>

**License**
MIT

[↑ Back to top](#together-elixpo-monorepo-project-index)

---

## kaggle_workflow — ML notebooks and workflows

- Description: End-to-end examples and notes covering text classification and generation.

**Contents**
- Logistic Regression classifier (TF-IDF + sklearn)
- Keras Sequential model for text classification
- Evaluation and prediction workflows
- Model saving (HDF5, tokenizer via pickle)
- T5-based text generation with sampling parameters

[↑ Back to top](#together-elixpo-monorepo-project-index)

---

## search.elixpo — Elixpo Search Agent

- Description: Python-based web search and synthesis API. Processes user queries, runs web and YouTube searches, scrapes content, and generates Markdown answers with citations and images. Built for extensibility, async/concurrency, and robust error handling.

**Features**
1. Advanced search & synthesis with iterative tool use
2. Web scraping (text and images, avoids SERPs)
3. YouTube metadata and transcript extraction
4. AI-powered reasoning with Pollinations API
5. REST API via Quart (`/search`, `/search/sse`, OpenAI-compatible `/v1/chat/completions`)
6. Async concurrency for performance

**File structure (high level)**
- `app.py` — API server
- `searchPipeline.py` — Orchestrates tools and LLM calls
- Tools: `clean_query.py`, `search.py`, `scrape.py`, `getYoutubeDetails.py`, `tools.py`, `getTimeZone.py`
- Packaging: `requirements.txt`, `Dockerfile`, `docker-compose.yml`

<details>
<summary>Run locally</summary>

```bash
pip install -r requirements.txt
python app.py
# API at http://127.0.0.1:5000/search
```

</details>

**Example requests**

<details>
<summary>JSON POST</summary>

```bash
curl -X POST http://localhost:5000/search \
  -H "Content-Type: application/json" \
  -d '{"query": "What are the latest trends in AI research? Summarize this YouTube video https://www.youtube.com/watch?v=dQw4w9WgXcQ"}'
```

</details>

<details>
<summary>OpenAI-compatible POST</summary>

```bash
curl -X POST http://localhost:5000/search \
  -H "Content-Type: application/json" \
  -d '{"messages": [{"role": "user", "content": "Tell me about the history of the internet."}]}'
```

</details>

<details>
<summary>SSE streaming</summary>

```bash
curl -N -X POST http://localhost:5000/search/sse \
  -H "Content-Type: application/json" \
  -d '{"query": "weather in London tomorrow"}'
```

</details>

**Configuration**
- `.env`: `TOKEN`, `MODEL`, `REFERRER` for Pollinations API

**Limitations**
- Dependent on Pollinations API (rate limits apply)
- Requires internet for search/scrape
- YouTube transcript extraction depends on third-party services

[↑ Back to top](#together-elixpo-monorepo-project-index)

---

## solanki.elixpo — Videolize Personal Portfolio

- Name: Videolize — Advanced Personal Portfolio
- Description: Modern portfolio site inspired by Diagram.com, featuring event-driven animations, modular sections, and Firebase-backed data.

**Features**
- Modern design with GSAP, BentoBox, Glass/Neumorphism
- Event-driven animations
- Modular sections: About, Skills, Projects, Gallery, Contact, Footer
- CV view/download
- Smooth navigation and fully responsive

**Tech**
- Frontend: HTML5, CSS3 (Tailwind, custom), JavaScript (ES6+)
- Animations: GSAP, Anime.js, ScrollReveal, Snap.svg, Locomotive Scroll
- Backend: Firebase (data, links), LocalStorage (scroll memory)

<details>
<summary>Getting started</summary>

```bash
git clone https://github.com/circuit-overtime/Videolize.git
cd Videolize
# open src/index.html in your browser
```

</details>

**Live site**
- [solanki.elixpo.com](https://solanki.elixpo.com)

**License**
MIT

[↑ Back to top](#together-elixpo-monorepo-project-index)

---

Notes
- This file is an aggregation of the following READMEs: `README.md`, `art.elixpo/README.md`, `chat.elixpo/README.md`, `elixpo-art-chrome-extension/README.md`, `inkflow/README.md`, `jackey.elixpo/README.md`, `kaggle_workflow/README.md`, `search.elixpo/README.md`, `solanki.elixpo/README.md`.
- Refer to each project’s README for the most current and authoritative details.

[↑ Back to top](#together-elixpo-monorepo-project-index)
