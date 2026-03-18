#Calculator Program Functions------------------------------------------------------------------------------------------------------------------------vvvv

#This program is responsible for displaying the program options and getting the user input
def display_program_options():

    print("\n-----------------Programs Menu-------------------\n")
    print("|\tEnter 0 - \t Exit Program")
    print("|\tEnter 1 - \t arithmetic_calulator")
    print("|\tEnter 2 - \t Even or Odd")
    print("|\tEnter 3 - \t Divisible by 3 & 5?")
    print("|\tEnter 4 - \t Division vs Floor Division")
    print("|\tEnter 5 - \t Print the largest of two numbers")
    print("|\tEnter 6 - \t Print the largest of three numbers")
    print("|\tEnter 7 - \t Age and country limits")
    print("|\tEnter 8 - \t Username or Email login")
    print("|\tEnter 9 - \t Check for membership (string and list)")
    print("|\tEnter 10 - \t Identity list and int comparison")
    print("|\tEnter 11 - \t Operator Precedence Explainations")
    print("|\tEnter 12 - \t More logical 'not' examples")

    print("\n")

    program_option = int(input("Enter a valid number from the Menu above: ")) #Gets a valid input that is convertable to an integer

    return program_option

#Menu for the operator selection and getting input
def operator_selection():

    print("\n\n-----------------Operator Selection-------------------\n")
    print("|\tEnter '+' - \t for 'Addition'")
    print("|\tEnter '-' - \t for 'Subtraction'")
    print("|\tEnter '*' - \t for 'Multiplication'")
    print("|\tEnter '/' - \t for 'Division(with decimals)'")
    print("|\tEnter '//' - \t for 'Division(round down)'")
    print("|\tEnter '%' - \t for 'Modulous Division(Gets only remainder)'")
    print("|\tEnter '**' - \t for 'Exponentiation/To-Power-Of'")

    operator_selected = input("\n\nEnter the operator you want to use from the menu above: ")

    #Only operands from the list is allowed else recurrsion until the user enters a valid operator
    if operator_selected in ["+", "-", "*", "/", "//", "%", "**"]:
        return operator_selected
    else:
        return operator_selection()

#Ensures user adds a valid number
def enter_valid_number(input_message):

    print(f"\n{input_message} ")
    input_number = input()

    try: #Valid number
        float(input_number)
        return input_number
    except:
        print(f"'{input_number}' is not a valid number, re-enter a valid number.")
        return enter_valid_number(input_message)

def result_calculation(first_number, second_number, operand):

    answer = 0

    if operand == "+":
        answer = first_number + second_number
    if operand == "-":
        answer = first_number - second_number
    if operand == "*":
        answer = first_number * second_number
    if operand == "/":
        answer = first_number / second_number
    if operand == "//":
        answer = first_number // second_number
    if operand == "%":
        answer = first_number % second_number
    if operand == "**":
        answer = first_number ** second_number

    return answer
    
def convert_number(value):

    if value.is_integer(): # check if number is an integer and convert it 
        return int(value)
    else:
        return value

def arithmetic_calculator():

    operator_selected = operator_selection()

    first_number = convert_number(float(enter_valid_number("Enter 1st number: ")))
    last_number = convert_number(float(enter_valid_number("Enter 2nd number: ")))
    
    result = result_calculation(first_number, last_number, operator_selected)

    print(f"{first_number} {operator_selected} {last_number} = {result}")

#Calculator Program Functions------------------------------------------------------------------------------------------------------------------------^^^


#Even Or Odd---------Division by 3 & 5---------------------------------------------------------------------------------------------------------------vvv

#if a number is divisible by 2 with no remainder it is an even number logically speaking, else it's a odd number
def check_even_or_odd():
    try:
        user_input = int(input("\n\nEnter Number to see if 'Even' or 'Odd': "))
    except:
        print("\nNot a valid number, re-enter please.")
        check_even_or_odd()

    if user_input % 2 == 0:
        print(f"{user_input} is 'Even'")
    else:
        print(f"{user_input} is 'Odd'")

