from uuid import uuid4

target = str(uuid4())
with open(".env", "a") as file:
    file.write(f"\nSECRET_API_TOKEN=\"{target}\"")

from dotenv import load_dotenv
load_dotenv(override=True)
from os import getenv

current = getenv("SECRET_API_TOKEN")

if target == current:
    token = current
    print(f"SECRET_API_TOKEN was successfully set to \"{token}\".")
else:
    print(f"SECRET_API_TOKEN was unsuccessfully set. It is currently \"{current}\", when target was \"{target}\".\nShutting down...")
    quit()