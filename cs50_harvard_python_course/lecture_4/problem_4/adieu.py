def main():
    names = []
    
    # Collect names until EOF (Ctrl+D)
    while True:
        try:
            name = input()
            names.append(name)
        except EOFError:
            break
    
    # Format the output based on number of names
    if len(names) == 1:
        print(f"Adieu, adieu, to {names[0]}")
    elif len(names) == 2:
        print(f"Adieu, adieu, to {names[0]} and {names[1]}")
    else:
        # Join all but the last name with commas
        first_part = ", ".join(names[:-1])
        # Add "and" before the last name
        print(f"Adieu, adieu, to {first_part}, and {names[-1]}")


if __name__ == "__main__":
    main()