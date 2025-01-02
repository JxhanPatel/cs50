accept = [5, 25, 10]
cost = 50
done = 0

while cost > 0:
    print (f"Amount Due: {cost}")
    get = int(input("Insert coin : "))
    if get in accept:
        cost = cost - get
        done = done + get

if done >= cost:
    a = done - 50
    print (f"Change Owed:", a)

