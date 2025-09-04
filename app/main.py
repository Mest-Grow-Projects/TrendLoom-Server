from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from app.database.db import init_db
from app.core.constants import messages, origins
from app.core.logging_config import logger
from app.auth.auth_route import router as auth_router
from app.products.products_routes import router as products_router
from app.users.users_route import router as users_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    logger.info(messages["db_connection"])

    try:
        yield
    finally:
        logger.info(messages["shutdown"])

app = FastAPI(
    title=messages["app_title"],
    description=messages["app_description"],
    version=messages["app_version"],
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get(
    "/",
    tags=["App"],
    summary="Application base route"
)
def read_root():
    return messages["welcome"]

app.include_router(auth_router, prefix="/api")
app.include_router(products_router, prefix="/api")
app.include_router(users_router, prefix="/api")