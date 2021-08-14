p1= 'x'
p2= 'o'

class Game:

    def __init__(self):
        self.Board = ['-']*9
        self.result = False
        self.winner=None
        self.turn=False
        self.count= 0

    def DrawBoard(self):
        temp= 0
        for i in self.Board:
            print(i, end=" ")
            temp+=1
            if temp==3:
                temp=0
                print('\n')

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

    def Start(self):
        while(self.result==False and self.count<9):
            self.DrawBoard()
            if(self.turn==False):
                self.Update(p1)
                self.turn= True
            else:
                self.Update(p2)
                self.turn = False
        if(self.result==True):
            self.DrawBoard()
            print("winner is: ",self.winner)
        else:
            print("Draw")
Board=Game()
Board.Start()