# build-in modules
from pathlib import Path
import os

def dotenv():

    PROJECT_ROOT = str(Path(__file__).resolve().parent.parent.parent)

    envFile = open(PROJECT_ROOT + "/.env", "r")

    if not envFile.readable():
        print(".env file in not read mode")
    else:
        for line in envFile.readlines():
            if line.startswith("#"):
                continue
            elif len(line) == 0:
                continue
            else:
                key, value = line.rstrip("\n").split("=")
                os.environ.setdefault(key, value)
    
    envFile.close()