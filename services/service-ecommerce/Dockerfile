ARG PYTHON_VERSION=3.10.2
FROM python:${PYTHON_VERSION}-slim as base

WORKDIR /usr/local/app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY ./app ./app

CMD ["python", "./app/serviceEcommerce.py"]