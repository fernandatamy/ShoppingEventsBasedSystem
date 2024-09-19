ARG PYTHON_VERSION=3.10.2
FROM python:${PYTHON_VERSION}-slim as base

WORKDIR /usr/local/app

# Install the application dependencies
COPY requirements.txt ./
RUN pip install -r requirements.txt

# Copy in the source code
COPY ./app ./app

CMD ["python", "./app/serviceshipping.py"]