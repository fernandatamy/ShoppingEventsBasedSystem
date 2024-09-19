ARG PYTHON_VERSION=3.10.2
FROM python:${PYTHON_VERSION}-slim as base

WORKDIR /usr/local/app

# Install the application dependencies
COPY requirements.txt ./
RUN pip install -r requirements.txt

# Copy in the source code
COPY ./app ./app

# # Setup an app user so the container doesn't run as the root user
# RUN useradd app
# USER app

# CMD ["app.main:app", "--host", "0.0.0.0", "--port", "8080"]

CMD ["python", "./app/serviceEcommerce.py"]