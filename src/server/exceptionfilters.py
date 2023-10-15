from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.status import HTTP_404_NOT_FOUND
from starlette.status import HTTP_409_CONFLICT
from starlette.status import HTTP_500_INTERNAL_SERVER_ERROR

from src.exceptions import order_exceptions
from src.exceptions import user_exceptions


def http_404_order_not_found(request: Request, exception: order_exceptions.OrderNotFound):
    return JSONResponse(status_code=HTTP_404_NOT_FOUND, content={"message": f"{str(exception)}"})


def http_404_user_not_found(request: Request, exception: user_exceptions.UserNotFound):
    return JSONResponse(status_code=HTTP_404_NOT_FOUND, content={"message": f"{str(exception)}"})


def http_409_order_already_exists(request: Request, exception: order_exceptions.OrderAlreadyExists):
    return JSONResponse(status_code=HTTP_409_CONFLICT, content={"message": f"{str(exception)}"})


def http_409_user_already_exists(request: Request, exception: user_exceptions.UserAlreadyExists):
    return JSONResponse(status_code=HTTP_409_CONFLICT, content={"message": f"{str(exception)}"})


def http_500_unknown_exception(request: Request, exception: Exception):
    return JSONResponse(status_code=HTTP_500_INTERNAL_SERVER_ERROR, content={"message": f"Unknown Error Occurred!"})


def register_exception_handlers(app: FastAPI):
    app.add_exception_handler(order_exceptions.OrderNotFound, http_404_order_not_found)
    app.add_exception_handler(order_exceptions.OrderAlreadyExists, http_409_order_already_exists)

    app.add_exception_handler(user_exceptions.UserNotFound, http_404_user_not_found)
    app.add_exception_handler(user_exceptions.UserAlreadyExists, http_409_user_already_exists)

    app.add_exception_handler(Exception, http_500_unknown_exception)
