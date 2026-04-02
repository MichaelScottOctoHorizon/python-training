For loops and while loops are both useful for solving problems in their own way.

For loops are mostly ideal when you:
Know how many times you want to loop
Used for iterating over lists
Running a fixed number of items
Example 1 - for number in range(20):
Example 2 - for item in [“Steak”, “Ribs”, “Samon”, “Wings”]:
Example 3 - for day in [“Friday”, “Saturday”, “Sunday”]

While loops are ideal when you:
Want an infinite loop to execute until some condition is met.
Don’t know how many iterations will be needed.
Great for user input loops
Example 1 - while True:
Example 2 - while user_input not in [“exit”, “close”]

There are three main forms of “range()” which all depend on the amount of arguments you give.

When the coder puts:
One argument - for number in range(20), the argument is classed as the ending value you want to iterate to starting from 0. This loop will count up to 20 from 0 in increments of 1 per iteration.

Two arguments - for number in range(start, stop) - the 1st argument is when you want to specify the starting value, like if you wanted to start counting from 5 you can set it as 5. The 2nd argument would be the value you want the iteration to go to or end on. In python though the loop will end short by 1 so it’s always advised to either set the end argument to 1 above where you want to end.

Three arguments - for number in range(increment_amount, start, end) - This range gives you the most control. It allows you to first specify how much you want to increment or count by. By default it’s one but you can set it to increment by any amount. The send argument is the starting point and the 3rd is the end point and they are used to set the starting and ending points of the loop.

There are three main loop control variables in python, and they are as follows:

Break - this is used used to completely break out of a loop without needing the loop condition to be met.
Example - You may want to loop through a list of users in a list, and when you find the user you want to break out of the loop because it is unnecessary to search through the remaining users which can range from 1000’s to over 100,000 in real live applications.

Continue - This is used to skip any code within the loop from executing that occurs after it. After continue is activated, it will automatically skip code from executing in that current iteration of the loop but if the loop still has more iterations left it will still continue to run from the next iteration.
Example - You may have a function that prints out all even numbers. You can create an if statement that activates when an odd number is detected. If the number is odd, continue can prevent the later occurring print statement of the number from printing, in turn only allowing even numbers to show up.

Pass - this is used as a placeholder  for bypassing an error being flagged within an empty loop, function, or if statement ect. It is useful because you may not always know what you want to put within a body of code right away but you still want the code to run.
Example - you may be creating a bunch of functions but haven’t yet thought of what you might want to put inside their body. So in this case you can put the operation ‘pass’ which will bypass flagging the error when you try to run the program.

Some common loop mistakes are as follows:
Off-By-One Error - This occurs when your range is either 1 too high or 1 too low.
Example - you may have a loop to count from 1 to 5 and have your range set as “range(5)”. You may think if you print based on the count you’ll get “1,2,3,4,5”, but that would be incorrect. Instead you would get “0, 1,2,3,4” which is 5 numbers but by default range starts from 0 based counting and not 1. The off by one comes in because though you specified 5 as the argument, it will be technically counting from 1 to 4. To fix this you can set the argument to 1 above what you want every time or by adding one to the variable.
Infinite loops - This can occur if a coder forgets to implement a loop control variable or an exit condition to exit the loop on meeting the condition.
Example - You may have a while loop that is set to ‘while True:’, and within the loop you may never specify a break point on an if condition being met like if the user types ‘exit’, ‘break’ can then exit the loop.
Forgetting to update loop variable.
In a while loop you may have initialised a loop variable called ‘count’ to 0, but within the loop you forgot to either increment or decrement it by an amount like 1. If the loop is ‘while count < 5:’ the loop will endlessly loop due to count being 0 and never getting to 5. To fix this always remember to increment and decrement the loop variables and test it many times.
Using break/continue/return in the wrong place can cause many logical flow issues like code needing to end the loop from ever running, to incorrect outputs.
Example - If you use break in a loop that is meant to sum up a list of integers it may skip summing up the remaining numbers in the list giving you an incorrect sum.
Example - if you use continue in the wrong place like right before you increment a count variable in the while loop the loop will never end as the variable never increments.
Example -  using return in the wrong place or too early may cause important logic from running. Like if you put a return statement before the database logic in a function to update the user in the Dateabse the user will not be updated.

Nested loops work by first iterating the outer loop instance 1st then the inner loop will do all of its iterations at once before the outer loop goes to its next iteration. The inner loop will do all of its iterations on repeat for every one iteration of the outer loop.

Handtrace example would be:

my_list = [
	[1,2,3],
	[4,5,6],
	[7,8,9]
] 
	
	for row in my_list:
	   for column in row:
		print(f“{column}”, end=”, ”)

	Output = 1,2,3,4,5,6,7,8,9,
	
Row = 0 , column loop will print 1, then 2, then 3
Row = 1 , column loop will print 4, then 5, then 6
Row = 2 , column loop will print 7, then 8, then 9

Tips for infinite loops are as follows:

Always ensure you have a loop control variable
Always ensure there is some criteria to exit a loop.
Always ensure you place your breaks, continue, and returns in the correct place
Always test code many times and try to break it to detect potential bugs.
Take your time to ensure your logic is tested on many different types of data.

In Section 4, I learned how to use conditional statements (if/elif/else) to make decisions in programs. In Section 5, loops build on this by allowing those decisions to be repeated multiple times.

Loops and conditionals work together by enabling repeated decision-making. A loop runs a block of code multiple times, while conditional statements inside the loop determine what happens during each iteration.

For example, conditions can be used to control when a loop exits, filter data, or update values based on certain criteria. This combination allows programs to handle multiple inputs, validate data, and perform more complex logic than using conditionals alone.
