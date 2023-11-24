from pydantic import BaseModel
from datetime import datetime

class PostDBSchema(BaseModel):
    post_id: str
    user_id: str
    content: str | None = None
    links: list[str] | None = None
    username: str | None = None
    likes: int = 0
    comments: int = 0
    shares: int | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None
