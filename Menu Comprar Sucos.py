def menu():

    print( "------------Menu------------")
    print("| Cód |   Sucos   |  Preço |")
    print("| 1  |   Uva     |  R$ 7,50|")
    print("| 2  |   Morango |  R$ 9,00|")
    print("| 3  |   Limão   |  R$ 8,50|")
    print("| 4  |   Maracujá|  R$ 7,00|")
    print("| 5  |   Abacaxi |  R$ 10,00|")
    print("|---(6)add-----(7)Fechar---|")

qtde = int()
psu = float()
c = int(input("Escolha sua opção: "))
if c != 6:
    print("Fechar a conta.")
    print("Obrigado, e volte sempre!")
if c == 6:

    while c == 6:
        menu()
        sucos = {'Uva' : 1, 'Morango' : 2, 'Limão' : 3, 'Maracujá' : 4, "Abacaxi" : 5}
        sucos = int(input("Escolha seu suco: "))
        if sucos == 1:
            qtde = qtde + 1
            psu = psu + 7.50
            print("Obrigado pela compra!")
        if sucos == 2:
            tde = qtde + 1
            psu = psu + 9.00
            print("Obrigado pela compra!")
        if sucos == 3:
            qtde = qtde + 1
            psu = psu + 8.50
            print("Obrigado pela compra!")
        if sucos == 4:
            qtde = qtde + 1
            psu = psu + 7.00
            print("Obrigado pela compra!")
        if sucos == 5:
            qtde = qtde + 1
            psu = psu + 10.00
            print("Obrigado pela compra!")
        if sucos > 5:
            print("Opção inválida.")

        c = int(input("Escolha sua opção: "))
        if c != 6:
            print("Fechar a conta.")
            print("Obrigado, e volte sempre!")
            print("A quantidade de sucos comprada = ", qtde)
            print("O preço total é = ""R$",psu)




