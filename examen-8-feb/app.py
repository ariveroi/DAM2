from flask import Flask, request, Response
import json

import mysql.connector

credentials = {
    'username': 'admin',
    'password': 'Retamarc-17',
    'dbname': 'dam1',
    'host': 'database-1.c7jleccanpci.eu-west-2.rds.amazonaws.com'
}

app = Flask(__name__)

mock_data = [
    {
        'id': 0,
        'username': '',
        'email': '',
        'date_birth': '',
        'password': ''
    },
    {
        'id': 1,
        'username': '',
        'email': '',
        'date_birth': '',
        'password': ''
    },
    {
        'id': 2,
        'username': '',
        'email': '',
        'date_birth': '',
        'password': ''
    }
]

def get(query):
    cnx = mysql.connector.connect(
        user=credentials["username"],
        password=credentials["password"],
        host=credentials["host"],
        database=credentials["dbname"],
    )
    # Create a cursor
    cursor = cnx.cursor()
    # Execute the SELECT query
    
    cursor.execute(query, )
    # Fetch all the rows
    rows = cursor.fetchall()
    # Iterate through the rows and print the products
    # Close the cursor and the connection
    cursor.close()
    cnx.close()
    return rows

@app.route('/registro', methods=['POST'])
def register_users():
    data = json.loads(request.data.decode('utf-8'))
    print(data)
    # TODO: insert en BBDD
    return "ok"

@app.route('/getUsers')
def get_all_users():
    # TODO: Llamada a base de datos
    # Connect to the database
    q = "SELECT * FROM new_table"
    rows = get(q)
    return rows

@app.route('/user/<id>')
def get_user(id):
    id = int(id)
    # Recorremos mock data
    cnx = mysql.connector.connect(
        user=credentials["username"],
        password=credentials["password"],
        host=credentials["host"],
        database=credentials["dbname"],
    )
    # Create a cursor
    cursor = cnx.cursor()
    # Execute the SELECT query
    q = 'SELECT * FROM new_table WHERE id=%s'
    cursor.execute(q, (id,))
    # Fetch all the rows
    rows = cursor.fetchall()
    # Iterate through the rows and print the products
    # Close the cursor and the connection
    cursor.close()
    cnx.close()
    
    return rows
    # return "Not found" #TODO: Error 404
    # TODO: query a base datos con el id

@app.route('/login', methods=['POST'])
def login():
    data = json.loads(request.data.decode('utf-8'))
    # TODO: query BBDD
    for user in mock_data:
        if user['username'] == data['username'] and user['password'] == data['password']:
            print('Aut')
            return 'ok'
    return Response('Unauthorized', status=401)