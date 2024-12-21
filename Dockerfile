# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Install Poetry
# Poetry provides its own mechanism for managing Python virtual environments and dependencies.
ENV POETRY_VERSION=1.7.1
RUN pip install "poetry==$POETRY_VERSION"

# Copy only the necessary files to install dependencies
# This layer will be cached and only re-built if these files change.
COPY pyproject.toml poetry.lock* ./

# Install project dependencies
RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi

# Copy the rest of your application's code
COPY . .

# Make port available to the world outside this container
# Expose any port if your application is a web application
EXPOSE 5002

# Define environment variable
# ENV NAME World

# Run calculator_cli.py when the container launches
CMD ["python", "./cicd_intro/app.py"]
