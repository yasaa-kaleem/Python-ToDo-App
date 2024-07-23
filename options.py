import actions

def select_option(select_option, task_dict):
    if select_option == "1":
        actions.view_dict(task_dict)

    elif select_option == "2":
        actions.add_item(task_dict)

    elif select_option == "3":
        actions.remove_item(task_dict)

    elif select_option == "4":
        actions.update_item_status(task_dict)
    
    elif select_option == "5":
        actions.edit_task(task_dict)

def show_options():
    print("What would you like do to?")
    print("Enter 1: View To-Do List")
    print("Enter 2: Add a task")
    print("Enter 3: Remove a task")
    print("Enter 4: Mark task as Complete")
    print("Enter 5: Edit a task")