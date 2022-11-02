import mysql.connector
from config import HOST, DATABASE, USERNAME, PASSWORD

def db_connect():
    connection = mysql.connector.connect(
                host = HOST,
                database = DATABASE,
                user = USERNAME,
                password = PASSWORD)
    return connection

def add_note(connection):
    cursor = connection.cursor()
    note = input("\nNote:\n")
    query = "INSERT INTO notes (note) VALUES (%s)"
    cursor.execute(query, (note,))
    connection.commit()

def edit_note(connection):
    cursor = connection.cursor()
    edit_sql = "UPDATE notes SET"
    cursor.execute(edit_sql)
    final_results = cursor.fetchone()
    connection.commit()

def delete_note(connection):
    cursor = connection.cursor()
    delete_query = "DELETE FROM notes WHERE id = "
    cursor.execute(delete_query)
    print("deleted")
    connection.commit()

def display_notes(cursor):
    cursor.execute()
    all_notes = cursor.fetchall()

def main():
    connection = db_connect()
    while True:
        user_action = input("\nPlease specify action: [View, Add, Edit, Delete, Exit]\n")
        if user_action.lower() == "view":
            display_notes(connection)
        elif user_action.lower() == "add":
            add_note(connection)
        elif user_action.lower() == "edit":
            edit_note(connection)
        elif user_action.lower() == "delete":
            delete_note(connection)
        elif user_action.lower() == "exit":
            break
        else:
            print("Please type a valid input")

if __name__ == '__main__':
    main()