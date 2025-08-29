# RestFul API article with FastAPI Python
To run it locally
- Clone
- Create virtual environment 
  - python -m venv venv
  - venv\Scripts\activate
- Setup dependencies
  - pip install -r requirements.txt
- Setup database > create new database article
- Setup env variable (for database) in .env file
- Run migration -> alembic upgrade head
- Run app locally -> uvicorn app.main:app --reload


Swagger/ API playground : http://127.0.0.1:8000/docs#/


FYI : URL BE Live https://sv-py-backend-production.up.railway.app/ and MySQL can't be accessed anymore, because my trial period has expired, so it can only be tried in the local environment
