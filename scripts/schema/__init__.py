from pydantic import BaseModel
from datetime import datetime

class Post(BaseModel):
    user_id: str
    content: str | None = None


