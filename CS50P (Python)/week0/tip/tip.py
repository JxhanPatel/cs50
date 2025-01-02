def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    f = float(d.strip().replace("$",""))
    return f


def percent_to_float(p):
    b = float(p.strip().replace("%",""))
    f = float(b/100)
    return f


main()