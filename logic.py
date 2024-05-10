from PyQt6.QtWidgets import *
from gui import *
import csv

class logic(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.__userinput: str = ''
        self.lineEdit_user_input.clicked.connect(lambda: self.SUBMIT())
    def add_symbol(self, symbol):
        pass
    def OR(self):
        pass
    def XOR(self):
        pass
    def AND(self):
        pass

    def IMPLIES(self):
        pass
    def EQUALS(self):
        pass

    def SUBMIT(self):
        pass

    def MAKE_TABLE(self):
        pass