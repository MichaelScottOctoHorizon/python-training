
#1. Infinite loop — missing update statement-----------------------------------------------------------------------
"""

#This function sums integers in a list - Broken 
def sum_list(list):
    sum = 0
    count = 0
    while count < len(list):
        sum += list[count]
    
    print(f"{sum} is the sum of the list.")
 
"""

#Fixed version
#The reason the commented code failed was due to the while loop not having the loop control variable called count increasing,
#since it was not being incremented the loop was infinite and continuously added the first index's value to the sum
def sum_list(list):
    sum = 0
    count = 0
    while count < len(list):
        sum += list[count]

        count += 1 # Fix is incrementing the loop control variable
    
    print(f"{sum} is the sum of the list {list}")
#1. Infinite loop — missing update statement-----------------------------------------------------------------------

#2. Off-by-one error — loop runs one too many or too few times-----------------------------------------------------------------------
"""

#This function loops through a list of numbers and displays it to the user - Broken
def off_by_one(list):
    
    for index in range(len(list) + 1): #Fix needed here
        print(f"{list[index]}", end=", ")

"""

#Fixed version
#The reason the commented code gave an error before was due to the loop counting one more time than it needed to which created
#an index that was out of bounds of the list's indeces. It was fixed by removing the + 1 from the length of the list
def off_by_one(list):
    
    for index in range(len(list)):
        print(f"{list[index]}", end=", ")

#2. Off-by-one error — loop runs one too many or too few times-----------------------------------------------------------------------


#3. Wrong accumulator initialization — sum starts at wrong value-----------------------------------------------------------------------
"""

#This function sums a list of numbers
def sum_list():
    list = [1, 5, 2, 2]
    sum = 1 #Fix needed here

    for number in list:
        sum += number
    
    print(f"Sum: {sum}")

"""

#Fixed version
#The accumulator variable sum starts off as '1' which will cause the answer to be wrong as it is summing the list contents
#and also adding '1' on top which is incorrect. The bugged code gives '11' as an answer, while the correct code gives '10'.
def sum_list():
    list = [1, 5, 2, 2]
    sum = 1 #Code fixed here

    for number in list:
        sum += number
    
    print(f"Sum: {sum}")

#3. Wrong accumulator initialization — sum starts at wrong value-----------------------------------------------------------------------

#4. Break in wrong position — loop exits too early-----------------------------------------------------------------------
"""

#This function is suppose to break out of a loop when it finds a person's name and display the index
def break_wrong_position():
    names = ['Michael', 'Brandon', 'Boris', 'Jovani', 'Ragna', 'Lagertha']
    search = "Boris"

    for index in range(len(names)):
        if search == names[index]:
            print(f"{search} found at index '{index}'")
        break #Fix here wrong place
"""

#Fixed version
#The code is syntactically correct, but the break is in the wrong place causing the loop to only execute once before breaking out
#To fix this the break needed to be inside of the if statement to only break out of the loop after finding the person and displaying
#the index of where they were found
def break_wrong_position():
    names = ['Michael', 'Brandon', 'Boris', 'Jovani', 'Ragna', 'Lagertha']
    search = "Boris"

    for index in range(len(names)):
        if search == names[index]:
            print(f"\n\t{search} found at index '{index}'")
            break
#4. Break in wrong position — loop exits too early-----------------------------------------------------------------------

#5. Nested loop with wrong variable — inner loop uses outer variable-----------------------------------------------------------------------
"""

#This function is suppose to print out a grid
def  nested_loop_wrong_variable():

    grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

    for row in grid:
        for column in row:
            print(f"{row[0]}", end=" ") #Fix we are using the wrong variable in the columns place
        print()

"""
#Fixed version
#The issue here was we were using the row's 1st value in every print, to fix this we used every column of each row to
#print out the grid accurately. The wrong version printed out a grid of first values of each row
def  nested_loop_wrong_variable():

    grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

    for row in grid:
        for column in row:
            print(f"{column}", end=" ") #Fix here we changes row to column instead
        print()

#5. Nested loop with wrong variable — inner loop uses outer variable-----------------------------------------------------------------------


#6. Wrong range arguments — loop never executes-----------------------------------------------------------------------
"""

#This function is supposed to count from 1 - 20
def wrong_loop_arguments():

    for number in range(21, 21):
        print(f"{number}", end="  ")

"""

#Fixed version
#The reason the broken version never printed any numbers was due to the loop parameters in range starting at the end value of
#21 and it needing to end up at 21. The fix was to start it at 1 instead so that the loop can properly execute
def wrong_loop_arguments():

    for number in range(1, 21): #Fix implemented here - switched from 21 to 1
        print(f"{number}", end="  ")


#6. Wrong range arguments — loop never executes-----------------------------------------------------------------------


#7. Continue skipping important logic-----------------------------------------------------------------------
"""

#This function prints out all even numbers between 1 - 20 
def continue_skipping_logic():
    
    for number in range(1, 21):

        if number % 2 == 0:
            continue #This continue is not needed and also in the wrong place
            print(f"{number}", end=",   ")

"""
#Fixed version
#The logic of the code overall is correct, but where it goes wrong is that continue is before the important print statement for
#printing the even numbers so the print never runs. Though the continue is pointless in this context, moving it after fixes it
def continue_skipping_logic():
    
    for number in range(1, 21):

        if number % 2 == 0:
            print(f"{number}", end=",   ")
            continue

#7. Continue skipping important logic-----------------------------------------------------------------------



#8. While loop condition never becomes False -----------------------------------------------------------------------
"""

#This function is suppose to loop infinitely until the user enters the word 'exit'
def while_never_false():

    while True:
        user_input = input("\n\tEnter anything you want Or enter exit to exit: ")

        if user_input in ['exit', 'Exit']:
            print("\n\tYou are now exiting...")
            #Issue is here , the loop never breaks out after the user types exit
"""

#Fixed version
#The issue in the broken code was that users even after entering 'exit' as an input the program still continued because there was
#no loop control feature like 'break' to escape the while loop when the condition was met
def while_never_false():

    while True:
        user_input = input("\n\tEnter anything you want Or enter exit to exit: ")

        if user_input in ['exit', 'Exit']:
            print("\n\tYou are now exiting...")
            break #Fix is to add the 'break' operation after the user is prompted they are exiting

#8. While loop condition never becomes False -----------------------------------------------------------------------


# sum_list([10,20,40, 5])
# off_by_one([10, 50, 20, 15,5])
# sum_list()
# break_wrong_position()
# nested_loop_wrong_variable()
# wrong_loop_arguments()
# continue_skipping_logic()
while_never_false()