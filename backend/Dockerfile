# Use the official MySQL 8.0 image as a base
FROM mysql:8.0

# Set environment variables for MySQL (password, database, etc.)
ENV MYSQL_ROOT_PASSWORD=password
ENV MYSQL_DATABASE=test_db

# Copy custom initialization SQL scripts (optional)
COPY ./init.sql /docker-entrypoint-initdb.d/

# Expose the MySQL default port
EXPOSE 3306

# Command to run MySQL server
CMD ["mysqld"]
