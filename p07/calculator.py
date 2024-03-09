is_run = True
while is_run:
    print('Calculator')
    print("You can: '+', '-', '*', '/', Exit: 'x', Continue: 'e'")

    action = input('Action: ')

    if action == 'e':
        x = int(input('Input first number:  '))
        y = int(input('Input second number:  '))
        z = int(input('1: + 2: - 3: / 4: * '))
        if z == 1:
            print(f"{x}+{y}={x + y}")
        else:
            if z == 2:
                print(f"{x}-{y}={x - y}")
            else:
                if z == 3:
                    print(f"{x}/{y}={x / y}")
                else:
                    if z == 4:
                        print(f"{x}*{y}={x * y}")

    if action == 'x':
        is_run = False

    # x = int(input('Input first number:  '))
    # y = int(input('Input second number:  '))
    # z = int(input('1: + 2: - 3: / 4: * '))
    # if z == 1:
    #     print(f"{x}+{y}={x+y}")
    # else:
    #     if z == 2:
    #         print(f"{x}-{y}={x - y}")
    #     else:
    #         if z == 3:
    #             print(f"{x}/{y}={x / y}")
    #         else:
    #             if z == 4:
    #                 print(f"{x}*{y}={x * y}")
