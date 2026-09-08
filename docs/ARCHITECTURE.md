# KKEVO STUDIO MEDIA — Technical Architecture & Editorial System

**Tagline:** *“Facts. Perspective. Impact.”*  
**Mission:** An independent African-centred global digital media institution delivering verified facts, geopolitical perspective, and in-depth structural analysis.

---

## 1. High-Level Architecture

The platform operates as an API-first, decoupled system designed for high editorial throughput, empirical verification, and global distribution.

- **Backend:** Django 5.x / Django REST Framework (DRF)
  - Modular, domain-driven Django applications (`core`, `accounts`, `taxonomy`, `authors`, `media_library`, `sources`, `articles`, `video`, `live`, `newsletter`, `community`, `analytics`, `seo`).
  - Strict 6-tier Role-Based Access Control (`Visitor`, `Reader`, `Contributor`, `Editor`, `Senior Editor`, `Publisher Admin`).
  - Granular Credibility & Source Scrutiny Engine (`Source`, `SourceType`, `Citation`, `Claim`, `VerificationStatus`, `Correction`, `ArticleRevision`).
- **Frontend:** Vue 3 (Composition API) + Vite + Tailwind CSS + Pinia + Vue Router
  - Authoritative, dark-navy newsroom aesthetic with electric blue and vivid green accents derived directly from the official KKEVO STUDIO MEDIA brand identity.
  - Interactive African geopolitical tools: Continental Map Explorer, "Who Owns Africa's Resources?" Value Chain Tracker, 60 Seconds of Context video reels, and Footnote/Citation drawers.
- **Database & Storage:** PostgreSQL 16 relational database with UUID primary keys and multi-index search; Redis 7 for caching and task queues.
- **DevOps:** Fully containerized via Docker & Docker Compose (`backend`, `frontend`, `db`, `redis`, `celery_worker`, `celery_beat`, `nginx`).

---

## 2. Editorial Credibility State Machine

```
[ DRAFT ] (Contributor drafts story & links primary sources)
   │
   ▼
[ SUBMITTED FOR REVIEW ] (Locks author edits, alerts editor desk)
   │
   ├──────────────► [ NEEDS CHANGES ] (Returned with editorial notes)
   │
   ▼
[ IN REVIEW ] (Structural, stylistic, and headline polish)
   │
   ▼
[ FACT CHECK & SOURCE AUDIT ] (All assertions categorized: Fact, Official Claim, Allegation)
   │
   ▼
[ APPROVED ]
   │
   ├──► [ SCHEDULED ] ──► (Automated release via Celery Beat)
   │
   ▼
[ PUBLISHED ] (Syndicated via Web, RSS 2.0, and XML News Sitemaps)
   │
   ▼
[ CORRECTED ] (Transparent public banner and archive entry if audited)
```

---

## 3. Brand Identity Tokens

- **Navy Canvas:** `#05080F` (Base), `#090E17` (Surface), `#111827` (Containers)
- **Cobalt Electric Blue:** `#0066FF` (Focus / Links / Video)
- **Emerald Vivid Green:** `#00D26A` (Verified Facts / Primary Accents)
- **Framing Bracket Cyan:** `#00F0FF` (Live Indicators)
- **Metallic Chrome Silver:** `#E2E8F0` / `#94A3B8`
- **Headline Typography:** `Outfit` / Editorial Serif
- **Body Typography:** `Plus Jakarta Sans`
