# this is the python nim game for discord

import random
marbles = 12

while marbles > 0:
    #start
    pmove = int(input("Take 1, 2 or 3 mabrles: "))
    if pmove < 1 or pmove > 3:
        print("no")
        pmove = int(input("Take 1, 2 or 3 mabrles: "))

    marbles -= pmove
    print("Remaining: ", marbles)

    if marbles <= 0:
        print("you win!")
        exit()

    cmove = random.randint(1, 3)
    print("The computer takes: ", cmove)
    marbles -= cmove
    if marbles <= 0:
        #end
        print("Computer wins!")
        exit()

    print("Remaining: ", marbles)

class Nims():
    def __init__(self):
        self.marbles = 12
        self.isBotTurn = 1;

    
    def step():
        pmove = int(input("Take 1, 2 or 3 mabrles: "))
            if pmove < 1 or pmove > 3:
                print("no")
                pmove = int(input("Take 1, 2 or 3 mabrles: "))

            marbles -= pmove
            print("Remaining: ", marbles)

            if marbles <= 0:
                print("you win!")
                exit()

            cmove = random.randint(1, 3)
            print("The computer takes: ", cmove)
            marbles -= cmove
            if marbles <= 0:
                #end
                print("Computer wins!")
                exit()
