x = int(input('   :   '))
y = int(input("   1: +  \n" "   2: -  \n" "   3: *  \n" "   4: /  \n"))
z = int(input('   :   '))
if y == 1:
    print(f'{x+z}')
else:
    if y == 2:
        print(f'{x-z}')
    else:
        if y == 3:
            print(f'{x*z}')
        else:
            if y == 4:
                print(f'{x/z}')
            else:
                print('Error')