from io import BytesIO
from tempfile import NamedTemporaryFile
from typing import List

from PIL import Image
from fastapi import APIRouter
from fastapi import Body
from fastapi import Depends
from fastapi.responses import FileResponse
from fastapi.responses import StreamingResponse

from src.definitions.webserver import Media
from src.docs.user import CREATE_USER_REQUEST
from src.mappers import io_mapper
from src.mappers import user_mapper
from src.models.httpclient import CreateUserAPIResponse
from src.models.httpclient import GetUserAPIResponse
from src.models.router import CreateUserRequest
from src.models.router import CreateUserResponse
from src.models.router import GetUserByIdResponse
from src.models.router import on_email
from src.models.router import on_user_id
from src.services import user_service

router = APIRouter(prefix='/user', tags=['user'])


@router.post("/id")
async def create_user(
        create_user_request: CreateUserRequest = Body(..., examples=CREATE_USER_REQUEST)) -> CreateUserResponse:
    """Create new user."""
    create_user_api_response: CreateUserAPIResponse = await user_service.create_user(create_user_request)
    create_user_response: CreateUserResponse = user_mapper.map_create_user_api_response_to_create_user_response(
        create_user_api_response)

    return create_user_response


@router.get("/id/{user_id}")
async def get_user_by_id(user_id: int = Depends(on_user_id)) -> GetUserByIdResponse:
    """Get user by id."""
    get_user_api_response: GetUserAPIResponse = await user_service.get_user_by_id(user_id)
    get_user_by_id_response: GetUserByIdResponse = user_mapper.map_get_user_api_response_to_get_user_by_id_response(
        get_user_api_response)

    return get_user_by_id_response


@router.get("/profile-picture")
async def find_users_profile_picture_by_email(email: str = Depends(on_email)):
    """Find user by email and return profile picture.
    Find user by fist and last name combination.
    """

    buf: List[BytesIO] = user_service.find_users_profile_picture_by_email(email)
    image: Image = io_mapper.bytes_to_png_image(buf)

    return StreamingResponse(image, media_type=Media.IMAGE_PNG)


@router.get("/resume")
async def find_users_resume_by_email(email: str = Depends(on_email)):
    """Find user by email and return resume."""
    buf: List[BytesIO] = user_service.find_users_resume_by_email(email)
    pdf = io_mapper.bytes_to_pdf(buf)

    with NamedTemporaryFile(mode="w+b", suffix=".pdf", delete=False) as temporary_pdf_file:
        filename: str = "{0}-resume.pdf".format(email)
        temporary_pdf_file.write(pdf)

        return FileResponse(temporary_pdf_file.name, media_type=Media.PDF, filename=filename)
