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

    students_list = [{'ID': student[0], 'nome': student[1], 'sobre_nome': student[2]} for student in students]
    return jsonify(students_list)

@app.route('/students', methods=['POST'])
def add_student():
    data = request.json
    nome = data.get('nome')
    sobre_nome = data.get('sobre_nome')

    if not nome or not sobre_nome:
        return jsonify({"error": "nome e sobre nome obrigatorios"}), 400

    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.execute('INSERT INTO students (nome, sobre_nome) VALUES (%s, %s)', (nome, sobre_nome))
    connection.commit()
    connection.close()

    return jsonify({"message": "estudante adicionado!"}), 201

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
