import random

random_number_list1 = []

for j in range(5):
    n = random.randint(0, 10)
    random_number_list1.append(n)
print(random_number_list1)


random_number_list2 = []

for j in range(5):
    h = random.randint(0, 10)
    random_number_list2.append(h)
print(random_number_list2)

list1 = []

for f in random_number_list1:
    if f in random_number_list2:
        list1.append(f)

print(list1)