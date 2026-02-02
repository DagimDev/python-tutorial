# Improving Your First Python Program
# In our text editor in hello.py we can add another function. input is a function that takes a prompt 
# as an argument. We can edit our code to say

input("What's your name? ")
print("hello, world")
# This edit alone, however, will not allow your program to output what your user inputs. For that, 
# we will need to introduce you to variables



# Further Improving Your First Python Program
# We can further edit our code as follows:

#  Ask the user for their name
name = input("What's your name? ")

#  Print hello and the inputted name
print("hello, " + name)
# It turns out that some functions take many arguments.
# We can use a comma , to pass in multiple arguments by editing our code as follows:

#  Ask the user for their name
name = input("What's your name? ")

# Print hello and the inputted name
print("hello,", name)
# The output in the terminal, if we typed “Dagim” we would be hello, Dagim. Success.