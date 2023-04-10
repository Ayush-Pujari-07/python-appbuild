def get_todos(filepath="Experimetn/file.txt"):
    with open(filepath, "r") as file:  # this with context manager method will not make us close
            # the opened file if we use this way to open a file.
            todos_local = file.readlines()
    return todos_local

def write_todos(filepath, todos_arg):
    with open(filepath, "w") as file:
        file.writelines(todos_arg)

def todo_():

    file_path = "Experimetn/file.txt"

    while True:
        # Get user input and strip space characters.
        user_action = input("Type 'Add', 'Show', 'Complete', 'Edit' or 'Exit': ").lower()
        user_action = user_action.strip()

        # add
        if user_action.startswith("add"):
            # todos = input('Enter the todos: ') + "\n"  # This will merge \n with the user inputs todos and wll add a
            # break line to it
            todo = user_action[4:]

            # Open the file and then read the present content in the file and then store it into the file aging
            # by creating a new one.
            todos = get_todos()

            todos.append(todo+ "\n")

            # Save the data into a file so the data cant be lost when the interpreter is closed.
            write_todos(file_path, todos)

        # Show
        elif user_action.startswith("show"):  # if any of the one is matched then will show the output

            # with open("Experimetn/file.txt", 'r') as file:  # by default the open function  mode= read 'r' for file
            #     # handling.
            #     todos = file.readlines()
            
            todos = get_todos()
            
            # file.close() no need to use close() while using with-context-manager
            # new_items = [item.strip('\n') for item in todos] one of the lists comprehend method for removing \n
            # from the lists items
            for index, items in enumerate(todos):
                items = items.strip("\n")
                rows = f"{index + 1}-{items}"
                print(rows)

        # Edit
        elif user_action.startswith("edit"):
            
            number = int(user_action[5:])
            number = number - 1  # as index count start from Zero

            todos = get_todos()

            if number < len(todos):
                new_todo = input("Enter the new todo: ")
                todos[number] = new_todo + "\n"  # this will enter the new data entered byt the user
            else:
                print("Kindly provide the valid number!!")

            write_todos(file_path, todos)


        # Complete
        elif user_action.startswith("complete"):
            number = int(user_action[9:])

            # with open("Experimetn/file.txt", "r") as file:  # writing the code this way will not want us to close
            #     # the file it will automatically be,
            #     todos = file.readlines()
            todos = get_todos()

            index = number - 1
            to_remove = todos[index].strip("\n")  # would strip \n from the item that's to be removed from the list.
            todos.pop(index)  # Will delete the finished task from the list.

            # with open("Experimetn/file.txt", "w") as file:  # Will Store the unfinished task
            #     file.writelines(todos)
            write_todos(file_path, todos)

            message = f"Todo '{to_remove}' was removed from the list."
            print(message)

            # if  _ in user_action:  # if any other input other than add, dispy, complete, show, exit.
            # print('Hey, you entered an unknown command!!')
        elif user_action.startswith("exit"):
            break

        else:
            print("Command is not valid.")

    print("Bye!!! C you Soon...")


# calling the function to execute the code.
todo_()


def file_zipping():
    content = ["This is first content", "This is second content", "This is Third content"]

    filenames = ["doc.txt", "report.txt", "presentation.txt"]

    for content, filenames in zip(content, filenames):  # zip will zip and combine the both list with their respective
        # index value.
        file = open(f"C:\\Users\\Ayush K Pujari\\PycharmProjects\\pythonProject\\Experimetn\\{filenames}", "w+")
        file.writelines(content)
        file.close()


# Example of list comprehension
def examples_todo_app():
    filename = ["1.dox", "2.report", "3.presentation"]
    print([file.replace(".", "-") + ".txt" for file in filename])

    names = ["john smith", "jay santi", "eva kuki"]
    print([name.title() for name in names])
    usernames = ["john 1990", "alberta1970", "magnola2000"]
    print([len(name) for name in usernames])
    user_var = ['10', '19.1', '20']
    print([float(var) for var in user_var])


# examples_todo_app()

def bug_fixer_exercise():
    temperatures = [10, 12, 14]
    file = open("Experimetn/file.txt", 'w')
    file.writelines([str(temp) + "\n" for temp in temperatures])
    file.close()
    numbers = [10.1, 12.3, 14.7]
    numbers = [int(item) for item in numbers]
    print(numbers)


# bug_fixer_exercise()

def journal_bonus():
    date = input("Enter today's date: ")
    mood = input("How do you rate your Mood today from 1 to 10: ")
    journal = input("Lets your thoughts flow:\n")
    with open(f"{date}.txt", "w") as file:
        file.write(f"My Mood is {mood} of 10 Today!!\n")  # could also be written as 2 * \n for 2 line break
        file.writelines(journal)

# journal_bonus()
