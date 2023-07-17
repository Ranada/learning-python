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

def print_completed(completed_todos):
    print(f"You completed {len(completed_todos)} tasks.")
    for todo in completed_todos:
        print(f"* {todo}")

def create_todos():
    todos = []
    completed_todos = []
    divider = "*" * 100
    print(divider)
    entry = ''

    while entry != 'q' or entry != 'quit':
        entry = input("Enter a command. Type 'h' for help:\n")
        if entry == 'q' or entry == 'quit':
            print("Print completed todos here.")
            print_completed(completed_todos)
            return
        todos.append(entry)
        print_todos(todos)

print_header();
create_todos()
