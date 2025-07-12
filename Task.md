Step 1: Project & Environment Setup
Create and verify the modular directory structure (already done).
Initialize Python environment for the backend (uv or venv).
Initialize a new React app (TypeScript) for the frontend.
Set up Git repository and make the initial commit.
Add placeholder README files and config files.
Step 2: Backend Foundation & LinkedIn OAuth
Install backend dependencies (FastAPI, SQLAlchemy, OpenAI SDK, python-dotenv, etc.).
Scaffold a basic FastAPI app (src/app.py) with a health check endpoint.
Set up environment variable loading (config/settings.yaml, .env).
Register a LinkedIn app and obtain Client ID/Secret.
Implement LinkedIn OAuth endpoints (/auth/linkedin, /auth/callback).
Test OAuth flow (ensure you can get an access token).
Step 3: Profile Data Fetching & Storage
Use the LinkedIn API to fetch user profile data (skills, education, experience) after authentication.
Design and implement SQLAlchemy models for User and Profile.
Store fetched profile data in SQLite.
Add endpoints to retrieve profile data for the frontend.
Step 4: Frontend Foundation & Integration
Set up basic routing/pages in React: Login and Dashboard.
Implement “Sign in with LinkedIn” button and connect to backend OAuth endpoint.
After login, fetch and display profile data from the backend on the dashboard.
Test the end-to-end flow: login → fetch profile → display on dashboard.
How to Merge Everything Together
After each step, commit your changes and test the integration.
Once all steps are complete, you’ll have a working MVP for authentication and profile viewing, with a modular, maintainable structure.