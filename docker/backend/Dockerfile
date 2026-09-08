# Backend Dockerfile for KKEVO STUDIO MEDIA
FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install python dependencies
COPY backend/requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend code
COPY backend/ /app/

# Expose Django port
EXPOSE 8000

CMD ["gunicorn", "kkevo_project.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "4"]
