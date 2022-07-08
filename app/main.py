from fastapi import FastAPI, status
from typing import Dict


app = FastAPI(title="😸Pets API🐶",
              version="0.0.1",
              description="Public API to have fun and share knowledge about our domestic pets. 😸🐤🐶")


@app.get(path="/",
         tags=['Index'],
         status_code=status.HTTP_200_OK)
def index() -> Dict[str, str]:
    return {
        "Hello": "Pet lovers"
    }
