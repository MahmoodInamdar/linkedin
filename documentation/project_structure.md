# Project Structure

This project is an AI-augmented LinkedIn Job Search and Profile Optimization Web Application. It is structured for extensibility and LLM (OpenAI/other) integration, and now includes:
- Automated Job Application Tracker
- Personalized Cover Letter Generator

## Directories

- `/backend/` — Python FastAPI backend, handles API, LinkedIn OAuth, data processing, LLM integration, job tracking, and cover letter generation.
  - `app.py` — Main FastAPI app, endpoints for auth, profile, job analysis, job application tracking, and LLM calls.
  - `models.py` — SQLAlchemy models for user/profile data and job applications.
  - `llm.py` — Utilities for OpenAI/LLM API calls (job/skill analysis, cover letter generation).
  - `requirements.txt` — Backend dependencies (FastAPI, SQLAlchemy, OpenAI, etc).
- `/frontend/` — React (TypeScript) frontend for user interaction.
  - `src/App.tsx` — Main app component.
  - `src/pages/` — Pages: Login, Dashboard, Job Analysis, Profile Optimizer, Job Tracker, Cover Letter Generator.
  - `src/components/` — UI components (Job Application Table, Cover Letter Modal, etc).
  - `src/api/` — API call utilities.
  - `package.json` — Frontend dependencies (React, axios, etc).
- `/documentation/` — Project documentation (this folder).
- `/.cursor/rules/` — Cursor AI rules for project context.

## LLM Integration
- LLM API keys stored in backend environment variables.
- LLM calls handled in `backend/llm.py` and exposed via FastAPI endpoints.
- Frontend interacts with LLM endpoints for job analysis, resume suggestions, profile optimization, and cover letter generation.

## New Features
- **Job Application Tracker:**
  - Backend endpoints and models for storing and updating job applications.
  - Frontend page for adding, viewing, and updating job applications and statuses.
- **Personalized Cover Letter Generator:**
  - LLM-powered endpoint to generate cover letters based on job description and user profile.
  - Frontend UI to request, view, and copy/download generated cover letters.
