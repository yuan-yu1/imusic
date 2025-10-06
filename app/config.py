import os
from dotenv import load_dotenv

load_dotenv()  # 先加载 .env（如果有）

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL") or "sqlite:///imusic.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("SECRET_KEY") or "dev-secret-key"