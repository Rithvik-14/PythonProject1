FILEPATH = "todos.txt"
def get_todo(filepath=FILEPATH):
    """
    REad a text file ad return the list of the to-do items
    """
    with open(filepath, 'r') as file:
        todos_func = file.readlines()
    return todos_func


def write_todo(todos_arg,filepath=FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

if __name__ == "__main__":
    print("Hello")
    print(get_todo())