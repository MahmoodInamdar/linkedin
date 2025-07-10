# Project Plan: LLM-Powered LinkedIn Job Search & Profile Optimizer

## 1. Project Setup
- Initialize Git repository.
- Create `/backend` (FastAPI) and `/frontend` (React/TypeScript) directories.
- Set up `/documentation` and `.cursor/rules` for docs and AI rules.

## 2. Backend Foundation
- Install FastAPI, SQLAlchemy, OpenAI SDK, and other dependencies.
- Set up environment variables for LinkedIn and OpenAI API keys.
- Create `app.py` with FastAPI app and health check endpoint.
- Create `models.py` for User, Profile, and JobApplication models.

## 3. LinkedIn OAuth & Data Fetching
- Register LinkedIn app, obtain Client ID/Secret.
- Implement OAuth 2.0 endpoints (`/auth/linkedin`, `/auth/callback`).
- Fetch and store profile data (skills, experience, education).

## 4. LLM Integration
- Create `llm.py` utility for OpenAI API calls (job analysis, profile optimization, cover letter generation).
- Add endpoints:
  - `/analyze_job` (job description analysis)
  - `/optimize_profile` (profile optimization)
  - `/generate_cover_letter` (cover letter generation)

## 5. Job Application Tracker
- Extend `models.py` with JobApplication model.
- Add CRUD endpoints for job applications (`/jobs`): create, update, list, delete.

## 6. Frontend Foundation
- Initialize React app with TypeScript.
- Set up routing for Login, Dashboard, Job Tracker, Job Analysis, Cover Letter Generator, Profile Optimizer.
- Create API utilities for backend communication.

## 7. Feature Integration
- **Login:** Connect frontend to backend OAuth flow.
- **Dashboard:** Display profile data from backend.
- **Job Tracker:** Add, view, update, and delete job applications. Connect to backend endpoints.
- **Job Analysis:** Paste job description, send to `/analyze_job`, display LLM suggestions.
- **Cover Letter Generator:** Select job, request cover letter from `/generate_cover_letter`, display/copy/download result.
- **Profile Optimizer:** Request tips from `/optimize_profile`, display actionable suggestions.

## 8. Testing & Documentation
- Test all backend endpoints and frontend flows.
- Log bugs in `documentation/bugtracking.md`.
- Update documentation for new features and API endpoints.

## 9. Finalization
- Polish UI/UX, ensure responsive design.
- Review security (API keys, user data).
- Prepare for deployment (optional).

---

**Integration Notes:**
- All LLM features are accessed via backend endpoints; frontend never calls LLM APIs directly.
- Job tracker and cover letter generator are tightly integrated: users can generate cover letters for tracked jobs.
- Documentation and code comments should be kept up to date as features evolve. 