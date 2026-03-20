#Global variables-------------------------------------------

atm_stored_cash = { #stored bills and their quantity in the atm
    "100": 10, 
    "50": 20, 
    "25": 40, 
    "10": 100, 
    "5": 200, 
    "1": 1000
}

#Global variables-------------------------------------------




#This helper function generates a attractive heading based on what's passed in
def heading_generator(heading):
    print(f"\n\n{heading} -----------------\n\n")

#This helper function simulates all the accounts in the atm system
def accounts_system():
    #In future if I was building a real application I would use file-writing or a database to get this info because it resets to the default on each program restart currently
    #I would also use classes instead of dictionaries
    accounts = {
        "ACC001": {"account_id": "ACC001", "account_holder": "Michael Scott", "card_number": "1888-8888-8888", "pin": "8888", "balance": 75000.75},
        "ACC002": {"account_id": "ACC002", "account_holder": "Boris Octo", "card_number": "1233-3338-8682", "pin": "0120", "balance": 1000000.00},
        "ACC003": {"account_id": "ACC003", "account_holder": "Brandon Stark", "card_number": "1001-4522-2299", "pin": "2288", "balance": 200000.50},
        "ACC004": {"account_id": "ACC004", "account_holder": "Homelander Supe", "card_number": "4218-8419-1006", "pin": "4110", "balance": 15000.20},
        "ACC005": {"account_id": "ACC005", "account_holder": "Wagyu Ribeye", "card_number": "2010-2012-2026", "pin": "9931", "balance": 430.00},
    }

    return accounts

#This helper function asks for a user's pin and checks if it's valid, 4 digit pin and only numbers 0 - 9
def ask_for_pin():

    print(f"\n\tEnter your pin below.")

    while True:
        pin = input("\tPin: ")
        if pin.isdigit() and len(pin) == 4:
            return pin
        
        print(f"\t{pin} isn't a valid pin. Try again")

def calculate_atm_total_available():

    total = 0

    for bill, amount in atm_stored_cash.items():
        total += (int(bill) * amount)

    return total

#This function checks that the withdrawal amount is possible by comparing the atm's available bills and the amnount the user wants to withdraw
def try_ejecting_cash(withdrawal):
    total_available = calculate_atm_total_available()
    
    if withdrawal > total_available:
        print(f"\n\tThe ATM doesn't have enough cash for ${withdrawal:.2f}")
        return False

    temp_cash = atm_stored_cash.copy() #create a copy as to not overwrite the original
    running_total = withdrawal

    withdrawed_cash = {bill: 0 for bill in atm_stored_cash}

    for bill in sorted(temp_cash.keys(), key=int, reverse=True):
        bill_value = int(bill)

        while running_total >= bill_value and temp_cash[bill] > 0:
            running_total -= bill_value
            temp_cash[bill] -= 1
            withdrawed_cash[bill] += 1

    if running_total != 0:
        print("\n\tNot enough correct denominations to complete withdrawal")
        return False

    # Commit changes to ATM
    for bill in withdrawed_cash:
        atm_stored_cash[bill] -= withdrawed_cash[bill]

    print("\n\tCash dispensed:")
    for bill, amount in withdrawed_cash.items():
        if amount > 0:
            print(f"\t{amount} x ${bill}")

    return True

def open_withdrawal_menu(account):

    available = round(account['balance'], 2)
    withdrawal_valid = False
    transaction_complete = False

    print(f"\n\tAvailable Amount: {available}")
    print("\n\tEnter how much you wish to withdraw")

    withdraw = input("Withdraw: $")

    while withdrawal_valid != True: #Only allows the exit of the loop when the user enters a valid decimal number
        try:
            withdraw = float(withdraw)
            withdrawal_valid = True
        except:
            print("Withdrawal amount must be a float/decimal number, re-enter!")
            withdraw = input("\tWithdraw: $")


    if withdraw <= available:
        transaction_complete = try_ejecting_cash(withdraw)

        if transaction_complete:
            account['balance'] -= withdraw
        
    else:
        print(f"\n\tYou have insufficient balance to withdraw ${withdraw:.2f}")


#2. This function allows users to see their account with their card at the atm and choose to withdraw if needed
def view_bank_account(account):
    user_account = account

    viewing_account = True

    while viewing_account:
        account_menu_displayed(user_account)
        option = wait_for_user_input()

        if option == "w":
            open_withdrawal_menu(user_account)
        else:
            viewing_account = False

#This helper function displays the user's account details
def account_menu_displayed(user_account):
    print(f"\n\tAccount #: {user_account['account_id']}")
    print(f"\tAccount holder: {user_account['account_holder']}")
    print(f"\tBalance: {user_account['balance']}")

