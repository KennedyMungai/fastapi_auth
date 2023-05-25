"""The file that handles the JWT i.e. signing, encoding, decoding and returning JWTs"""
import os
from time import time

from jwt import encode
from dotenv import find_dotenv, load_dotenv


load_dotenv(find_dotenv())

JWT_SECRET = os.environ.get("SECRET")
JWT_ALGORITHM = os.environ.get("ALGORITHM")


def token_response(token: str):
    """The function that returns a generated token

    Args:
        token (str): The JWT token

    Returns:
        dict: access token
    """
    return {
        "access_token": token
    }


def signJWT(userID: str):
    """A function that encodes a signJWT

    Args:
        userID (str): The user ID

    Returns:
        dict: The token
    """
    payload = {
        "userID": userID,
        "expiration_date": time() + 600
    }

    token = encode(payload, JWT_SECRET, JWT_ALGORITHM)

    return token_response(token)
