word = 'ventilador'
digited = []
secret_digited = []
cont = 0

while True:
    letter = input("Try to guess a letter: ")

    if letter.isnumeric():
        print("TypeError: only letters are allowed.")
        continue
    elif letter.isdigit():
        letter = str()
    elif letter.upper() in letter:
        letter = letter.lower()

    if letter == word:
        print("Congratulations, you won.")
        break
    elif len(letter) > 1:
        print("You can't do that!")
        continue

    if letter in digited:
        print(digited)
        print("This letter was already digited, please type another.")
        continue

    digited.append(letter)

    if letter in word:
        print("Good, you guessed this letter, try to guess more.")
    else:
        cont += 1
        if cont <= 7:
            print(f'Sorry, but now you have only {8 - cont} more tries!')
            print(digited)
        else:
            print("You have no more chances.")
            print("Game Over!")
            break

    secret_digited = ''
    for secret_letter in word:
        if secret_letter in digited:
            secret_digited += secret_letter
        else:
            secret_digited += '*'
    print(secret_digited)

    if secret_digited == word:
        print("Congratulations, you won.")
        break
