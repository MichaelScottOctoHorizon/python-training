import time

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


#This function only allows positive integers
def get_positive_integer(prompt):

    while True:
        user_input = input("\n\t" + prompt + " ")

        try:
            user_input = int(user_input)

            if user_input <= 0:
                raise Exception()
            return user_input
        except:
            print(f"\n\t{user_input} is not a positive number, Try again.")

#This function only allows integers
def get_any_integer(prompt):

    while True:
        user_input = input("\n\t" + prompt + " ")

        try:
            user_input = int(user_input)

            return user_input
        except:
            print(f"\n\t{user_input} is not an integer, Try again.")

#1. Search for a number in a list using break-------------------------------------------------
#This function searches for a number in a list and displays the index when found and utilizes break
def seach_in_list():

    task_heading("1. Search for a number in a list using break")

    search = 110
    number_list = [4, 30, 20, 10, 115]
    index = 0

    for number in number_list:
        if search == number:
            print(f"\n'{search}' found at index '{index}'")
            break
        index += 1
    
    if search not in number_list:
        print(f"\n'{search}' is not within the list.")


#1. Search for a number in a list using break-------------------------------------------------


#2. Print all numbers except multiples of 3 using continue-------------------------------------------------
#This function counts from 1 to 20 but skips multiples of 3
def exclude_multiples_of_three():
    task_heading("2. Print all numbers except multiples of 3 using continue")
    count = 1

    while count <= 20:

        if count % 3 == 0:
            count += 1
            continue
        
        print(f"{count}", end=" ", flush=True)
        time.sleep(0.05)
        count += 1 

    print()

#2. Print all numbers except multiples of 3 using continue-------------------------------------------------


#3. Skip negative numbers in a list using continue-------------------------------------------------------

def skip_negatives_in_list():
    task_heading("3. Skip negative numbers in a list using continue")

    number_list = [10, 22, -64, 64, 122, 0, 99, -1, 1]

    for number in number_list:

        if number < 0:
            continue

        print(f"{number}", end=" ", flush=True)
        time.sleep(0.05)

#3. Skip negative numbers in a list using continue-------------------------------------------------------


#4. Exit a while loop when condition is met using break-------------------------------------------------------
#This function allows you to type numbers as much as you want that are outside the range of 1-5
def exit_while_loop_when_condition_met():
    task_heading("4. Exit a while loop when condition is met using break")
    number = 1

    while True:

        number = get_any_integer("Enter any number that is not in the range 1-5 to continue entering numbers:")

        if 1 <= number <=5:
            print("\n\tCondition Met, Exiting while loop...")
            break

#4. Exit a while loop when condition is met using break-------------------------------------------------------


#5. Password attempt system — max 3 tries using break-------------------------------------------------------
#This function allows a user to type a password 3 times before locking them out if they haven't typed it right on attempt 3
def password_max_attempts():
    task_heading("5. Password attempt system — max 3 tries using break")

    attempts = 0
    passwords = ["pass", "success", "winning"]
    login_success = False

    while attempts < 3:

        password_input = input(f"\n\tEnter your password to login: ")
        attempts += 1

        if password_input in passwords:
            print("\n\tCorrect password, Logging in...")
            login_success = True
        else:
            print(f"Incorrect password: Attempt - {attempts}")
    
    if not login_success:
        print(f"\n\tAccount locked, you failed to login {attempts} times.")

#5. Password attempt system — max 3 tries using break-------------------------------------------------------

#6. Use pass as a placeholder in an empty loop body-------------------------------------------------------
#This function shows that you can bypass a loop being completely empty by using the keyword pass as a placeholder
def pass_in_loop_body():
    task_heading("6. Use pass as a placeholder in an empty loop body")

    for count in range(5):
        pass
    print("\n\tMy loop is practically empty but still works!")

#6. Use pass as a placeholder in an empty loop body-------------------------------------------------------


