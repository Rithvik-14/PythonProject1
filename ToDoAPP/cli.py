#from functions import get_todo,write_todo
import functions
import time


now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is",now)
while True:
    user_action = input('Type add , show, edit, complete or exit: ')
    user_action = user_action.strip()  # for removing extra space if user adds in input

    if user_action.startswith("add"):
        todo = user_action[4:] + "\n"

        todos = functions.get_todo()        # function call for reading the todos file.

        todos.append(todo)  # append only goes with list type.

        functions.write_todo(todos, 'todos.txt')

       # file = open('todos.txt', 'w')
       # file.writelines(todos)
       # file.close()

    elif user_action.startswith("show"):
        todos = functions.get_todo()

    #   new_item = [item.strip('\n') for item in todos]
        for index, item in enumerate(todos, 1):  # added 1 here to show for user listing starts from 1.
            item = item.capitalize()
            item = item.strip('\n')
            print(f'{index}-{item}')  # or we can do index +1 here also
    # result = ' '.join(todos)
    # print(result)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            print(number)
            number = number - 1  # this did it bcz user doesn't know python index start from 0.

            todos = functions.get_todo()

            new_todo = input('Enter new todo: ')
            todos[number] = new_todo + "\n"

            functions.write_todo(todos, 'todos.txt')
        except ValueError:
            print('Your command is not valid.')
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = functions.get_todo()
            todo_to_remove = todos[number -1].strip('/n')
            todos.pop(number-1)

            functions.write_todo(todos, 'todos.txt')

            message = f"todo {todo_to_remove} was removes from the list."
            print(message)
        except IndexError:
            print('No item with that number:')
            continue
    elif user_action.startswith("exit"):
        print(todos)
        break
    else:
        print("Invalid Command")

print('Done')
