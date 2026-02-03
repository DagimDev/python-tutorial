# Meal Time
# Suppose that you’re in a country where it’s customary to eat breakfast between 7:00 and 8:00, lunch 
# between 12:00 and 13:00, and dinner between 18:00 and 19:00. Wouldn’t it be nice if you had a program 
# that could tell you what to eat when?

# In meal.py, implement a program that prompts the user for a time and outputs whether it’s breakfast 
# time, lunch time, or dinner time. If it’s not time for a meal, don’t output anything at all. Assume 
# that the user’s input will be formatted in 24-hour time as #:## or ##:##. And assume that each meal’s 
# time range is inclusive. For instance, whether it’s 7:00, 7:01, 7:59, or 8:00, or anytime in between, 
# it’s time for breakfast.

# Structure your program per the below, wherein convert is a function (that can be called by main) 
# that converts time, a str in 24-hour format, to the corresponding number of hours as a float. 
# For instance, given a time like "7:30" (i.e., 7 hours and 30 minutes), convert should return 7.5 
# (i.e., 7.5 hours).


# How to Test
# Here’s how to test your code manually:

# Run your program with python meal.py. Type 7:00 and press Enter. Your program should output:
# breakfast time   
# Run your program with python meal.py. Type 7:30 and press Enter. Your program should output:
# breakfast time
# Run your program with python meal.py. Type 12:42 and press Enter. Your program should output
# lunch time
# Run your program with python meal.py. Type 18:32 and press Enter. Your program should output
# dinner time

def main():
    # Get time from user
    time = input("What time is it? ")

    # Convert time to hours as float
    hours = convert(time)

    # Check which meal time it is
    if 7.0 <= hours <= 8.0:
        print("breakfast time")
    elif 12.0 <= hours <= 13.0:
        print("lunch time")
    elif 18.0 <= hours <= 19.0:
        print("dinner time")
    # If not meal time, output nothing


def convert(time):
    """
    Convert time string to hours as float.
    Example: "7:30" -> 7.5
    """
    # Split hours and minutes
    hours, minutes = time.split(":")

    # Convert to float and calculate total hours
    total_hours = float(hours) + float(minutes) / 60
    print(total_hours)
    return total_hours


if __name__ == "__main__":
    main()
