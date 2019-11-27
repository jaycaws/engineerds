# this is the python nim game for discord
import random

class Nims:
    def __init__(self):
        self.marbles = 12
        self.state = 0
    
    def step(self,arg):
            if self.state == 0:
                self.state = 1;
                return "Take 1, 2 or 3 mabrles: "
            elif self.state == 1:
                pmove = int(arg);
                if pmove < 1 or pmove > 3:
                    self.state = 0;
                    return "Invalid input\n" + self.step(None)
                else:
                    self.state = 0
                    self.marbles -= pmove
                    moveLog = "Remaining: " + str(self.marbles) + "\n"
                    if self.marbles <= 0:
                        self.state = None
                        return moveLog + "you win!"
                        #BREAK DIS SHIT
                    else:
                        cmove = random.randint(1, 3)
                        moveLog += "The computer takes: "+ str(cmove) + "\n"
                        self.marbles -= cmove
                        if self.marbles <= 0:
                            #end
                            self.state = None
                            return moveLog + "Computer wins!"
                            #BREAK DIS SHIT
                        else:
                            moveLog += "Remaining: " + str(self.marbles) + "\n"
                            state = 0; 
                            return moveLog + self.step(None)
            

               
