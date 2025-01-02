import re
import sys


def main():
    print(convert(input("Time: ")))

def convert(s):
    pattern = "(0?[1-9]|1[0-2]):?\.?([0-5][0-9])? (AM|PM)"
    match = re.search(r"^" + pattern + " to " + pattern + "$", s)
    if match:
        t1 = normalize(match.group(1), match.group(2), match.group(3))
        t2 = normalize(match.group(4), match.group(5), match.group(6))
        return f"{t1} to {t2}"
    else:
        raise ValueError



def normalize(hour, minute, period):
    if hour == "12":
        if period == "AM":
            hr = "00"
        else:
            hr = "12"
    else:
        if period == "AM":
            hr = f"{int(hour):02}"
        else:
            hr = f"{int(hour) + 12}"
    if minute is None:
        min = "00"
    else:
        min = f"{int(minute):02}"
    return f"{hr}:{min}"



if __name__ == "__main__":
    main()
