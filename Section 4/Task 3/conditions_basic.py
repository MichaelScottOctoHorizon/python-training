import getpass
import time

#This helper function makes it so a user types only an integer number
def get_user_integer():
    number = input("\n\tEnter a number: ")
    try:
        return int(number)
    except:
        print(f"{number} is not an integer! Try again\n")
        return get_user_integer()
    
def valid_percentage(percentage):

    if percentage >= 0 and percentage <= 100:
        return percentage
    else:
        print(f"\n\t{percentage} is not a valid percentage between 0 and 100, Try again!")
        return valid_percentage(get_user_integer())

#This helper function makes it so a user types only an integer number
def get_yes_or_no():
    answer = input("\n\Type Yes or No: ")
    
    if answer.lower() == "yes":
        return True
    
    if answer.lower() == "no":
        return False
    
    print(f"\n{answer} is invalid, type Yes or No.")
    return get_yes_or_no() 

#1. Check positive / negative / zero
#This function displays whether a number inputed by the user is positive, negative or zero
def check_positive_negative_zero():

    print(f"\n1. Check positive / negative / zero -----------------------\n")
    user_number = get_user_integer()

    if user_number > 0:
        print(f"{user_number} is positive")
    if user_number < 0:
        print(f"{user_number} is negative")
    if user_number == 0:
        print(f"{user_number} is zero")


#2. Even or odd
#This function displays whether a user's input is even or odd
def even_or_odd():
    print(f"\n2. Even or Odd -----------------------\n")
    user_number = get_user_integer()

    if user_number % 2 == 0:
        print(f"\t\t{user_number} is Even")
    else:
        print(f"\t\t{user_number} is Odd")

#3. Voter eligibility
#This function gets a user's age and where they are from to determine whether they are eligetable to vote
def voter_eligibility():
    print(f"\n3. Voter Eligibility  -----------------------\n\n")
    
    print(f"\tEnter your age below: ")
    age = get_user_integer()

    print("\nIf you are from the Cayman Islands or Dubai")
    citizen = get_yes_or_no()

    if age >= 18 and citizen:
        print(f"\nYou are a eligable voter!")
    else:
        print(f"\nYou're not an eligable voter")

#4. Pass or fail
#This function gets a user's percent grade and tells them if they pass or failed. 60% and up is a pass
def pass_or_fail():
    print(f"\n4. Pass or Fail  -----------------------\n\n")
    print("Enter percentage grade from 0 to 100 to see if you passed or failed.")
    percent_grade = valid_percentage(get_user_integer())

    if percent_grade >= 60:
        print(f"{percent_grade} is a passing grade, Congrats!")
    else:
        print(f"{percent_grade} is a not a passing grade, Don't give up!")

#5. Grade calculator (A / B / C / D / F)
#This function gets the grade percentage from a user and displays the letter grade they earned
def grade_calculator():
    print(f"\n5. Grade calculator (A / B / C / D / F) -----------------------\n\n")

    print("Enter percentage grade from 0 to 100 to get your letter grade.")
    percent_grade = valid_percentage(get_user_integer())

    if percent_grade >= 95:
        print("Your letter grade is: 'A'")
    elif percent_grade >= 84:
        print("Your letter grade is: 'B'")
    elif percent_grade >= 73:
        print("Your letter grade is: 'C'")
    elif percent_grade >= 65:
        print("Your letter grade is: 'D'")
    else:
        print("Your letter grade is: 'F'")

#6.  Maximum of two numbers
#This function returns the max of 2 numbers
def max_of_two():
    print(f"\n6.  Maximum of two numbers -----------------------\n\n")

    print("Enter two numbers to get the bigger of the two.")
    number_1 = get_user_integer()
    number_2 = get_user_integer()

    if number_1 > number_2:
        print(f"\n\t{number_1} is bigger than {number_2}")
    elif number_1 < number_2:
        print(f"\n\t{number_2} is bigger than {number_1}")
    else:
        print(f"\n\t{number_1} is the same as {number_2}")

#7.  Maximum of three numbers
#This function returns the max of 3 numbers
def max_of_three():
    print(f"\n7.  Maximum of three numbers -----------------------\n\n")

    maximum = 0

    for _ in range(3):
        input_number = get_user_integer()

        if maximum <= input_number:
            maximum = input_number
    
    print(f"\n\t{maximum} is the largest of the three numbers.")

#8.  Leap year checker
#This function gets a user's input of a year and displays whether the year is a leap year or not - leap year = 366 days
def leap_year_checker():
    print(f"\n8.  Leap year checker -----------------------\n\n")
    print(f"\tEnter the year you want to check")
    year = get_user_integer()

    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print(f"\n\t{year} is a leap year.")
    else:
        print(f"\n\t{year} is NOT a leap year.")

