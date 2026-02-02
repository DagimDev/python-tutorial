## Variables

- A variable is just a container for a value within your own program.
- In your program, you can introduce your own variable in your program by editing it to read

```python
name = input("What's your name? ")
print("hello, world")
```

- Notice that this equal = sign in the middle of name = input("What's your name? ") has a special role in programming. This equal sign literally assigns what is on the right to what is on the left. Therefore, the value returned by input("What's your name? ") is assigned to name.

- If you edit your code as follows, you will notice an unexpected result:
```python
name = input("What's your name? ")
print("hello, name")
```
- The program will return hello, name in the terminal window regardless of what the user types.
- Further editing our code, you could type
```python
name = input("What's your name? ")
print("hello,")
print(name)
```
- The result in the terminal window would be

        What's your name? Dagim
        hello
        Dagim