def wait_for_user_input():
    print("\n\tEnter 'w' if you want to withdraw cash or anything else if you want to exit")
    option = input("\tEnter here: ")

    return option

#This helper function reads the user's card number
def read_inserted_card(card_number):
    accounts = accounts_system()
    account = next((acc for acc in accounts.values() if acc["card_number"] == card_number), None) #if the account with the card number is found return it else return none

    if account != None:
        correct_pin = ask_for_pin()

        if correct_pin == account["pin"]:
            view_bank_account(account) #I'm using the card as the key to view the account here
        else:
            print("\n\tPin was entered wrong too many times, Card Account Blocked.")
    else:
        print(f"\tYour card is not allowed. --Eject Card")


#1. ATM withdrawal system--------------------- and 2. Bank account status checker ------------------------
#This function allows you to sign in using your atm card and view your balance as well as withdraw cash from the atm
def atm_withdrawal_system():
    heading_generator("1.  ATM withdrawal system and 2. Bank account status checker")
    read_inserted_card("1888-8888-8888")

#3. Admission eligibility system------------------------------------------------------
#This function checks to see if an applicant meets the criteria to be accepted into University
def admission_eligibility_system():
    heading_generator("3.   Admission eligibility system")
    
    age = get_positive_integer("\tWhat is your age: ")
    grade_average_percentage = get_positive_integer("\tWhat is your average grade percentage: ")
    entrance_exam = get_yes_or_no("\tDid you pass your entrance exam (y/n): ")
    
    eligible, message = check_admission_eligibility(age, grade_average_percentage, entrance_exam)
    
    print(f"\n\t{message}")

    print(f"\n\t{'You are a fit for our Uni!' if eligible else 'Your application was not accepted.'}")

#This helper function returns true if all of the criteria is met for age, grade percentage and passed exam. And false if any of those fail - Uni
def check_admission_eligibility(age, grade_percentage, passed_exam):
    # Example rules: age >= 18, grade >= 70%, entrance exam passed
    if age < 18:
        return False, "You must be at least 18 years old."
    if grade_percentage < 70:
        return False, "Your average grade must be at least 70%."
    if not passed_exam:
        return False, "You must pass the entrance exam."
    return True, "Congratulations! You are eligible for admission."


#This helper function gets a positive integer generically like (age or grade)
def get_positive_integer(prompt):
    while True:
        value = input(prompt)
        if value.isdigit():
            return int(value)
        print(f"\t'{value}' is not a valid positive number. Try again.")

#This helper function gets a integer whethere it's positive or negative
def get_integer(prompt):
    while True:
        value = input(prompt)
        try:
            return int(value)
        except:
            print(f"\t'{value}' is not a valid integer. Try again.")

#This helper function gets a generic positive float value from the user
def get_positive_float(prompt):
    while True:
        value = input(prompt)
        try:
            number = float(value)

            if number >= 0:
                return number
            else:
                print("\tAmount must be positive.")
        except:
            if value in ['e', 'exit']:
                return 'exit'
            print(f"\t'{value}' is not a valid dollar amount. Try again.")

#This helper function prompts yes/no input generically
def get_yes_or_no(prompt):
    while True:
        answer = input(prompt).strip().lower()
        if answer in ["y", "yes"]:
            return True
        elif answer in ["n", "no"]:
            return False
        print(f"\t'{answer}' is not valid. Type 'y' or 'n'.")

#This helper function prompts the user for their gender (Male or Female)
def get_gender(prompt="Enter your gender (M/F): "):
    while True:
        gender = input(prompt).strip().lower()
        if gender in ["m", "male"]:
            return "Male"
        elif gender in ["f", "female"]:
            return "Female"
        print(f"\t'{gender}' is not valid. Please enter 'M' or 'F'.")

#This helper function prompts the user for their prefered coverage
def get_prefered_coverage(prompt="Enter your preferred coverage (F / 3rd): "):
    while True:
        coverage = input(prompt).strip().lower()
        if coverage in ["f", "full"]:
            return "Full"
        elif coverage in ["3rd", "third", "3"]:
            return "Third-party"
        print(f"\t'{coverage}' is not valid. Please enter 'F' or '3rd'.")

#4. Job eligibility checker----------------------------------------------------------------------
def job_eligibility_checker():
    heading_generator("4. Job eligibility checker")

    age = get_positive_integer("\tWhat is your age? ")
    experience_years = get_positive_integer("\tHow many years of relevant experience do you have? ")
    has_degree = get_yes_or_no("\tDo you have a relevant degree? (y/n) ")
    has_certification = get_yes_or_no("\tDo you have a relevant professional certification? (y/n) ")

    eligible, message = check_job_eligibility(age, experience_years, has_degree, has_certification)

    print(f"\n\t{message}")

    print(f"\n\t{'You are eligible' if eligible else 'You are not eligible'}")

