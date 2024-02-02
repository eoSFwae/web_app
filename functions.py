def get_todos(filepath='todoreal.txt'):
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos


def write_todos(todos_arg, filepath='todoreal.txt'):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)