from uuid import uuid4
from os import getenv

token = str(uuid4())
with open(".env", "a") as file:
    file.write(f"\nSECRET_API_TOKEN=\"{token}\"")

from dotenv import load_dotenv
load_dotenv(override=True)

print(getenv("SECRET_API_TOKEN"))
