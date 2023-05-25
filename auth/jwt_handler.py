"""The file that handles the JWT i.e. signing, encoding, decoding and returning JWTs"""
import os
from time import datetime

import jwt
from dotenv import find_dotenv, load_dotenv


load_dotenv(find_dotenv())

JWT_SECRET = os.environ.get("SECRET")
JWT_ALGORITHM = os.environ.get("ALGORITHM")