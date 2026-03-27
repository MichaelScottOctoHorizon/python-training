import random

#This function creates a attractive main heading enclosed in a box for task headings
def task_heading(text):
    border_length = 80
    padding = 2  # spaces after the left border

    border_line = '-' * border_length
    content_width = border_length - 2  # for the two "|"

    padded_text = " " * padding + text
    remaining_space = content_width - len(padded_text)

    print(f"\n{border_line}")
    print("|" + padded_text + " " * remaining_space + "|")
    print(f"{border_line}\n")

#returns number only if the user enters a positive integer number
def get_positive_integer(prompt, allow_zero=False):

    while True:
        user_input = input(f"{prompt} ")
        try:

            user_input = int(user_input)
            
            if user_input <= 0 and allow_zero == False:
                raise ValueError()
            
            return user_input
        except:
            print(f"\n\t{user_input} is not a valid positive number, Please re-enter!")
            user_input = input(f"{prompt} ")

#returns a singular character as input
def get_one_character(prompt):

    while True:
        user_input = input(f"\n\t{prompt} ")

        if len(user_input) == 1:
            return user_input
        else:
            print(f"\t'{user_input}' is not a singular character, Try Again.")

#Helper functions------------------------------------------------------


#1. Print numbers 1 to 20 using a while loop---------------------------------------------------------------
#This function prints numbers 1 to 20 using a while loop
def print_one_to_twenty_while_loop():
    task_heading("1. Print numbers 1 to 20 using a while loop")

    count = 1

    while count <= 20:
        print(f"{count} ", end=" ", flush=True)
        count += 1
    print("\n")

#1. Print numbers 1 to 20 using a while loop---------------------------------------------------------------

#2. Countdown from 10 to 1-------------------------------------------------------------------
#This function decrements to count down from 10 to 1 using a while loop
def countdown_from_ten_to_zero():
    task_heading("2. Countdown from 10 to 1")

    count = 10

    while count >= 1:
        print(f"{count}", end=" ")
        count -= 1
    print()

#2. Countdown from 10 to 1-------------------------------------------------------------------


#3. Sum of digits of a number-------------------------------------------------------------------
#This function sums up each digit in a number together to display it by converting it first to a string and then going through each string digit.
def sum_digits_of_number():
    task_heading("3. Sum of digits of a number")

    user_input = 1234
    number_converted_string = str(user_input)
    sum = 0
    index = 0

    while index < len(number_converted_string):
        sum += int(number_converted_string[index])
        index += 1
    
    print(f"The sum of '{user_input}' is '{sum}'")

#3. Sum of digits of a number-------------------------------------------------------------------

#4. Reverse a number (e.g. 1234 → 4321)-------------------------------------------------------------------
#This function reversed a number by converting it to a string then reversing the string in the while loop
def reverse_number():
    task_heading("4. Reverse a number (e.g. 1234 -> 4321)")

    user_input = 1234
    number_converted_string = str(user_input)
    reversed_number = ""
    index = len(number_converted_string) - 1

    while index >= 0:
        reversed_number += number_converted_string[index]
        index -= 1
    
    print(f"'{user_input}' reversed is '{reversed_number}'")

#4. Reverse a number (e.g. 1234 → 4321)-------------------------------------------------------------------



#5. Check if a number is a palindrome-------------------------------------------------------------------
#This function checks if a number is a palindrome by first converting it to a string and then comparing each character from the end to the start and vice versa
def check_if_palindrome():
    task_heading("5. Check if a number is a palindrome")

    user_input = 1234321
    user_input_text = str(user_input)
    pointer_end = len(user_input_text) - 1
    pointer_start = 0
    is_palindrome = True #It's a palindrome until the loop below detects a difference

    while pointer_start <= pointer_end: #There was no need to check the other numbers because once the pointers were intersecting without detecting a difference the rest is just rechecking the same thing
        if user_input_text[pointer_start] != user_input_text[pointer_end]:
            is_palindrome = False
            break #Once detected a difference no point to check other numbers
        pointer_start += 1 #We are moving from left to right of the letters
        pointer_end -= 1 #We are moving from right to left of the letters
    
    if is_palindrome:
        print(f"\t'{user_input}' is a palindrome.")
    else:
        print(f"\t'{user_input}' is NOT a palindrome.")

