# Length
- We can utilize len as a way of checking the length of the list called students.
- Imagine that you don’t simply want to print the name of the student but also their position in the list. To accomplish this, you can edit your code as follows:
```py
students = ["Hermione", "Harry", "Ron"]

for i in range(len(students)):
    print(i + 1, students[i])
```
Notice how executing this code results in not only getting the position of each student plus one using i + 1, but also prints the name of each student. len allows you to dynamically see how long the list of the students is regardless of how much it grows.