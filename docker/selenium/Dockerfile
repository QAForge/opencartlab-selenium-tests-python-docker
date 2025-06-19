FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY ../../requirements.txt .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code into the container
COPY ../../src ./src
COPY ../../tests ./tests

# Set the entry point for the container
CMD ["pytest", "./tests"]