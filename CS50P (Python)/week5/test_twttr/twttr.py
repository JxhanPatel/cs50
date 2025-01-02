def main():
    user_input = input("Please input some text: ")
    output_text = shorten(user_input)
    print(f"Shortened text: {output_text}")

def shorten(text):
    vowels_list = ["a", "e", "i", "o", "u"]
    shortened_list = []
    for char in text:
        if char.casefold() not in vowels_list:
            shortened_list.append(char)
    shortened_text = "".join(shortened_list)
    return shortened_text

if __name__ == "__main__":
    main()
