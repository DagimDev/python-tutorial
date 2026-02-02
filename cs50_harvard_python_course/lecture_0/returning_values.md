# Returning Values
You can imagine many scenarios where you don’t just want a function to perform an action but also to return a value back to the main function. For example, rather than simply printing the calculation of x + y, you may want a function to return the value of this calculation back to another part of your program. This “passing back” of a value we call a return value.
Returning to our calculator.py code by typing code calculator.py. Erase all code there. Rework the code as follows:
```py
def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))


def square(n):
    return n * n


main()
```
Effectively, x is passed to square. Then, the calculation of x * x is returned back to the main function.