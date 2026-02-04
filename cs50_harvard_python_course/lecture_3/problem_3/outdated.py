# Outdated
# In the United States, dates are typically formatted in month-day-year order (MM/DD/YYYY), otherwise known as middle-endian order, which is arguably bad design. Dates in that format can’t be easily sorted because the date’s year comes last instead of first. Try sorting, for instance, 2/2/1800, 3/3/1900, and 1/1/2000 chronologically in any program (e.g., a spreadsheet). Dates in that format are also ambiguous. Harvard was founded on September 8, 1636, but 9/8/1636 could also be interpreted as August 9, 1636!

# Fortunately, computers tend to use ISO 8601, an international standard that prescribes that dates should be formatted in year-month-day (YYYY-MM-DD) order, no matter the country, formatting years with four digits, months with two digits, and days with two digits, “padding” each with leading zeroes as needed.

# In a file called outdated.py, implement a program that prompts the user for a date, anno Domini, in month-day-year order, formatted like 9/8/1636 or September 8, 1636, wherein the month in the latter might be any of the values in the list below:

# [
#     "January",
#     "February",
#     "March",
#     "April",
#     "May",
#     "June",
#     "July",
#     "August",
#     "September",
#     "October",
#     "November",
#     "December"
# ]
# Then output that same date in YYYY-MM-DD format. If the user’s input is not a valid date in either format, prompt the user again. Assume that every month has no more than 31 days; no need to validate whether a month has 28, 29, 30, or 31 days.

# How to Test
# Here’s how to test your code manually:

# Run your program with python outdated.py. Type 9/8/1636 and press Enter. Your program should output:
# 1636-09-08
# Run your program with python outdated.py. Type September 8, 1636 and press Enter. Your program should output:
# 1636-09-08


def main():
    # List of month names
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    while True:
        try:
            # Get date from user
            date = input("Date: ").strip()

            # Try MM/DD/YYYY format first
            if "/" in date:
                month, day, year = date.split("/")

                # Convert to integers
                month = int(month)
                day = int(day)
                year = int(year)

                # Validate month and day
                if 1 <= month <= 12 and 1 <= day <= 31:
                    # Format as YYYY-MM-DD with leading zeros
                    print(f"{year:04d}-{month:02d}-{day:02d}")
                    break

            # Try Month Day, Year format
            elif "," in date:
                # Split by space
                parts = date.split()

                if len(parts) == 3:
                    month_str, day_str, year_str = parts

                    # Remove comma from day
                    day_str = day_str.rstrip(",")

                    # Check if month is valid
                    if month_str.title() in months:
                        month = months.index(month_str.title()) + 1
                        day = int(day_str)
                        year = int(year_str)

                        # Validate day
                        if 1 <= day <= 31:
                            print(f"{year:04d}-{month:02d}-{day:02d}")
                            break

        except (ValueError, IndexError, AttributeError):
            # If any error occurs, reprompt
            pass


if __name__ == "__main__":
    main()
