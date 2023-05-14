
from PyQt5.QtWidgets import *
from dani import *
def showMenuWindow():
    dialog = QDialog()
    dialog.show()
    questLbl = QLabel("Питання")
    answerLbl = QLabel("Правильна відповідь")
    wrongAnswerLbl1 = QLabel("Не правильна відповідь")
    wrongAnswerLbl2 = QLabel("Не правильна відповідь")
    wrongAnswerLbl3 = QLabel("Не правильна відповідь")
    okeyBtn = QPushButton("Добавити")
    cancelBtn = QPushButton("Відминити")
    questEdit = QLineEdit()
    answerEdit = QLineEdit()
    wrongAnswerEdit1 = QLineEdit()
    wrongAnswerEdit2 = QLineEdit()
    wrongAnswerEdit3 = QLineEdit()

    mainLine = QVBoxLayout()
    hor1 = QHBoxLayout()
    hor1.addWidget(questLbl)
    hor1.addWidget(questEdit)
    mainLine.addLayout(hor1)

    hor2 = QHBoxLayout()
    hor2.addWidget(answerLbl)
    hor2.addWidget(answerEdit)
    mainLine.addLayout(hor2)

    mainLine.addWidget(wrongAnswerLbl1)
    mainLine.addWidget(wrongAnswerEdit1)
    mainLine.addWidget(wrongAnswerLbl2)
    mainLine.addWidget(wrongAnswerEdit2)
    mainLine.addWidget(wrongAnswerLbl3)
    mainLine.addWidget(wrongAnswerEdit3)

    mainLine.addStretch(1)
    mainLine.addWidget(okeyBtn)
    mainLine.addWidget(cancelBtn)

    def addQuest():
        quest = questEdit.text()
        answer = answerEdit.text()
        wrongAnswer1 = wrongAnswerEdit1.text()
        wrongAnswer2 = wrongAnswerEdit2.text()
        wrongAnswer3 = wrongAnswerEdit3.text()


        d = {
            "питання": quest,
            "правильна відповідь": answer,
            "не правильна1":wrongAnswer1,
            "не правильна2":wrongAnswer2,
            "не правильна3": wrongAnswer3,
        }
        listQuestion.append(d)
        dialog.close()

    okeyBtn.clicked.connect(addQuest)
    dialog.setLayout(mainLine)
    dialog.exec_()
