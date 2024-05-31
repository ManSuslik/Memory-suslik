from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from random import shuffle



class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
		

question_list = []	
question_list.append(Question('Государственный язык Бразили' ,"Португальский", 'Испанский', 'Англиский', 'Бразильский'))
question_list.append(Question('Какого цвета нет на флаге России', "Зеленый", "Красный", "Белый", "Синий"))
question_list.append(Question('Национальная хижана якутов',"Ураса", "Юрта", "Иглу", "Хата"))

app = QApplication([])


window = QWidget()
window.setWindowTitle('Memory Card')
window.total = 0
window.score = 0

question = QLabel('Какой национальности не существует?')
btn_Ok = QPushButton('Ответить')

# main_layout = QvBoxLayout()
layout_1 = QVBoxLayout()


RadioGroupBox = QGroupBox("Варианты ответов")
rbtn_1 = QRadioButton("Эицы")
rbtn_2 = QRadioButton("Смурфы")
rbtn_3 = QRadioButton("Чулымцы")
rbtn_4 = QRadioButton("Алеуты")
layout_ans1 = QHBoxLayout()

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

ansGroupBox = QGroupBox('Результаты теста')
lb_result = QLabel('Правильно или нет')
lb_correct = QLabel('Ответ будет тут.')

layout_res = QVBoxLayout()

layout_res.addWidget(lb_result, alignment=Qt.AlignLeft)
layout_res.addWidget(lb_correct, alignment=Qt.AlignCenter)
ansGroupBox.setLayout(layout_res)

line1 = QHBoxLayout()
line2 = QHBoxLayout()
line3 = QHBoxLayout()

line1.addWidget(question, alignment=Qt.AlignCenter)
line2.addWidget(RadioGroupBox, alignment=Qt.AlignCenter)
line2.addWidget(ansGroupBox)
ansGroupBox.hide()

line3.addWidget(btn_Ok)

layout_1.addLayout(line1)
layout_1.addLayout(line2)
layout_1.addLayout(line3)

def show_question():
	RadioGroupBox.show()
	# ansGroupBox.show()
	btn_Ok.setText('Ответить')
	RadioGroup.setExclusive(False)
	rbtn_1.setChecked(False)
	rbtn_2.setChecked(False)
	rbtn_3.setChecked(False)
	rbtn_4.setChecked(False)
	RadioGroup.setExclusive(True)
	
def show_result():
    RadioGroupBox.show()
    # ansGroupBox.hide()
    btn_Ok.setText('Следующий вопрос')


answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(q:Question):
	shuffle(answers)
	answers[0].setText(q.right_answer)
	answers[1].setText(q.wrong1)
	answers[2].setText(q.wrong2)
	answers[3].setText(q.wrong3)
	question.setText(q.question)
	show_question()

def show_correct(res):
	lb_result.setText(res)
	show_result()
	
def check_answer():
	if answers[0].isChecked():
		show_correct('Правильно')
		score =+ 1
	else:
		if answers[1].isChecked() or answers[2].isChecked or answers[3].isChecked():
			show_correct('Неправильно!')

def next_question():
	window.total += 1
	window.cur_question = window.cur_question+1
	if window.cur_question >= len(question_list):
		window.cur_question = 0
	q = question_list[window.cur_question]
	ask(q)
	
def click_OK():
	if btn_Ok.text() == 'Ответить':
		check_answer()
	else:
		next_question()
		
window.setLayout(layout_1)
window.cur_question = 0
next_question()
btn_Ok.clicked.connect(click_OK)
window.resize(400, 300)
window.show()
app.exec_()