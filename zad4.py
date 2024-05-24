import random as rand
import time

rand.seed(time.time())  # Generowanie numeru wg czasu
print(rand.random())  # Losowy nr w postaci float
print(rand.randint(1, 100))  # Losowy nr od 1 do 100 typu int
print(rand.randrange(1, 250))  # Losowy nr od 1 do 250