def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 2 <= len(s) <= 6 and s.isalnum():
        if s.isalpha() or (s[:2].isalpha() and s[-2:].isdigit()):
            for i in range(len(s)):
                if s[i].isdigit() and (not s[i].startswith("0") and not s[i:].isalpha()):
                    return True
            return False
    return False


if __name__ == "__main__":
    main()
