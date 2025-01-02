def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    a = len(s)
    if  2 <= a and a <= 6 and s.isalnum():
        if s.isalpha():
            return True
        else:
            if s[:2].isalpha() and s[-2:].isdigit():
                for b in range(a):
                    if s[b].isdigit():
                        if s[b].startswith('0'):
                            return False
                        else:
                            return True
            else:
                return False
    else:
        return False




main()
