from fastapi import FastAPI, status
from .routers import facts_router, pets_router, users_router

from typing import Dict


app = FastAPI(title="😸Pet Facts API🐶",
              version="0.0.1",
              description="Public API to have fun and share knowledge about our domestic pets. 😸🐤🐶")


app.include_router(facts_router.router, prefix="/api/v1")
app.include_router(pets_router.router, prefix="/api/v1")
app.include_router(users_router.router, prefix="/api/v1")


@app.get(path="/", tags=['Index'], status_code=status.HTTP_200_OK)
def index() -> Dict[str, str]:
    return {"Hello": "Pet lovers"}