#9.  Simnple Login System ---- 16.  Username validation
#This function gets the user's email or username with a password as inputs to log a user in, it checks if the user's email/username and password exists together correctly
def simple_login():
    print(f"\n9.  Simnple Login System -----------------------\n\n")
    user_email_or_username = input(f"\tEnter your username Or email: ")
    password = input(f"\tEnter your password: ")

    user = check_login(user_email_or_username, password)

    if user is None:
        print("\n\tLogin failed.")
        return None
    else:
        return user

#Returns true if email/username and password match --- Linked to simple_login()
def check_login(username, password):
    users_database = [
        {"name": "Michael Scott", "username": "Mescott93", "email": "mescottbusiness@gmail.com", "password": "satoshi", "role": "admin"},
        {"name": "Boris Octo", "username": "Boris_Octo", "email": "Boris@octo.com", "password": "octo-admin", "role": "admin"},
        {"name": "Tester Testing", "username": "Test", "email": "test@test.com", "password": "test", "role": "basic"},
        {"name": "John Wick", "username": "Pencilman", "email": "Jw@gmail.com", "password": "pencil_power", "role": "human-resources"}
    ]

    for user in users_database:
        if (user["email"] == username or user["username"] == username) and password == user["password"]:
            print(f"\n\tWelcome, {user['name']}!")
            return user
        
    print("\n\tUser details don't match in the database!")

    return None

#10.  Age group classification
#This function gets a user's age as input and classifies them as either a child / teen / adult / senior
def age_group_classification():
    print(f"\n10.  Age group classification -----------------------\n\n")
    print(f"\n\tEnter your age in years below: Examples - 12 or 22 or 32 or 52 ect")
    age = get_user_integer()

    if age >= 0 and age <= 12:
        print(f"\n\t{age} is a 'Child'")
    elif age >= 13 and age <= 19:
        print(f"\n\t{age} is a 'Teen(Adolescent)'")
    elif age >= 20 and age <= 64:
        print(f"\n\t{age} is a 'Adult'")
    elif age >= 65:
        print(f"\n\t{age} is a 'Senior'")

    if age < 0:
        print(f"\n\tNegative numbers aren't allowed, try again\n")
        age_group_classification()

#11.  Temperature classification (freezing / cold / warm / hot)
#This function gets a temperature as either Celsius or Fahrenheit and classifies it as (freezing / cold / warm / hot)
def temperature_classification():
    print(f"\n11.  Temperature classification -----------------------\n\n")
    measurement = get_temperature_measurement() #0 = Celsius and 1 = Fahrenheit
    print(f"\n\tEnter the degrees below ")
    degrees = get_user_integer()

    if measurement == 0:
        classify_cels(degrees)
    else:
        classify_fahr(degrees)

#Helper function that classifies a temparature for Celsius
def classify_cels(degrees):

    if degrees <= 0:
        print(f"\n\t{degrees} degrees Celsius is 'Freezing'\n")
    elif degrees >= 1 and degrees <= 15:
        print(f"\n\t{degrees} degrees Celsius is 'Cold'\n")
    elif degrees >= 16 and degrees <= 25:
        print(f"\n\t{degrees} degrees Celsius is 'Warm'\n")
    elif degrees >= 26 and degrees <= 35:
        print(f"\n\t{degrees} degrees Celsius is 'Hot'\n")
    elif degrees >= 35:
        print(f"\n\t{degrees} degrees Celsius is 'Very Hot'\n")

#Helper function that classifies a temparature for Fahrenheit
def classify_fahr(degrees):

    if degrees <= 32:
        print(f"\n\t{degrees} degrees Fahrenheit is 'Freezing'\n")
    elif degrees >= 33 and degrees <= 59:
        print(f"\n\t{degrees} degrees Fahrenheit is 'Cold'\n")
    elif degrees >= 60 and degrees <= 77:
        print(f"\n\t{degrees} degrees Fahrenheit is 'Warm'\n")
    elif degrees >= 78 and degrees <= 95:
        print(f"\n\t{degrees} degrees Fahrenheit is 'Hot'\n")
    elif degrees >= 95:
        print(f"\n\t{degrees} degrees Fahrenheit is 'Very Hot'\n")

    
#Helper function that lets the user select whether they want to use Celsius Or Fahrenheit
def get_temperature_measurement():
    options = ["Celsius","Fahrenheit"]

    while True:
        print("\n\tEnter the number of your preferred measurement from the Menu below")
        print("\n\t----------Degree Menu Options----------\n")
        print("\t\t0 - Celsius")
        print("\t\t1 - Fahrenheit")
        print("\n\t----------Degree Menu Options----------")

        option = get_user_integer()  # Make sure this returns an integer

        if option in [0, 1]:
            print(f"\n\t{options[option]} was selected!")
            return option
        else:
            print(f"\n\t{option} is not a valid option, try again!")

