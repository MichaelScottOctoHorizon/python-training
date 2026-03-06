#This function accepts as parameters a string: name, int: age and string: city and prints it to the console
def display_formatted_sentence(name, age, city):

    print("\n----------------------USER DETAILS---------------------------\n")
    print(f"\tName: {name}")
    print(f"\tAge: {age}")
    print(f"\tCity: {city}")
    print(f"\n\t{name} is {age} years of age and lives in the city of {city}")
    print("\n----------------------USER DETAILS---------------------------\n\n")

#This function accepts input from the user and converts it to a integer number type
def display_and_accept_user_input():

    user_number = input("Enter a number ")
    
    try:
        user_number = int(user_number)
        print(f"{user_number} is {type(user_number)}")
    except ValueError:
        print(f"{user_number} cannot be converted to an integer")


def add_two_string_numbers(num_1, num_2):
    try:
        sum = int(num_1) + int(num_2)
        print(f"{num_1} + {num_2} = {sum}")
    except ValueError:
        print("One or More value is not a valid number")

display_formatted_sentence("Michael Scott", 32, "Bodden Town")
display_and_accept_user_input()
add_two_string_numbers("15", "17")