

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

#This function accepts a yes or no exclusive answer as input from the user
def yes_no_answer(prompt):

    while True:
        answer = input(f"\n\t{prompt}")

        if answer in ["y","yes", "Yes", "n", "no", "No"]:
            return answer
        else:
            print(f"\n\t{answer} is not a valid 'yes' or 'no' answer. Try again!")

#This function gets a dollar floating point value as input
def get_dollar_value(prompt):
    
    while True:
        amount = input(f"\n\t{prompt}: $")

        try:
            amount = float(amount)
            return amount
        except:
            print(f"\n\t{amount} is not a valid dollar amount. Try again!")

#This function gets a valid name which excludes numbers, empty input and special characters
def get_valid_name(prompt):

    while True:

        name = input(f"\n\t{prompt} ")

        if name.replace(" ", "").isalpha(): #The name can have spaces allowing multiple names in one string and option for first and/or last names as one string
            return name
        else:
            print("Invalid name detected, Do not use special characters/symbols or numbers. Try again")

#This function gets valid percentage amounts from the user
def get_percentage(prompt):

    while True:
        percentage_input = input(f"\n\t{prompt} %")

        try:
            percentage_input = float(percentage_input)
            return round(percentage_input, 2)
        except:
            print(f"\n\t{percentage_input} isn't a valid percentage, Try again")

