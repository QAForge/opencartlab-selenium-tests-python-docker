FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the source code into the container
COPY src/ ./src/
COPY tests/ ./tests/

# Set the environment variable for Python unbuffered mode
ENV PYTHONUNBUFFERED=1

# Command to run the tests
CMD ["pytest", "tests/TestSelenium.py"]