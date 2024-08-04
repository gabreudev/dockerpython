import mysql.connector
from flask import Flask, request, jsonify

app = Flask(__name__)

def connect_to_db():
    connection = mysql.connector.connect(
        user='root', password='root', host='mysql', port="3306", database='db')
    return connection

@app.route('/students', methods=['GET'])
def list_students():
    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM students')
    students = cursor.fetchall()
    connection.close()

    students_list = [{'ID': student[0], 'FirstName': student[1], 'Surname': student[2]} for student in students]
    return jsonify(students_list)

@app.route('/students', methods=['POST'])
def add_student():
    data = request.json
    first_name = data.get('first_name')
    surname = data.get('surname')

    if not first_name or not surname:
        return jsonify({"error": "First name and surname are required"}), 400

    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.execute('INSERT INTO students (FirstName, Surname) VALUES (%s, %s)', (first_name, surname))
    connection.commit()
    connection.close()

    return jsonify({"message": "Student added successfully!"}), 201

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
