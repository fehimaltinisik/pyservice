from io import BytesIO
from tempfile import NamedTemporaryFile
from typing import List

from PIL import Image
from fastapi import APIRouter
from fastapi import Depends
from fastapi.responses import FileResponse
from starlette.responses import StreamingResponse

from src.definitions.webserver import Media
from src.models import Name
from src.models import User
from src.schemas.user import inject_email
from src.schemas.user import inject_name
from src.services import user as user_service
from src.view import bytes_to_pdf
from src.view import bytes_to_png_image

router = APIRouter(prefix="/user")


@router.get("/by-name")
async def find_user_by_name(name: Name = Depends(inject_name)):
    """Find user by fist and last name combination."""
    user: User = user_service.find_user_by_name(name)

    return user


@router.get("/age")
async def find_user_by_email_and_return_age(email: str = Depends(inject_email)):
    """Find user by email and return age."""
    age: int = user_service.find_user_by_email_and_calculate_age(email)

    return {"age": age}


@router.get("/profile-picture")
async def find_users_profile_picture_by_email(email: str = Depends(inject_email)):
    """Find user by email and return profile picture."""
    buf: List[BytesIO] = user_service.find_users_profile_picture_by_email(email)
    image: Image = bytes_to_png_image(buf)

    return StreamingResponse(image, media_type=Media.IMAGE_PNG)


@router.get("/resume")
async def find_users_resume_by_email(email: str = Depends(inject_email)):
    """Find user by email and return resume."""
    buf: List[BytesIO] = user_service.find_users_resume_by_email(email)
    pdf = bytes_to_pdf(buf)

    with NamedTemporaryFile(mode="w+b", suffix=".pdf", delete=False) as temporary_pdf_file:
        filename: str = "{0}-resume.pdf".format(email)
        temporary_pdf_file.write(pdf)

        return FileResponse(temporary_pdf_file.name, media_type=Media.PDF, filename=filename)
