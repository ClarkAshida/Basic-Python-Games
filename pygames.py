import random
from tictactoe import tictactoe
from hangman import hangman
from jokenpo import jokenpo

gameChoice = int(input("\n"
    "Bem-vindo ao Pygames! Escolha qual jogo você deseja jogar? \n"
    "1- Jogo da velha \n"
    "2- Jogo da forca \n"
    "3- Jokenpo \n"))

if gameChoice == 1: tictactoe()
if gameChoice == 2: hangman()
if gameChoice == 3: jokenpo()
