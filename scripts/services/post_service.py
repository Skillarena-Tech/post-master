from scripts.db.dynamodb.post_db import PostDB
from scripts.schema import Post
import uuid

class PostService:
    def __init__(self) -> None:
        self.post_db = PostDB()
    
    def get_all_posts(self, user_id: str) -> list:
        return self.post_db.get_all_posts(user_id=user_id)
    
    def get_post(self, post_id: str) -> dict:
        return self.post_db.get_post(post_id=post_id)
    
    def create_post(self, post: Post) -> str:
        post_id: str = str(uuid.uuid4())
        return self.post_db.create_post(post_id=post_id, post=post)
    
    def update_post(self, post_id: str, post: Post) -> bool:
        return self.post_db.update_post(post_id=post_id, post=post)
    
    def delete_post(self, post_id: str) -> bool:
        return self.post_db.delete_post(post_id=post_id)