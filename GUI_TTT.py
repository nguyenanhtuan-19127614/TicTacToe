import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'TicTacToe-Game-NAT'
        self.Icon='TicTacToe.png'
        self.width = 315
        self.height = 500
        self.push_list= []

    def GameWindow(self):
        #WindowGui
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.Icon))
        self.setGeometry(500, 500, self.width, self.height)

        #ButtonList
        for i in range(3):
            temp = []
            for j in range(3):
                temp.append((QPushButton(self)))
            self.push_list.append(temp)
        button_x = 90
        button_y = 90
        for i in range(3):
            for j in range(3):
                self.push_list[i][j].setGeometry(button_x * i + 20, button_y * j + 20, 90, 85)
                self.push_list[i][j].clicked.connect(self.ButtonAction)

        self.show()

    def ButtonAction(self):
        button = self.sender()
        button.setEnabled(False)
        button.setText("O")



app = QApplication(sys.argv)
ex = App()
ex.GameWindow()
sys.exit(app.exec_())

