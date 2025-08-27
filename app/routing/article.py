from fastapi import APIRouter, HTTPException, Depends, status, Query
from pydantic import BaseModel
from typing import Annotated
import app.models.article
from app.core.database import engine, get_db
from sqlalchemy import or_
from sqlalchemy.orm import Session

router = APIRouter()
app.models.article.Base.metadata.create_all(bind=engine)

class ArticleBase(BaseModel):
    title: str
    content: str
    category: str
    status: str

@router.get("/article", status_code=status.HTTP_200_OK)
def get_articles(db: Session = Depends(get_db)):
    return db.query(app.models.article.Article).all()

@router.get("/article/{id}", status_code=status.HTTP_200_OK)
def get_article(id: int, db: Session = Depends(get_db)):
    article = db.query(app.models.article.Article).filter(app.models.article.Article.id == id).first()
    if not article:
        raise HTTPException(status_code=404, detail="Not found article with that id!")
    return article

@router.post("/article", status_code=status.HTTP_200_OK)
def create_article(article: ArticleBase, db: Session = Depends(get_db)):
    db_article = app.models.article.Article(**article.model_dump())
    db.add(db_article)
    db.commit()
    return {"message": "New article created"}