#5. Check if a number is a palindrome-------------------------------------------------------------------


#6. Count the number of digits in a number-------------------------------------------------------------------
#This function counts the number of digits of a number using a while loop
def count_number_digits():

    task_heading("6. Count the number of digits in a number")

    user_input = 2026
    digit_length = len(str(user_input)) #This alone gives the answer but since a while loop is a requirement I will only use this to end the loop
    number_count = 0

    while number_count < digit_length:
        number_count += 1

    print(f"There are '{number_count}' digits in '{user_input}'")

#6. Count the number of digits in a number-------------------------------------------------------------------


#7. Keep asking for input until user types "quit"-------------------------------------------------------------------
#This function continuously asks the user for input until they type "quit" as an input
def end_with_quit():
    task_heading("7. Keep asking for input until user types 'quit'")

    while True:
        user_input = input("Enter anything or 'quit' to exit the loop: ")

        if user_input in ["quit"]: #I used the in operator to future proof the code to be able to use more than just 'quit', example - ["quit", "Quit", "exit"] gives you options
            print("You're now exiting the loop...")
            break

#7. Keep asking for input until user types "quit"-------------------------------------------------------------------


#8. Guess the number game (random number, user guesses)-------------------------------------------------------------------
#This function generates a random number between 1 and 20 and continuously asks for input until the user guesses right.
def guess_random_number():
    task_heading("8. Guess the number game (random number, user guesses)")

    random_integer = random.randint(1,20)
    attempts = 0

    while True:
        user_input = get_positive_integer("Guess the number: ")
        attempts += 1

        if user_input == random_integer:
            print(f"\n{user_input} was correct! congrats!")
            break
        elif user_input > random_integer:
            print(f"\n{user_input} is too high! Keep trying.")
        else:
            print(f"\n{user_input} is too low! Keep trying.")

    print(f"\nYou guessed right after '{attempts}' attempts!")
#8. Guess the number game (random number, user guesses)-------------------------------------------------------------------


#9. Calculate power of a number without using **-------------------------------------------------------------------
#This function calculates a user's inputed integer to the power of a user's inputed power amount all using a while loop instead of **
def power_of_number_using_while():
    task_heading("9. Calculate power of a number without using **")

    user_input = get_positive_integer("Enter a number: ", True)
    power = get_positive_integer("Enter the power amount: ", True)
    count = 0
    answer = 1

    while count < power:
        if power == 0:
            print(f"\n'{user_input}' to the power of '{power}' = 1")
            break
        elif power == 1:
            print(f"\n'{user_input}' to the power of '{power}' = {user_input}")
            break
        else:
            answer *= user_input
        
        count += 1
    if user_input == 0:
        if power == 0:
            print(f"\n'{user_input}' to the power of '{power}' = 1")
        else:
            print(f"\n'{user_input}' to the power of '{power}' = 0")
            

    if power > 1:
        print(f"\n'{user_input}' to the power of '{power}' = {answer}")

#9. Calculate power of a number without using **-------------------------------------------------------------------


#10. Find GCD of two numbers (Euclidean algorithm)-------------------------------------------------------------------
#This function finds the GCD of two numbers using the 'Euclidean algorithm' and a while loop
def gcd_of_two_numbers():

    task_heading("10. Find GCD of two numbers (Euclidean algorithm)")
    number_1 = 20
    number_2 = 10

    larger = max(number_1, number_2)
    smaller = min(number_1, number_2)

    while smaller != 0:
        remainder = larger % smaller
        larger = smaller
        smaller = remainder
    
    print(f"The GCD of '{number_1}' and '{number_2}' is '{larger}'")

#10. Find GCD of two numbers (Euclidean algorithm)-------------------------------------------------------------------


