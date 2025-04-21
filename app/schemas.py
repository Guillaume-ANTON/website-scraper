from pydantic import BaseModel

class ArticleCreate(BaseModel):
    title: str

class ArticleOut(BaseModel):
    id: int
    title: str

    class Config : 
        orm_mode = True