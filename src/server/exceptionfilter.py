from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.status import HTTP_404_NOT_FOUND
from starlette.status import HTTP_409_CONFLICT
from starlette.status import HTTP_500_INTERNAL_SERVER_ERROR

from src.exceptions.exceptions import UserAlreadyExists
from src.exceptions.exceptions import UserNotFound


def http_404_form_submission_not_found(request: Request, exception: UserNotFound):
    return JSONResponse(status_code=HTTP_404_NOT_FOUND, content={"message": f"{str(exception)}"})


def http_409_multiple_form_submissions_found(request: Request, exception: UserAlreadyExists):
    return JSONResponse(status_code=HTTP_409_CONFLICT, content={"message": f"{str(exception)}"})


def http_500_unknown_exception(request: Request, exception: Exception):
    return JSONResponse(status_code=HTTP_500_INTERNAL_SERVER_ERROR, content={"message": f"Unknown Error Occurred!"})


def register_exception_filter(app: FastAPI):
    app.add_exception_handler(UserNotFound, http_404_form_submission_not_found)
    app.add_exception_handler(UserAlreadyExists, http_409_multiple_form_submissions_found)
    app.add_exception_handler(Exception, http_500_unknown_exception)
