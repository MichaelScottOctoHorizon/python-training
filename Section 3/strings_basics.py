
# This function concatenates a name to the greeting "My name is " example - My name is Michael, 
# and it returns a new string of the combination
def concatenate_string(name):
    greeting = "My name is"
    return greeting + name

# This function is responsible for displaying the length of the string name 
# and the length of the greeting appended to the string name
def compare_lengths_of_strings(name_param):
    name = name_param
    name_with_greeting = concatenate_string(name)

    print(f"{name} length = {len(name)}")
    print(f"{name_with_greeting} length = {len(name_with_greeting)} \n\n")


#This function is responsible for showing how the various string methods effect a string - lower, upper, strip, replace, split
def using_string_methods(phrase):
    phrase_replaced = phrase.replace("---", "") #All --- replaced with an empty string to clean up the phrase
    phrase_lowercased = phrase_replaced.lower() #I make every character lowercase letters
    phrase_uppercased = phrase_replaced.upper() #I make every character uppercase letters
    phrase_stripped = phrase_replaced.strip() #I get rid of the blank spaces at the start and end of a string
    phrase_splitted = phrase_replaced.split() #I create an array of words gathered from the string
    phrase_title = phrase_replaced.title() #Formats a string where every new word starts off with a capital letter

    print(f"--------------Original Phrase = {phrase} \n")
    print(f"\t replaced: {phrase_replaced}")
    print(f"\t lowercase: {phrase_lowercased}")
    print(f"\t uppercase: {phrase_uppercased}")
    print(f"\t stripped: {phrase_stripped}")
    print(f"\t split: {phrase_splitted}")
    print(f"\t title: {phrase_title}\n\n")

#This function accepts a string and a index to display details about the index in the string
def access_char_by_index(text, index):
    print(f"'{text}' has a '{text[index]}' at index '{index}'\n\n")

#Using slicing I got the first half of the phrase
def slicing_half_of_text(text):
    print(f"First half of '{text}' = '{text[0:len(text) // 2]}'") #integer division used to make a valid index not a float

compare_lengths_of_strings("Michael")
using_string_methods(" hi im a --- random phrase ---- change me please ") #lower, upper, replace, strip, split, extra = title
access_char_by_index("Game of thrones is my favorite show!", 8) #Positive Index access
access_char_by_index("Game of thrones is my favorite show!", -1) #Negative Index access
slicing_half_of_text("Game of thrones is my favorite show!")
