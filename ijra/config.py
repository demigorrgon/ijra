import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    CORS_HEADERS = "Content-Type"
    SECRET_KEY = os.getenv("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.getenv("POSTGRES_URI")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
