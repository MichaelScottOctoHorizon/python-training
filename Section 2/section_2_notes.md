
Dynamic typing in python means variables don't have to be initialized to a type such as int, str, or float ect. Variables can also be interchangable between different types which means if you create a variable called "number_var" and set the value to an integer value, you can later mutate the variable to hold another type such as a float, string or boolean to name a few.

The main reasons why Python was made to be dynamically typed was to make coding more efficient to read, write and experiment with. By removing things such as declaring variable types, developers didn't need to waste time writing boiler plate code. This helped alot in both the declaration of variables and functions were more robust because you could make one function do the job of many other simular functions.

Since Python is dynamically typed, when reasigning variables to different types after initializing it'll just work and only break your program depending on the logic set out in your code. Example of this could be if you set a num_1 variable to an actual integer and do computations on it everything should work, but if you mutate it without proper exception handling to like a string you may get an error when trying to divide a string by a number.

int("10") will work fine, but  int("10.5") will give you an error because you can't go directly from a float string to an integer. If you wanted to accomplish this you would need to first do something like this int(float("10.5")) which would give you the value 10 because converting to an int would ignore everything after the decimal point.

bool("False") returns True because python considers any value that isn't empty, null, or of type None to be true. In this case the string "False" has content in it so it's not empty nor null nor of type None.