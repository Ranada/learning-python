def print_header():
    header = """
     _______        __           
     |_   _|__   __| | ___  ___ 
       | |/ _ \ / _` |/ _ \/ __|
       | | (_) | (_| | (_) \__ \\
       |_|\___/ \__,_|\___/|___/
    """
    print(header)


def create_todos():
    todos = []
    completed = []
    divider = "*" * 100
    print(divider)
    entry = input("Enter a command. Type 'h' for help:\n")

    if entry == 'q' or entry == 'quit':
        print("Print completed todos here.")
        return

    while entry != 'q' or entry != 'quit':
        todos.append(entry)

print_header();
create_todos()
