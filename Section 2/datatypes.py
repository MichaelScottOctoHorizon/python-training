
#This function is for creating a variable for every data type - int, float, str, bool, NoneType
def all_data_types():
    
    integer_type = 32       #integer whole number - int
    decimal_type = 75.50    #decimal point number - float
    text_type = "Array of characters also known as a string" #array of characters also known as a String = str
    null_type = None #null type, known in python as None and stands for nothing or nothing type

    print(f"--------------------------Main Data Types-------------------------------\n")
    print(f"|\t integer_type: {integer_type}  {type(integer_type)}")
    print(f"|\t decimal_type: {decimal_type}  {type(decimal_type)}")
    print(f"|\t text_type: {text_type}  {type(text_type)}")
    print(f"|\t null_type: {null_type}  {type(null_type)}\n")
    print(f"|--------------------------Main Data Types-------------------------------")


all_data_types()