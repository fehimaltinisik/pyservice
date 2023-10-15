from contextlib import asynccontextmanager

from fastapi import FastAPI
from starlette.responses import RedirectResponse
from src.clients import HTTPClient
from src.clients import SQLiteClient
from src.config.logging import configure_logger
from src.routers import user_router
from src.routers import order_router
from src.server.exceptionfilters import register_exception_handlers

configure_logger()


@asynccontextmanager
async def lifespan(_: FastAPI):
    await HTTPClient.init()
    SQLiteClient.init()

    yield

    await HTTPClient.close()
    SQLiteClient.close()

app = FastAPI(
    title="PyService",
    docs_url="/docs",
    lifespan=lifespan)


register_exception_handlers(app)

app.include_router(user_router)
app.include_router(order_router)


@app.get("/")
async def redirect_to_docs():
    response = RedirectResponse(url="/docs")

    return response
