"""Created the Model file for the User"""
from pydantic import BaseModel, Field, EmailStr


class UserSchema(BaseModel):
    fullname: str = Field(default=None)
    email: EmailStr = Field(default=None)
    password: str = Field(default=None)

    class Config:
        the_schema = {
            "user_demo": {
                "name": "Somebody's Name",
                "email": "chicken@wings.com",
                "password": "password"
            }
        }
