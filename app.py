from fastapi import FastAPI
from routes.user import user
from docs import tags_metadata

app = FastAPI(
        title="REST API with FastAPI and Mongodb",
        description="this a simple REST API",
        version="0.0.1",
        openapi_tags=tags_metadata
)

app.include_router(user)
