def main():
    a = do("fraction:")
    print(a)


def do(get):
    while True:
        try:

            x, y = input(get).split("/")

            z= int(x)/int(y)

            if 0 <= z <= 0.1:
                return("E")
            elif 0.9 <= z <= 1:
                return("F")
            elif 0.1 < z < 0.9:
                b = round(z*100)
                return str(b) + "%"
        except (ValueError, ZeroDivisionError):
            pass


main()
