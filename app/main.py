"""The main file for the app"""
import uvicorn
from fastapi import FastAPI

from models.PostsModel import PostsModel

app = FastAPI()

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


@app.get("/", name="Main Root", description="The main endpoint for the app", tags=['Root'])
async def root() -> dict[str, str]:
    """The main endpoint for the app"""
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run(app, host="0000000", port=8000)
