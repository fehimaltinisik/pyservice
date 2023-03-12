from enum import Enum


class Media(str, Enum):
    PDF: str = "application/pdf"
    IMAGE_PNG: str = "image/png"
