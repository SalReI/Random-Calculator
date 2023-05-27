# напиши здесь код основного приложения и первого экрана
from PyQt5.QtCore import Qt,QTimer, QTime
from PyQt5.QtWidgets import QLabel, QWidget, QApplication, QPushButton, QHBoxLayout, QVBoxLayout, QMessageBox
from random import randint

app = QApplication([])
sc = QWidget()
sc.setWindowTitle('das')
sc.resize(100,100)

#1
Generate1 = QPushButton('Сгенерировать первое число')
Generate2 = QPushButton('Сгенерировать второе число')
Summ = QPushButton('Сложить')
Substract = QPushButton('Отнять')
Divide = QPushButton('Разделить')
Multiply = QPushButton('Умножить')
title1 = QLabel('Сгенерируй любое число')

Num1 = QLabel()
Num2 = QLabel()

#2
H1 = QHBoxLayout()
H2 = QHBoxLayout()
H3 = QHBoxLayout()
H4 = QHBoxLayout()
V1 = QVBoxLayout()

#2.5
V1.addLayout(H1)
V1.addLayout(H2)
V1.addLayout(H3)
V1.addLayout(H4)
sc.setLayout(V1)

#3
H1.addWidget(title1, alignment = Qt.AlignCenter)
H2.addWidget(Num1, alignment = Qt.AlignLeft)
H2.addWidget(Num2, alignment = Qt.AlignRight)
H3.addWidget(Generate1, alignment = Qt.AlignLeft)
H3.addWidget(Generate2, alignment = Qt.AlignRight)
H4.addWidget(Summ, alignment = Qt.AlignLeft)
H4.addWidget(Substract, alignment = Qt.AlignCenter)
H4.addWidget(Multiply, alignment = Qt.AlignCenter)
H4.addWidget(Divide, alignment = Qt.AlignRight)
#4
def Number1():
    global a
    a = randint(1,100)
    Num1.setText('Сгенерировано число ' + str(a))

def Number2():
    global b
    b = randint(1,100)
    Num2.setText('Сгенерировано число ' + str(b))

def Summary():
    Sumo = QMessageBox()
    Sumo.setText('Ответ: ' + str(int(a+b)))
    Sumo.exec_()
def Divid():
    Div = QMessageBox()
    Div.setText('Ответ: ' + str(int(a/b)))
    Div.exec_()
def multiplication():
    Mult = QMessageBox()
    Mult.setText('Ответ: ' + str(int(a*b)))
    Mult.exec_()
def Substraction():
    Subs = QMessageBox()
    Subs.setText('Ответ: ' + str(int(a-b)))
    Subs.exec_()

#5
Generate1.clicked.connect(Number1)
Generate2.clicked.connect(Number2)
Summ.clicked.connect(Summary)
Divide.clicked.connect(Divid)
Multiply.clicked.connect(multiplication)
Substract.clicked.connect(Substraction)


sc.show()
app.exec_()
