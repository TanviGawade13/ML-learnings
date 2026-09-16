# Tasks API

A minimal in-memory REST API built with FastAPI.

## Run it

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn main:app --reload
```

Open http://127.0.0.1:8000/docs for interactive API documentation.

## Endpoints

| Method | Endpoint | Purpose |
| --- | --- | --- |
| GET | `/` | Health check |
| GET | `/tasks` | List tasks |
| GET | `/tasks/{task_id}` | Get one task |
| POST | `/tasks` | Create a task |
| PUT | `/tasks/{task_id}` | Replace a task |
| DELETE | `/tasks/{task_id}` | Delete a task |

Example request body for POST and PUT:

```json
{
  "title": "Learn FastAPI",
  "completed": false
}
```

Tasks are kept only in memory, so restarting the server clears them.