#12.    Discount eligibility
#This function is responsible for giving a buyer a 10% discount if they spend over $1000 and a 15% discount if they spend over $2000
def discount_eligibility():
    print(f"\n12.  Discount eligibility -----------------------\n\n")
    spend = get_user_spend()
    discount = 0

    if spend >= 1000 and spend < 2000:
        discount = 0.10
    
    if spend >= 2000:
        discount = 0.15
    
    print(f"\n\tProducts Cost: {spend}")
    print(f"\tDiscount: {int(discount * 100)}%") #Multiplying by 100 moves the decimal point 2 to the right
    print(f"\tYou save: {spend * discount}")
    print(f"\tFinal Price: {spend - (spend * discount)}")

#This helper function makes it so a user types only an integer number or float that is positive
def get_user_spend():
    number = input("\n\tEnter a positive $ amount you want to spend: ")
    try:
        return float(number)
    except:
        print(f"{number} is not a valid amount! Try again\n")
        return get_user_spend()

#13.    Salary tax calculation (UK editition)
#This function is responsible for calculating how much tax you need to pay based on your yearly salary
def salary_tax_calculation():
    print(f"\n13.  Salary tax calculation -----------------------\n\n")
    print(f"\n\n\t-----Tax Brackets---------------------------")
    print(f"\n\t\t$0 - $12,570              Tax rate: 0%")
    print(f"\n\t\t$12,571 - $50,270         Tax rate: 20%")
    print(f"\n\t\t$50,271 - $125,140        Tax rate: 40%")
    print(f"\n\t\t$125,140+                 Tax rate: 45%")
    print(f"\n\n\t-----Tax Brackets---------------------------")
    salary = get_yearly_salary()
    tax_amount = get_tax_amount(salary)
    taxed_amount_value = calculate_tax(salary) 

    print(f"\n\tGross Salary: ${salary:,.2f}")
    print(f"\tTax Amount percentile: {int(tax_amount * 100)}%") #I multiplied by 100 to move the decimal point to the right
    print(f"\tTax Amount value: ${taxed_amount_value:,.2f}") # You are only taxable on the extra money above 12570 not the whole salary
    print(f"\tSalary after Taxed: ${(salary - taxed_amount_value):,.2f}")

#This helper function makes it so a user types only an integer number or float that is positive
def get_yearly_salary():
    salary = input("\n\tEnter a positive $ amount you make a year: ")
    try:
        if float(salary) < 0:
            return get_yearly_salary()
        return float(salary)
    except:
        print(f"{salary} is not a valid amount! Try again\n")
        return get_yearly_salary()

#This helper function calculates how much is taxed based on the tax bracket
def calculate_tax(salary):

    tax = 0

    if salary > 12570:
        taxable = min(salary, 50270) - 12570
        tax += taxable * 0.20

    if salary > 50270:
        taxable = min(salary, 125140) - 50270
        tax += taxable * 0.40

    if salary > 125140:
        taxable = salary - 125140
        tax += taxable * 0.45

    return tax

#This helper function gets the taxable amount for the salary
def get_tax_amount(salary):
    if salary <= 12570:
        return 0
    elif salary >= 12571 and salary <= 50270:
        return 0.20
    elif salary >= 50271 and salary <= 125140:
        return 0.40
    elif salary >= 125141:
        return 0.45
    
    return 0
    
#14.    Traffic light simulator
#This function simulates a traffic light where each light will have a user defined seconds on each light and will pause before looping again for 5 seconds
def traffic_light_simulator():
    lights = ["Red", "Yellow", "Green", "Yellow"]
    current_light = 0
    time_per_light = 5
    counter = 1
    pause_time = 5
    
    print(f"\n14.  Traffic light simulator -----------------------\n\n")

    print(f"\n\tEnter below the time you want each light to stay on for, examples - 1, 3, 5, 10 ect\n")
    time_per_light = get_user_integer()

    while True:
        
        print(f"\t\t{lights[current_light]} - secs: {counter}")

        if counter == time_per_light:
            if current_light >= 3:
                current_light = 0
                time.sleep(pause_time)
            else:
                current_light+=1
            counter = 1
        else:
            counter+=1

        time.sleep(1)

#15.    Simple calculator using if/elif
#This function acts as a simple calculator for addition, subtraction, division and multiplacation for a user's two given numbers
def simple_if_elif_calculator():
    answer = 0
    print(f"\n15.  Simple calculator using if/elif -----------------------\n\n")
    print("Choose from the menu below if you want to add, subtract, multiply or divide")
    option = simple_calc_menu()

    print(f"\n\tEnter 1st number")
    number_1 = get_user_integer()

    print(f"\n\tEnter 2nd number")
    number_2 = get_user_integer()

    if option == "+":
        answer = number_1 + number_2
    elif option == "-":
        answer = number_1 - number_2
    elif option == "/":
        answer = number_1 / number_2
    elif option == "*":
        answer = number_1 * number_2

    print(f"\n\n\t{number_1} {option} {number_2} = {answer}")

