import re

def main():
    print(parse(input("HTML: ")))

def parse(s):
    pattern = r'<iframe.*?src="(https?://(?:www\.)?youtube\.com/embed/([^"/]+))".*?>'
    match = re.search(pattern, s)

    if match:
        vid_id = match.group(2)
        url = f"https://youtu.be/{vid_id}"
        return url
    else:
        return None

if __name__ == "__main__":
    main()
