# Pythonic
# In the programming world, there are types of programming that are called “Pythonic” in nature. That is, 
# there are ways to program that are sometimes only seen in Python programming. Consider the following revision to our program:
def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")


def is_even(n):
    return True if n % 2 == 0 else False


main()
# Notice that this return statement in our code is almost like a sentence in English. This is a unique way of coding only seen in Python.

# We can further revise our code and make it more and more readable:

def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")


def is_even(n):
    return n % 2 == 0


main()
# Notice that the program will evaluate what is happening within the n % 2 == 0 as either True or False and simply return that to the main function.