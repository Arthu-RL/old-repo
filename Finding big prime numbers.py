x = int(input("Put the number you want to discover if it is prime: "))
cont = 2
a = "That is not a prime number!"
r = x % cont


if x == 2:
    print("YOU FIND A PRIME NUMBER!!!")
elif r == 0 or x == 1:
    print(a)
else:
    cont = 3
    while True:
        r = x % cont

        if r != 0 and cont <= (x/2):
            print(f'The remainder of {x} divided by {cont} is {r}')
        elif r == 0 and cont <= (x/2):
            print(a)
            print(f'Because the remainder of {x} divided by {cont} is {r}')
            break
        else:
            print("YOU FIND A PRIME NUMBER!!!")
            break

        cont += 2
