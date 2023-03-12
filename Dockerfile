FROM python:3.10

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

COPY ./ /app

CMD ["python", "run.py"]

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