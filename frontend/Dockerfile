# Use Python official image as a base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt
ENV MYSQL_HOST="mysql-service"
ENV MYSQL_USER="root"
ENV MYSQL_PASSWORD="password"
ENV MYSQL_DATABASE="test_db"
# Copy the rest of the application code into the container
COPY . .

# Expose the port the Flask app will run on (5000)
EXPOSE 5000

# Set environment variables for Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Run the Flask application
CMD ["flask", "run"]
