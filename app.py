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
    id_map = display_notes(connection)
    try:
        id_num = int(input("\nPlease enter a number to edit:\n"))
        id = id_map[id_num]
        new_note = input("\nNew Note:\n")
        query = "UPDATE notes SET note = %s WHERE id = %s"
        cursor.execute(query, (new_note, id))
        connection.commit()
    except:
        print("\nPlease input a valid number.\n")

def delete_note(connection):
    cursor = connection.cursor()
    id_map = display_notes(connection)
    try:
        delete_id = int(input("\nPlease enter a number to delete:\n"))
        id = id_map[delete_id]
        query = "DELETE FROM notes WHERE id = %s" 
        cursor.execute(query, (id,))
        print(f"{delete_id}. was Deleted!")
        connection.commit()
    except:
        print("\nPlease input a valid number.\n")

def display_notes(connection):
    cursor = connection.cursor()
    query = "SELECT id, note FROM notes"
    cursor.execute(query,)
    all_notes = cursor.fetchall()
    id_map = {}
    for index, (id, note) in enumerate(all_notes,1):
        note_item = f"{index}. {''.join(note)}"
        id_map[index] = id
        print(note_item)
    return id_map

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
            print("\nPlease type a valid input\n")

if __name__ == '__main__':
    main()