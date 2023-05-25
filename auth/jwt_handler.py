"""The file that handles the JWT i.e. signing, encoding, decoding and returning JWTs"""
from time import datetime

import jwt
from dotenv import find_dotenv, load_dotenv


load_dotenv(find_dotenv())
