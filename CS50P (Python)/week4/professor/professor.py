import random


def main():
    correct = 0
    lives = 3
    good = 10
    lvl = get_level()

    while good !=0:
        if lives == 3:
            x, y = generate_integer(lvl)

        try:
            uans = int(input(f"{x} + {y} = "))
            rans = x + y

            if uans == rans:
                good = good - 1
                correct = correct + 1
                lives = 3
                continue
            else:
                raise ValueError
        except (ValueError, NameError):
            print ("EEE")
            lives = lives - 1
            pass

        if lives == 0:
            print((f"{x} + {y} = {rans}"))
            lives = 3
            good = good - 1
            continue
    print(f"score: {correct}")

def get_level():
    while True:
        try:
            a = int(input("Enter Level:"))
            if 1 <= a <= 3:
                return a
        except:
            pass


def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)

    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)

    elif level == 3:
        x = random.randint(100, 999)
        y = random.randint(100, 999)

    return x, y


if __name__ == "__main__":
    main()
