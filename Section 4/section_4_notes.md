836 words excluding this line------------------------------------------------------------------------------------------

There are 6 main types of operators in python and they are as follows: (Excluding Bitwise)
    1. Arithmatic Operators which are used for doing mathematical calculations.

        i.  '+' is used for addition of numbers or apending strings together.
        ii. '-' is used for subtraction of numbers like integers and floats.
        iii. '*' is used for multiplication of integers and floats.
        iv. '/' is used for division decimal division that also shows a remainder.
        v.  '//' is used for integer division where you want to get only the rounded number like 10 // 3 = 3
        vi. '%' also known as the modulas operator is used for getting specifically the remainder from division
        vii. '**' is used for getting a number to the power of another / exponents 

    2. Comparison Operators are used to return 'True' or 'False' when comparing values or conditions.
        
        i.  '==' is used for checking equivalancy of values or conditions, where it returns true if equal and false if not.
        ii. '!=' also known as 'not equal to' is used to return true if something is not equivalant and false otherwise.
        iii.'>' known as the 'greater than' symbol is used to compare if a number or string is greater than another.
        iv. '<' known as the 'less than' symbol is used to compare if a number or string is less than another.
        v.  '>=' known as 'greater than or equal to' is used to test for equivalancy or if a value is greater than another.
        vi. '<=' known as 'less than or equal to' is used to test for equivalancy or if a value is less than another.

    3. Logical Operators are used to combine logic together or test for either or situations.

        i.  'and' is used to return true if both comparisons return true. example - you are an adult 'and' you are employed
        ii. 'or' is used to return true if either of the conditions/comparisons return true. example - you can vote if you are a citizen Or have status.
        iii 'not' is used to return true if something is not equivalant or contained within something else. example 'answer not in ["yes", "no"]'.

    4. Assignment Operators are used to assign and update values.

        i.  '=' is used to set 1 value to another, like a variable to a string or number. example - username = "Michael"
        ii. '+=' is used to append values onto an existing value. example - first_name += " Scott", assuming first_name was "Michael" before, the new first_name will be "Michael Scott". It can also be used to increment number values.
        iii. '-=' is used to update a value with itself minus whatever value is on the right of the equation.
        iv. '*=' is used to update a value by multiplying itself to whatever is to the right of the queation.
        v.  '/=' is used to update a value by dividing  itself by whatever is to the right of the queation.

    5. Membership Operators are used to check if a value is in or not contained within a collection

        i.  'in' is used to see if a value is contained within a collection. example - maybe in ["yes", "no"] = False
        ii. 'not in' is used to see if a value is not contained within a collection. example - "maybe" not in ["yes", "no"] = True

    6. Identity Operators are used to check if two variables refer to the same object.

        i.  'is' is used to return true if variables point to the same object. 
                example 1 - a = [1,2], b = a, a is b = True
                example 2 - a = [1,2], b = [1,2], a is b = False
                This is because the value itself isn't the deciding factor but instead whether one points to the other
        ii. 'is not' is used to return true if variables do NOT point to the same object.
                example 1 - a = [1,2], b = a, a is not b = False
                example 2 - a = [1,2], b = [1,2], a is not b = True

    The main difference between "==" and "is" operators is that "==" compares the values if they are equal, and "is" compares if they share the same reference.

        example 1 - [1,2] == [1,2] would return True as they contain the same values, but they are two entirely seperate objects.
        example 2 - [1,2] is [1,2] would return False as they refer to two different objects regardless of their values contained within.

    When choosing between nested and flat conditions the main reasons to use one over another is:

        1. Flat Conditions:
            i. When you want to combine logic in one line using 'and' or 'or' operators.
            ii. The logic is simple and more human readable together.
            iii. The conditions do not depend on each other to work.
            iv. Conditions are simple and related.
            v. You want clean and easily readable code

        2. Nested Conditions:
            i. Your previous condition is depended on by the previous condition being true to do it's function.
            ii. You want a clear step by step logic format.
            iii. You want something different to happen based on specific conditions being met.
            iv. There is too much going on in one line making it harder to follow a flat structure.