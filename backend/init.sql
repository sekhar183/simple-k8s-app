CREATE DATABASE IF NOT EXISTS test_db;

USE test_db;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100)
);

-- Create the user with a password (if it doesn't already exist)
CREATE USER IF NOT EXISTS 'root'@'10.%' IDENTIFIED BY 'password';

-- Grant privileges to the user
GRANT ALL PRIVILEGES ON *.* TO 'root'@'10.%';
GRANT ALL PRIVILEGES ON *.* TO 'root'@'localhost' IDENTIFIED BY 'password';
-- Reload privilege tables
FLUSH PRIVILEGES;
