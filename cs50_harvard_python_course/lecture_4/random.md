# Random
    - random is a library that comes with Python that you could import into your own project.
    - It’s easier as a coder to stand on the shoulders of prior coders.
    - So, how do you load a module into your own program? You can use the word import in your program.
    - Inside the random module, there is a built-in function called random.choice(seq). random is the module you are importing. Inside that module, there is the choice function. That function takes into it a seq or sequence that is a list.
    - In your terminal window type code generate.py. In your text editor, code as follows:
```py
    import random

    coin = random.choice(["heads", "tails"])
    print(coin)
```
    Notice that the list within choice has square braces, quotes, and a comma. Since you have passed in two items, Python does the math and gives a 50% chance for heads and tails. Running your code, you will notice that this code, indeed, does function well!

    - We can improve our code. from allows us to be very specific about what we’d like to import. Prior, our import line of code is bringing the entire contents of the functions of random. However, what if we want to only load a small part of a module? Modify your code as follows:
```py
    from random import choice

    coin = choice(["heads", "tails"])
    print(coin)
```
    Notice that we now can import just the choice function of random. From that point forward, we no longer need to code random.choice. We can now only code choice alone. choice is loaded explicitly into our program. This saves system resources and potentially can make our code run faster!

    - Moving on, consider the function random.randint(a, b). This function will generate a random number between a and b. Modify your code as follows:
```py
    import random

    number = random.randint(1, 10)
    print(number)
```
    Notice that our code will randomly generate a number between 1 and 10.

    - We can introduce the function random.shuffle(x), which shuffles a list into a random order.
```py
    import random

    cards = ["jack", "queen", "king"]
    random.shuffle(cards)
    for card in cards:
        print(card)
    ```
    Notice that random.shuffle will shuffle the cards in place. Unlike other functions, it will not return a value. Instead, it will take the cards list and shuffle them inside that list. Run your code a few times to see the code functioning.

    - We now have these three ways above to generate random information.