import random

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
        


