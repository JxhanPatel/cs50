import re
import sys

def main():
    print(count(input("Input: ")))

def count(s):
    pattern = r"(^|\W)um($|\W)"
    ss = s.lower()
    matched = re.findall(pattern, ss)
    if matched:
        return(len(matched))


if __name__ == "__main__":
    main()
