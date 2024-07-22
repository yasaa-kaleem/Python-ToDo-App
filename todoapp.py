'''Build a simple command-line To-Do list application where users can add, remove, view, and mark tasks completed.'''

#Room 7- Hamzeh Hamad, Stephen Druessl, Yasaa Kaleem

task_dict = {}

def throw_error(user_input, expected_input):
    while user_input not in expected_input:
        user_input = input("Wrong input, Please try again!: ")
        
    return user_input
            
def view_dict():
    if len(task_dict) > 0:
        for k, v in task_dict.items():
            print(f"{k, v}")
    else:
        print("Nothing in To-Do list")

def add_item():
    add_task = input("What task would you like to add to the To-Do List? ")
    task_dict[add_task] = "Pending"
    print(task_dict)

def remove_item():
    print(task_dict)
    remove_task = input("Which task would you like to remove? ")
    task_dict.pop(remove_task)
    print(task_dict)

def update_item_status():
    print(task_dict)
    complete_task = input("Which task would you like to mark as Complete? ")
    task_dict[complete_task] = "Completed"
    print(task_dict)

def edit_task():
    print(task_dict)
    complete_task = input("Which task would you like to Edit? ")
    new_key_name = input("What would you like to rename it to? ")

    temp_val = task_dict[complete_task]
    task_dict[new_key_name] = temp_val
    del task_dict[complete_task]
    print(task_dict)

def to_do_list(select_option):
    if select_option == "1":
        view_dict()

    elif select_option == "2":
        add_item()

    elif select_option == "3":
        remove_item()

    elif select_option == "4":
        update_item_status()
    
    elif select_option == "5":
        edit_task()

def show_options():
    print("What would you like do to?")
    print("Enter 1: View To-Do List")
    print("Enter 2: Add a task")
    print("Enter 3: Remove a task")
    print("Enter 4: Mark task as Complete")
    print("Enter 5: Edit a task")
        
def start_program():
    print("===== Welcome to your TO-DO List APP! =====")
    continue_program = ""

    while continue_program != "N":
        show_options()
        select_option = input("Enter Here: ")
    
        to_do_list(select_option)
        continue_program = input("Would you like to do something else?\nN ---> Exit ---- Any other key ---> Continue: ").upper()
    
    print("Exiting program")

start_program()