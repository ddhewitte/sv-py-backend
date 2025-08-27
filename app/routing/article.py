from fastapi import APIRouter, HTTPException, Depends, status, Query
from pydantic import BaseModel, constr, field_validator
from typing import Annotated
import app.models.article
from app.core.database import engine, get_db
from sqlalchemy import or_
from sqlalchemy.orm import Session

router = APIRouter()
app.models.article.Base.metadata.create_all(bind=engine)

class ArticleBase(BaseModel):
    title: constr(min_length=20)
    content: constr(min_length=200)
    category: constr(min_length=3)
    status: str

    @field_validator("status")
    def cek_status(cls, stat):
        if stat not in ["publish", "draft", "thrash"]:
            raise ValueError("Status must be publish/draft/thrash")
        return stat

@router.get("/article", status_code=status.HTTP_200_OK)
def get_articles(db: Session = Depends(get_db)):
    return db.query(app.models.article.Article).all()

@router.get("/article/{id}", status_code=status.HTTP_200_OK)
def get_article(id: int, db: Session = Depends(get_db)):
    article = db.query(app.models.article.Article).filter(app.models.article.Article.id == id).first()
    if not article:
        raise HTTPException(status_code=404, detail="Not found article with that id!")
    return article

@router.post("/article", status_code=status.HTTP_201_CREATED)
def create_article(article: ArticleBase, db: Session = Depends(get_db)):
    db_article = app.models.article.Article(**article.model_dump())
    db.add(db_article)
    db.commit()
    return {"message": "New article created!"}

@router.put("/article/{id}", status_code=status.HTTP_200_OK)
def update_article(id: int, article: ArticleBase, db: Session = Depends(get_db)):
    findArticle = db.query(app.models.article.Article).filter(app.models.article.Article.id == id).first()
    if findArticle is None:
        raise HTTPException(status_code=404, detail="Article not found")
    db_article = app.models.article.Article(**article.model_dump())
    db.query(app.models.article.Article).filter(app.models.article.Article.id == id).update({
        app.models.article.Article.title: db_article.title,
        app.models.article.Article.content: db_article.content,
        app.models.article.Article.category: db_article.category,
        app.models.article.Article.status: db_article.status
    }, synchronize_session=False)
    db.commit()
    return {"message": "Article updated!"}

@router.delete("/article/{id}", status_code=status.HTTP_200_OK)
async def delete_article(id: int, db: Session = Depends(get_db)):
    findArticle = db.query(app.models.article.Article).filter(app.models.article.Article.id == id).first()
    if findArticle is None:
        raise HTTPException(status_code=404, detail="Article not found")
    db.delete(findArticle)
    db.commit()
    return {"message": "Article deleted!"}

@router.get("/article/{limit}/{offset}")
def get_articles_with_limit_offset(limit: int, offset: int, db: Session = Depends(get_db)):
    return db.query(app.models.article.Article).offset(offset).limit(limit).all()