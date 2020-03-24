import os
import json
from pathlib import Path
from dotenv import load_dotenv

# Load the environment variables from .env file
load_dotenv()


class Config:
    base_path = Path(__file__).resolve().parent
    db_path = base_path / "app" / "data" / "chinook.db"

    SECRET_KEY = os.getenv("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = r"sqlite:///" + str(db_path)
    SQLALCHEMY_TRACK_MODIFICATIONS = json.loads(
        os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS").lower()
    )
    SQLALCHEMY_ECHO = json.loads(os.getenv("SQLALCHEMY_ECHO").lower())
    DEBUG = json.loads(os.getenv("DEBUG").lower())
