#create a memory card application
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QHBoxLayout, QVBoxLayout, QButtonGroup,
    QGroupBox, QRadioButton, QPushButton, QLabel)

from random import shuffle
from random import randint

class Question():
    def __init__(self, question, right_answer, wrong_answer1, wrong_answer2, wrong_answer3):
        # all the lines must be given when creating the object, and will be recorded as properties
        self.question = question
        self.right_answer = right_answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3

questions_list = [] 
questions_list.append(Question('Who is your python teacher?', 'Apireak', 'Thida', 'Natt', 'Chenda'))
questions_list.append(Question('Which class are you learning at?', 'Purple', 'Orange', 'yellow', 'Pink'))
questions_list.append(Question('What school are you learning at?', 'Algorithmics', 'Build Bright', 'Hight bright', 'Panhasas'))

app = QApplication([])

btn_OK = QPushButton('start question')

LabelQuestion = QLabel()
QuestionRadioGroupBox = QGroupBox("Answer options")

rbtn_1 = QRadioButton()
rbtn_2 = QRadioButton()
rbtn_3 = QRadioButton()
rbtn_4 = QRadioButton()

QuestionRadioGroup = QButtonGroup() 
QuestionRadioGroup.addButton(rbtn_1)
QuestionRadioGroup.addButton(rbtn_2)
QuestionRadioGroup.addButton(rbtn_3)
QuestionRadioGroup.addButton(rbtn_4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout() # the vertical ones will be inside the horizontal one
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1) # two answers in the first column
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) # two answers in the second column
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2) 
layout_ans1.addLayout(layout_ans3)

QuestionRadioGroupBox.setLayout(layout_ans1) 

# Create a results panel
AnswerRadioGroupBox = QGroupBox("Test result")
labelAnswer = QLabel() # “Correct” or “Incorrect” text will be here
labelCorrectAnswer = QLabel() # correct answer text will be written here 

layout_respone = QVBoxLayout()
layout_respone.addWidget(labelAnswer, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_respone.addWidget(labelCorrectAnswer, alignment=Qt.AlignHCenter)
AnswerRadioGroupBox.setLayout(layout_respone)

# Place all the widgets in the window:
layout_line1 = QHBoxLayout() # question
layout_line2 = QHBoxLayout() # answer options or test result
layout_line3 = QHBoxLayout() # “Answer” button

layout_line1.addWidget(LabelQuestion, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(QuestionRadioGroupBox)   
layout_line2.addWidget(AnswerRadioGroupBox)  

# hide the answer panel because the question panel should be visible first
AnswerRadioGroupBox.hide() 


layout_line3.addStretch(1)	
layout_line3.addWidget(btn_OK) # the button should be large
layout_line3.addStretch(1)	


whole_layout = QVBoxLayout()

whole_layout.addLayout(layout_line1)
whole_layout.addLayout(layout_line2)

whole_layout.addStretch(1)
whole_layout.addLayout(layout_line3)
whole_layout.addStretch(1)

whole_layout.setSpacing(5) # spaces between content


def show_result():
    ''' show answer panel '''
    QuestionRadioGroupBox.hide() 
    AnswerRadioGroupBox.show()
    btn_OK.setText('Next Question')

def show_questioin():
    ''' show question panel '''
    QuestionRadioGroupBox.show() 
    AnswerRadioGroupBox.hide()
    btn_OK.setText('Click to answer')

    # clear selecte redio button
    QuestionRadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    QuestionRadioGroup.setExclusive(True)


answer = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(q: Question):
    shuffle(answer)
    answer[0].setText(q.right_answer)
    answer[1].setText(q.wrong_answer1)
    answer[2].setText(q.wrong_answer2)
    answer[3].setText(q.wrong_answer3)
    LabelQuestion.setText(q.question)
    labelCorrectAnswer.setText(q.right_answer)
    show_questioin()

def show_correct(respone):
    labelAnswer.setText(respone)
    show_result()

def check_answer():
    if answer[0].isChecked():
        show_correct('Corrected!')
        window.score += 1
    else:
        if answer[1].isChecked() or answer[2].isChecked() or answer[3].isChecked():
            show_correct('Incorrected!')

def next_question(): 
    window.total += 1
    print('Statistics\n-Total questions: ', window.total, '\n-Right answers: ', window.score)

    current_question = randint(0, len(questions_list) - 1)

    q = questions_list[current_question]
    ask(q) 

def click_OK():
    if btn_OK.text() == 'Click to answer':
        check_answer()
    else:
        next_question()

window = QWidget()
window.setLayout(whole_layout)
window.setWindowTitle('Memory Card')


btn_OK.clicked.connect(click_OK)

window.score = 0
window.total = 0

next_question()

window.resize(400, 300)

window.show()
app.exec()


