# UI/UX and Wireframes

## Pages
- **Login Page**: Centered LinkedIn login button, app branding.
- **Dashboard**: Profile summary (skills, experience, education), navigation menu.
- **Job Tracker**: Table of job applications (title, company, status, date, notes), add/edit form, status update dropdown, filter/sort options.
- **Job Analysis**: Text area for job description, submit button, results list of LLM suggestions.
- **Cover Letter Generator**: Select job (from tracker or analysis), generate button, display generated cover letter, copy/download options.
- **Profile Optimizer**: List of actionable profile improvement tips, refresh button.

## Wireframe Sketches (Textual)

```
[Login Page]
+-----------------------------+
|   [App Logo]                |
|   Sign in with LinkedIn     |
+-----------------------------+

[Dashboard]
+-----------------------------+
| [Nav] Profile | Job | Opt   |
+-----------------------------+
| Name, Photo, Headline       |
| Skills: [list]              |
| Experience: [list]          |
| Education: [list]           |
+-----------------------------+

[Job Tracker]
+-----------------------------+
| Job Applications            |
| +-------------------------+ |
| | Title | Company | Status | |
| |-------------------------| |
| | ...                     | |
| +-------------------------+ |
| [Add New] [Edit] [Delete]   |
| [Status Dropdown] [Notes]   |
+-----------------------------+

[Job Analysis]
+-----------------------------+
| Paste Job Description       |
| [ Text Area         ]       |
| [Analyze Button]            |
| Suggestions:                |
| - Highlight X skill         |
| - Add Y experience          |
+-----------------------------+

[Cover Letter Generator]
+-----------------------------+
| Select Job: [Dropdown]      |
| [Generate Cover Letter]     |
| [Cover Letter Output]       |
| [Copy] [Download]           |
+-----------------------------+

[Profile Optimizer]
+-----------------------------+
| Profile Optimization Tips   |
| - Add skill Z               |
| - Update summary            |
| [Refresh]                   |
+-----------------------------+
```

## UX Notes
- Responsive design for desktop/mobile.
- Clear feedback/loading states for LLM calls.
- Actionable, easy-to-read suggestions.
- Easy navigation between job tracker, analysis, and cover letter generator.
