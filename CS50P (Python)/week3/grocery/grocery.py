buy = {}

while True:
    try:
        item = input().upper().strip()
        if item not in buy:
            buy[item] = 1

        else:
            buy[item] = buy[item] + 1

    except EOFError:
        d = dict(sorted(list(buy.items())))
        for item in d:
            print(d[item], item, sep=" ")
        break

    except KeyError:
        pass
