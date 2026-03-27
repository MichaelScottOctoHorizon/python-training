import time

#Helper functions------------------------------------------------------

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
def get_positive_integer(prompt):

    while True:
        user_input = input(f"{prompt} ")
        try:

            user_input = int(user_input)
            
            if user_input <= 0:
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

#1. Print numbers 1 to 50 using range()------------------------------------------------------

#This function prints from 1 to 50
def one_to_fifty_using_range():
    task_heading("1. Print numbers 1 to 50 using range()")
    for number in range(1,51): #In range the 1 is the start value and 50 is the end value
        print(f"{number}", end=" , ", flush=True) # end makes each print on the same line, flush forces the print to happen right away
        
        if number % 10 == 0:
            print()

        time.sleep(0.2) #wait for 200 millie secs after every number to show realistic counting where everything doesn't pop up at once

#1. Print numbers 1 to 50 using range()------------------------------------------------------

#2. Print all even numbers between 1 and 100------------------------------------------------------

#This function prints out all numbers from 1 to 100 but only if they are 'Even' numbers
def all_even_numbers_to_100():
    task_heading("2. Print all even numbers between 1 and 100")

    for number in range(1,101):

        if number % 2 == 0: #Only even numbers to be printed
            print(f"{number}", end=" , ", flush=True)

        if number % 20 == 0:
            print()

        time.sleep(0.05)

#2. Print all even numbers between 1 and 100------------------------------------------------------


#3. Print all odd numbers between 1 and 100------------------------------------------------------

#This function prints out all numbers from 1 to 100 but only if they are 'Odd' numbers
def all_odd_numbers_to_100():
    task_heading("3. Print all odd numbers between 1 and 100")

    count = 1

    for number in range(1,101):

        if number % 2 != 0: #If the number isn't even then it's odd
            print(f"{number}", end=" , ", flush=True)

        if count % 20 == 0:
            print()
        
        count += 1

        time.sleep(0.05)

#3. Print all odd numbers between 1 and 100------------------------------------------------------

#4. Sum of first N natural numbers (user input)------------------------------------------------------

#This function prints out all natural numbers up to a user's input 
def nth_natural_numbers():

    task_heading("4. Sum of first N natural numbers (user input)")

    total = 0
    user_input  = get_positive_integer("\n\tEnter a positive integer: ")

    for number in range(1, user_input + 1):
        total += number
        if number == user_input:
            print(f"{number}", end="", flush=True)
        else:
            print(f"{number}", end=" + ", flush=True)
        time.sleep(0.05)

    print(f" = {total}")

#4. Sum of first N natural numbers (user input)------------------------------------------------------

#5. Factorial of a number using a for loop ------------------------------------------------------------

#This function prints out the factorial of a user inputed number
def factorial_of_a_number():

    task_heading("5. Factorial of a number using a for loop")

    user_input = get_positive_integer("Enter a number to be factorialized: ")
    total = 1

    if user_input == 0 or user_input == 1:
        print(f"{user_input} factorial = 1")
    else:
        for number in range(user_input, 0, -1):
            if number == 1:
                print(f"{number}", end="", flush=True)
            else:
                print(f"{number}", end=" x ", flush=True)

            total *= number
            time.sleep(0.05)
        print(f" = {total}")

#5. Factorial of a number using a for loop ------------------------------------------------------------

#6. Print multiplication table for a given number ------------------------------------------------------------

#This function shows the multiplication table of any number the user enters from 1 to 10
def multiplication_table_for_number():

    task_heading("6. Print multiplication table for a given number")
    user_input = get_positive_integer("Enter Multiplication Table Number: ")

    for number in range(1, 11):
        print(f"{number} x {user_input} = {number * user_input}")

#6. Print multiplication table for a given number ------------------------------------------------------------

#7. Count vowels in a user-provided string ------------------------------------------------------------

#This function counts how many vowels are in the user's typed/inputed text - vowels = a e i o u
def vowels_counter():
    task_heading("7. Count vowels in a user-provided string")

    user_text = input("\n\tEnter text for the vowel counter: ")

    vowel_count = 0

    for character in user_text:
        if character in ["a", "e", "i", "o", "u"]:
            vowel_count += 1

    print(f"\n\tThere are '{vowel_count}' vowels in the word '{user_text}'")

#7. Count vowels in a user-provided string ------------------------------------------------------------

#8. Count consonants in a user-provided string ------------------------------------------------------------

#This function counts the amount of times a consanant appears in a user's input text
def consonants_counter():
    task_heading("8. Count consonants in a user-provided string")

    user_text = input("\n\tEnter text for the vowel counter: ")

    consonants_count = 0

    for character in user_text:
        if character not in ["a", "e", "i", "o", "u"]:
            consonants_count += 1

    print(f"\n\tThere are '{consonants_count}' consonants in the word '{user_text}'")

