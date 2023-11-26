from pydantic import BaseModel

class PostDBSchema(BaseModel):
    id: int
    title: str
    content: str