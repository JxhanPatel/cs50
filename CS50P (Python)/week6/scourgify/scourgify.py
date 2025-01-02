import sys
import csv


def clean(input_file, output_file):
    try:
        with open(input_file) as file_input:
            reader = csv.DictReader(file_input)
            with open(output_file, "w") as file_output:
                headers = ["first", "last", "house"]
                writer = csv.DictWriter(file_output, fieldnames=headers)
                writer.writeheader()
                for student in reader:
                    last_name, first_name = student["name"].split(", ")
                    house = student["house"]
                    writer.writerow({"first": first_name, "last": last_name, "house": house})
    except FileNotFoundError:
        sys.exit(f"Could not read {input_file}")


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        if not sys.argv[1].endswith(".csv"):
            sys.exit("Not a CSV file")
        else:
            clean(sys.argv[1], sys.argv[2])


if __name__ == "__main__":
    main()
