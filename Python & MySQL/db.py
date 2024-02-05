import mysql.connector

config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'studentdb'
}

db = mysql.connector.connect(**config)

cursor = db.cursor()