from random import randint
secret = randint(1,10)
print("welcome\n")
x = 0
while x != secret:
    x = int(input("fuel\n"))
    if x == secret:
        print("you win\n")
    elif x == secret+1:
        print("YOU ARE GOD\n")
    elif x < secret:
        print("too low\n")
    elif x > secret:
        print("too high\n")