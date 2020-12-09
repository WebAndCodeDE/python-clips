my_dict = {
    "Tisch" : "table",
    "Stuhl" : "chair"
}

a = input().split()
if len(a)>1:
    x,y = a
    print(x)
    print(y)
    my_dict[x]=y
    print(my_dict)

if len(a)<2:
    my_dict[a[0]]()
    print(my_dict)