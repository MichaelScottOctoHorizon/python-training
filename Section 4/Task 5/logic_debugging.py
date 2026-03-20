
#1. Incorrect grading System-----------------------------------------------vvvv

"""
    Explaination--vvvv-----------------------------------------------------------------------------------------
    |
    |    Broken - The below code is syntactically correct, but logically flawed. This is due to the use of '>' by
    |    itself without using '>='. 
    |    
    |        example 1 - A 'A' grade is 95 and higher. By using '>' alone the code is saying everything above 95 but excluding it
    |        example 2 - A 'B'  grade is 84 to 94. By using '>' alone the code is saying everything from 85 to 95, excluding 84 and including 95 incorrectly
    |
    |   Fix - Add in the '=' symbol beside the '>' symbol to correctly include the number that is excluded
    Explaination--^^^^-----------------------------------------------------------------------------------------

    Broken Code--vvvv-----------------------------------------------------------------------------------------

        def get_letter_grade(percent_grade=70):

            if percent_grade > 95:
                print("Your letter grade is: 'A'")
            elif percent_grade > 84:
                print("Your letter grade is: 'B'")
            elif percent_grade > 73:
                print("Your letter grade is: 'C'")
            elif percent_grade > 65:
                print("Your letter grade is: 'D'")
            else:
                print("Your letter grade is: 'F'")
            
    Broken Code--^^^^-----------------------------------------------------------------------------------------
"""
#Working Code includes the = symbol
#Notes the solution can also be to just adjust the numbers up by one
def get_letter_grade(percent_grade=70):
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

#1. Incorrect grading System-----------------------------------------------^^^^


#2. Broken Login logic-----------------------------------------------vvvv
"""
    Explaination--vvvv-----------------------------------------------------------------------------------------
    |   Broken - The below code is also syntactically correct but it is not logically right due to the misuse
    |   of the 'or' and 'and'.
    |   
    |   Our requirement for this was to make the user login with either their username or password but in the
    |   broken code below we put 'and' which says, 'Lets take the user where the inputed username matches AND
    |   their username and email are equivalent.'.
    |   
    |   Fix - We need an 'or' instead which will compare if the user's input is equal to either the username or the
    |   email in the database
    Explaination--^^^^-----------------------------------------------------------------------------------------

    Broken Code--vvvv-----------------------------------------------------------------------------------------

        for user in users_database:       vvv
            if (user["email"] == username and user["username"] == username) and password == user["password"]:
                print(f"\n\tWelcome, {user['name']}!")
                return user

    Broken Code--^^^^-----------------------------------------------------------------------------------------
"""

#Working Code replaces the 'and' with an 'or'.
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

#2. Broken Login logic-----------------------------------------------^^^^

#3. Wrong discount calculation-----------------------------------------------vvvv
"""
    Explaination--vvvv-----------------------------------------------------------------------------------------
    |   Broken - The below code is logically broken because it only applies a discount if the customer spends
    |   between $1000 and 1999.
    |   
    |   This makes it that customers who spend even more don't get a discount.
    |   
    |   Fix - We need to add a 2nd if condition to give customers who spend above 1999 either the same discount
    |   or a greater discount.
    Explaination--^^^^-----------------------------------------------------------------------------------------

    Broken Code--vvvv-----------------------------------------------------------------------------------------

        if spend >= 1000 and spend < 2000: ----Flawed logic on its own
            discount = 0.10

    Broken Code--^^^^-----------------------------------------------------------------------------------------

"""

#The fixed function with the if logic added for above the 1000 to 1999 range.
def discount_eligibility():
    print(f"\n12.  Discount eligibility -----------------------\n\n")
    # spend = get_user_spend()
    spend = 88000
    discount = 0

    if spend >= 1000 and spend < 2000:
        discount = 0.10
    
    #Fix added here where it considers discounts above the 1999 threashhold-------
    if spend >= 2000:
        discount = 0.15
    
    print(f"\n\tProducts Cost: {spend}")
    print(f"\tDiscount: {int(discount * 100)}%") #Multiplying by 100 moves the decimal point 2 to the right
    print(f"\tYou save: {spend * discount}")
    print(f"\tFinal Price: {spend - (spend * discount)}")

#3. Wrong discount calculation-----------------------------------------------^^^^

#4. Incorrect age classification-----------------------------------------------vvvv
"""
    Explaination--vvvv-----------------------------------------------------------------------------------------
    |   Broken - The if/elif conditions have a slight flaw that breaks the logic. By using the 'or' in this
    |   scenario we are saying the following:
    |   
    |   example 1 - if age >= 0 or age <= 12: - if age is zero or greater, or if age is 12 or less it's a child
    |               logically the condition takes any positive or negative number that exists and classes it
    |               as a 'child'.
    |   
    |   example 2 - elif age >= 13 or age <= 19: - The sane issue as example 1, the range is all possible integers
    |   
    |   Fix - We need to replace all instances of the 'or' with 'and' which will restrict the age group to the
    |         ranges in the conditions.
    Explaination--^^^^-----------------------------------------------------------------------------------------

    Broken Code--vvvv-----------------------------------------------------------------------------------------
        if age >= 0 or age <= 12:
            print(f"\n\t{age} is a 'Child'")
        elif age >= 13 or age <= 19:
            print(f"\n\t{age} is a 'Teen(Adolescent)'")
        elif age >= 20 or age <= 64:
            print(f"\n\t{age} is a 'Adult'")
        elif age >= 65:
            print(f"\n\t{age} is a 'Senior'")
    Broken Code--^^^^-----------------------------------------------------------------------------------------
"""

#The fixed function logic, all the or's were replaced with and's in the conditions
def age_group_classification():
    print(f"\n10.  Age group classification -----------------------\n\n")
    print(f"\n\tEnter your age in years below: Examples - 12 or 22 or 32 or 52 ect")
    age = 32

    #Fixes in the if and elif blocks below - or's replaced with and's
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

#4. Incorrect age classification-----------------------------------------------^^^^

#5. Faulty comparison logic -----------------------------------------------vvvv
"""
    Explaination--vvvv-----------------------------------------------------------------------------------------
    |   Broken - There is a logical issue in the if and elif conditions. Instead of checking if one value is
    |            equivalant to another we are assigning it to the other using '='
    |   
    |            By using '=' we are setting the value to the other instead of testing if the values match.
    |   
    |   Fix - We need to use the correct operation which is '==' for comparison instead of '='
    |         ranges in the conditions.
    Explaination--^^^^-----------------------------------------------------------------------------------------

    Broken Code--vvvv-----------------------------------------------------------------------------------------

        if user is None:
            print("User failed login")
            return
        else:
            if user["role"] = "admin":
                print(f"\n\t-------Admin role!")
            elif user["role"] = "human-resources":
                print(f"\n\t-------Human Resources role!")
            else:
                print(f"\n\t-------Basic User role!")
    
    Broken Code--^^^^-----------------------------------------------------------------------------------------
"""

#The working function below replaced occurances of '=' with '==' in the conditional statements
def result_system_login():
    user = {"role" : "admin"}

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
#5. Faulty comparison logic -----------------------------------------------^^^^

