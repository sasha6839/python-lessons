import random

tuplex = ()

for y in range(10):
    n = random.randint(1, 1000)
    tuplex += (n,)

print(tuplex)


