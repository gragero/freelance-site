import os
from dotenv import load_dotenv
from pathlib import Path

basedir = Path(__file__).parent
load_dotenv(basedir / ".env")

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-key")
    DEBUG = False

    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    MAIL_DEFAULT_SENDER = ("Abo 7gag Portfolio", os.environ.get("MAIL_USERNAME"))
