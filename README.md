# KKEVO STUDIO MEDIA
### *“Facts. Perspective. Impact.”*

An independent, African-centred global digital media institution delivering verified facts, geopolitical perspective, and in-depth structural analysis.

---

## Brand Visual Identity
The platform incorporates the complete authentic **KKEVO STUDIO MEDIA** logo and visual identity:
- **Navy & Near-Black Palette:** `#05080F`, `#090E17`, `#111827`
- **Cobalt Electric Blue:** `#0066FF`
- **Emerald Vivid Green:** `#00D26A`
- **Framing Bracket Cyan:** `#00F0FF`
- **Metallic Chrome Details:** `#E2E8F0`, `#94A3B8`
- **Typography:** `Outfit` (Headlines) & `Plus Jakarta Sans` (Body)

---

## Tech Stack
- **Backend:** Python 3.13 / Django 5.x / Django REST Framework
- **Frontend:** Vue 3 (Composition API) / Vite / Tailwind CSS / Pinia / Vue Router
- **Database:** PostgreSQL (production) with SQLite fallback (development)
- **Task Queue & Cache:** Redis + Celery
- **Containerization:** Docker & Docker Compose with Nginx Reverse Proxy
- **Documentation:** OpenAPI 3 / Swagger (`/api/docs/`)

---

## Quickstart (Local Development)

### 1. Backend Setup
```bash
# Activate virtual environment
cd backend
python -m venv venv
venv\Scripts\activate   # On Windows
# or source venv/bin/activate on Unix

# Install dependencies
pip install -r requirements.txt

# Run migrations & seed data
python manage.py migrate
python manage.py seed_kkevo_media

# Start Django development server
python manage.py runserver 8000
```

### 2. Frontend Setup
```bash
cd frontend
npm install
npm run dev
```
Open [http://localhost:5173](http://localhost:5173) in your browser.

---

## Running with Docker Compose (Production Stack)
```bash
# Build and start all services (Postgres, Redis, Django, Celery, Vue, Nginx)
docker-compose up -d --build

# Run migrations inside backend container
docker-compose exec backend python manage.py migrate
docker-compose exec backend python manage.py seed_kkevo_media
```
Access the application at [http://localhost](http://localhost).

---

## Key Credentials & User Accounts

| Role | Email | Password | Access |
|---|---|---|---|
| **Publisher / Admin** | `admin@kkevostudiomedia.com` | `kkevoAdmin2026!` | Django Admin, Full Newsroom Control |
| **Senior Editor** | `editor@kkevostudiomedia.com` | `editorPass2026!` | Newsroom Desk, Review & Publishing |
| **Field Reporter** | `kwame.mensah@kkevostudiomedia.com` | `reporterPass2026!` | Draft Stories, Attach Sources |

---

## API & Newsroom Endpoints

- **Swagger / OpenAPI 3 UI:** `/api/docs/`
- **Redoc Interactive UI:** `/api/redoc/`
- **Health Check:** `/api/v1/health/`
- **Consolidated Homepage Feed:** `/api/v1/homepage/`
- **Articles & Sourcing:** `/api/v1/articles/`
- **Country Intelligence Hubs:** `/api/v1/countries/`
- **Topic Hubs (AfCFTA, Critical Minerals, AES):** `/api/v1/topics/`
- **Video & 60s Context Reels:** `/api/v1/videos/`
- **Public Corrections Ledger:** `/api/v1/corrections/`
- **Intelligence Briefing Subscriptions:** `/api/v1/newsletter/subscribe/`
- **Editorial Workflow State Transitions:** `/api/v1/editorial/articles/`
- **RSS 2.0 Feed:** `/feeds/rss/`
- **XML News Sitemap:** `/feeds/sitemap.xml`

---

## Running Automated Tests
```bash
# Run backend Django test suite
python backend/manage.py test apps.articles

# Run frontend production build test
cd frontend
npm run build
```
