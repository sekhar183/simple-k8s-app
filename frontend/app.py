from flask import Flask, request, jsonify
import mysql.connector
import os

app = Flask(__name__)

# Get MySQL connection details from environment variables
MYSQL_HOST = os.getenv('MYSQL_HOST')
MYSQL_USER = os.getenv('MYSQL_USER')
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')
MYSQL_DATABASE = os.getenv('MYSQL_DATABASE')

# Database connection
def get_db_connection():
    print(MYSQL_HOST,MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE )
    connection = mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DATABASE
    )
    return connection

@app.route('/')
def home():
    return "Welcome to the Python MySQL Frontend!"

@app.route('/add', methods=['POST'])
def add_data():
    data = request.json
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (data['name'], data['email']))
    connection.commit()
    cursor.close()
    connection.close()
    return jsonify({"message": "Data added successfully!"})

@app.route('/get', methods=['GET'])
def get_data():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify(users)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
