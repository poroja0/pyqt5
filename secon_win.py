from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont # проверка типов вводимых значений
from PyQt5.QtWidgets import (
       QApplication, QWidget,
       QHBoxLayout, QVBoxLayout, QGridLayout,
       QGroupBox, QRadioButton,
       QPushButton, QLabel, QListWidget, QLineEdit)


from instr import *
from fin_win import *



     
class TestWin(QWidget):
   def __init__(self):
       ''' окно, в котором располагается приветствие '''
       super().__init__()


       #устанавливает, как будет выглядеть окно (надпись, размер, место)
       self.set_appear()


       # создаём и настраиваем графические элементы:
       self.initUI()


       #устанавливает связи между элементами
       self.connects()


       # старт:
       self.show()


   def initUI(self):
       ''' создаёт графические элементы '''
       self.text_age = QLabel( txt_age)
       self.text_pol1 = QLineEdit('0')
       self.but1 = QPushButton('Начать первый тест')

       self.text_age2 = QLabel(txt_starttest1)
       self.text_pol2 = QLineEdit('0')
       self.but2 = QPushButton(txt_starttest2)

       self.text_age3 = QLabel()
       self.text_pol3 = QLineEdit()
       self.bu3 = QPushButton(txt_starttest3)

       self.text_age4 = QLabel()
       self.text_age5 = QLabel()

       self.text_pol4 = QLineEdit('0')
       self.text_pol5 = QLineEdit('0')

       self.but4 = QPushButton(txt_sendresults)


       self.layoutH = QHBoxLayout()
       self.layoutV1 = QVBoxLayout()
       self.layoutV2 = QVBoxLayout()

       self.layoutV1.addWidget(self.text_age, alignment = Qt.AlignLeft)
  



       self.layoutH.addLayout(self.layoutV1)
       self.layoutH.addLayout(self.layoutV2)
       self.setLayout(self.layoutH)

   def next_click(self):
       self.tw = secon_win.TestWin()
       self.hide()


   def connects(self):
       self.but4.clicked.connect(self.next_click)


   ''' устанавливает, как будет выглядеть окно (надпись, размер, место) '''
   def set_appear(self):
       self.setWindowTitle(txt_title)
       self.resize(win_width, win_height)
       self.move(win_x, win_y)

