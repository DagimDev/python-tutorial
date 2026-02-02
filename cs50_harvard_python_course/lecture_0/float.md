# Float Basics
A floating point value is a real number that has a decimal point in it, such as 0.52.
You can change your code to support floats as follows:

x = float(input("What's x? "))
y = float(input("What's y? "))

print(x + y)
This change allows your user to enter 1.2 and 3.4 to present a total of 4.6.

Let’s imagine, however, that you want to round the total to the nearest integer. Looking at the Python documentation for round, you’ll see that the available arguments are round(number[, ndigits]). Those square brackets indicate that something optional can be specified by the programmer. Therefore, you could do round(n) to round a digit to its nearest integer. Alternatively, you could code as follows:

# Get the user's input
x = float(input("What's x? "))
y = float(input("What's y? "))

# Create a rounded result
z = round(x + y)

# Print the result
print(z)
The output will be rounded to the nearest integer.

What if we wanted to format the output of long numbers? For example, rather than seeing 1000, you may wish to see 1,000. You could modify your code as follows:

# Get the user's input
x = float(input("What's x? "))
y = float(input("What's y? "))

# Create a rounded result
z = round(x + y)

# Print the formatted result
print(f"{z:,}")
Though quite cryptic, that print(f"{z:,}") creates a scenario where the outputted z will include commas where the result could look like 1,000 or 2,500.


# More on Floats
How can we round floating point values? First, modify your code as follows:

# Get the user's input
x = float(input("What's x? "))
y = float(input("What's y? "))

# Calculate the result
z = x / y

# Print the result
print(z)
When inputting 2 as x and 3 as y, the result z is 0.6666666666, seemingly going on to infinity as we might expect.

Let’s imagine that we want to round this down. We could modify our code as follows:

# Get the user's input
x = float(input("What's x? "))
y = float(input("What's y? "))

# Calculate the result and round
z = round(x / y, 2)

# Print the result
print(z)
As we might expect, this will round the result to the nearest two decimal points.

We could also use an f-string to format the output as follows:

# Get the user's input
x = float(input("What's x? "))
y = float(input("What's y? "))

# Calculate the result
z = x / y

# Print the result
print(f"{z:.2f}")
This cryptic f-string code displays the same as our prior rounding strategy.
