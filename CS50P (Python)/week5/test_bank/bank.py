def main():
    user_greet = (input("Enter a greeting: ")).lower().strip()
    print(f"${value(user_greet)}")

def value(g):
    if g.startswith("hello"):
        return 0
    elif g.startswith("HELLO"):
        return 0
    elif g.startswith("h"):
        return 20
    elif g.startswith("H"):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
