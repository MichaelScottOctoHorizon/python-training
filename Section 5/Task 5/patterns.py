
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


#1. Right-aligned triangle --------------------------------------------------------------------------------------------
"""
        *
       **
      ***
     ****
    *****
"""
#This function prints a right aligned triangle like the example above
def right_aligned_triangle():
    task_heading("1. Right-aligned triangle")

    triangle_rows = 5

    for index in range(0, triangle_rows + 1):

        print("\t\t", end="")

        #Add spaces
        for space in range(0, triangle_rows - index):
            print(" ", end="", flush=True)
        
        #Add stars
        for star in range(0, index):
            print("*", end="", flush=True)
        
        print("\n")

#1. Right-aligned triangle --------------------------------------------------------------------------------------------


#2. Diamond pattern --------------------------------------------------------------------------------------------------
"""
      *
     ***
    *****
     ***
      *
"""

#This function prinnts out a diamond using 2 loops , 1 for rendering the top pyramid and the other for rendering the bottom half
def diamond_pattern():
    task_heading("1. Right-aligned triangle")

    diamond_height = 3

    # Top half of pyramid
    for i in range(diamond_height):
        print(" " * (diamond_height - i - 1) + "*" * (2 * i + 1))

    # Bottom half of pyramid
    for i in range(diamond_height - 2, -1, -1):
        print(" " * (diamond_height - i - 1) + "*" * (2 * i + 1))
#2. Diamond pattern --------------------------------------------------------------------------------------------------


#3. Hollow square -----------------------------------------------------------------------------------------------------
"""
    *****
    *   *
    *   *
    *   *
    *****
"""
#This function prints out a square but with a hollow interior, in short a outline of a square
def hollow_square():
    task_heading("3. Hollow square")

    square_sides = 5

    for row in range(0, square_sides):
        print("\n\t", end="")

        for column in range(0, square_sides):
            if (0 < column < square_sides - 1) and (0 < row < square_sides - 1):
                print(" ", end="", flush=True)
            else:
                print("*", end="", flush=True)

#3. Hollow square -----------------------------------------------------------------------------------------------------


#4. Hollow triangle -----------------------------------------------------------------------------------------------------

"""
    *
    **
    * *
    *  *
    *****
"""
#This function prints out a hollowed triangle using stars to shape the border
def hollow_triangle():
    task_heading("4. Hollow triangle")

    triangle_height = 5

    for row in range(1, triangle_height + 1):

        for column in range(0, row):
            if (2 < row < triangle_height and 0 < column < row - 1):
                print(" ", end="", flush=True)
            else:
                print("*", end="", flush=True)
        print("")

#4. Hollow triangle -----------------------------------------------------------------------------------------------------


#5. Number triangle (1 / 12 / 123 / 1234) -----------------------------------------------------------------------------------------------------
"""
    1
    12
    123
    1234
"""
#This function prints a triangle shape using numbers that count up by one each row
def number_triangle():
    task_heading("5. Number triangle (1 / 12 / 123 / 1234)")

    height = 4

    for row in range(1, height+2):
        for column in range(1, row):
            print(f"{column}", end="", flush=True)
        print("")

#5. Number triangle (1 / 12 / 123 / 1234) -----------------------------------------------------------------------------------------------------


#6. Reverse number triangle-----------------------------------------------------------------------------------------------------
"""
    4321
    321
    21
    1
"""
#This function displays a reversed triangle of numbers that are decrementing from top to bottom
def reverse_number_triangle():
    task_heading("#6. Reverse number triangle")

    height = 4

    for row in range(0, height+2):
        for column in range(height - row, 0, -1):
            print(f"{column}", end="", flush=True)
        print("")

#6. Reverse number triangle-----------------------------------------------------------------------------------------------------


#7. Alphabet triangle--------------------------------------------------------------------------------------------------------
"""
    A
    AB
    ABC
"""
#This function creates a triangle by using letters
def alphabet_triangle():
    task_heading("7. Alphabet triangle")

    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
           'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
           'U', 'V', 'W', 'X', 'Y', 'Z']
    
    height = 3

    for row in range(0, height + 1):
        for column in range(0, row):
            print(f"{letters[column]}", end="", flush=True)
        print("")

#7. Alphabet triangle--------------------------------------------------------------------------------------------------------


