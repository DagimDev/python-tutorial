import random

def main():
    # Get level from user (positive integer)
    while True:
        try:
            level = int(input("Level: "))
            if level > 0:
                break
        except ValueError:
            continue
    
    # Generate random number between 1 and level
    target = random.randint(1, level)
    
    # Guessing loop
    while True:
        try:
            guess = int(input("Guess: "))
            
            # Check if guess is positive
            if guess <= 0:
                continue
            
            # Compare guess to target
            if guess < target:
                print("Too small!")
            elif guess > target:
                print("Too large!")
            else:
                print("Just right!")
                break
                
        except ValueError:
            continue


if __name__ == "__main__":
    main()