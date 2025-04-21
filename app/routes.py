from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import models, schemas, database, scraper

router = APIRouter()
from app.database import get_db
from sqlalchemy.orm import Session

# @router.on.event("startup")
# async def startup_event():
#     models.Base.metadata.create_all(bind=database.engine)
#     titles = await scraper.scrape()
#     with database.SessionLocal() as db:
#         for title in titles:
#             db_article = models.Article(title=title)
#             db.add(db_article)
#         db.commit()

@router.get("/articles", response_model=list[schemas.ArticleOut])
def get_articles(db: Session = Depends(get_db)):
    return db.query(models.Article).all()

@router.post("/articles", response_model=schemas.ArticleOut)
def create_article(article: schemas.ArticleCreate, db: Session = Depends(get_db)):
    db_article = models.Article(title=article.title)
    db.add(db_article)
    db.commit()
    db.refresh(db_article)
    return db_article