# NOTE name need to be Dockerfile
FROM python:3.9

# Install dependencies
RUN pip install mysql-connector-python flask

WORKDIR /usr/app/src

# Copy the application code
COPY hello_world.py ./

# Set the command to run the Flask application
CMD ["python", "hello_world.py"]