#This helper function displays the menu and gets the user's chosen option 
def simple_calc_menu():
    print(f"\n\t-----Options-----\n")
    print(f"\t\t1. Enter '+' for Addition")
    print(f"\t\t2. Enter '-' for Subtraction")
    print(f"\t\t3. Enter '/' for Division")
    print(f"\t\t4. Enter '*' for Multiplication\n")

    option = input("\t\tEnter from the options above: ")

    if option in ["+", "-", "/", "*"]:
        return option
    elif option not in ["+", "-", "/", "*"]:
        print(f"{option} is not allowed as an operator, re-enter an operator!")
        return simple_calc_menu()
    
#17.    Password length validation
#This function allows the user to create a valid password that is limited to 5 characters
def password_length_validation():
    print(f"\n17.  Password length validation -----------------------\n\n")
    min_pass = 5
    max_pass = 10

    password = input("\n\tEnter a password that is 5 t0 10 characters in length: ")
    pass_length = len(password)

    if pass_length < min_pass:
        print("\tPassword is too short!, re-enter a new password")
        password_length_validation()
    elif pass_length > max_pass:
        print("\tPassword is too long!, re-enter a new password")
        password_length_validation()
    else:
        print("\tPassword is within range! SUCCESS")

#18.    Time-based greeting (morning / afternoon / evening)
#This function checks the current hourly time inputed by the user and gives them a greeting based on that time (based on the 24 hour clock)
def time_based_greeting():
    print(f"\n18.  Time-based greeting -----------------------\n\n")

    print("\n\tEnter what hour of the day it is from 0 to 24")
    input_hour = get_user_hour()

    if input_hour < 12:
        print("\tGood Morning!")
    elif 12 <= input_hour < 18:
        print("\tGood afternoon!")
    else:
        print("\tGood evening!")

#This helper function gets a user's hour of the day as input and restricts it to 0 to 24
def get_user_hour():
    hour = input("\n\tEnter a hour: ")
    try:
        if int(hour) >= 0 and int(hour) <= 24:
            return int(hour)
        else:
            return get_user_hour()
    except:
        print(f"{hour} is a valid hour! Try again\n")
        return get_user_hour()

#19.    Loan eligibility checker
#This function checks whether a user is eligable for a lone based on their age, credit score and whether they are employed
def loan_eligibility_checker():
    print(f"\n19.  Loan eligibility checker -----------------------\n\n")
    print(f"\n\tEnter your current years of age below.")
    age = get_user_integer()
    print(f"\n\tEnter your credit score below.")
    credit_score = get_user_integer()

    employed = input("\n\tEnter 'yes' or 'no' if you are employed: ")

    eligible = check_eligible(age, credit_score, employed)

    if eligible:
        print("\n\n\tYou Pass")
    else:
        print("\n\n\tYou Fail")

#This helper function returns true if the borrower meets all 3 of the criteria and false if any of the checks don't pass
def check_eligible(age, credit_score, employed):

    checks = True
    print("\n\n")
    if age < 18: 
        print("\tYou are too young for a loan.")
        checks = False
    if credit_score < 500:
        print(f"\tYour credit score of {credit_score} is too low, it needs to be greater than 500 to get a loan")
        checks = False
    if employed.lower() == "no":
        print(f"\tYou need to be employed to be eligible for a loan")
        checks = False

    if checks:
        print(f"\tYou passed all the checks and are eligible for a loan.")
    
    return checks

#20.    Result system with nested conditions
#This function determines if a user is logged in and what role they have
def result_system_login():
    user = simple_login()

    if user is None:
        print("User failed login")
        return
    else:
        if user["role"] == "admin":
            print(f"\n\t-------Admin role!")
        elif user["role"] == "human-resources":
            print(f"\n\t-------Human Resources role!")
        else:
            print(f"\n\t-------Basic User role!")


#This function loads all of the programs for task 3 
def task_3():
    #------------Uncomment any of the below functions to try them out!----------
    # check_positive_negative_zero()
    # even_or_odd()
    # voter_eligibility()
    # pass_or_fail()
    # grade_calculator()
    # max_of_two()
    # max_of_three()
    # leap_year_checker()
    # simple_login()
    # age_group_classification()
    # discount_eligibility()
    # salary_tax_calculation()
    # traffic_light_simulator()
    # simple_if_elif_calculator()
    # password_length_validation()
    # time_based_greeting()
    # loan_eligibility_checker()
    result_system_login()
task_3()