#This helper function checks if the age, experience, applicant has a degree or certificate and returns true if they pass all criteria
def check_job_eligibility(age, experience_years, has_degree, has_certification):
    if age < 18:
        return False, "You must be at least 18 years old."
    if experience_years < 2:
        return False, "You must have at least 2 years of experience."
    if not (has_degree or has_certification):
        return False, "You must have a degree or relevant certification."
    return True, "Congratulations! You are eligible for the job."

#5. Shipping cost calculator------------------------------------------------------------------------
#This function accepts the cost of as many items as a user wants and gives them how much it will cost which includes all the fees, discounts and gross total
def shipping_cost_calculator():
    heading_generator("5. Shipping cost calculator")
    gross_total = get_items_total()
    total_customer_cost, base_fee, percentage_fee, discount_percent, discounted_amount = get_all_costs(gross_total)

    heading_generator("-----Shipping and Total cost Receipt----")
    print(f"\n\n\t\tGross total: +${gross_total:.2f}")
    print(f"\t\tPercentage Fee: +${percentage_fee:.2f}")
    print(f"\t\tDiscount %: {discount_percent}%")
    print(f"\t\tDiscounted Amount: -${discounted_amount:.2f}")
    print(f"\t\tBase Shipping Fee: +${base_fee:.2f}")
    print(f"\t\tTotal Cost: +${total_customer_cost:.2f}")
    

#This helper function gets item's costs and adds them to a total until the user specifies they want to stop adding item's via 'e' or 'exit'
def get_items_total():

    total = 0

    while True:
        user_input = get_positive_float("Enter an item's cost or 'e'/'exit' to finish adding: ")

        if user_input == 'exit':
            return total
        
        total += user_input

#This helper function is responsible for getting all the fees, discounts and calculating the total cost to the customer
def get_all_costs(gross_total):

    base_fee = 100 # $100 base fee
    percentage_fee = gross_total * 0.05 # 5% of gross total fee example if the 

    #More you spend the higher the discount
    if gross_total > 5000:
        discount = 0.10
    elif gross_total > 1000:
        discount = 0.05
    else:
        discount = 0

    discount_percent = int(discount * 100)
    total_fees = (base_fee + percentage_fee)
    discounted_amount = total_fees * discount
    
    total_fees_after_discount = total_fees - discounted_amount

    total_cost_to_customer = gross_total + total_fees_after_discount

    return total_cost_to_customer, base_fee, percentage_fee, discount_percent, discounted_amount

#6. Electricity bill calculator ------------------------------------------------------------------------
#This function is responsible for getting a customer's kWh usage and calculating what they owe or are owed (solar panels can reduce costs or even make you money)
def electricity_bill_calculator():
    heading_generator("6.   Electricity bill calculator ")
    customer_monthly_kwh = get_integer("\tEnter how much kwh you used this month: ")
    customer_cost = get_customer_cost(customer_monthly_kwh)

    if customer_monthly_kwh < 0: #Solar panels so the electricity company owes the customer
        print(f"\n\tCustomer is owed: ${customer_cost} for supplying {abs(customer_monthly_kwh)} kWh")
    else:
        print(f"\n\tCustomer owes: ${customer_cost} for using {customer_monthly_kwh} kWh")

#This helper function calculates and returns how much a customer's kWh usage is worth in dollar value at 15 cents per kWh
def get_customer_cost(customer_usage):

    kwh_rate = 0.15 #15 cents per kWh
    cost = abs(kwh_rate * customer_usage)

    return f"{cost:.2f}"

#7. Restaurant order system------------------------------------------------------------------------------------------
def restaurant_order_system():
    menu = { #Restaurant dictionary
        0: {"id": 0,"name":"18 oz. Ribeye Steak", "price": 26.50},
        1: {"id": 1,"name":"French Fries", "price": 3.50},
        2: {"id": 2,"name":"10 Buffalo Wild Wings", "price": 8.99},
        3: {"id": 3,"name":"Cesar Salad", "price": 8.99},
        4: {"id": 4,"name":"Pene Pasta with Pesto", "price": 12.00},
        5: {"id": 5,"name":"Pepsi", "price": 2.00},
        6: {"id": 6,"name":"Inflation priced water 4 oz", "price": 8.00},
        7: {"id": 7,"name":"Cheeze Cake dessert", "price": 5.00}
    }

    heading_generator("#7. Restaurant order system")
    order = customer_selections(menu)
    display_customer_order(order)

