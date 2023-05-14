from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle("Конкурс!")
main_win.resize(500, 500)

text = QLabel("Який зараз рік?")
answer1 = QRadioButton("зараз 2022")
answer2 = QRadioButton("зараз 6666")
answer3 = QRadioButton("зараз 2020")
answer4 = QRadioButton("зараз 2021")

mainLine = QVBoxLayout()
mainLine.addWidget(text)

hline1 = QHBoxLayout()
hline1.addWidget(answer1)
hline1.addWidget(answer2)
mainLine.addLayout(hline1)

mainLine.addWidget(answer3)
mainLine.addWidget(answer4)


main_win.setLayout(mainLine)


def messageRight():
    victoryWin = QMessageBox()
    victoryWin.setText("Правильно!!!!!!!!!!")
    victoryWin.exec_()

def messageWrong():
    victoryLoss = QMessageBox()
    victoryLoss.setText("Не правильно!!!!!!!!!!")
    victoryLoss.exec_()

answer1.clicked.connect(messageRight)
answer2.clicked.connect(messageWrong)
answer3.clicked.connect(messageWrong)
answer4.clicked.connect(messageWrong)
main_win.show()
app.exec_()
