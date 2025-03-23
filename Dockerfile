# Dockerfile
FROM python:3.12-alpine

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Install dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r /requirements.txt

# Copy project
WORKDIR /app
COPY . /app/