import os
from dotenv import load_dotenv

load_dotenv()

TRAVIS_TOKEN = os.getenv("TRAVIS_TOKEN")
FONT = os.getenv("FONT")
TRAVIS_GIF = os.getenv("TRAVIS_GIF")