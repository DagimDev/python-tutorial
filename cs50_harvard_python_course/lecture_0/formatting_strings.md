## Formatting Strings
- Probably the most elegant way to use strings would be as follows:
```py
# Ask the user for their name
name = input("What's your name? ")
print(f"hello, {name}")
```
Notice the f in `print(f"hello, {name}")`. This f is a special indicator for Python to treat this string a special way, different than previous approaches

# More on Strings
You should never expect your user to cooperate as intended. Therefore, you will need to ensure that the input of your user is corrected or checked.
It turns out that built into strings is the ability to remove whitespace from a string.
By utilizing the strip method on name (for example, name = name.strip()), you will remove any whitespace from the left and right of the user’s input. You can modify your code to be:
```py
# Ask the user for their name
name = input("What's your name? ")

# Remove whitespace from the str
name = name.strip()

# Print the output
print(f"hello, {name}")
# Rerunning this program, regardless of how many spaces you type before or after the name, it will strip # off all the whitespace.

# Using the title method, it would title case the user’s name:

# Ask the user for their name
name = input("What's your name? ")

# Remove whitespace from the str
name = name.strip()

# Capitalize the first letter of each word
name = name.title()

# Print the output
print(f"hello, {name}")
```
By this point, you might be very tired of typing python repeatedly in the terminal window. You can use the up-arrow key on your keyboard to recall the most recent terminal commands you have entered.
Notice that you can modify your code to be more efficient:
```py
# Ask the user for their name
name = input("What's your name? ")

# Remove whitespace from the str and capitalize the first letter of each word
name = name.strip().title()

# Print the output
print(f"hello, {name}")
We could even go further!

# Ask the user for their name, remove whitespace from the str and capitalize the first letter of each word
name = input("What's your name? ").strip().title()

# Print the output
print(f"hello, {name}")
```