#This function converts a percentage grade into its letter equivalant
def get_letter_grade(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"

#This helper function gets a positive integer generically like (age or grade)
def get_positive_integer(prompt):
    while True:
        value = input(prompt)
        if value.isdigit():
            return int(value)
        print(f"\t'{value}' is not a valid positive number. Try again.")

#1. Simple interest calculator for multiple customers---------------------------------------------------------------------------------------------------
#This function accepts customer's info like their name, principal and expected interest per month when they invest into a crypto bank
def interest_calculator_customers():
    task_heading("1. Simple interest calculator for multiple customers")

    customers = []

    while True:
        user_input = yes_no_answer("Enter 'Yes' or 'No' if you want to addd a customer: ")

        if user_input in ["y","yes", "Yes"]:
            customers.append(add_new_customer())
        else:
            print("\n\tNo selected, Exiting...")
            break
    
    if len(customers) > 0: #if there were customers added let's display their interest
        display_all_customer_interests(customers)
    else:
        print("\n\tNo customers were added..")

#Prompts and adds a new customer based on user input
def add_new_customer():
    name = get_valid_name("Enter name of customer: ")
    principal = get_dollar_value("Enter the principal (starting value) amount: ")
    interest_percentage = get_percentage("What is the interest percentage a year: ")

    return {"name": name, "principal": principal, "interest_percentage": interest_percentage}

#Displays all the expected gains for all of the customers added
def display_all_customer_interests(customers):
    count = 1
    for customer in customers:
        principal = customer["principal"]
        yearly_interest = customer["interest_percentage"] / 100
        yearly_value = round(principal * yearly_interest, 2)
        month_1 = round(yearly_value / 12, 2)
        month_6 = round(yearly_value / 6, 2)
        year_total = round(yearly_value + principal, 2)

        print(f"\nName: {customer['name']}")
        print(f"\tMonth 1: +${month_1:.2f} -> Month 6: +${month_6:.2f} -> Year: +${yearly_value:.2f}")
        print(f"\t\tEnd Balance: {year_total:.2f}")
        count += 1
#1. Simple interest calculator for multiple customers---------------------------------------------------------------------------------------------------

#2. Student grade processor — process N students, find class average--------------------------------------------------------------------------------------------------------
#This function processes grades of a class of students and calculate's the class's average
def student_grade_processor():
    task_heading("2. Student grade processor — process N students, find class average")

    students = []

    while True:
        user_input = yes_no_answer("Enter 'Yes' or 'No' if you want to addd a student grade: ")

        if user_input in ["y","yes", "Yes"]:
            students.append(add_new_student())
        else:
            print("\n\tNo selected, Exiting...")
            break
    
    if len(students) > 0: #if there were students added let's display the class's average grade
        display_class_average(students)
    else:
        print("\n\tNo student grades were added..")

#Allows the user/teacher to add individual student's grades
def add_new_student():
    name = get_valid_name("Enter student name: ")
    percent_grade = get_percentage("Enter the percentage grade earned for {name}: ")

    return {"name": name, "percent_grade": percent_grade}

#calculates and displays the class's average grade
def display_class_average(students):
    sum = 0
    student_count = len(students)

    print(f"\n\tStudents in class: \n")
    
    for student in students:
        sum += student['percent_grade']
        print(f"\tName: {student['name']} - Grade: %{student['percent_grade']}")
    
    class_average = sum / student_count
    letter_grade_average = get_letter_grade(class_average)

    print(f"\n\tAverage Class grade is: Percentage - %{class_average} and Letter - '{letter_grade_average}'")


#2. Student grade processor — process N students, find class average--------------------------------------------------------------------------------------------------------

#3. Inventory stock checker — loop through items, flag low stock--------------------------------------------------------------------------------------------------------
#This function loops through a list of items and flags if a item is less than 5 in stock and allows the manager to post an order for more to be delivered
def inventory_stock_checker():
    task_heading("3. Inventory stock checker — loop through items, flag low stock")

    inventory = [
        {"name": "Apples", "quantity": 50, "price": 0.75},
        {"name": "Bananas", "quantity": 30, "price": 0.50},
        {"name": "Oranges", "quantity": 40, "price": 0.65},
        {"name": "Milk", "quantity": 2, "price": 2.99},
        {"name": "Bread", "quantity": 25, "price": 1.99},
        {"name": "Eggs", "quantity": 3, "price": 0.20},
        {"name": "Chicken", "quantity": 15, "price": 5.49},
        {"name": "Rice", "quantity": 35, "price": 3.25}
    ]

    orders = [] #When stock is low on something the inventory manager can choose to order more and added to this list for future

    for item in inventory:
        low_stock_flag = "---LOW STOCK!"

        print(f"\tName: {item['name']} - Quantity: {item['quantity']} - Price: ${item['price']}")

        if item['quantity'] < 5:
            order_more = yes_no_answer(f"'{item['name']}' are low, do you want to order more (yes/no)? ")

            if order_more in ["y","yes", "Yes"]:
                orders.append(low_quantity_prompt(item))
            else:
                print(f"\tRe-Ordering of {item['name']} skipped.")
    
    
#Prompts the user for how much items should be re-ordered
def low_quantity_prompt(item):

    quantity = get_positive_integer(f"Enter how much {item['name']} should be ordered: ")

    print(f"\t{quantity} {item['name']} ordered...")

    return {"name": item['name'], "quantity": quantity, "price": item['price']}

#3. Inventory stock checker — loop through items, flag low stock--------------------------------------------------------------------------------------------------------

#4. Bill calculator — keep adding items until user says "done"--------------------------------------------------------------------------------------------------------
#This function allows a user to continuously add items to a list until they type 'done'
def bill_calculator():
    task_heading("4. Bill calculator — keep adding items until user says 'done'")

    items = []
    total = 0

    while True:

        item_name = input("\n\tEnter item name to add, or type 'done' to exit: ")

        if item_name not in ['done', 'Done']:
            items.append(add_new_item(item_name))
            total += items[len(items) - 1]['price']
        else:
            print(f"\n\t'Done' typed...Exiting List Adder...")
            break
    
    print(f"\n\tYour total is: ${total:.2f}")

#Allows the adding of an item to the list
def add_new_item(name):

    price = get_dollar_value(f"Enter the price for '{name}'")
    return {"name": name, "price": price}

#4. Bill calculator — keep adding items until user says "done"--------------------------------------------------------------------------------------------------------


#5. Fibonacci series up to N terms------------------------------------------------------------------------------------------------------------
#This function prints out numbers of fibonacci up to the user defined nth number
def nth_fibonacci():
    task_heading("5. Fibonacci series up to N terms")

    nth_number = get_positive_integer("Enter an end number for the fib series: ")

    num_1 = 0
    num_2 = 1

    for _ in range(nth_number):
        
        print(f"{num_1}", end=", ", flush=True)
        temp = num_2
        num_2 = num_1 + num_2
        num_1 = temp

#5. Fibonacci series up to N terms------------------------------------------------------------------------------------------------------------


#6. Armstrong number checker------------------------------------------------------------------------------------------------------------
#This function accepts a user's input number and tells the user if it is a armstrong number or not
def armstrong_number_checker():
    task_heading("6. Armstrong number checker")

    str_number = str(get_positive_integer("Enter a number for Armstrong check: "))
    number_length = len(str_number)
    sum = 0

    for number in str_number:
        sum += (int(number) ** number_length) #digit to the power of the length of the number

    if str_number == str(sum):
        print(f"'{str_number} is a Armstrong number'")
    else:
        print(f"'{str_number} is NOT an Armstrong number'")

#6. Armstrong number checker------------------------------------------------------------------------------------------------------------


#7. Find all Armstrong numbers between 1 and 1000------------------------------------------------------------------------------------------------------------
#This function prints all armstrong numbers between 1 and 1000
def armstrong_1_to_1000():
    task_heading("7. Find all Armstrong numbers between 1 and 1000")

    print("\t", end="")
    for num in range(1, 1000):
        str_number = str(num)
        number_length = len(str_number)
        sum = 0

        for number in str_number:
            sum += (int(number) ** number_length) #digit to the power of the length of the number

        if str_number == str(sum):
            print(f"{str_number}", end=", ")
    print()


#7. Find all Armstrong numbers between 1 and 1000------------------------------------------------------------------------------------------------------------
#This function converts a list of temperatures from celcius to fahrenheit
def batch_temperature_converter():
    task_heading("")
    temperatures = [
        0, 1, 14, 19, 23, 27, 28, 35, 78
    ]

    for temperature in temperatures:
        temp = (temperature * 1.8) + 32
        print(f"\t{temperature} degrees Celcius = {temp} degrees fahrenheit")


#8. Batch temperature converter for a list of values------------------------------------------------------------------------------------------------------------


#9. Word frequency counter — count each word in a sentence------------------------------------------------------------------------------------------------------------
#This function counts how many times each word in a sentence shows up and displays it to the user
def word_frequency_counter():
    task_heading("9. Word frequency counter — count each word in a sentence")

    sentence = input(f"Enter a sentence to count each occurance of each word: ")
    sentence = sentence.replace(".", "").replace("?", "").replace("!", "") #gets rid of typical sentence symbols so only words remain
    words_split = sentence.lower().split(" ")

    words_count = {}

    for word in words_split: #Adds words to the list and increments their count each time they are detected again
        
        if word in words_count:
            words_count[word] += 1
        else:
            words_count[word] = 1
    
    for word, count in words_count.items(): #Displays the word with how many times it occured
        print(f"{word}: {count}")

#9. Word frequency counter — count each word in a sentence------------------------------------------------------------------------------------------------------------


#10. Simple ATM system with loop (check balance, withdraw, deposit, exit)------------------------------------------------------------------------------------------------------------
#
def atm_system():
    task_heading("10. Simple ATM system with loop (check balance, withdraw, deposit, exit)")

    bank_balance = 85000

    options = [
        {"id": 1, "name": "Check Balance"},
        {"id": 2, "name": "Withdraw"},
        {"id": 3, "name": "Deposit"},
        {"id": 4, "name": "Exit"},
    ]

    #Atm menu - Check balance -> Withdraw -> Deposit -> Exit
    while True:
        
        menu_option = display_menu_options(options)


        if menu_option['id'] == 1: #Check Balance menu
            check_balance(bank_balance)
        elif menu_option['id'] == 2: #Withdraw menu
            bank_balance -= withdraw_menu(bank_balance)
        elif menu_option['id'] == 3: #Deposit menu
            bank_balance += deposit_menu()
        elif menu_option['id'] == 4: #Exit
            print(f"\n\tYou chose to exit...Exiting...")
            break

        # print(f"\n\t{menu_option['name']} was selected")


#Check Balance option
def check_balance(bank_balance):
    print("\n\t-------Bank Balance Menu-------\n")
    print(f"\t\tYour balance is: ${bank_balance:.2f}\n")

    option = yes_no_answer("Do you want to go back to the menu? ")

    if option in ["y","yes", "Yes"]:
        return
    else:
        check_balance(bank_balance)

#Withdraw menu option
def withdraw_menu(bank_balance):
    while True:
        withdrawal_amount = get_dollar_value("Enter a withdrawal amount")

        if withdrawal_amount > bank_balance: #If your balance is less than your withdrawal request , unable to withdraw
            print(f"\tCurrent Balance: ${bank_balance}")
            print(f"\tYou are ${(withdrawal_amount - bank_balance):.2f} short, please enter a smaller amount.")

            exit_to_menu = yes_no_answer("Do you want to return to the menu (yes/no)? ")

            if exit_to_menu in ["y","yes", "Yes"]:
                return 0
        else:
            return withdrawal_amount
        
#Deposit menu option
def deposit_menu():

    deposit_amount = get_positive_integer("\tEnter the dollar amount you want to deposit: $")

    return deposit_amount

#Displays the atm menu visually
def display_menu_options(options):
    options_length = len(options)

    print("\n\t-------Atm Menu Options-------\n")

    for option in options:
        print(f"\t\t{option['id']} - {option['name']}")

    print("\n\t-------Atm Menu Options-------\n")

    selected_option = get_positive_integer("\n\tEnter the number from the options above: ") - 1
    
    if selected_option < 0 or options_length < selected_option: #If an option outside the range is selected flag the mistake and recursively ask again
        print(f"\n\t{selected_option + 1} is not a valid option, Try again!")
        return display_menu_options(options)
    else:
        return options[selected_option]


#10. Simple ATM system with loop (check balance, withdraw, deposit, exit)------------------------------------------------------------------------------------------------------------

#This function loads all the programs for task 6
def task_6_loader():
    # interest_calculator_customers()
    # student_grade_processor()
    # inventory_stock_checker()
    # bill_calculator()
    # nth_fibonacci()
    # armstrong_number_checker()
    # armstrong_1_to_1000()
    # batch_temperature_converter()
    # word_frequency_counter()
    atm_system()

task_6_loader()