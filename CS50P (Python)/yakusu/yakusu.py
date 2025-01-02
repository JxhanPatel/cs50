import requests
from lxml import html
from googletrans import Translator



# KANJI
def search_kanji(word):
    try:
        url = f"https://jisho.org/search/{word}%23kanji"
        response = requests.get(url)
        tree = html.fromstring(response.content)
        kanji = tree.xpath('//*[@id="secondary"]/div/div/div/div[3]/span/a/text()')
        result = kanji[0].strip() if kanji else "Oh no! No Kanji found!"
        return result
    except Exception as error:
        return f"Error: {error}"




# ROMAJI
def to_romaji(word):
    try:
        url = f"https://tangorin.com/kanji?search={word}"
        response = requests.get(url)
        tree = html.fromstring(response.content)
        romaji = tree.xpath('/html/body/div[1]/main/div[1]/div[1]/section/div/dl/div[1]/dd[2]/dl/div[1]/dt/ruby/rt')
        result = romaji[0].text.strip() if romaji else "Oops! No Romaji Found?"
        return result
    except Exception as error:
        return f"Error: {error}"




# HIRAGANA
def to_hiragana(word):
    try:
        response = requests.get(f"https://www.sljfaq.org/cgi/romaji-kana.cgi?text={word}")
        tree = html.fromstring(response.content)
        elements = tree.xpath("//table[@class='r2k']//tr//td")
        result = elements[4].text_content().strip()
        return result
    except Exception as error:
        return f"Error: {error}"




# ENGLISH
def to_english(word):
    try:
        translator = Translator()
        t = translator.translate(word, src='ja', dest='en')
        return t.text
    except Exception as error:
        return f"Error: {error}"




# MAIN
def main():
    try:
        print("------------------------")
        print("Welcome to Yakusu! Your ultimate Kanji learning companion!")
        print("------------------------")
        print('Choose Translation Option')
        print('Option 1: English → Japanese')
        print('Option 2: Japanese → English')
        choice = input("1 or 2? ")
        theword = input("Please enter a word: ")

        if choice == "1":
            kanji = search_kanji(theword)
            romaji = to_romaji(kanji)
            hiragana = to_hiragana(romaji)
            print(f"Kanji: {kanji}")
            print(f"Romaji: {romaji}")
            print(f"Hiragana: {hiragana}")

        elif choice == "2":
            japanese = theword
            engg = to_english(japanese)
            print(f"Japanese: {japanese}")
            print(f"English Translation: {engg}")

        else:
            print("Invalid choice. Please choose 1 or 2.")



    except Exception as error:
        print(f"An error occurred: {error}")



if __name__ == "__main__":
    main()
