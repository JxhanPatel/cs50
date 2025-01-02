import sys
import operator
from datetime import date
import inflect



a = inflect.engine()



def convert(time):
    mins = time * 24 * 60
    return f"{(a.number_to_words(mins, andword='')).capitalize()} minutes"



def main():
    try:
        birth = input("Date of Birth: ")
        x = date.today()
        y = date.fromisoformat(birth)
        diff = operator.sub(x, y)
        print(convert(diff.days))
    except ValueError:
        sys.exit("Error with Date")



if __name__ == "__main__":
    main()
