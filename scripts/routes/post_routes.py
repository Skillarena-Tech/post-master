from scripts.services.post_service import PostService
from scripts.constants.api import APIEndpoints
from scripts.schema import Post
from fastapi import APIRouter, HTTPException

router = APIRouter(prefix=APIEndpoints.api_prefix)

@router.get(APIEndpoints.get_posts)
def get_posts(user_id: str):
    return PostService().get_all_posts(user_id=user_id)

def get_post(post_id: str):
    post = PostService().get_post(post_id=post_id)
    if not post:
        raise HTTPException(status_code=404, detail='Post not found')
    return post

@router.get(APIEndpoints.get_post)
def get_post_api(post_id: str):
    return get_post(post_id=post_id)

@router.post(APIEndpoints.create_post)
def create_post(post: Post):
    return PostService().create_post(post=post)

@router.put(APIEndpoints.update_post)
def update_post(post_id: str, post: Post):
    if not get_post(post_id=post_id):
        raise HTTPException(status_code=404, detail='Post not found')
    return PostService().update_post(post_id=post_id, post=post)

@router.delete(APIEndpoints.delete_post)
def delete_post(post_id: str):
    if not get_post(post_id=post_id):
        raise HTTPException(status_code=404, detail='Post not found')
    return PostService().delete_post(post_id=post_id)