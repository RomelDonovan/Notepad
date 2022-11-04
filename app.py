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
    try:
        id_num = int(input("Which number would you like to edit?: "))
        new_note = input("New Note: ")
        query = "UPDATE notes SET note = %s WHERE id = %s"
        cursor.execute(query, (new_note,id_num))
        connection.commit()
    except:
        print("Sorry invalid number.")

def delete_note(connection):
    cursor = connection.cursor()
    try:
        delete_id = input("Please enter the number you want to delete: ")
        query = "DELETE FROM notes WHERE id = %s" 
        cursor.execute(query, (delete_id,))
        print("Deleted!")
        connection.commit()
    except:
        print("Sorry invalid number.")

def display_notes(connection):
    cursor = connection.cursor()
    num_list = 0
    query = "SELECT note FROM notes"
    cursor.execute(query)
    all_notes = cursor.fetchall()
    for note in all_notes:
        num_list += 1
        # print(num_list)
        print(f"{str(num_list)}. {''.join(note)}")
        # view_list = num_list + note
        # print(view_list)

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