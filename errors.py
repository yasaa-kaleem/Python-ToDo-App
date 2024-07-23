#needs to be implemented
def check_input(user_input, expected_input):
    while user_input not in expected_input:
        user_input = input("Wrong input, Please try again!: ")
        
    return user_input