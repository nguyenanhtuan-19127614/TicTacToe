import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class AppTicTacToe(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'TicTacToe-Game-NAT'
        self.Icon='TicTacToe.png'
        self.width = 315
        self.height = 500

        self.turn=False
        self.Result=False
        self.count=0
        self.button_list= []


    def GameWindow(self):
        #WindowGui
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.Icon))
        self.setGeometry(500, 500, self.width, self.height)
        #WinnerButton
        self.Winner=QPushButton(self)
        self.Winner.setGeometry(8,350,300,50)
        self.Winner.setStyleSheet("background-color: cyan;")
        self.Winner.setFont(QFont('Arial', 25))
        self.Winner.setEnabled(False)
        #ButtonList
        for i in range(3):
            temp = []
            for j in range(3):
                temp.append((QPushButton(self)))
            self.button_list.append(temp)
        button_x = 90
        button_y = 90
        for i in range(3):
            for j in range(3):
                self.button_list[i][j].setGeometry(button_x * i + 20, button_y * j + 20, 90, 85)
                self.button_list[i][j].setFont(QFont('Arial', 50))
                self.button_list[i][j].setStyleSheet("background-color: Yellow;")
                self.button_list[i][j].clicked.connect(self.Update)

        self.show()

    def Update(self):
        button = self.sender()
        button.setEnabled(False)
        if self.turn==False:
            button.setText("X")
            self.count +=1
            self.turn=True
        else:
            button.setText("O")
            self.count +=1
            self.turn = False
        self.Rule()
        if(self.Result==True):
            for i in self.button_list:
                for j in i:
                    j.setEnabled(False)
            if(self.turn==True):
                self.Winner.setText("X is the Winner")
            else:
                self.Winner.setText("O is the Winner")
        if(self.count==9):
            self.Winner.setText("Draw")

    def Rule(self):
        for i in range(3):
            if (self.button_list[i][0].text() == self.button_list[i][1].text()
                    == self.button_list[i][2].text() != ""):
                self.Result = True
                return

        for j in range(3):
            if (self.button_list[0][j].text() == self.button_list[1][j].text()
                    == self.button_list[2][j].text() != ""):
                self.Result = True
                return

        if (self.button_list[0][0].text() == self.button_list[1][1].text()
                == self.button_list[2][2].text() != ""):
            self.Result = True
            return

        if (self.button_list[0][2].text() == self.button_list[1][1].text()
                == self.button_list[2][0].text() != ""):
            self.Result = True
            return


app = QApplication(sys.argv)
ex = AppTicTacToe()
ex.GameWindow()
sys.exit(app.exec_())

