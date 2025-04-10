import os
from dotenv import load_dotenv

load_dotenv()

APP_DOMAIN = os.getenv("APP_DOMAIN", "http://localhost:8000")

GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID", "dummy_client_id")
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET", "dummy_client_secret")
GOOGLE_CALLBACK_PATH = "/auth/google/callback"
