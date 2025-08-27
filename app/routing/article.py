from fastapi import APIRouter, HTTPException, Depends, status, Query
from pydantic import BaseModel
from typing import Annotated
import app.models.article
from app.core.database import engine, get_db
from sqlalchemy import or_
from sqlalchemy.orm import Session

router = APIRouter()
app.models.article.Base.metadata.create_all(bind=engine)

@router.get("/article", status_code=status.HTTP_200_OK)
def get_articles(db: Session = Depends(get_db)):
    return db.query(app.models.article.Article).all()