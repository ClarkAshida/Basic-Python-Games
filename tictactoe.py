import random

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