#This function displays whether a user's input number is divisible by 3 and 5 Or not
def divisible_by_3_and_5():
    try:
        user_input = int(input("\n\nEnter Number to see if divisible by '3' and '5': "))
    except:
        print("\nNot a valid number, re-enter please.")
        divisible_by_3_and_5()

    if user_input % 3 == 0 and user_input % 5 == 0:
        print(f"{user_input} is divisible by both 3 and 5")
    else:
        print(f"{user_input} is not divisible by both 3 and 5")

#Even Or Odd------------Division by 3 & 5------------------------------------------------------------------------------------------------------------^^^


#Floor vs Division------------------------------------------------------------------------------------------------------------vvv

#This function shows the difference between the division operator and the floor division operator
def floor_vs_division():
    try:
        first_number = convert_number(float(input("\n\nEnter 1st Number: ")))
        second_number = convert_number(float(input("\n\nEnter 2nd Number: ")))

        division_answer = first_number / second_number
        floor_answer = first_number // second_number

        print(f"\n{first_number} / {second_number} = {division_answer}")
        print(f"{first_number} // {second_number} = {floor_answer}")
    except:
        print("\nNot a valid number, re-enter please.")
        floor_vs_division()

#Floor vs Division------------------------------------------------------------------------------------------------------------^^^

#Largest of Three------------------------------------------------------------------------------------------------------------vvv

#This function prints the largest of three numbers
def largest_of_three():

    numbers = [22, -40, 32]
    largest = numbers[0]

    for number in numbers:
        if largest <= number:
            largest = number

    print(f"\n\nThree numbers are: {numbers}\n")
    print(f"The largest of the 3 numbers is : {largest}")


#Largest of Three------------------------------------------------------------------------------------------------------------^^^

#Print Larger of 2 numbers------------------------------------------------------------------------------------------------------------vvv

def print_largest_of_two_numbers():

    print("\n\n-------Print the larger of 2 numbers----------\n")
    try:
        first_number = convert_number(float(input("\n\nEnter 1st Number: ")))
        second_number = convert_number(float(input("\n\nEnter 2nd Number: ")))

        if first_number >= second_number:
            print(f"{first_number} is the larger of the two numbers.")
        else:
            print(f"{second_number} is the larger of the two numbers.")

    except:
        print("\nNot a valid number, re-enter both numbers please.")
        print_largest_of_two_numbers()

#Print Larger of 2 numbers------------------------------------------------------------------------------------------------------------^^^

#User applications------------------------------------------------------------------------------------------------------------vvv

#This function gets a user's age and country and let's them know whether they are allowed to participate
def age_and_country_check():

    allowed_locations = ["Cayman Islands", "Dubai"]

    print("\n\nCheck if the user meets the criteria: Age: 18+ , Country: Cayman Islands or Dubai\n\n")

    user_age = int(input("Enter age as a positive integer. example - 14 or 17 or 20 or 25 ect: "))
    user_country = input("Enter your country (caps ignored)").title()

    if user_age >= 18 and user_country in allowed_locations:
        print("You're the right age and are in the allowed locations.")
    elif user_age < 18:
        print(f"{user_age} is too young to participate")
    elif user_country not in allowed_locations: #Logical not condition example
        print(f"{user_country} isn't an allowed country, allowed countries are {allowed_locations}")

#This function allows the user to login via email or username if they are in the database
def username_or_email_login():
    allowed_usernames = ["mescott93", "borisDubai", "topGcoder"]
    allowed_emails = ["myEmail@google.com", "yourEmail@yahoo.com", "tester@hotmail.com"]

    login_input = input("Enter your 'Email' or your 'Username': ")

    if login_input in allowed_usernames or login_input in allowed_emails:
        print(f"{login_input} has successfully logged in!")
    else:
        print(f"{login_input} is not in the database. Login aborted")

#User applications------------------------------------------------------------------------------------------------------------^^^


#Membership Checkers------------------------------------------------------------------------------------------------------------vvv

