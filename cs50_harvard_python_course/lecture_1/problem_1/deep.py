# Deep Thought
# In deep.py, implement a program that prompts the user for the answer to the Great Question of Life, 
# the Universe and Everything, outputting Yes if the user inputs 42 or (case-insensitively) forty-two or 
# forty two. Otherwise output No.

# How to Test
# Here’s how to test your code manually:

# Run your program with python deep.py. Type 42 and press Enter. Your program should output:
# Yes 
# Run your program with python deep.py. Type Forty Two and press Enter. Your program should output:
# Yes
# Run your program with python deep.py. Type forty-two and press Enter. Your program should output
# Yes
# Run your program with python deep.py. Type 50 and press Enter. Your program should output
# No

# Get user input
answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

# Clean the input: convert to lowercase and remove spaces
clean_answer = answer.lower().strip()

# Check all possible correct answers
if clean_answer == "42" or clean_answer == "forty-two" or clean_answer == "forty two":
    print("Yes")
else:
    print("No")
