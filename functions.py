# functions with argument
FILEPATH = 'Tasks.txt'

def get_tasks(filepath=FILEPATH):
    # doc strings
    """Read a text file and return
    the number of to-do list"""

    with open(filepath, 'r') as file_local:
        tasks_local = file_local.readlines()
    return tasks_local


def write_tasks(tasks_arg, filepath=FILEPATH):
    # doc strings
    """ Write the to-do item lists in text file"""
    with open(filepath, 'w') as file:
        file.writelines(tasks_arg)


print(__name__)

if __name__ == "__main__":
    print('Hello')
    print(get_tasks())
