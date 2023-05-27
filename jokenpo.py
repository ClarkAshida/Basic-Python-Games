import random

def jokenpo():
    option = int(input("Escolha sua jogada! \n"
    "1- Pedra \n"
    "2- Papel\n"
    "3- Tesoura\n"))

    if option == 1: print("Você escolheu pedra!")
    elif option == 2: print("Você escolheu papel!")
    elif option == 3: print("Você escolheu tesoura!")
    else: 
        print("Escolha inválida!")
        jokenpo()
    pc = random.randrange(1, 4)
    if pc == 1: print("O computador escolheu pedra!")
    elif pc == 2: print("O computador escolheu papel!")
    elif pc == 3: print("O computador escolheu tesoura!")

    #empate
    if pc == 1 and option == 1: print("Empate!")
    if pc == 2 and option == 2: print("Empate!")
    if pc == 3 and option == 3: print("Empate!")

    #Jogador ganha
    if pc == 1 and option == 2: print("Você venceu!")
    if pc == 2 and option == 3: print("Você venceu!")
    if pc == 3 and option == 1: print("Você venceu!")

    #Pc ganhou

    if pc == 1 and option == 3: print("O computador ganhou!")
    if pc == 2 and option == 1: print("O computador ganhou!")
    if pc == 3 and option == 2: print("O computador ganhou!")