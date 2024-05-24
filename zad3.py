def piramida (wys):
    for i in range(wys):
        for j in range(wys*2):
            if j < (wys-i) or j > (wys+i):
                print(' ', end='')
            else:
                print('A', end='')
        print()


n = int(input("Podaj wysokość piramidy, ma być nie większa niż 10:"))
if n < 1:
    raise Exception("Wysokość nie moż być ujemna!")
elif n > 10:
    raise Exception("Wysokość nie może być większa niż 10!")
else:
    piramida(n)