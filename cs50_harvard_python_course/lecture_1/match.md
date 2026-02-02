# match
# Similar to if, elif, and else statements, match statements can be used to conditionally run code that matches certain values.
# Consider the following program:
```py
    name = input("What's your name? ")
  if name == "Harry":
      print("Gryffindor")
  elif name == "Hermione":
      print("Gryffindor")
  elif name == "Ron": 
      print("Gryffindor")
  elif name == "Draco":
      print("Slytherin")
  else:
      print("Who?")
```
# Notice the first three conditional statements print the same response.

# We can improve this code slightly with the use of the or keyword:
```py
  name = input("What's your name? ")

  if name == "Harry" or name == "Hermione" or name == "Ron": 
      print("Gryffindor")
  elif name == "Draco":
      print("Slytherin")
  else:
      print("Who?")
# Notice the number of elif statements has decreased, improving the readability of our code.

# Alternatively, we can use match statements to map names to houses. Consider the following code:
  name = input("What's your name? ")

  match name: 
      case "Harry":
          print("Gryffindor")
      case "Hermione":
          print("Gryffindor")
      case "Ron": 
          print("Gryffindor")
      case "Draco":
          print("Slytherin")
      case _:
          print("Who?")
# Notice the use of the _ symbol in the last case. This will match with any input, resulting in similar behavior as an else statement.

# A match statement compares the value following the match keyword with each of the values following the case keywords. In the event a match is found, the respective indented code section is executed, and the program stops the matching.
# We can improve the code:
  name = input("What's your name? ")

  match name: 
      case "Harry" | "Hermione" | "Ron":
          print("Gryffindor")
      case "Draco":
          print("Slytherin")
      case _:
          print("Who?")
# Notice, the use of the single vertical bar |. Much like the or keyword, this allows us to check for
# multiple values in the same case statement.
```