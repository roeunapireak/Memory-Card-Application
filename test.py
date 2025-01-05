#create a memory card application
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, 
                             QHBoxLayout, QLabel, QPushButton,
                             QGroupBox, QRadioButton, QButtonGroup)
# import datetime

from random import shuffle

class Question():
    def __init__(self, quiz, right_answer, wrong_2, wrong_3, wrong_4):
        self.quiz = quiz
        self.right_answer = right_answer
        self.wrong_2 = wrong_2
        self.wrong_3 = wrong_3
        self.wrong_4 = wrong_4

question_list = list()

quiz_1 = Question(quiz='What are you studying at AlgoPP?',
         right_answer='Python Start 2', 
         wrong_2='Python Start 1',
         wrong_3='Visual Programming',
         wrong_4='Game Design')
question_list.append(quiz_1)

quiz_2 = Question(quiz='Who is your python teacher?',
         right_answer='Apireak', 
         wrong_2='Natt',
         wrong_3='Chenda',
         wrong_4='Thida')
question_list.append(quiz_2)

quiz_3 = Question(quiz='Which program return error?',
         right_answer='print(hello world)', 
         wrong_2='print("hello world")',
         wrong_3='print("hello"+"world")',
         wrong_4='print("hello","world")')
question_list.append(quiz_3)


app = QApplication([])


question = QLabel()

answer_bottun = QPushButton('Answer')

quiz_group_box = QGroupBox('Answer options:')
option_1 = QRadioButton()
option_2 = QRadioButton()
option_3 = QRadioButton()
option_4 = QRadioButton()

button_group = QButtonGroup()
button_group.addButton(option_1)
button_group.addButton(option_2)
button_group.addButton(option_3)
button_group.addButton(option_4)


group_v_line = QVBoxLayout()
group_hline_1 = QHBoxLayout()
group_hline_2 = QHBoxLayout()

group_hline_1.addWidget(option_1)
group_hline_1.addWidget(option_2)
group_hline_2.addWidget(option_3)
group_hline_2.addWidget(option_4)

group_v_line.addLayout(group_hline_1)
group_v_line.addLayout(group_hline_2)

quiz_group_box.setLayout(group_v_line)

quiz_group_box.show()


answer_group_box = QGroupBox('check answer:')
answer_result = QLabel('True/False')
check_result = QLabel('Correct Answer')

answer_v_line = QVBoxLayout()

answer_v_line.addWidget(answer_result, alignment=Qt.AlignLeft)
answer_v_line.addWidget(check_result, alignment=Qt.AlignVCenter)
answer_group_box.setLayout(answer_v_line)

answer_group_box.hide()

window_v_line = QVBoxLayout()
h_line_1 = QHBoxLayout()
h_line_2 = QHBoxLayout()
h_line_3 = QHBoxLayout()


h_line_1.addWidget(question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
h_line_2.addWidget(quiz_group_box, alignment= Qt.AlignVCenter)
h_line_2.addWidget(answer_group_box, alignment= Qt.AlignVCenter)
h_line_3.addWidget(answer_bottun, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))

window_v_line.addLayout(h_line_1)
window_v_line.addLayout(h_line_2)
window_v_line.addLayout(h_line_3)

'''' functions '''
def show_answer():
    quiz_group_box.hide()
    answer_group_box.show()
    answer_bottun.setText('Next question')

    # timestamp_ = datetime.datetime.now()
    # # timestamp_ = timestamp_.timestamp()
    # print(timestamp_, 'clicked answer.')

def show_question():
    answer_group_box.hide()
    quiz_group_box.show()
    answer_bottun.setText('Answer')

    # timestamp_ = datetime.datetime.now()
    # # timestamp_ = timestamp_.timestamp()
    # print(timestamp_, 'clicked question.')

    # unselected answer option
    button_group.setExclusive(False)
    option_1.setChecked(False)
    option_2.setChecked(False)
    option_3.setChecked(False)
    option_4.setChecked(False)
    button_group.setExclusive(True)
    

def is_check():
    if 'Answer' == answer_bottun.text():
        is_correct()
    else:
        next_question()

answer_options = [option_1, option_2, option_3, option_4]

def ask(instance_: Question):
    shuffle(answer_options)
    answer_options[0].setText(instance_.right_answer)
    answer_options[1].setText(instance_.wrong_2)
    answer_options[2].setText(instance_.wrong_3)
    answer_options[3].setText(instance_.wrong_4)

    question.setText(instance_.quiz)
    check_result.setText(instance_.right_answer)

    show_question()

def show_correct(respose):
    answer_result.setText(respose)
    show_answer()

def is_correct():   
    if answer_options[0].isChecked():
        show_correct(respose='Corrected!')
        window.score += 1
    else:
        if answer_options[1].isChecked() or answer_options[2].isChecked() or answer_options[3].isChecked():
            show_correct(respose='Incorrected!')

def next_question():
    window.current_quiz += 1
    window.quiz_total += 1
    if window.current_quiz >= len(question_list):
        window.current_quiz = 0
    instance_ = question_list[window.current_quiz]

    ask(instance_)

    if window.quiz_total == 0 or window.score == 0:
        print('\nSTATISTIC Collection:')
        print('     - Total question:', window.quiz_total)
        print('     - Correct answer:', window.score)
        print('     - Rating:', None)   
    if window.quiz_total != 0 or window.score != 0:
        print('\nSTATISTIC Collection:')
        print('     - Total question:',window.quiz_total)
        print('     - Correct answer:', window.score)
        print('     - Rating:', (window.score / window.quiz_total) * 100) 

    

# ask(quiz='which is your school?', 
#     right_answer='AlgoPP', 
#     wrong_2='ABA', 
#     wrong_3='WING School', 
#     wrong_4='ACLEDA insti..')


window = QWidget()
window.current_quiz = 0
window.quiz_total = -1
window.score = 0
window.setWindowTitle('Memory Card Application')
window.resize(400, 300)

window.setLayout(window_v_line)

answer_bottun.clicked.connect(is_check)
next_question()
window.show()
app.exec_()
