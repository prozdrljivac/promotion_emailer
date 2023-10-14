import os
from dotenv import load_dotenv

load_dotenv()

EMAIL_SERVICE = os.getenv("EMAIL_SERVICE")
