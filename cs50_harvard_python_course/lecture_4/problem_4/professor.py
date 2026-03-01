import random

def main():
    level = get_level()
    score = 0
    
    # Generate 10 math problems
    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        correct_answer = x + y
        
        # Give user 3 tries for each problem
        for try_count in range(3):
            try:
                # Prompt user for answer
                user_answer = int(input(f"{x} + {y} = "))
                
                if user_answer == correct_answer:
                    score += 1
                    break  # Correct answer, move to next problem
                else:
                    print("EEE")
                    
            except ValueError:
                print("EEE")
            
            # If 3 incorrect attempts, show correct answer
            if try_count == 2:
                print(f"{x} + {y} = {correct_answer}")
    
    # Output final score
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            continue


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError


if __name__ == "__main__":
    main()