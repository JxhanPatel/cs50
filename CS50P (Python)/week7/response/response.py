import validators

def check(e):
    if validators.email(e) == True:
        return f"Valid"
    else:
        return f"Invalid"

def main():
    print(check(input("Your Email Please: ")))

main()
