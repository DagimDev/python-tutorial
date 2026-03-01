## Unit Tests
Up until now, you have been likely testing your own code using print statements.
Alternatively, you may have been relying upon CS50 to test your code for you!
It’s most common in industry to write code to test your own programs.
In your console window, type code calculator.py. Note that you may have previously coded this file in a previous lecture. In the text editor, make sure that your code appears as follows:
```py
def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))


def square(n):
    return n * n


if __name__ == "__main__":
    main()
```
Notice that you could plausibly test the above code on your own using some obvious numbers such as 2. However, consider why you might want to create a test that ensures that the above code functions appropriately.

Following convention, let’s create a new test program by typing code test_calculator.py and modify your code in the text editor as follows:

from calculator import square

```py
def main():
    test_square()


def test_square():
    if square(2) != 4:
        print("2 squared was not 4")
    if square(3) != 9:
        print("3 squared was not 9")


if __name__ == "__main__":
    main()
```
Notice that we are importing the square function from calculator.py on the first line of code.

In the console window, type python test_calculator.py. You’ll notice that nothing is being outputted. It could be that everything is running fine! Alternatively, it could be that our test function did not discover one of the “corner cases” that could produce an error.
Right now, our code tests two conditions. If we wanted to test many more conditions, our test code could easily become bloated. How could we expand our test capabilities without expanding our test code?