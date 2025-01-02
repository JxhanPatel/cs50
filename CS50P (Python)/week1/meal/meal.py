def main():
    time = input('What time is there? ').strip()
    if convert(time) >=7 and convert(time) <=8:
            print('breakfast time')
    elif convert(time) >=12 and convert(time) <=13:
            print('lunch time')
    elif convert(time) >=18 and convert(time) <=19:
            print('dinner time')

def convert(time):
    x, y = time.split(':')
    m = float(y)*1/60
    h = float(x)
    return float(m+h)


if __name__ == "__main__":
    main()
