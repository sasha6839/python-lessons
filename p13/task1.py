# def calculator(num1, action, num2):
#     if action == "+":
#         result = num1 + num2
#
#     if action == "-":
#         result = num1 - num2
#
#     if action == "*":
#         result = num1 * num2
#
#     if action == "/":
#         result = num1 / num2
#
#     if action == "**":
#         result = num1 ** num2
#
#     if action == "%":
#         result = num1 % num2
#
#     if action == "//":
#         result = num1 // num2
#
#     return result
#
# num11=int(input("num1: "))
# action1=str(input("action: "))
# num21=int(input("num2: "))
#
# x = calculator(num11, action1, num21)
#
# print(x)

def addition_subtract(a: int, b: int, action: str):
    if action == '+':
        return a + b
    elif action == '-':
        return a - b



res: int = 0
a1: int = 12
a2: int = 6
act: str = '+'

res = addition_subtract(a1, a2, act)
print(res)










