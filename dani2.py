from PyQt5.QtWidgets import *
from dani import *

def showEditWindow():
    dialog = QDialog()
    dialog.show()
    questLbl = QLabel("Питання")
    questEdit = QLineEdit()
    pravilnaVidpodid=QLabel("Правильна відповідь")
    questEdit.setText(listQuestion[currntQuest]["питання"])

    wrongLbl1 = QLabel("Не правильна відповідь 1")
    regBtn = QPushButton("Редагувати")
    cancelBtn = QPushButton("Відминити")

    mainLine = QVBoxLayout()
    h1 = QHBoxLayout()
    h1.addWidget(questLbl)
    h1.addWidget(questEdit)
    mainLine.addLayout(h1)
    mainLine.addWidget(regBtn)
    mainLine.addWidget(pravilnaVidpodid)

    def redaguvanya():
        global currntQuest
        listQuestion[currntQuest]["питання"] = questEdit.text()

    regBtn.clicked.connect(redaguvanya)
    dialog.setLayout(mainLine)
    dialog.exec_()
