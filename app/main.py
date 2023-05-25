"""The main file for the app"""
from fastapi import FastAPI


app = FastAPI()


@app.get("/", name="Main Root", description="The main endpoint for the app")
async def root() -> dict[str, str]:
    """The main endpoint for the app"""
    return {"message": "Hello World"}
