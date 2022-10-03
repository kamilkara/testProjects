# simple TicTacToe program

import random
import TTT_asci

gameTable = {
    1 : "",
    2 : "",
    3 : "",
    4 : "",
    5 : "",
    6 : "",
    7 : "",
    8 : "",
    9 : ""
};

options = [1,2,3,4,5,6,7,8,9]

gameOver = False;

# def putSigns():
    #
    # for i in gameTable:
    #     if gameTable[i] == "X":


while gameOver == False:
    put_x = int(input("Please choose the place: (1 to 9) "))

    while gameTable[put_x] != "":
        put_x = int(input("Please choose an empty place: (1 to 9) "))

    gameTable[put_x] = "X"
    options.remove(put_x)
    # print(gameTable)
    # print(options)

    chosen_O = int(options[random.randint(1,len(options)-1)])
    gameTable[chosen_O] = "O"
    # print(gameTable)
    options.remove(chosen_O)
    # print(options)







