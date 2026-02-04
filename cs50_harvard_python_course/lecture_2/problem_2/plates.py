# Vanity Plates
# CS50 license plate

# In Massachusetts, home to Harvard University, it’s possible to request a vanity license plate for your 
# car, with your choice of letters and numbers instead of random ones. Among the requirements, though, are:

# “All vanity plates must start with at least two letters.”
# “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 
# characters.”
# “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 
# would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot 
# be a ‘0’.”
# “No periods, spaces, or punctuation marks are allowed.”
# In plates.py, implement a program that prompts the user for a vanity plate and then output Valid if 
# meets all of the requirements or Invalid if it does not. Assume that any letters in the user’s input 
# will be uppercase. Structure your program per the below, wherein is_valid returns True if s meets all 
# requirements and False if it does not. Assume that s will be a str. You’re welcome to implement 
# additional functions for is_valid to call (e.g., one function per requirement).

# def main():
#     plate = input("Plate: ")
#     if is_valid(plate):
#         print("Valid")
#     else:
#         print("Invalid")


# def is_valid(s):
#     ...


# main()


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Check length requirement (2-6 characters)
    if len(s) < 2 or len(s) > 6:
        return False

    # Check first two characters are letters
    if not (s[0].isalpha() and s[1].isalpha()):
        return False

    # Check for invalid characters (only alphanumeric allowed)
    if not s.isalnum():
        return False

    # Check number placement rules
    found_number = False
    for i in range(len(s)):
        # If we find a digit
        if s[i].isdigit():
            # If it's the first number and it's '0', invalid
            if not found_number and s[i] == '0':
                return False
            found_number = True
        # If we find a letter after we've already found a number, invalid
        elif found_number and s[i].isalpha():
            return False

    return True


if __name__ == "__main__":
    main()
