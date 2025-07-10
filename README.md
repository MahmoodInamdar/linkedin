# LLM-Powered LinkedIn Job Search & Profile Optimizer

A web application that uses LinkedIn data and large language models (OpenAI/other) to help you search for jobs, track your applications, generate personalized cover letters, optimize your resume, and improve your LinkedIn profile with AI-driven suggestions.

## Features
- **Secure LinkedIn OAuth login** (user-only)
- **Profile data fetching** (skills, experience, education)
- **Job application tracker** (add, update, view, delete applications, status tracking)
- **Job description analysis** (LLM-powered)
- **Personalized cover letter generator** (LLM-powered)
- **Resume suggestions** (LLM-powered)
- **Profile optimization tips** (LLM-powered)
- **Dashboard** for profile viewing
- **Bug tracking** and error handling

## Technology Stack
- **Backend:** Python (FastAPI), SQLAlchemy, OpenAI SDK
- **Frontend:** React (TypeScript)
- **Database:** SQLite (MVP)
- **AI:** OpenAI GPT models (or other LLMs)

## Project Structure
See `documentation/project_structure.md` for a detailed directory overview.

## Setup Instructions
1. **Clone the repository**
2. **Backend setup:**
   - `cd backend`
   - `python -m venv venv && source venv/bin/activate`
   - `pip install -r requirements.txt`
   - Set environment variables for LinkedIn and OpenAI API keys
   - `uvicorn app:app --reload`
3. **Frontend setup:**
   - `cd frontend`
   - `npm install`
   - `npm start`
4. **Documentation:**
   - See the `documentation/` folder for implementation, workflow, UI/UX, and requirements.

## Usage
- Log in with LinkedIn
- View your profile data on the dashboard
- Track your job applications and update their status
- Paste job descriptions to get resume suggestions
- Generate personalized cover letters for jobs
- Get actionable profile optimization tips

## Contributing
- Follow PEP 8 for Python and use functional React components
- Document all LLM prompt strategies and API endpoints
- Log bugs in `documentation/bugtracking.md`

## License
MIT (or specify your license)

## Acknowledgments
- OpenAI, LinkedIn, FastAPI, React
- See `documentation/prd.md` for citations and references 