
#Gets the user's name and age as inputs and converts them to valid data types, also capitalizes the name in a title format
def set_user_data():
    name = input("Enter your name: ").title()
    age = input("Enter your age as a number: ")

    try:
        print(f"Name: {name}\n")
        print(f"Age: {int(age)}")
    except ValueError:
        print(f"{age} is not a valid age number! Re-enter details. \n\n")
        set_user_data()


set_user_data()