#8. Count consonants in a user-provided string ------------------------------------------------------------

#9. Reverse a string using a for loop (no slicing allowed) ------------------------------------------------------------

#This function reverses a string input and shows its characters in reverse order
def reverse_string_for_loop():

    task_heading("9. Reverse a string using a for loop (no slicing allowed)")

    user_text = input("\n\tEnter text to reverse it: ")
    reversed_text = ""

    for index in range(len(user_text) -  1, -1, -1):
        reversed_text += user_text[index]
    
    print(f"User Text: {user_text}")
    print(f"Reversed Text: {reversed_text}")

#9. Reverse a string using a for loop (no slicing allowed) ------------------------------------------------------------

#10. Iterate over a list and print each item with its index ------------------------------------------------------------

#This function iterates through a list of crypto using it's index and alongside its index
def list_iteration_with_index():

    task_heading("10. Iterate over a list and print each item with its index")

    crypto_list = ["Bitcoin", "Ethereum", "Tether", "Binance Coin", "Cardano", "XRP", "Solana"]

    for index in range(len(crypto_list)):
        print(f"{index}.    {crypto_list[index]}")

#10. Iterate over a list and print each item with its index ------------------------------------------------------------


#11. Find the largest number in a list (no max() allowed)------------------------------------------------------------

#This function finds and displays the largest number in a list without using the inbuilt max() function
def largest_in_list():
    task_heading("11. Find the largest number in a list (no max() allowed)")

    numbers_list = [20, 112, 3, 51, 90, 120, 90, 99]
    
    max_number = numbers_list[0]

    for number in numbers_list:
        if max_number < number:
            max_number = number

    print(f"The Largest number is: {max_number}")

#11. Find the largest number in a list (no max() allowed)------------------------------------------------------------

#12. Find the smallest number in a list (no min() allowed)------------------------------------------------------------

#This function finds and displays the smallest number in a list without using the inbuilt min() function
def smallest_in_list():
    task_heading("12. Find the smallest number in a list (no min() allowed)")

    numbers_list = [20, 112, 3, 51, 90, 120, 90, 99]
    
    min_number = numbers_list[0]

    for number in numbers_list:
        if min_number > number:
            min_number = number

    print(f"The Smallest number is: {min_number}")

#12. Find the smallest number in a list (no max() allowed)------------------------------------------------------------


#13. Calculate the average of numbers in a list ------------------------------------------------------------

#This function gets the average of the numbers in a list using a for loop to sum the numbers inside then divide the sum by the quantity of numbers
def average_of_numbers_in_list():
    task_heading("13. Calculate the average of numbers in a list")

    numbers_list = [10, 4, 15, 4, 8, 12]

    sum = 0

    for number in numbers_list:
        sum += number

    average = sum / len(numbers_list)

    print(numbers_list)
    print(f"The averages is: {average}")

#13. Calculate the average of numbers in a list ------------------------------------------------------------


#14. Print ASCII value of each character in a string  ------------------------------------------------------------

#This function prints out the ASCII value of each character in a string
def ascii_values_of_characters():

    task_heading("14. Print ASCII value of each character in a string")
    
    my_string = "Crypto to the MOON!"

    for character in my_string:
        print(f"'{character}': #{ord(character)}")

#14. Print ASCII value of each character in a string  ------------------------------------------------------------

#15. Count occurrences of a specific character in a string  ------------------------------------------------------------

#This function finds and counts the occurances of a character in a string
def char_occurance_counter():
    task_heading("#15. Count occurrences of a specific character in a string")

    string_document = "Hi there I'm  a Software Engineer Master!"

    print(f"\n\t{string_document}")
    user_finder = get_one_character("\n\tEnter the character you want to find in the above string: ")

    occurances = 0

    for character in string_document:
        if character == user_finder:
            occurances += 1

    print(f"\n\tThere are '{occurances}' occurances of the letter '{user_finder}'")


#15. Count occurrences of a specific character in a string  ------------------------------------------------------------

def task_1_loader():
    # one_to_fifty_using_range()
    # all_even_numbers_to_100()
    # all_odd_numbers_to_100()
    # nth_natural_numbers()
    # factorial_of_a_number()
    # multiplication_table_for_number()
    # vowels_counter()
    # consonants_counter()
    # reverse_string_for_loop()
    # list_iteration_with_index()
    # largest_in_list()
    # smallest_in_list()
    # average_of_numbers_in_list()
    # ascii_values_of_characters()
    char_occurance_counter()

task_1_loader()