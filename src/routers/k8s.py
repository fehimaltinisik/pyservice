from fastapi import APIRouter

router = APIRouter(prefix="/k8s")


@router.get("/namespace")
async def get_namespaces():
    """List namespaces"""

    return {"message": "OK!"}
