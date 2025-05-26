FROM python:3.10.2

# Set the working directory inside the container
WORKDIR /usr/src/app

# Install yfinance using pip
RUN pip install --no-cache-dir yfinance

# Copy the Python script into the container
COPY yfin.py .

# Define the command to run the script
CMD ["python", "yfin.py"]