#This function displays the restuarant menu for the customer 
def display_restaurant_menu(menu):

    print(f"\n\t----Menu Selection-----------\n")
    for item in menu.values():
        print(f"\t\t{item['id']}.   {item['name']}  - ${item['price']}")

#This helper function is responsible for getting items from the food menu that the customer wants to buy
def customer_selections(menu):
    
    user_order = {} #initial empty dictionary

    while True:
        display_restaurant_menu(menu) #Displays the restaurant's food menu
        selection = get_positive_integer("\n\tEnter a number from the menu to add it to your list Or a none listed number to exit/finalize: ")

        if selection < 0 or selection >= len(menu): #If option isn't on the menu return
            print(f"\n\tOrder finalized!")
            return user_order
        
        if selection in user_order: #if item is already in the customer's list add 1 to the quantity else add the item to the list
            user_order[selection]["quantity"] += 1
            print(f"\n\tYou now have: {user_order[selection]['quantity']} - {user_order[selection]['name']}'s")
        else:
            user_order[selection] = {"id": selection, "name": menu[selection]["name"], "price": menu[selection]["price"], "quantity": 1}
            print(f"\n\tAdded: {menu[selection]['name']} for ${menu[selection]['price']:.2f}")

#This helper function displays the customer's entire order and their total cost
def display_customer_order(order):

    print(f"\n\n\t----Customer Order:-------------------------\n")

    total_price = 0
    count = 1

    for item in order.values():
        total_cost_of_duplicates = item["price"] * item["quantity"]

        print(f"\t\t{count}.   {item['quantity']} - {item['name']} - ${total_cost_of_duplicates:.2f}")
        total_price += total_cost_of_duplicates
        count += 1
    
    print(f"\n\n\t\tTotal Cost: ${total_price:.2f}")   

#8. Insurance premium calculator--------------------------------------------------------------------------------
#This function displays a driver's expected premium based on factors such as age, gender, driving history and their vehicles details
def insurance_premium_calculator():
    heading_generator("#8. Insurance premium calculator")
    
    age = get_positive_integer("\n\tWhat is your age")
    gender = get_gender("\n\tWhat is your gender? ")
    insurance_claims = get_positive_integer("\n\tHow many claims have you taken in the past 5 years")
    years_of_experience = get_positive_integer("\n\tHow many years of experience do you have? ")
    user_coverage = get_prefered_coverage()
    print(f"\tYou selected: {user_coverage}")

    vehicle_year = get_positive_integer("\n\tEnter the year of your vehicle: ")
    vehicle_value = get_positive_float("\n\tEnter the current market value of your vehicle: $")

    premium = calculate_insurance_premium(age, gender, insurance_claims, years_of_experience, user_coverage, vehicle_year, vehicle_value)

    print(f"\n\n\tYour insurance premium is: ${premium}")

#This helper function calculates how much a customer's insurance premium should be based on their age, gender, claims, experience, coverage, vehicle_year, vehicle_value
def calculate_insurance_premium(age, gender, claims, experience, coverage, vehicle_year, vehicle_value):

    #1. Base premium by vehicle value and coverage
    if coverage.lower() in ["f", "full"]:
        base_premium = vehicle_value * 0.05  # 5% of vehicle value for full coverage
    else:  # Third-party
        base_premium = vehicle_value * 0.03  # 3% of vehicle value

    #2. Age adjustment
    if age < 25:
        base_premium *= 1.2  # 20% higher for young drivers
    elif age > 60:
        base_premium *= 1.1  # 10% higher for senior drivers

    #3. Gender adjustment more for males (sad face) and Karen drivers
    if gender.lower() == "male":
        base_premium *= 1.05  # 5% higher for males
    
    if gender.lower() == "karen":
        base_premium *= 1.80 # 80% higher for angry karens

    #4. Claims adjustment
    base_premium += claims * 100  # Add $100 per past claim

    #5. Experience adjustment
    if experience < 5:
        base_premium *= 1.1  # 10% higher for less experienced drivers
    elif experience > 20:
        base_premium *= 0.9  # 10% discount for very experienced drivers

    # 6. Vehicle age adjustment
    vehicle_age = 2026 - vehicle_year  # assuming current year 2026
    if vehicle_age > 10:
        base_premium *= 0.95  # 5% discount for old vehicles
    elif vehicle_age < 3:
        base_premium *= 1.05  # 5% increase for very new cars

    return round(base_premium, 2)

