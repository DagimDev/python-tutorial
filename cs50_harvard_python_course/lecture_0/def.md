Def
Wouldn’t it be nice to create our own functions?
Let’s bring back our final code of hello.py by typing code hello.py into the terminal window. Your starting code should look as follows:

# Ask the user for their name, remove whitespace from the str and capitalize the first letter of each word
name = input("What's your name? ").strip().title()

# Print the output
print(f"hello, {name}")
We can better our code to create our own special function that says “hello” for us!

Erasing all our code in our text editor, let’s start from scratch:

```py
name = input("What's your name? ")
hello()
print(name)
Attempting to run this code, your interpreter will throw an error. After all, there is no defined function for hello.

We can create our own function called hello as follows:

def hello():
    print("hello")


name = input("What's your name? ")
hello()
print(name)
```
Notice that everything under def hello() is indented. Python is an indented language. It uses indentation to understand what is part of the above function. Therefore, everything in the hello function must be indented. When something is not indented, it treats it as if it is not inside the hello function. Running python hello.py in the terminal window, you’ll see that your output is not exactly as you may want.

We can further improve our code:
```py
# Create our own function
def hello(to):
    print("hello,", to)


# Output using our own function
name = input("What's your name? ")
hello(name)
```

Here, in the first lines, you are creating your hello function. This time, however, you are telling the interpreter that this function takes a single parameter: a variable called to. Therefore, when you call hello(name) the computer passes name into the hello function as to. This is how we pass values into functions. Very useful! Running python hello.py in the terminal window, you’ll see that the output is much closer to our ideal presented earlier in this lecture.

We can change our code to add a default value to hello:
```py
# Create our own function
def hello(to="world"):
    print("hello,", to)


# Output using our own function
name = input("What's your name? ")
hello(name)

# Output without passing the expected arguments
hello()
```
Test out your code yourself. Notice how the first hello will behave as you might expect, and the second hello, which is not passed a value, will, by default, output hello, world.

We don’t have to have our function at the start of our program. We can move it down, but we need to tell the interpreter that we have a main function and a separate hello function.
```py
def main():

    # Output using our own function
    name = input("What's your name? ")
    hello(name)

    # Output without passing the expected arguments
    hello()


# Create our own function
def hello(to="world"):
    print("hello,", to)
```
This alone, however, will create an error of sorts. If we run python hello.py, nothing happens! The reason for this is that nothing in this code is actually calling the main function and bringing our program to life.

The following very small modification will call the main function and restore our program to working order:

```py
def main():

    # Output using our own function
    name = input("What's your name? ")
    hello(name)

    # Output without passing the expected arguments
    hello()


# Create our own function
def hello(to="world"):
    print("hello,", to)


main()
```