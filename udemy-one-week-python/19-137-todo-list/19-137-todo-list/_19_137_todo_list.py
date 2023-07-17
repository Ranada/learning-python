def print_header():
    header = """
     _______        __           
     |_   _|__   __| | ___  ___ 
       | |/ _ \ / _` |/ _ \/ __|
       | | (_) | (_| | (_) \__ \\
       |_|\___/ \__,_|\___/|___/
    """
    print(header)

def print_todos(todos):
    for i, todo in enumerate(todos):
        print(f"{i + 1}) {todo}")
    print()

def print_completed(completed):
    print(f"You completed {len(completed)} tasks:")
    for todo in completed:
        print(f"* {todo}")
    print()

def print_help_menu():
    menu = """
TODO LIST HELP
Type 'q' to quit
To add a todo to the list, type it and hit enter
To complete a todo enter its number
"""
    print(menu)

def create_todos():
    todos = []
    completed = []
    divider = "*" * 100
    entry = ''

    while entry != 'q' or entry != 'quit':
        print(divider)
        entry = input("Enter a command. Type 'h' for help:\n")
        if ord(entry[0]) >= ord('0') and ord(entry[0]) <= ord('9'):
            num = int(entry) - 1
            task = todos.pop(num)
            completed.append(task)
        elif entry == 'h':
            print_help_menu()
            continue
        elif entry == 'q' or entry == 'quit':
            print_completed(completed)
            return
        else:
            todos.append(entry)
        print_todos(todos)

print_header();
create_todos()
