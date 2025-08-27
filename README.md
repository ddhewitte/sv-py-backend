# RestFul API article with FastAPI Python
To run it locally
- Clone
- Buat virtual environment 
  - python -m venv venv
  - venv\Scripts\activate
- Setup dependencies
  - pip install -r requirements.txt
- Setup env variable (for database) (*we must create database (database only) first manually)
- Run migration -> alembic upgrade head
- Run app locally -> uvicorn app.main:app --reload

