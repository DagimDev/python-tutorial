while True:
    try: 
        fraction = input("Fraction: ")
        x, y = fraction.split("/")

        x = int(x)
        y = int(y)

        if x > y:
            continue

        percentage = (x/y) * 100
        percentage_rounded = round(percentage)

        if percentage_rounded <= 1:
            print("E")
            break
        elif percentage_rounded >= 99:
            print("F")
            break
        else:
            print(f"{percentage_rounded}%")
            break
    
    except (ValueError, ZeroDivisionError):
                # Handle non-integer input or division by zero
        continue