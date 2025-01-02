import random

while True:
    try:
        level = int(input("Enter a positive integer for the level: "))
        target = random.randint(1, level)
        while True:
            try:
                guess = int(input("Guess the number between 1 and {}: ".format(level)))
                if guess < target:
                    print("Too small!")
                elif guess > target:
                    print("Too large!")
                else:
                    print("Just right!")
                    raise EOFError
            except ValueError:
                pass
    except ValueError:
        pass
    except EOFError:
        break
