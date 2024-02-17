import random
# x = input()
# my_list = [1, 2, 'ggff', 4.655, 3.14, [1, 11, 2, 4], 2, 'ggfeety', 'red']
# for t in my_list:
#    print(t)

# string = 'Sasha'
# print(string[0])
# print(string[0])
# for s in string:
#     print(s)


# ctrl + /
# number_list = [2, 6, 9, 0, 1]
# print(number_list)
#
# number_list.append(88)
# number_list.append(66)
# number_list.append(24)
# print(number_list)
#
# l = len(number_list)
# print(l)

random_number_list_1 = []
random_number_list_2 = []

for j in range(10):
    n = random.randint(0, 100)

    if n % 2 == 0:
        random_number_list_2.append(n)
    else:
        random_number_list_1.append(n)
random_number_list_2.sort()
sum1 = 0
for i in random_number_list_2:
    sum1 += i
    print('\u2588'*i)
sum2 = 0
for y in random_number_list_1:
    sum2 += y
    # print('\u2588'*y)

print(random_number_list_2)
print(random_number_list_1)
print('sum = ', sum1)
print('sum = ', sum2)



# print('\u2588'*sum2)