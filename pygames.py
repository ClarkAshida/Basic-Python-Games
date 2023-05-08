import random

gameChoice = int(input("\n"
    "Bem-vindo ao Pygames! Escolha qual jogo você deseja jogar? \n"
    "1- Jogo da velha \n"
    "2- Jogo da forca \n"
    "3- Jokenpo \n"))

def tictactoe():

    board = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],]

    def displayBoard():
        print("")
        print(" ", board[0][0], ",", board[0][1], ",", board[0][2])
        print("--------------")
        print(" ", board[1][0], ",", board[1][1], ",", board[1][2])
        print("--------------")
        print(" ", board[2][0], ",", board[2][1], ",", board[2][2])
        print("")

    displayBoard()

    def verifyWin(board):
        for row in board:
            if row[0] == row[1] == row[2]:
                return row[0]
        for col in range(3):
            if board[0][col] == board[1][col] == board[2][col]:
                return board[0][col]
        if board[0][0] == board[1][1] == board[2][2]:
            return board[0][0]
        if board[0][2] == board[1][1] == board[2][0]:
            return board[0][2]
        return None

    def verifyDraw(board):
        winner = verifyWin(board)
        if winner != None:
                print("\n"
                    "O jogador:", winner, "Ganhou!"
                    "\n")
                exit()
        for row in board:
            for element in row:
                if isinstance(element, int):
                    return False
        return True


    def yourTurn():
        gameOver = False
        row = -1
        column = -1
        winner = verifyWin(board)
        if winner != None:
                print("\n"
                    "O jogador:", winner, "Ganhou!"
                    "\n")
                exit()

        while gameOver == False:
            move = int(input("\n"
            "Escolha a casa onde deseja jogar: \n"
            ""))
            
            if move == -1:
                print("\n"
                    "Partida encerrada!"
                    "")
                exit()

            if move < 1 or move > 9: 
                print("\n"
                    "Movimento inválido, escolha entre 1 e 9!"
                    "")
                exit()

            for i in range(len(board)):
                for j in range(len(board[i])):
                    if board[i][j] == move:
                        row = i
                        column = j
                        break
            
            if board[row][column] == "X" or board[row][column] == "O":
                print("\n"
                    "Movimento inválido, essa casa já está ocupada com:", board[row][column])
                displayBoard()
                print("Escolha outra casa para jogar seu movimento! ", "\n")
                yourTurn()

            elif board[row][column] != "X" or board[row][column] != "O": 
                board[row][column] = "X"
            verifyWin(board)
            displayBoard()
            pcTurn()
            

    def pcTurn():

        print("\n"
            "Vez do PC \n"
            "")
        
        def pcTurnMove():
            pcMove = int(random.randrange(1, 10))
            row = -1
            column = -1

            for i in range(len(board)):
                    for j in range(len(board[i])):
                        if board[i][j] == pcMove:
                            row = i
                            column = j
                            break
        
            if board[row][column] == "X" or board[row][column] == "O":
                while board[row][column] == "X" or board[row][column] == "O":
                    pcMove = int(random.randrange(1, 10))
                    draw = verifyDraw(board)
                    if draw == True: 
                        print("Empate!")
                        exit()
                    if draw == False: pcTurn()

            elif board[row][column] != "X" or board[row][column] != "O": 
                    board[row][column] = "O"
                    displayBoard()
            verifyWin(board)
            yourTurn()

        pcTurnMove()

    yourTurn()

def hangman():
    words = ["motocicleta", "melancia", "zangado", "urgente", "continuar"]
    word = words[random.randrange(0, len(words) - 1)]
    wordLength = len(word)
    secretWord = ["_"] * wordLength
    displayedWord = " ".join(secretWord)
    currentWord = '_' * len(word)
    lifes = 6

    def drawHangman(tentativas):
        if tentativas == 6:
            print("________      ")
            print("|      |      ")
            print("|             ")
            print("|             ")
            print("|             ")
            print("|             ")
        elif tentativas == 5:
            print("________      ")
            print("|      |      ")
            print("|      O      ")
            print("|             ")
            print("|             ")
            print("|             ")
        elif tentativas == 4:
            print("________      ")
            print("|      |      ")
            print("|      O      ")
            print("|      |      ")
            print("|             ")
            print("|             ")
        elif tentativas == 3:
            print("________      ")
            print("|      |      ")
            print("|      O      ")
            print("|     /|      ")
            print("|             ")
            print("|             ")
        elif tentativas == 2:
            print("________      ")
            print("|      |      ")
            print("|      O      ")
            print("|     /|\     ")
            print("|             ")
            print("|             ")
        elif tentativas == 1:
            print("________      ")
            print("|      |      ")
            print("|      O      ")
            print("|     /|\     ")
            print("|     /       ")
            print("|             ")
        else:
            print("________      ")
            print("|      |      ")
            print("|      O      ")
            print("|     /|\     ")
            print("|     / \     ")
            print("|             ")
            return True
        return False

    print("\n"
        "A palavra tem:", wordLength, "letras:", displayedWord)
    drawHangman(lifes)

    while lifes != 0:
        move = input("\n"
            "Digite uma letra: ")
        if move in word:
            print("\n"
            "Você acertou!, a letra {", move, "} faz parte da palavra! \n"
            )
            for i in range(wordLength):
                if word[i] == move:
                    secretWord[i] = move
                    displayedWord = " ".join(secretWord)
            for i, l in enumerate(word):
                if l == move:
                    currentWord = currentWord[:i] + move + currentWord[i+1:]
                    
            print(displayedWord)
        elif move not in word:
            lifes -= 1
            drawHangman(lifes)
            print("\n"
                "Você errou! a letra {", move, "} não faz parte da palavra!")
            print("\n"
                "Você tem:", lifes, "tentativas restantes")
        
        if lifes == 0: print("\n"
            "Você perdeu! A palavra era:", word)
        if currentWord == word:
            print("\n"
                "Você ganhou! A palavra era:", word)
            exit()

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

if gameChoice == 1: tictactoe()
if gameChoice == 2: hangman()
if gameChoice == 3: jokenpo()
    