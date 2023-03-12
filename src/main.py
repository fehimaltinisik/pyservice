from fastapi import FastAPI
from starlette.responses import RedirectResponse

from src.logging import configure_logger
from src.routers import k8s_router
from src.routers import user_router
from src.server.exceptionfilter import register_exception_filter

configure_logger()

app = FastAPI(title="PyService", docs_url="/docs")

register_exception_filter(app)

app.include_router(k8s_router)
app.include_router(user_router)


@app.get("/")
async def redirect_to_docs():
    response = RedirectResponse(url="/docs")

    return response
