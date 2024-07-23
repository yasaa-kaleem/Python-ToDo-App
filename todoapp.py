'''Build a simple command-line To-Do list application where users can add, remove, view, and mark tasks completed.'''

#Room 7- Hamzeh Hamad, Stephen Druessl, Yasaa Kaleem

import options
        
def start_program():
    print("===== Welcome to your TO-DO List APP! =====")
    task_dict = {}
    continue_program = ""

    while continue_program != "N":
        options.show_options()
        select_option = input("Enter Here: ")
    
        options.select_option(select_option, task_dict)
        continue_program = input("Would you like to do something else?\nN ---> Exit ---- Any other key ---> Continue: ").upper()
    
    print("Exiting program")