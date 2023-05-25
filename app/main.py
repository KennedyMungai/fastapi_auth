"""The main file for the app"""
import uvicorn
from fastapi import Body, Depends, FastAPI, status

from auth.jwt_handler import signJWT
from models.PostsModel import PostsSchema
from models.user_model import UserLoginSchema, UserSchema

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


@app.post(
    "/posts",
    name="Create Post",
    description="Create a new post",
    tags=['Posts'],
    status_code=status.HTTP_201_CREATED
)
async def create_new_post_endpoint(_post: PostsSchema):
    """Endpoint for creating a new post

    Args:
        _post (PostsSchema): The post to create

    Returns:
        dict: The post
    """
    _post.id = len(posts) + 1
    posts.append(_post.dict())
    return {"info": "Post Added"}


@app.post('/user/signup', tags=['Users'])
async def user_signup_endpoint(_user: UserSchema = Body(default=None)):
    """The endpoint for the user signup

    Args:
        _user (UserSchema, optional): The User Id. Defaults to Body(default=None).

    Returns:
        _type_: _description_
    """
    users.append(_user)
    return signJWT(_user.email)


def check_user(_data: UserLoginSchema):
    """Check if the user exists

    Args:
        _data (UserLoginSchema): The user data

    Returns:
        bool: True if the user exists
    """
    for user in users:
        if user.email == _data.email and user.password == _data.password:
            return True
    return False


@app.post(
    '/user/login',
    tags=['Users'],
    name="User Login",
    description="An endpoint to check User Login"
)
async def user_login_endpoint(_user: UserLoginSchema = Body(default=None)):
    """Defined the user login endpoint

    Args:
        _user (UserLoginSchema, optional): The user Login details. Defaults to Body(default=None).

    Returns:
        _type_: _description_
    """
    if check_user(_user):
        return signJWT(_user.email)
    else:
        return {"error": "Invalid Credentials"}


if __name__ == "__main__":
    uvicorn.run(app, host="0000000", port=8000, reload=True)
