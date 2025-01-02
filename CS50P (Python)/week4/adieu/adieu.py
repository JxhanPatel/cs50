import inflect

p = inflect.engine()
list = []

while True:
    try:
        name = input("Name: ").strip().title()
        list.append(name)

    except EOFError:
        print()
        print("Adieu, adieu, to", p.join(list))
        break
