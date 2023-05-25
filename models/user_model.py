"""Created the Model file for the User"""
from pydantic import BaseModel, Field, EmailStr


class UserSchema(BaseModel):
    """The model for the user

    Args:
        BaseModel (Pydantic): The parent class for the User Model
    """
    fullname: str = Field(default=None)
    email: EmailStr = Field(default=None)
    password: str = Field(default=None)

    class Config:
        """The config file for the class """
        the_schema = {
            "user_demo": {
                "name": "Somebody's Name",
                "email": "chicken@wings.com",
                "password": "password"
            }
        }
