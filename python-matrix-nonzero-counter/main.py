import numpy as matriz

m = matriz.array([[a * j for j in range(5)]for a in range(5)])
nulo = 0
for a in range(5):
    for j in range(5):
        if m[a][j] != 0:
            nulo = 1 + nulo

print(m,"\n--------------\n", nulo)

