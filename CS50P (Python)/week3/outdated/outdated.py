given = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    ask = input("Write Date: ")
    try:
        if "/" in ask:
            m, d, y = ask.split("/")
        elif "," in date:
            md, y = ask.split(", ")
            m, d = mmdd.split(" ")
            m = (given.index(mm)) + 1

        if int(m) > 12 or int(d) > 31:
            raise ValueError

    except (AttributeError, ValueError, NameError, KeyError):
        pass

    else:
        print(f"{int(y)}-{int(m):02}-{int(d):02}")
        break
