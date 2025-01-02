def main():
    frac = input("Fraction: ")
    try:
        pct = convert(frac)
        print(gauge(pct))
    except ValueError:
        print("Invalid fraction format")


def convert(fraction):
    x, y = map(int, fraction.split("/"))
    if x > y or y == 0:
        raise ValueError
    return int(x / y * 100)


def gauge(percentage):
    if 0 <= percentage <= 1:
        return "E"
    elif 99 <= percentage <= 100:
        return "F"
    elif 1 < percentage < 99:
        return f"{int(percentage)}%"
    else:
        return None


if __name__ == "__main__":
    main()