#Checks for membership of a string and list using 'in'
def check_for_membership():

    database = ["Michael", "Boris", "Scott", "Ragna", "Stark"]

    search = input("\n\nEnter a name or phrase to search for: ").title()

    if search in database: #checks if the word is in the database
        print(f"\n{search} user is in the database.\n")
    else:
        print(f"\n{search} is not a user")

    
    for user in database: #loops through each database item and checks if the input is contained within any of the items as a substring
        if search in user:
            print(f"{search} is a substring of : {user}")


#Membership Checkers------------------------------------------------------------------------------------------------------------^^^


#Identity functions------------------------------------------------------------------------------------------------------------vvv

#Checks if a input is contained within an array/list and int comparison
def identity_integers_and_list():
    input = 10
    custom_list = [4,34, 10, 40, 55]
    custom_list2 = custom_list

    reference_number = 12

    if input is reference_number:
        print(f"input: {input} references the same object reference: {reference_number}")
    else:
        print(f"input: {input} doesn't reference the same object reference: {reference_number}")

    if custom_list is custom_list2: #Identity in list
        print(f"{custom_list} is  {custom_list2}")
    else:
        print(f"{custom_list} is not {custom_list2}")

#Identity functions------------------------------------------------------------------------------------------------------------^^^

#Operator Precedence Explains------------------------------------------------------------------------------------------------------------vvv

def operator_precedence_explainations():

    print("""\n\n
        Operator Precedence List (Highest Priority to Lowest / Left to Right)
            () => ** => * => / => // => % => + => -
    """)

    print("10 * 5 + 5 = 55, this is because multiplication is done first then addition in operator precedence, so it is 10 * 5 = 50, then 50 + 5 = 55")
    print("10 * (5 + 5) = 100, the numbers are the same but since the () brackets are priority over * , " \
    "then everything contained in the brackets are added first so 5 + 5 = 10, then multiplication is done giving us 10 * 10 = 100")


#Operator Precedence Explains------------------------------------------------------------------------------------------------------------^^^

#12.    More logical 'not' examples------------------------------------------------------------------------------------------------------------vvv
#Boris amend 2
def more_logical_not_examples():
    etherium_chain = {"Eth","USDT", "USDC","Chainlink", "Uniswap", "Shib"}
    solana_chain = {"Sol","USDC", "Myro","Bonk", "Render", "Shib"}

    stable_coins = ["USDC", "USDT", "BUSD"]
    counter = 1

    crypto_chains_combined = etherium_chain | solana_chain #This combines the etherium chain and solana chain as 1 Set and removes the duplicates like USDC

    print(f"\n\tBelow is a list of crypto that are in both the eth and sol chains but are 'not' stable coins\n")
    
    for crypto in crypto_chains_combined:
         if crypto not in stable_coins: #not example 1
            print(f"\t\t{counter}. {crypto}")
            counter+=1

#12.    More logical 'not' examples------------------------------------------------------------------------------------------------------------^^^

#This function's single responsibility is to run other programs
def programs_loader():

    program_option = 0

    try:
        program_option = display_program_options() #Displays the menu of programs and returns the option the user entered
    except:
        print("You didn't enter a valid number, try again")
        programs_loader()
    
    if program_option ==  0:
        return #Exits the function and in turn ends the program
    if program_option == 1:
        arithmetic_calculator() #Program 1
    if program_option == 2:
        check_even_or_odd() #Program 2
    if program_option == 3:
        divisible_by_3_and_5() #Program 3
    if program_option == 4:
        floor_vs_division() #Program 4
    if program_option == 5:
        print_largest_of_two_numbers() #Program 5
    if program_option == 6:
        largest_of_three() #Program 6
    if program_option == 7:
        age_and_country_check() #Program 7
    if program_option == 8:
        username_or_email_login() #Program 8
    if program_option == 9:
        check_for_membership() #Program 9
    if program_option == 10:
        identity_integers_and_list() #Program 10
    if program_option == 11:
        operator_precedence_explainations() #Program 11
    if program_option == 12:
        more_logical_not_examples() #Program 12

programs_loader()