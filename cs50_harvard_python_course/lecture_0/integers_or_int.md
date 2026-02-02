# Integers or int
- In Python, an integer is referred to as an int.
- In the world of mathematics, we are familiar with +, -, *, /, and % operators. That last operator % or modulo operator may not be very familiar to you.
- You don’t have to use the text editor window to run Python code. Down in your terminal, you can run python alone. You will be presented with >>> in the terminal window. You can then run live, interactive code. You could type 1+1, and it will run that calculation. 
- Opening up VS Code again, we can type code calculator.py in the terminal. This will create a new file in which we will create our own calculator.
First, we can declare a few variables.

x = 1
y = 2

z = x + y

print(z)
Naturally, when we run python calculator.py we get the result in the terminal window of 3. We can make this more interactive using the input function.

x = input("What's x? ")
y = input("What's y? ")

z = x + y

print(z)
Running this program, we discover that the output is incorrect as 12. Why might this be?
Prior, we have seen how the + sign concatenates two strings. Because your input from your keyboard on your computer comes into the interpreter as text, it is treated as a string. We, therefore, need to convert this input from a string to an integer. We can do so as follows:

x = input("What's x? ")
y = input("What's y? ")

z = int(x) + int(y)

print(z)
The result is now correct. The use of int(x) is called “casting,” where a value is temporarily changed from one type of variable (in this case, a string) to another (here, an integer).

We can further improve our program as follows:

x = int(input("What's x? "))
y = int(input("What's y? "))

print(x + y)
This illustrates that you can run functions on functions. The inner function is run first, and then the outer one is run. First, the input function is run. Then, the int function.
