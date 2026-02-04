# Exceptions

- Exceptions are things that go wrong within our coding.
- Exceptions are problems that arise while your program is running.
- In our text editor, type code hello.py to create a new file. Type as follows (with the intentional errors included):

```py
print("hello, world)
```

Notice that we intentionally left out a quotation mark.

Running python hello.py in the terminal produces an error. The interpreter reports a syntax error. Syntax errors generally mean you should double-check that you typed your code correctly.

# Runtime Errors

Runtime errors refer to those created by unexpected behavior within your code. For example, perhaps you intended for a user to input a number, but they input a character instead. Your program may throw an error because of this unexpected input from the user.
In your terminal window, run code number.py. Code as follows in your text editor:

```py
x = int(input("What's x? "))
print(f"x is {x}")
```

Notice that by including the f, we tell Python to interpolate what is in the curly braces as the value of x. Further, testing out your code, you can imagine how one could easily type in a string or a character instead of a number. Even still, a user could type nothing at all – simply hitting the enter key.

As programmers, we should be defensive to ensure that our users are entering what we expected.

If we run this program and type “cat”, we’ll see `ValueError: invalid literal for int() with base 10: 'cat'.` In other words, the int function cannot convert the text “cat” into a number.

An effective strategy to fix this potential error would be to create “error handling” to ensure the user behaves as we intend.
