# File Extensions
# In a file called extensions.py, implement a program that prompts the user for the name of a file and 
# then outputs that file’s media type if the file’s name ends, case-insensitively, in any of these suffixes:

# .gif
# .jpg
# .jpeg
# .png
# .pdf
# .txt
# .zip
# If the file’s name ends with some other suffix or has no suffix at all, output application/octet-stream 
# instead, which is a common default.

# How to Test
# Here’s how to test your code manually:

# Run your program with python extensions.py. Type happy.jpg and press Enter. Your program should output:
# image/jpeg   
# Run your program with python extensions.py. Type document.pdf and press Enter. Your program should output:
# application/pdf


filename = input("File name: ")

clean_filename = filename.strip().lower()

if clean_filename.endswith(".gif"):
    print("image/gif")
elif clean_filename.endswith(".jpg") or clean_filename.endswith(".jpeg"):
    print("image/jpeg")
elif clean_filename.endswith(".png"):
    print("image/png")
elif clean_filename.endswith(".pdf"):
    print("application/pdf")
elif clean_filename.endswith(".txt"):
    print("text/plain")
elif clean_filename.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")
