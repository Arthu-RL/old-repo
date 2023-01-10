x = int(input("Put the number you want to discover if it is prime: "))
cont = 2
a = "That is not a prime number!"

while True:
    y = x % cont

    if y != 0 and cont <= (x/2):
        print(f'The remainder of {x} divided by {cont} is {y}')
    elif y == 0 and cont <= (x/2):
        print(a)
        print(f'Because the remainder of {x} divided by {cont} is {y}')
        break
    elif x == 2:
        print("YOU FIND A PRIME NUMBER!!!")
        break
    elif y == 0 or x == 1:
        print(a)
        break
    else:
        print("YOU FIND A PRIME NUMBER!!!")
        break

    cont += 1
