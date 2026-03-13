
#1. Expression with mixed arithmetic operators
#This function campares how python prioritizes an expression based on arithmetic operators
def mixed_arithmetic():
    
    value_1 = 10
    value_2 = 0
    value_3 = 18

    print(f"\n---------Expression with mixed arithmetic operators---------\n")
    print(f"\tTest 1 - {value_1} + {value_2} * {value_3} = {(value_1 + value_2 * value_3)}")
    print(f"\tTest 2 - ({value_1} + {value_2}) * {value_3} = {((value_1 + value_2) * value_3)}")
    print(f"\tTest 3 - {value_1} * {value_2} - {value_3} = {(value_1 * value_2 - value_3)}")
    print(f"\tTest 4 - {value_1} ** {value_2} * {value_3} = {(value_1 ** value_2 * value_3)}")
    print(f"\n---------Expression with mixed arithmetic operators---------\n")

#2. Expression combining comparison and arithmetic
#This function compares expressions together to see if they are equivalent in value
def comparing_expressions():
    print(f"\n---------Expression combining comparison and arithmetic---------\n")
    print(f"\tTest 1 - (10 + 20 = 30) == (10 * 20 = 200) : {(10 + 20) == (10 * 20)}")
    print(f"\tTest 2 - (20 ** 0 * 10 = 10) == (10 * 1 / 1 = 10) : {(20 ** 0 * 10) == (10 * 1 / 1)}")
    print(f"\tTest 3 - 20 == 5? : {20 == 5}")
    print(f"\tTest 4 - 100 ==  1000 / 10? : {100 ==  1000 / 10}")
    print(f"\n---------Expression combining comparison and arithmetic---------\n")

#3. Expression using parentheses to change the result
#This function displays the differences in result depending on positioning of parentheses
def parentheses_change_result():
    print(f"\n---------Expression using parentheses to change the result---------\n")
    print(f"\tTest 1 - 100 * 10 + 15 = {100 * 10 + 15}")
    print(f"\tTest 2 - 100 * (10 + 15) = {100 * (10 + 15)}")
    print(f"\tTest 3 - (100 * 10) + 15 = {(100 * 10) + 15}")
    print(f"\n---------Expression using parentheses to change the result---------\n")

#4. Boolean expression evaluation
#This function compares values and expressions together and displays true if they are equivalent or false if they aren't
def boolean_expressions():
    print(f"\n---------Boolean expression evaluation---------\n")
    print(f"\tTest 1 - 200 == '200' : {200 == '200'}")
    print(f"\tTest 2 - 200 == 200 : {200 == 200}")
    print(f"\tTest 3 - '200' == '200' : {'200' == '200'}")
    print(f"\tTest 4 - 200 == 100 + 100 : {200 == 100 + 100}")
    print(f"\n---------Boolean expression evaluation---------\n")

#5. Chained comparison (e.g. 1 < x < 10)
#This function accepts a user's age as an input and evaluates whether they are a young adult or not
def chained_comparison():
    print(f"\n---------Chained comparison (e.g. 1 < x < 10)---------\n")
    age = int(input("\t\nEnter your age: "))

    if age > 18 and age < 50:
        print("You are a young adult! ")
    else:
        print("You are not a young adult! ")

    print(f"\n---------Chained comparison (e.g. 1 < x < 10)---------\n")

#6. Short-circuit logic example
#This function evaluates whether a person is old enough to invest Or is a special case individual
def short_circuit_example():

    people = [
                {"name": "Michael", "age": 32, "status": "special"},
                {"name": "Ernest", "age": 16, "status": "basic"},
                {"name": "Scott", "age": 15, "status": "special"},
              ]
    
    print(f"\n---------Short-circuit logic example---------\n")
    print(f"\tInvestors must be 18 or older or be of special status\n")
    
    for person in people:
        if person["age"] >= 18 or person["status"] == "special":
            print(f"\t\t{person['name']} aged {person['age']} and of '{person['status']}' status is allowed to invest.")
        else:
            print(f"\t\t{person['name']} aged {person['age']} and of '{person['status']}' status is NOT allowed to invest.")

    print(f"\n---------Short-circuit logic example---------\n") 

#7. Expression that returns a boolean
#This function shows what people are allowed based on their country, Cayman Islands and Dubai are allowed.
def boolean_expressions():

    persons = [
        { "name": "Michael Scott", "country": "Cayman Islands"},
        { "name": "Boris Octo", "country": "Dubai"},
        { "name": "Brandon", "country": "Cayman Islands"},
        { "name": "Jovanni", "country": "Cayman Islands"},
        { "name": "Elon Musk", "country": "Australia"},
        { "name": "Bill Gaytes", "country": "America"},
        { "name": "Tarzan", "country": "Africa"},
        ]
    
    allowed_countries = ["Cayman Islands", "Dubai"]

    print(f"\n---------Expression that returns a boolean---------\n")
    for person in persons:
        print(f"\t{person['name']} - from {person['country']} - Allowed: {person['country'] in allowed_countries}")
    print(f"\n---------Expression that returns a boolean---------\n")

#8. Expression that returns an integer
#This function returns an integer of how old a person will be in 80 years and what year
def integer_expression():

    age = 32
    age_in_eighty_years = age + 80
    year_in_eighty_years = 2026 + 80 #In a serious application I would get the current year by date.today().year and importing the library for date

    print(f"\n---------Expression that returns an integer---------\n")
    print(f"\tHow old you will be in 80 years and what year it will be\n")
    print(f"\t\tAt age {age} you will be {age_in_eighty_years} years old in 80 years from now")
    print(f"\t\t80 years from now it'll be the year {year_in_eighty_years}")

    print(f"\n---------Expression that returns an integer---------\n")

#9. Expression that returns a float
#This function deducts the withdrawal amount from a bank balance. Both values are floats so the return type will be float
def float_expression():
    
    bank_balance = 1000000.89
    withdrawal_amount = 380000.39

    print(f"\n---------Expression that returns a float---------\n")
    print(f"\tYour Bank balance: ${bank_balance}")
    print(f"\tYour withdrawal amount: ${withdrawal_amount}")
    print(f"\tBalance after withdrawal: ${(bank_balance - withdrawal_amount):.2f}") #2 decimal point minimum like real world applications
    print(f"\n---------Expression that returns a float---------\n")

#10.    Debug a wrong expression — show original, explain mistake, show fix
def expression_debugging():

    sum = 0
    increment_amount = "10" #This is where the issue started because the increment amount is a string we can't directly use computation for the desired effect

    for _ in range(0,10,1):
        sum += int(increment_amount) #I converted the string 10 to an actual integer 10 for it to work

    print(f"sum is: {sum}")

def task_2():
    mixed_arithmetic()
    comparing_expressions()
    parentheses_change_result()
    boolean_expressions()
    chained_comparison()
    short_circuit_example()
    boolean_expressions()
    integer_expression()
    float_expression()
    expression_debugging()

task_2()
