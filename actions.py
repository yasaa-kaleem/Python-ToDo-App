def view_dict(task_dict):
    if len(task_dict) > 0:
        for k, v in task_dict.items():
            print(f"{k, v}")
    else:
        print("To-Do list is Empty! Please Add Items to the list to view!")

def add_item(task_dict):
    add_task = input("What task would you like to add to the To-Do List? ")
    task_dict[add_task] = "Pending"
    view_dict(task_dict)

def remove_item(task_dict):
    view_dict(task_dict)
    remove_task = input("Which task would you like to remove? ")
    task_dict.pop(remove_task)
    view_dict(task_dict)

def update_item_status(task_dict):
    view_dict(task_dict)
    complete_task = input("Which task would you like to mark as Complete? ")
    task_dict[complete_task] = "Completed"
    view_dict(task_dict)

def edit_task(task_dict):
    view_dict(task_dict)
    complete_task = input("Which task would you like to Edit? ")
    new_key_name = input("What would you like to rename it to? ")

    temp_val = task_dict[complete_task]
    task_dict[new_key_name] = temp_val
    del task_dict[complete_task]
    view_dict(task_dict)