# FastAPI Setup

## Create Virtual Environment

```bash
python -m venv venv
```

Activate

```powershell
venv\Scripts\activate
```

Install FastAPI

```bash
pip install fastapi
```

Install Uvicorn

```bash
pip install uvicorn
```

Run

```bash
uvicorn main:app --reload
```

Swagger UI

```
http://127.0.0.1:8000/docs
```