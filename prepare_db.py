import mysql.connector
from config import HOST, DATABASE, USERNAME, PASSWORD

connection = mysql.connector.connect(
            host = HOST,
            user = USERNAME,
            password = PASSWORD)
cursor = connection.cursor()

# Create DB
cursor.execute("CREATE DATABASE %s" % DATABASE)
cursor.close()

# Create TABLE (id, note)
connection = mysql.connector.connect(
            host = HOST,
            database = DATABASE,
            user = USERNAME,
            password = PASSWORD)
cursor = connection.cursor()
cursor.execute("CREATE TABLE notes (id INT AUTO_INCREMENT PRIMARY KEY, note TEXT)")