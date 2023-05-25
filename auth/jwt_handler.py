"""The file that handles the JWT i.e. signing, encoding, decoding and returning JWTs"""
from time import datetime
import jwt
from dotenv import load_dotenv, find_dotenv
