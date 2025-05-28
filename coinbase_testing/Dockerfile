FROM python:3.12-slim

# Set the working directory
WORKDIR /usr/src/app

# Install system dependencies (if needed)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your code
COPY candles.py .
COPY main.py .
# COPY key.json .

# Default command (can be overridden)
CMD ["python3", "main.py"]