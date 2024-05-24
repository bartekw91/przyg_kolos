def wieza (wys):
    for i in range(wys):
        for j in range(i+1):
            print('A', end='')
        print()


n = int(input("Podaj wysokość wieży, ma być nie większa niż 10:"))
if n < 1:
    raise Exception("Wysokość nie moż być ujemna!")
elif n > 10:
    raise Exception("Wysokość nie może być większa niż 10!")
else:
    wieza(n)