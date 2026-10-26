# TaskFlow — Python + JavaScript Task Manager

TaskFlow is a beginner-friendly full-stack project built with Python (Flask), SQLite, HTML, CSS, and vanilla JavaScript.

## Features
- Create tasks with title, description, and priority
- View all tasks and filter by status
- Update task status: Pending, In Progress, Completed
- Delete tasks with a confirmation prompt
- REST API with validation and useful error messages
- SQLite database is created automatically on first run
- Responsive layout for desktop and mobile

## Requirements
- Python 3.10 or newer
- pip
- A modern web browser

## Run locally

### Windows (PowerShell)
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python app.py
```

If PowerShell blocks activation, you can use:
```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe app.py
```

### macOS / Linux
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:5000 in your browser. The local SQLite database is created automatically.

## API endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/api/tasks` | List tasks |
| GET | `/api/tasks?status=Pending` | Filter by status |
| POST | `/api/tasks` | Create a task |
| PATCH | `/api/tasks/<id>` | Update task fields/status |
| DELETE | `/api/tasks/<id>` | Delete a task |

### Example: create a task
```json
{
  "title": "Learn Flask APIs",
  "description": "Build and test the task endpoints",
  "priority": "High"
}
```

## Project structure
```text
TaskFlow_Python_JavaScript_Project/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── templates/
│   └── index.html
└── static/
    ├── css/styles.css
    └── js/app.js
```

## How the logic works
1. The browser form collects task details.
2. JavaScript sends JSON to Flask using `fetch()`.
3. Flask validates the request and writes to SQLite through SQLAlchemy.
4. Flask returns JSON to the browser.
5. JavaScript renders the tasks and updates the screen without a full page reload.

## Upload to GitHub
1. Create a new, empty GitHub repository.
2. Extract this ZIP file.
3. Open a terminal in the extracted project folder.
4. Run:
```bash
git init
git add .
git commit -m "Initial TaskFlow project"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
git push -u origin main
```
Replace the example remote URL with your own repository URL. Do not upload virtual environments, passwords, or secret keys.

## Notes
- This is a local learning/demo project, not a production deployment.
- Flask debug mode is enabled for local development only. Turn it off before deploying publicly.
- Authentication, automated tests, pagination, and production hosting are useful next improvements.
