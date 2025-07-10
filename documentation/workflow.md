# User Workflow

1. **Login**
   - User clicks "Sign in with LinkedIn" (frontend).
   - Redirected to LinkedIn OAuth, then back to app.

2. **Profile Fetch**
   - Backend fetches and stores LinkedIn profile data.
   - Dashboard displays skills, experience, education.

3. **Job Application Tracker**
   - User navigates to the Job Tracker page.
   - User adds a new job application (job title, company, status, date, notes).
   - User can update the status (applied, interview, offer, rejected) and add notes.
   - All applications are listed in a table with filtering and sorting options.

4. **Job Analysis**
   - User pastes a job description into the Job Analysis page.
   - Frontend sends description to backend `/analyze_job` endpoint.
   - LLM extracts key requirements, compares to user profile, and returns suggestions.
   - Suggestions are displayed (e.g., "Highlight X skill", "Add Y experience").

5. **Personalized Cover Letter Generation**
   - User selects a job application or job description.
   - User requests a cover letter via the Cover Letter Generator page or from the job tracker.
   - Frontend sends job and profile data to `/generate_cover_letter` endpoint.
   - LLM returns a tailored cover letter, which is displayed for review, copy, or download.

6. **Profile Optimization**
   - User navigates to Profile Optimizer.
   - Frontend requests optimization tips from `/optimize_profile` endpoint.
   - LLM suggests profile improvements (skills to add, summary tips, etc).

7. **Resume Suggestions**
   - LLM can generate resume bullet points or summaries tailored to job descriptions.

8. **Iterate**
   - User can refresh data, analyze new jobs, update applications, generate new cover letters, and update their profile/resume iteratively.
