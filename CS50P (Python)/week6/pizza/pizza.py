#wget https://cs50.harvard.edu/python/2022/psets/6/pizza/sicilian.csv
#wget https://cs50.harvard.edu/python/2022/psets/6/pizza/regular.csv

import sys
from tabulate import tabulate
import csv




def table_generator(file_name):
    try:
        with open(file_name) as file:
            csv_reader = csv.reader(file)
            table = tabulate(csv_reader, headers="firstrow", tablefmt="grid")
            return table
    except FileNotFoundError:
        sys.exit("File does not exist")


def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        if not sys.argv[1].endswith(".csv"):
            sys.exit("Not a CSV file")
        else:
            print(table_generator(sys.argv[1]))


if __name__ == "__main__":
    main()


