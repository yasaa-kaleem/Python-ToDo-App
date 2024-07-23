import options, errors
        
def start_program():
    print("\n\t\t\t===== Welcome to your TO-DO List APP! =====")
    task_dict = {}
    continue_program = ""

    while continue_program != "N":
        options.show_options()
        print("----------------------------")
        selected_option = input("Enter Here: ")
        
        valid_input = errors.check_input(selected_option, ["0", "1", "2", "3", "4", "5"])
    
        if valid_input != "0":
            options.select_option(valid_input, task_dict)
            continue_program = input("\nWould you like to do something else?\nN/Y: ").upper()
        else:
            break
    
    print("\n\t\t\t===== Exiting Program! =====")