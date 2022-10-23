# Simple To-Do list

# Users list of tasks
user_list = []

#1 Add tasks
def add_task(task):
    while True:
        user_list.append(task)
        # print(user_list)
        ans = input("\nWant to add more?\n")
        if ans == "yes":
            task = input("\nWhat to do?:\n")
        new_list = '\n'.join(user_list)
        if ans == 'no':
            ans = False
            break
    print(new_list)


# Edit tasks
def edit_task():
    pass

# Delete tasks
def delete_task():
    pass

# Users view of tasks
def display_tasks():
    pass

def main():
    user_task = input("\nWhat to do?:\n")
    add_task(user_task)
    edit_task()
    delete_task()
    display_tasks()


if __name__ == '__main__':
    main()