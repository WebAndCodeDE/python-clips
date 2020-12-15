my_dict = {
    "Tisch": "table",
    "Stuhl": "chair"
}

a = input().split()
if len(a) > 1:
    x, y = a
    print(x)
    print(y)
    my_dict[x] = y
    print(my_dict)
    