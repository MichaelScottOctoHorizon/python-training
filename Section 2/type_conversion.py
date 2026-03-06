
#This function is responsable for converting the following, int -> float, float -> int, and string -> int
#This function also calls a function that tries to convert a string to an integer but fails due to an invalid type conversion
def type_conversions():
    int_type = 18
    float_type = 12.50
    string_type_1 = "1993"
    string_type_2 = "Hello"

    print(f"int: {int_type} converted to float = {float(int_type)}")
    print(f"float: {float_type} converted to int = {int(float_type)}")
    print(f"str: {string_type_1} converted to int = {int(string_type_1)}")
    
    invalid_conversion(string_type_2)

# This function accepts a parameter string and displays an appropriate message depending 
# on whether the string is convertable to an integer or not
def invalid_conversion(string_type_2):
    
    try:
        string_type_2 = f"{int(string_type_2)} was converted to an integer successfully!"
    except ValueError:
        string_type_2 = f"The String '{string_type_2}' is not convertable to a integer"
    
    print(string_type_2)

type_conversions()