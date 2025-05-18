#для начала скопируй сюда интерфейс "Умных заметок" и проверь его работу

#затем запрограммируй демо-версию функционала
import random
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QListWidget, QVBoxLayout, QHBoxLayout, QGroupBox, QRadioButton, QTextEdit

def freq():
    Present = ['С новым годом🎉', 'С праздником🎁', 'Здоровья, счатстья✨', 'Новых планов и идей🎊', 'Новых радостных затей!🎈', 'С Новым 2025 годом!🥳', 'Вкусного шампанского с  и вкусных мандаринов🥂🍊' ]
    index  = random.randint(0, 5)
    text.setText(Present[index])

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Поздравление к новому 2025 году🍊🍊🍊')
main_win.resize(550, 600)

text = QLabel('Поздравление к новому году, и много пожеланий🐍')
button = QPushButton('Поздравление к 2025🌲☘')
main_layout = QVBoxLayout()
main_layout.addWidget(text)
main_layout.addWidget(button)
Stretch = (2)
button.clicked.connect(freq)
main_win.setLayout(main_layout)
main_win.show()
app.exec_()