#7. Find the first prime number after a given number using break-------------------------------------------------------
#This function uses nested while loops to loop through all possible numbers before each number after the given number
#It checks from 1 up to the numbers above and keeps track of how much possible divisions, if there are 2 divisions,
#logically it is a prime because 1 can divide into anything (except 0) and a number can divide once into itself
def first_prime_number_after_given_number():
    task_heading("7. Find the first prime number after a given number using break")
    given_number = 0
    number_above = given_number + 1
    divisible_counts = 0
    count = 1

    while True:

        while count <= number_above:
            if number_above % count == 0: #add one to divisible count
                divisible_counts += 1
            
            count += 1

        if divisible_counts == 2:
            print(f"\n\t'{number_above}' is the first prime number after '{given_number}'")
            break
        number_above += 1

        count = 1
        divisible_counts = 0
    
#7. Find the first prime number after a given number using break-------------------------------------------------------


#8. Print all characters of a string except spaces using continue-------------------------------------------------------
#This function prints every character in a given string excluding spaces, it accomplishes this by using continue if a space is detected
def print_all_characters_excluding_spaces():

    task_heading("8. Print all characters of a string except spaces using continue\n")
    given_string = "My grandpa's deck has no pothetic cards Kaiba...But it does contain...The unstoppable Exodia!"

    print(f"Before: {given_string}")
    print(f"After: ", end="")

    for character in given_string:

        if character == " ":
            continue

        print(f"{character}", end="", flush=True)

#8. Print all characters of a string except spaces using continue-------------------------------------------------------


#9. Stop processing orders when total exceeds budget using break-------------------------------------------------------
#This function accepts orders of crypto buys until the running total exceeds the budget, break was used to exit the loop
def break_when_budget_exceeded():
    task_heading("9. Stop processing orders when total exceeds budget using break")

    orders = [
        {"name": "Bitcoin",      "value": 20000},
        {"name": "Ethereum",     "value": 15000},
        {"name": "Cardano",      "value": 12000},
        {"name": "Solana",       "value": 10000},
        {"name": "Ripple",       "value": 8000},
        {"name": "Polkadot",     "value": 7000},
        {"name": "Dogecoin",     "value": 6000},
        {"name": "Shiba Inu",    "value": 5000},#This last order exceeds the budget
        {"name": "Bitcoin",    "value": 25000},
        {"name": "Solana",    "value": 20000}
    ]

    budget = 85000
    total = 0

    for crypto in orders:

        if total > budget: #Exit loop when total exceeds budget
            print(f"\n\tTotal Budget Exceeded by: ${(total - budget):.2f}")
            break
        print("-----------------------------------------------------------------")
        total += crypto["value"]
        print(f"\tOrder: '{crypto['name']}' - '${crypto['value']:.2f}' \n\tRunning Total = ${total:.2f} / ${budget:.2f}\n")
        print("-----------------------------------------------------------------")

#9. Stop processing orders when total exceeds budget using break-------------------------------------------------------


#10. Skip weekends in a list of days using continue--------------------------------------------------------------------
#This function uses continue to skip printing weekends detected in the days list in turn printing only mondays to fridays
def skip_weekends_in_list():
    task_heading("10. Skip weekends in a list of days using continue")

    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "Monday", "Tuesday"]

    for day in days:

        if day in ["Saturday", "Sunday"]:
            continue

        print(f"{day}", end=", ", flush=True)
        time.sleep(0.10)


#10. Skip weekends in a list of days using continue--------------------------------------------------------------------

#This function loads all the programs for Task 3
def task_3_loader():
    # seach_in_list()
    # exclude_multiples_of_three()
    # skip_negatives_in_list()
    # exit_while_loop_when_condition_met()
    # password_max_attempts()
    # pass_in_loop_body()
    # first_prime_number_after_given_number()
    # print_all_characters_excluding_spaces()
    # break_when_budget_exceeded()
    skip_weekends_in_list()

task_3_loader()