#9. Online exam eligibility---------------------------------------------------------------------------
#This function check if a student is eligible by checking if they are atleast 18 years old, have math in their completed courses and average grade is 70+
def online_exam_eligibility():
    heading_generator("9. Online exam eligibility")

    # Ask user for age
    age = get_positive_integer("\n\tEnter your age: ")

    # Ask user for completed courses
    completed_courses_input = input("\n\tEnter the courses you have completed, separated by commas: ")
    completed_courses = [course.strip() for course in completed_courses_input.split(",")]

    average_grade = get_positive_integer("\n\tEnter your average grade percentage: ")

    # Check eligibility
    eligible, message = check_online_exam_eligibility(age, completed_courses, average_grade)

    print(f"\n\t{message}")

    if eligible:
        print(f"\n\tWelcome you are eligible!")
    else:
        print(f"\n\tSorry you are not eligible!")

#This helper function returns if the applicant meets the criteria to take an exam or not, and a message is displayed on anything they are missing
def check_online_exam_eligibility(age, completed_courses, average_grade):
    if age < 18:
        return False, "You must be at least 18 years old to take the exam."
    if "Math101" not in completed_courses:
        return False, "You must have completed Math101 to be eligible."
    if average_grade < 70:
        return False, "Your average grade must be at least 70%."
    
    return True, "You are eligible to take the online exam."

#10.    User role access system ------------------------------------------------------------------------------------
def user_role_access_system():
    heading_generator("#10. User role access system")
    attempts = 3

    while True:
        username = input(f"\tEnter your username or email: ")
        password = input(f"\tEnter your password: ")
        user = check_login(username, password)

        if user is None: #If user login details don't match
            attempts -= 1 #Decrement the attempts by 1 giving users only 3  attempts of entering wrong before they are locked out
        else:
            attempts = 3 #If the user successfully logs in we can reset previous failed attempts to 3
            user_roles_menu(user)
            break

        if attempts == 0:
            print("\n\tYou failed to login too many times! Exiting System...")
            break #If user attempts 3 times to login unsuccessfully  the login loop ends

#This function is responsible for sending user's down their specific menu path based on their roles
def user_roles_menu(user):
    
    if user['role'] == "admin":
        admin_menu(user)
    elif user['role'] == "human-resources":
        hr_menu()
    else:
        basic_user_menu(user)

    input("\n\tEnter any key to exit: ")

#Admin users can view both their own details in full like the Basic user and other user's like the HR
def admin_menu(user):
    basic_user_menu(user)
    hr_menu()

#Basic users can view their own details only
def basic_user_menu(user):
    print("\n\n\t My User Details-------------------\n\n")
    print(f"\t\tName: {user['name']} - Username: {user['username']} - Email: {user['email']} - Role: {user['role']} - Holidays: {user['holiday_allowance']}")

#Humnan Resources can view all user's and their roles with other details
def hr_menu():
    heading_generator("\tHR Menu")

    print("\n\t All Employees List-------------------\n\n")

    for employee in users_database: #displays a list of all employees and their basic details
        print(f"\tName: {employee['name']} - Email: {employee['email']} - Role: {employee['role']} - Holidays: {employee['holiday_allowance']}")

users_database = [ #users details here so you can login without scrolling all the way up to see the login info
        {"name": "Michael Scott", "username": "Mescott93", "email": "mescottbusiness@gmail.com", "password": "satoshi","holiday_allowance": 30, "role": "admin"},
        {"name": "Boris Octo", "username": "Boris_Octo", "email": "Boris@octo.com", "password": "octo-admin", "holiday_allowance": 75, "role": "admin"},
        {"name": "Tester Testing", "username": "Test", "email": "test@test.com", "password": "test", "holiday_allowance": 25, "role": "basic"},
        {"name": "John Wick", "username": "Pencilman", "email": "Jw@gmail.com", "password": "pencil_power","holiday_allowance": 25, "role": "human-resources"}
    ]

#Login system from task 3-----
def check_login(username, password):

    for user in users_database:
        if (user["email"] == username or user["username"] == username) and password == user["password"]:
            print(f"\n\tWelcome, {user['name']}!")
            return user
        
    print("\n\tUser details don't match in the database!")

    return None


#This function loads all of the programs for task 4
def task_4():
    # atm_withdrawal_system() #The atm_withdrawal_system allows the user to both withdraw cash and see their balance so it solves for both 1 and 2.
    # admission_eligibility_system()
    # job_eligibility_checker()
    # shipping_cost_calculator()
    # electricity_bill_calculator()
    # restaurant_order_system()
    # insurance_premium_calculator()
    # online_exam_eligibility()
    user_role_access_system()
task_4()