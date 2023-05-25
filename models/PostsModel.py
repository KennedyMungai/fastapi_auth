"""The Posts model file"""
from pydantic import BaseModel, Field, EmailStr


class PostsSchema(BaseModel):
    """The template for the posts data

    Args:
        BaseModel (Pydantic): The parent for the Posts
    """
    id: int = Field(default=None)
    title: str = Field(default=None)
    content: str = Field(default=None)

    class Config:
        """The config for the Posts model"""
        schema_extra = {
            "post_demo": {
                "title": "some title about animals",
                "content": "some content about animals",
            }
        }
