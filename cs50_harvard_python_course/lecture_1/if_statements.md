# if Statements
- In your terminal window, type code compare.py. This will create a brand new file called “compare.”
- In the text editor window, begin with the following:

```py
x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y:
    print("x is less than y")
```
Notice how your program takes the input of the user for both x and y, casting them as integers and saving them into their respective x and y variables. Then, the if statement compares x and y. If the condition of x < y is met, the print statement is executed.

if statements use bool (Boolean) values (True or False) to decide whether or not to execute code. If the comparison x > y is True, the interpreter runs the indented block.