"""The main file for the app"""
import uvicorn
from fastapi import FastAPI

from models.PostsModel import PostsSchema

app = FastAPI(title="FastAPI Auth Example",
              description="A simple fastapi backend app for messing around with authentication")

posts = [
    {
        "id": 1,
        "title": "Penguins",
        "content": "Tuxedo Birds are pretty awesome"
    },
    {
        "id": 2,
        "title": "Pigs",
        "content": "Pigs are cool"
    },
    {
        "id": 3,
        "title": "Cats",
        "content": "Cats are cool"
    }
]

users = []

@app.get("/", name="Main Root", description="The main endpoint for the app", tags=['Root'])
async def root() -> dict[str, str]:
    """The main endpoint for the app"""
    return {"message": "Hello World"}


@app.get("/posts", name="Get Posts", description="Get all posts", tags=['Posts'])
async def get_all_posts_endpoint():
    """Get all posts endpoint"""
    return {"data": posts}


@app.get("/posts/{post_id}", name="Get Post", description="Get a single post", tags=['Posts'])
async def get_single_post_endpoint(post_id: int):
    """Endpoint for retrieving a single post

    Args:
        post_id (int): The id of the post

    Returns:
        dict: The post
    """
    return posts[post_id]


if __name__ == "__main__":
    uvicorn.run(app, host="0000000", port=8000, reload=True)
