import os
from dotenv import load_dotenv
load_dotenv()

ANTHROPIC_URL = os.getenv("ANTHROPIC_URL")
print(ANTHROPIC_URL)

