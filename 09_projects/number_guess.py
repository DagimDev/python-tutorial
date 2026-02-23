import random
num = random.randint(1,5)
guess = int(input("Guess: "))
print("Correct!" if guess==num else "Wrong")