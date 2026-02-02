## Strings and Parameters
A string, known as a str in Python, is a sequence of text.
Rewinding a bit in our code back to the following, there was a visual side effect of having the result appear on multiple lines:

```py
# Ask the user for their name
name = input("What's your name? ")
print("hello,")
print(name)
```
Functions take arguments that influence their behavior. If we look at the documentation for print you’ll notice we can learn a lot about the arguments that the print function takes.
Looking at this documentation, you’ll learn that the print function automatically includes the argument end='\n'. This \n indicates that the print function will automatically create a line break when run. The function takes an argument called end, and the default is to create a new line.
However, we can technically provide an argument for end ourselves such that a new line is not created!
We can modify our code as follows:
```py
# Ask the user for their name
name = input("What's your name? ")
print("hello,", end="")
print(name)
```
By providing end="" we are overwriting the default value of end such that it never creates a new line after this first print statement. Providing the name as “Dagim”, the output in the terminal window will be hello, Dagim.

# Parameters, therefore, are arguments that can be taken by a function.

## A small problem with quotation marks
Notice how adding quotation marks as part of your string is challenging.
print("hello,"friend"") will not work, and the interpreter will throw an error.
Generally, there are two approaches to fixing this. First, you could simply change the quotes to single quotation marks.
Another, more commonly used approach would be to write print("hello, \"friend\""). The backslashes tell the interpreter that the following character should be treated as a quotation mark in the string and avoid an interpreter error.