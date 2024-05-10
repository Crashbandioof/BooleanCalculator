from PyQt6.QtWidgets import *
from gui import *


class logic(QMainWindow, Ui_MainWindow):
    def __init__(self) -> None:
        '''
        Maps the push button to the compile function
        Defines the boolean lists for p, q, and the statement
        Defines the string statements

        '''
        super().__init__()
        self.setupUi(self)
        self.__userinput: str = ''
        self.pushButton_calculate.clicked.connect(lambda: self.compile())

        self.__statement_list: list = [False, False, False, False]
        self.__p_value_list: list = [True, True, False, False]
        self.__q_value_list: list = [True, False, True, False]
        self.__statement_text_list = [self.label_statement_1, self.label_statement_2, self.label_statement_3, self.label_statement_4]
        self.__statement: str = ''
        self.__plane_letter_statement: str = ''
    def or_operator(self, p_list, q_list) -> None:
        '''For each combination of true and false for p and q,
        adds true to statement text list if either p or q is true
         Adds false otherwise'''
        for i in range(0, 4):
            self.__statement_list[i] = p_list[i] or q_list[i]
            self.__statement_text_list[i].setText(str(self.__statement_list[i]))

    def xor_operator(self, p_list, q_list) -> None:
        '''For each combination of true and false for p and q,
            adds true to statement text list  if p doesn't equal q.
            Adds false otherwise
        '''
        for i in range(0,4):
            self.__statement_list[i] = p_list[i] != q_list[i]
            self.__statement_text_list[i].setText(str(self.__statement_list[i]))
    def and_operator(self, p_list, q_list) -> None:
        '''For each combination of true and false for p and q,
            adds true to statement text list  if p and q are true.
            Adds false otherwise
                '''
        for i in range(0,4):
            self.__statement_list[i] = p_list[i] and q_list[i]
            self.__statement_text_list[i].setText(str(self.__statement_list[i]))

    def implies_operator(self, p_list, q_list) -> None:
        '''For each combination of true and false for p and q,
            adds false to statement text list  if p is true and
            q is false
            Adds true otherwise
        '''
        for i in range(0,4):
            if (p_list[i] == True) and (q_list[i] == False):
                self.__statement_list[i] = False
            else:
                self.__statement_list[i] = True
            self.__statement_text_list[i].setText(str(self.__statement_list[i]))
    def equals_operator(self, p_list, q_list) -> None:
        '''For each combination of true and false for p and q,
            adds true to statement text list  if p equals q.
            Adds false otherwise
                '''
        for i in range(0,4):
            self.__statement_list[i] = p_list[i] == q_list[i]
            self.__statement_text_list[i].setText(str(self.__statement_list[i]))

    def compile(self) -> None:
        '''
        Creates a truth table based on user input.
        Triggers make.statement()
        Writes the truth table to calc.history.txt
        '''
        self.make_statement()
        p_list_compile: list = [0, 0, 0, 0]
        q_list_compile: list = [0, 0, 0, 0]

        if self.checkBox_p_not.isChecked() == False:
            p_list_compile = self.__p_value_list
        else:
            for i in range(0, len(self.__p_value_list)):
                p_list_compile[i] = not self.__p_value_list[i]
        if self.checkBox_q_not.isChecked() == False:
            q_list_compile = self.__q_value_list
        else:
            for i in range(0, len(self.__q_value_list)):
                q_list_compile[i] = not self.__q_value_list[i]
        if self.comboBox_operator.currentText() == '→':
            self.implies_operator(p_list_compile, q_list_compile),
        elif self.comboBox_operator.currentText() == '↔':
            self.equals_operator(p_list_compile, q_list_compile),
        elif self.comboBox_operator.currentText() == '∧':
            self.and_operator(p_list_compile, q_list_compile),
        elif self.comboBox_operator.currentText() =='∨':
            self.or_operator(p_list_compile, q_list_compile),
        elif self.comboBox_operator.currentText() =='⊕':
            self.xor_operator(p_list_compile, q_list_compile)
        self.make_unicode_friendly_statement()
        with open('calc_history.txt', 'a') as file:

            file.write(f'p      q      {self.__plane_letter_statement}\n')
            for i in range(0,4):
                file.write(f'{p_list_compile[i]} {p_list_compile[i]} {self.__statement_list[i]}\n')
        self.__plane_letter_statement = ''


    def make_statement(self) -> None:
        '''
        Creates the equation that the user inputted and writes it down on the table
        '''
        self.__statement = ''
        if self.checkBox_p_not.isChecked():
            self.__statement += '¬'
        self.__statement += 'p ' + self.comboBox_operator.currentText() + ' '
        if self.checkBox_q_not.isChecked():
            self.__statement += '¬'
        self.__statement += 'q'
        self.label_statement.setText(self.__statement)
    def make_unicode_friendly_statement(self) -> None:
        '''
        Creates a statement based on user input that
        doesn't have special characters
        This function is needed because the interpreter
        didn't like the special characters
        '''
        if self.checkBox_p_not.isChecked():
            self.__plane_letter_statement += 'not'
        symbol_map = {
            '→': 'follows',
            '↔': 'equals',
            '∧': 'and',
            '∨': 'or',
            '⊕': 'xor,'
        }
        self.__plane_letter_statement += 'p ' + symbol_map[self.comboBox_operator.currentText()] +' '
        if self.checkBox_q_not.isChecked():
            self.__plane_letter_statement += 'not'
        self.__plane_letter_statement += 'q'
