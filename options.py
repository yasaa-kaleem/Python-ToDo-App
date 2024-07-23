import actions

def select_option(selected_option, task_dict):
    if selected_option == "1":
        actions.view_dict(task_dict)

    elif selected_option == "2":
        actions.add_item(task_dict)

    elif selected_option == "3":
        actions.remove_item(task_dict)

    elif selected_option == "4":
        actions.update_item_status(task_dict)
    
    elif selected_option == "5":
        actions.edit_task(task_dict)

def show_options():
    print("\nWhat would you like do to?")
    print("Enter 1: View To-Do List")
    print("Enter 2: Add a task")
    print("Enter 3: Remove a task")
    print("Enter 4: Mark task as Complete")
    print("Enter 5: Edit a task")
    print("Enter 0: To Exit")