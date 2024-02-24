# 1
# Print i as long as i is less than 5.
# i = 1
# while True:
#     print(i)
#     i += 1000000000

# 2
# Stop the loop if i is 3.
# i = 1
# while i < 6:
#     if i == 3:
#         break
#     i += 1
#     print(i)


# 3
# In the loop, when i is 3, jump directly to the next iteration.
# i = 0
# while i < 17:
#     i += 1
#     if i == 3:
#         print('i=%d' % i)
#     if i % 2 == 0:
#         print('Парне')
#     if i == 15:
#         break
#
#     print(i)
# 4
# Print a message once the condition is false.
# i = 1
# while i < 6:
#     i += 1
#     print(i)
# else:
#     print("i is no longer less than 6")

x = int(input('Input first number:  '))
y = int(input('Input second number:  '))
while x > 1:
    x = x // y
    print(x)
