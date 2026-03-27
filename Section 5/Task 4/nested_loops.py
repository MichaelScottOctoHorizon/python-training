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

#1. Print multiplication tables from 1 to 10-------------------------------------------------
#This function prints the multiplication table as rows and columns for 1 to 10
def multiplication_table_to_10():
    task_heading("1. Print multiplication tables from 1 to 10")

    for x in range(1,10,1):
        for y in range(1,10,1):
            print(f"\t{x * y}", end="", flush=True)
        print() #For going to the next row

#1. Print multiplication tables from 1 to 10-------------------------------------------------


#2. Rectangular star pattern (rows × columns)-------------------------------------------------
#This function prints out the * symbol into rows and columns to represent a rectangle primitive GUI
def rectangular_star_pattern():
    task_heading("2. Rectangular star pattern (rows × columns)")

    rectangle_length = 8
    rectangle_height = 5

    for x in range(1, rectangle_height, 1):
        for y in range(1, rectangle_length, 1):
            print("*", end="", flush=True)
        print()

#2. Rectangular star pattern (rows × columns)-------------------------------------------------


#3. Right-angled triangle star pattern------------------------------------------------------------
#This function creates a right angled triangle using the * symbol and nested for loops
def right_angled_triangle_star_pattern():
    task_heading("3. Right-angled triangle star pattern")

    triangle_length = 8

    for x in range(0, triangle_length):
        for y in range(0, x):
            print("*", end="")
        print()
#3. Right-angled triangle star pattern------------------------------------------------------------

#4. Inverted Right-angled triangle star pattern------------------------------------------------------------
#This function creates an inverted right angled triangle using the * symbol and nested for loops
def inverted_right_angled_triangle_star_pattern():
    task_heading("4. Inverted Right-angled triangle star pattern")

    triangle_length = 8

    for x in range(0, triangle_length):
        for y in range(0, triangle_length - x):
            print("*", end="")
        print()

#4. Inverted Right-angled triangle star pattern------------------------------------------------------------



#5. Number pyramid pattern----------------------------------------------------------------
#This function prints out numbers to shape a pyramid
def number_pyramid():
    task_heading("5. Number pyramid pattern")

    pyramid_height = 10
    
    for row in range(1, pyramid_height + 1):
        for space in range(pyramid_height - row): #Adds less space the more the row is incremented by deducting the row from the overal pyramid height
            print(f" ", end="", flush=True)
        for number in range(1, row + 1): #Prints the numbers normally with a space since the appropriate space was already added
            print(f"{number}", end=" ", flush=True)
        print()

#5. Number pyramid pattern----------------------------------------------------------------


#6. Floyd's triangle------------------------------------------------------------------------
#This function creates a triangle with numbers that are counting up in a nested loop
def floyds_triangle():
    task_heading("6. Floyd's triangle")

    end_number = 25
    current_number = 1
    row = 1
    
    while current_number <= end_number:
        for number in range(row):
            print(f"{current_number}", end=" ", flush=True)#
            current_number += 1
        row += 1
        print()
#6. Floyd's triangle--------------------------------------------------------------------------


#7. Check if a number is prime--------------------------------------------------------------------------
#This function uses a loop to see if a number is a prime, I don't see why two loops are needed though
def check_if_prime():
    task_heading("7. Check if a number is prime")

    given_number = 10
    divisible_counts = 0
    count = 1

    while count <= given_number:
        if given_number % count == 0: #add one to divisible count
            divisible_counts += 1
        
        count += 1

    if divisible_counts == 2:
        print(f"\n\t'{given_number}' is a prime")
    else:
        print(f"\n\t'{given_number}' is a NOT a prime")


#7. Check if a number is prime--------------------------------------------------------------------------


#8. Print all prime numbers between 1 and 100--------------------------------------------------------------------------
#This functions uses nested loops to print all primes between 1 and 100
def print_primes_to_100():
    task_heading("8. Print all prime numbers between 1 and 100")

    prime_count = 10

    for number in range(1, 101):
        divisible_count = 0

        for divisor in range(1, number + 1): #Check all numbers up to the number each time if it's divisible and add to the count of divisible numbers for that number
            if number % divisor == 0: #If divisible add 1
                divisible_count += 1
        
        if divisible_count == 2: #Print the number because it only has 2 possible divisors meeting the criteria of a prime.
            if prime_count == 10: #Every 10 numbers go to the next line
                prime_count = 0
                print("\n")
                print("\t", end="", flush=True)

            print(f"{number}", end=", ", flush=True)
            prime_count += 1


#8. Print all prime numbers between 1 and 100--------------------------------------------------------------------------


#9. Matrix addition using two lists of lists--------------------------------------------------------------------------
#This function adds the values between each matrix and creates a new result matrix from them
def matrix_addition():
    task_heading("9. Matrix addition using two lists of lists")
    matrix_1 = [
        [5, 2, 10],
        [12, 7, 1],
        [6, 8, 1]
    ]
    matrix_2 = [
        [2, 3, 2],
        [5, 11, 1],
        [2, -20, 1]
    ]

    result_matrix = []

    for row in range(0, len(matrix_1)):
        result_matrix.append([]) #Add a row before you add the numbers to it
        for column in range(0, len(matrix_1[row])): 
            result_matrix[row].append(matrix_1[row][column] + matrix_2[row][column]) #Add the sum of the 2 numbers in each matrix to the sum_matrix

    print(f"\n\tSummed Matrix: {result_matrix}")

#9. Matrix addition using two lists of lists--------------------------------------------------------------------------


#10. Find common elements between two lists (no sets allowed)--------------------------------------------------------------------------
#This function finds what is common between 2 lists and adds the number to a commons list
def find_common_elements():
    task_heading("10. Find common elements between two lists (no sets allowed)")

    list1 = [12, 34, 56, 78, 5, 11, 30]
    list2 = [5, 10, 12, 20, 25, 30, 35, 40, 11]
    commons_list = [] 

    min_list_length = min(len(list1), len(list2))

    if len(list1) < len(list2): #I want to base the loop on the shorter list because there is never a need to compare past it's elements
        shorter_list = list1
        longer_list = list2
    else:
        shorter_list = list2
        longer_list = list1

    count = 0

    while count < min_list_length:
        if (shorter_list[count] in longer_list) and (shorter_list[count] not in commons_list):
            #If the shorter list's number is in the longer/other list AND the number hasn't been added to the commons list then add it to the commons list
            commons_list.append(shorter_list[count])
        count += 1
    
    print(f"\n\t Commons Elements: {commons_list}")

#10. Find common elements between two lists (no sets allowed)--------------------------------------------------------------------------

#This function loads all the programs in Task 4
def task_4_loader():
    # multiplication_table_to_10()
    # rectangular_star_pattern()
    # right_angled_triangle_star_pattern()
    # inverted_right_angled_triangle_star_pattern()
    # number_pyramid()
    # floyds_triangle()
    # check_if_prime()
    # print_primes_to_100()
    # matrix_addition()
    find_common_elements()

task_4_loader()