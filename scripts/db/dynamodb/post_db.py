from scripts.utils.dynamodb_utility import DynamoDBUtility
from scripts.constants import DatabaseConstants
from scripts.db.schema import PostDBSchema
from scripts.schema import Post
from datetime import datetime


class PostDB:
    def __init__(self) -> None:
        self.post_table = DynamoDBUtility(table_name=DatabaseConstants.post_table, primary_key=DatabaseConstants.primary_key)

    def get_all_posts(self, user_id: str) -> list:
        return self.post_table.get_all_items(user_id=user_id)

    def get_post(self, post_id: str) -> dict:
        return self.post_table.get_by_primary_key(post_id)

    def create_post(self, post_id:str, post: Post) -> str:
        post = post.model_dump()
        post['post_id'] = post_id
        post['created_at'] = post['updated_at'] = datetime.now()
        post_db_schema = PostDBSchema(post)
        self.post_table.create(post_db_schema.model_dump())
        return post_id

    def update_post(self, post_id: str, post: Post) -> bool:
        post_db_schema = PostDBSchema(**post.model_dump())
        return self.post_table.update(post_id, post_db_schema.model_dump())

    def delete_post(self, post_id: str) -> bool:
        return self.post_table.delete(post_id)
