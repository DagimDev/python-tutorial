# camelCase
# In some languages, it’s common to use camel case (otherwise known as “mixed case”) for variables’ 
# names when those names comprise multiple words, whereby the first letter of the first word is 
# lowercase but the first letter of each subsequent word is uppercase. For instance, whereas a variable 
# for a user’s name might be called name, a variable for a user’s first name might be called firstName, 
# and a variable for a user’s preferred first name (e.g., nickname) might be called preferredFirstName.

# Python, by contrast, recommends snake case, whereby words are instead separated by underscores (_), 
# with all letters in lowercase. For instance, those same variables would be called name, first_name, 
# and preferred_first_name, respectively, in Python.

# In a file called camel.py, implement a program that prompts the user for the name of a variable in 
# camel case and outputs the corresponding name in snake case. Assume that the user’s input will indeed 
# be in camel case.

# How to Test
# Here’s how to test your code manually:

# Run your program with python camel.py. Type name and press Enter. Your program should output:
# name   
# Run your program with python camel.py. Type firstName and press Enter. Your program should output:
# first_name
# Run your program with python camel.py. Type preferredFirstName and press Enter. Your program should 
# output
# preferred_first_name


# Get input from user (camel case variable name)
camel_case = input("camelCase: ")

# Initialize empty string for snake case result
snake_case = ""

# Iterate through each character in the input
for char in camel_case:
    # If character is uppercase
    if char.isupper(): 
        # Add underscore and the lowercase version of the character
        snake_case += "_" + char.lower()  
    # Otherwise, just add the character as is
    else:
        snake_case += char
        
print(snake_case)