#8. Butterfly pattern--------------------------------------------------------------------------------------------------------
"""

    *      *
    **    **
    ***  ***
    ********
    ***  ***
    **    **
    *      *

"""
#This function creates the butterfly pattern by increasing the stars by one up until the midpoint then reducing the stars by 1 each side past the midpoint
def butterfly_pattern():
    task_heading("8. Butterfly pattern")

    height = 8
    midway = (height // 2) + 1 # The halfway point of the butterfly

    for row in range(0, height):

        if midway > row: #If we reach halfway change the direction
            stars = "*" * row
            spaces = " " * ((height - row) - len(stars) + 1)
        else:
            stars = "*" * (height - row)
            spaces = " " * (row - len(stars) + 1)

        print(f"{stars}{spaces}{stars}", end="", flush=True)
        print("")

#8. Butterfly pattern--------------------------------------------------------------------------------------------------------


#9. Sandglass pattern--------------------------------------------------------------------------------------------------------
"""
    *********
     *******
      *****
       ***
        *
       ***
      *****
     *******
    *********
"""
#This function creates a sandglass pattern which is also the opposite to the butterfly pattern
def sand_glass_pattern():
    task_heading("9. Sandglass pattern")

    height = 8
    midway = (height // 2) + 1 # The halfway point of the butterfly

    for row in range(0, height + 1):

        if midway > row: #If we reach halfway change the direction
            space = " " * row
            glass = "*" * ((height - row) - len(space) + 1)
        else:
            space = " " * (height - row)
            glass = "*" * (row - len(space) + 1)

        print(f"{space}{glass}{space}", end="", flush=True)
        print("")

#9. Sandglass pattern--------------------------------------------------------------------------------------------------------


#10. Pascal's triangle (first 5 rows)--------------------------------------------------------------------------------------------------------
"""
        1
       1 1
      1 2 1
     1 3 3 1
    1 4 6 4 1
"""
#This function generates a pascal triangle
def pascals_triangle():
    task_heading("10. Pascal's triangle (first 5 rows)")
    rows = 5

    triangle = []

    for row in range(rows):

        #spaces
        spaces = " " * (rows - row) #get spaces for the row
        print(f"{spaces}", end="", flush=True)

        #numbers
        num = 1
        for col in range(row + 1):
            print(f"{num} ", end="")
            num = num * (row - col) // (col + 1)
        print("")
        
#10. Pascal's triangle (first 5 rows)--------------------------------------------------------------------------------------------------------


#11. Checkerboard pattern using * and spaces--------------------------------------------------------------------------------------------------------
"""
 * * * *
  * * * *
 * * * *
  * * * *
 * * * *
  * * * *
 * * * *
  * * * *
"""
#This function prints a checkers board with spaces and  star symbols using odd and even logic to alternate symbols
def checker_board_pattern():
    task_heading("11. Checkerboard pattern using * and spaces")

    checker_dimensions = 8 # checkerboars are 8 x 8

    for row in range(checker_dimensions):
        for column in range(checker_dimensions):

            if (row + column) % 2 == 0:
                print("*", end="")
            else:
                print(" ", end="")
        print()


#11. Checkerboard pattern using * and spaces--------------------------------------------------------------------------------------------------------

#12. Christmas tree pattern--------------------------------------------------------------------------------------------------------
"""
    *
   ***
  *****
 *******
    *
"""

#This function creates a christmas tree by first creating the top of the tree which is a pyramid then adding on the trunk as a singular star in the center bottom
def christmas_tree():
    task_heading("12. Christmas tree pattern")
    rows = 5

    triangle = []

    for row in range(rows):

        #spaces
        spaces = " " * (rows - row) #get spaces for the row
        print(f"{spaces}", end="", flush=True)

        for col in range(row + 1):
            print(f"*", end=" ")
        print("")
    
    tree_trunk_space = " " * rows
    print(f"{tree_trunk_space}*{tree_trunk_space}")
        
#12. Christmas tree pattern--------------------------------------------------------------------------------------------------------

#This function is responsible for loading task 5 programs
def task_5_loader():
    # right_aligned_triangle()
    # diamond_pattern()
    # hollow_square()
    # hollow_triangle()
    # number_triangle()
    # reverse_number_triangle()
    # alphabet_triangle()
    # butterfly_pattern()
    # sand_glass_pattern()
    # pascals_triangle()
    # checker_board_pattern()
    christmas_tree()

task_5_loader()