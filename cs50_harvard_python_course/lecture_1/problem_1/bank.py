# Home Federal Savings Bank
# In a file called bank.py, implement a program that prompts the user for a greeting. If the greeting 
# starts with “hello”, output $0. If the greeting starts with an “h” (but not “hello”), output $20.
# Otherwise, output $100. Ignore any leading whitespace in the user’s greeting, and treat the user’s 
# greeting case-insensitively.

# How to Test
# Here’s how to test your code manually:

# Run your program with python bank.py. Type Hello and press Enter. Your program should output:
# $0 
# Run your program with python bank.py. Type Hello, Newman and press Enter. Your program should output:
# $0
# Run your program with python bank.py. Type How you doing? and press Enter. Your program should output
# $20
# Run your program with python bank.py. Type What's happening? and press Enter. Your program should output
# $100

greeting = input("Greeting: ")

clean_greeting = greeting.strip().lower()

if clean_greeting.startswith("hello"):
    print("$0")
elif clean_greeting.startswith("h"):
    print("$20")
else:
    print("$100")
