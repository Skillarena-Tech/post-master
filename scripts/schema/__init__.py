from pydantic import BaseModel
from datetime import datetime

class Post(BaseModel):
    user_id: str
    content: str | None = None
    links: list[str] | None = None
    username: str | None = None
    likes: int | None = None
    comments: int | None = None
    shares: int | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None

