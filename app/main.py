from fastapi import FastAPI
from app.routes import router
from app import models, database, scraper

app = FastAPI()
app.include_router(router)


@app.on_event("startup")
async def startup_event():
    models.Base.metadata.create_all(bind=database.engine)
    titles = await scraper.scrape()
    print("[SCRAPER] Articles récupérés :", titles)
    with database.SessionLocal() as db:
        for title in titles:
            db_article = models.Article(title=title)
            db.add(db_article)
        db.commit()