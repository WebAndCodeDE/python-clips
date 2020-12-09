def sum1(n):

    final_sum = 0
    for x in range(n+1):
        print("x= ",x)
        final_sum += x
        print(final_sum)
        
    return final_sum

def sum2(n):
    return (n*(n+1)) / 2


n = int(input("Eingabe: "))
print("Ergebnis sum1: ",sum1(n))
print("Ergebnis sum2: ",sum2(n))