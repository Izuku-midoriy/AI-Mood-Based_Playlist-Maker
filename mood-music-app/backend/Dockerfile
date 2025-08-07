# Use official Python image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Create working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy source code
COPY . .

# Expose port (Render uses 0.0.0.0:$PORT)
ENV PORT 10000
EXPOSE $PORT

# Start server
CMD gunicorn app:app --bind 0.0.0.0:$PORT
