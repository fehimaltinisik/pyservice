from io import BytesIO

import fitz  # noqa
from PIL import Image
from PIL import Image
from matplotlib.figure import Figure

from src.models import Name


def figure_to_bytes(fig: Figure, fmt: str = 'png', dpi: int = 300) -> BytesIO:
    buf = BytesIO()
    fig.savefig(buf, format=fmt, dpi=dpi)
    buf.seek(0)

    return buf


def bytes_to_png_image(raw_images):
    images = [Image.open(image) for image in raw_images]
    widths, heights = zip(*(i.size for i in images))

    total_width = max(widths)
    max_height = sum(heights)

    new_im = Image.new('RGB', (total_width, max_height))

    y_offset = 0
    for im in images:
        new_im.paste(im, (0, y_offset))
        y_offset += im.size[1]

    ims = BytesIO()
    new_im.save(ims, format="png")
    ims.seek(0)

    return ims


def bytes_to_pdf(buf):
    document = fitz.Document(filetype='pdf')
    for image in buf:
        pdf_bytes = fitz.Document(filetype='png', stream=image).convert_to_pdf()
        pdf_page = fitz.Document(filetype='pdf', stream=pdf_bytes)
        document.insert_pdf(pdf_page)

    return document.convert_to_pdf()


def pdf_file_name_from_email(email: str, assessment_name: str) -> str:
    return "{0}-{1}.pdf".format(email, assessment_name.lower().replace(' ', '-'))


def pdf_file_name_from_name(name: Name, assessment_name: str) -> str:
    return "{0}-{1}-{2}.pdf".format(name.first, name.last, assessment_name.lower().replace(' ', '-'))


def save_image(image_name, image_bytes):
    image = Image.open(image_bytes)
    image.save(f"{image_name}.png")