#11. Menu-driven program that loops until the user exits-----and-----12.Validate user input---------------------------------------------
#This function displays a food restuarant menu where user's can view food items in each food section And also allows them to exit by typing 0
def menu_program():
    task_heading("11. Menu-driven program that loops until the user exits AND 12. Validate user input")
    current_page = 6

    while current_page != 0:

        if current_page == 6: #Menu Page
            show_food_menu()
        elif current_page > 0 and current_page < 6: #Sub Menus
            display_sub_menu(current_page)
            
        current_page = get_positive_integer("\nEnter a page number to view or 0 to exit: ", True)

#This function displays the menu options
def show_food_menu():
    print("""
        -------Menu Pages-------
         Page 1 - Appetizers
         Page 2 - Breakfast
         Page 3 - Lunch
         Page 4 - Dinner
         Page 5 - Dessert
         Page 6 - View Pages
    """)
#This function creates and displays sub-menus
def display_sub_menu(page_selected):
    sub_menus = {
        1: {
            "title": "Appetizers",
            "items": [
                {"name": "Potato Skins", "price": 7.99},
                {"name": "5 Grilled Shrimp", "price": 11.00},
                {"name": "Garlic Bread", "price": 4.50},
                {"name": "Mozzarella Sticks", "price": 6.50},
                {"name": "Buffalo Wings", "price": 9.99},
                {"name": "Onion Rings", "price": 5.99},
                {"name": "Stuffed Mushrooms", "price": 8.50},
            ]
        },
        2: {
            "title": "Breakfast",
            "items": [
                {"name": "Pancakes", "price": 6.99},
                {"name": "Omelette", "price": 7.99},
                {"name": "French Toast", "price": 6.50},
                {"name": "Breakfast Burrito", "price": 8.99},
                {"name": "Bagel with Cream Cheese", "price": 3.50},
                {"name": "Avocado Toast", "price": 7.50},
            ]
        },
        3: {
            "title": "Lunch",
            "items": [
                {"name": "Cheeseburger", "price": 10.99},
                {"name": "Caesar Salad", "price": 8.50},
                {"name": "Club Sandwich", "price": 9.99},
                {"name": "Grilled Chicken Wrap", "price": 9.50},
                {"name": "Veggie Burger", "price": 10.00},
                {"name": "Tomato Soup", "price": 5.50},
            ]
        },
        4: {
            "title": "Dinner",
            "items": [
                {"name": "Steak", "price": 18.99},
                {"name": "Salmon Fillet", "price": 16.50},
                {"name": "Spaghetti Bolognese", "price": 12.99},
                {"name": "Grilled Chicken", "price": 14.50},
                {"name": "Vegetable Stir Fry", "price": 11.50},
                {"name": "Shrimp Scampi", "price": 17.00},
            ]
        },
        5: {
            "title": "Dessert",
            "items": [
                {"name": "Chocolate Cake", "price": 6.99},
                {"name": "Ice Cream Sundae", "price": 5.50},
                {"name": "Apple Pie", "price": 6.00},
                {"name": "Cheesecake", "price": 6.50},
                {"name": "Brownie", "price": 4.99},
                {"name": "Tiramisu", "price": 7.00},
            ]
        },
    }

    print(f"----------{sub_menus[page_selected]['title']}----------")
    for index, item in enumerate(sub_menus[page_selected]['items'], start=1):
        print(f"\t{index}. {item['name']} - ${item['price']:.2f}")


#11. Menu-driven program that loops until the user exits-----and-----12.Validate user input---------------------------------------------

#This function loads the functions for task 2
def task_2_loader():
    # print_one_to_twenty_while_loop()
    # countdown_from_ten_to_zero()
    # sum_digits_of_number()
    # reverse_number()
    # check_if_palindrome()
    # count_number_digits()
    # end_with_quit()
    # guess_random_number()
    # power_of_number_using_while()
    # gcd_of_two_numbers()
    menu_program()

task_2_loader()