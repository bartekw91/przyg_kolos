import random as rand


n = int(input("Podaj wymiar tablicy n:"))
tab = []
for i in range(n):
    temp = []
    for j in range(n):
        temp.append(rand.randrange(1, 500))
    tab.append(temp)
print(tab)
print('\nSumujemy:')
for i in tab:
    print(sum(i))