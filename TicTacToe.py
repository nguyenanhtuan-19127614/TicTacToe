p1= 'x'
p2= 'o'

class Game:

    def __init__(self):
        self.Board = ['-']*9
        self.result = False
        self.winner=None
        self.count= 0



    def CheckRule(self,player):
        if self.Board[0]==self.Board[1]==self.Board[2]!='-':
            self.result=True
        elif self.Board[3]==self.Board[4]==self.Board[5]!='-':
            self.result=True
        elif self.Board[6]==self.Board[7]==self.Board[8]!='-':
            self.result=True
        elif self.Board[0] == self.Board[4] == self.Board[8] != '-':
            self.result = True
        elif self.Board[2] == self.Board[4] == self.Board[6] != '-':
            self.result = True
        elif self.Board[0] == self.Board[3] == self.Board[6] != '-':
            self.result = True
        elif self.Board[1] == self.Board[4] == self.Board[7] != '-':
            self.result = True
        elif self.Board[2] == self.Board[5] == self.Board[8] != '-':
            self.result = True
        if self.result == True:
            self.winner = player


    def Update(self,player):
        flag=False
        while (flag==False):
            move = int(input("Your Move: "))-1
            if self.Board[move]=='-' and move <= 9 and move >= 0:
                self.Board[move] = player
                self.count+=1
                flag = True
            else:
                print("Please choose another position ")
        self.CheckRule(player)

    def Start(self,turn, player):
        while(self.result==False and self.count<9):

            if(turn==False):
                self.Update(player)
                self.turn= True
            else:
                self.Update(player)
                self.turn = False
        if(self.result==True):
            return self.winner
        else:
            return 0
