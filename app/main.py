"""The main file for the app"""
from fastapi import FastAPI
import uvicorn


app = FastAPI()


@app.get("/", name="Main Root", description="The main endpoint for the app")
async def root() -> dict[str, str]:
    """The main endpoint for the app"""
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run(app, host="0000000", port=8000)
