import sys


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        if sys.argv[1][-3:] != ".py":
            sys.exit("Not a Python file")
        else:
            print(countr(sys.argv[1]))


def countr(input_file):
    try:
        countrr = 0
        with open(input_file, "r") as f:
            for line in f:
                if not (line.strip() == "" or line.lstrip().startswith("#") ):
                    countrr += 1
            return countrr
    except FileNotFoundError:
        sys.exit("File Does Not Exist")


if __name__ == "__main__":
    main()
