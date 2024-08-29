from dotenv import load_dotenv
import os
from pathlib import Path

dotenv_path = Path(__file__).with_name(".env")  # path to .env file
load_dotenv(dotenv_path=dotenv_path)

TOKEN = os.getenv("TOKEN", "0")
