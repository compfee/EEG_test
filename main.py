import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import time
class MainWindow(QDialog):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi('eeg_test_main.ui', self)
        self.pushButton.clicked.connect(self.gotoScreen2)

    def gotoScreen2(self):
        widget.setCurrentIndex(widget.currentIndex()+1)

class Screen2(QDialog):
    def __init__(self, labels):
        super(Screen2, self).__init__()
        loadUi('eeg_test_exp.ui', self)
        self.labelsTitle = labels[0]
        self.labels = labels[1:]
        self.counter = 0
        self.len_labels = len(self.labels)
        # self.label.setText("Подготовтесь к эксперименту")
        self.wordLabel = QLabel(self)
        self.wordLabel.setStyleSheet('font-size: 18pt; color: blue;')
        self.wordLabel.setGeometry(250, 120, 200, 100)

        # self.timerEvent(seconds_num = 5, wid = self.label_2)
        timer = QTimer(self)
        timer.timeout.connect(self.onTimeout)
        timer.start(2000)

    def onTimeout(self):
        if self.counter >= self.len_labels:
            self.counter = 0

        self.wordLabel.setText(str(self.labels[self.counter]))
        self.counter += 1

labels =  ['Подготовка к эксперименту',"Сжимайте", "Расжимайте"]

app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
mainwindow = MainWindow()
screen2 = Screen2(labels)
widget.addWidget(mainwindow)
widget.addWidget(screen2)
widget.setFixedHeight(400)
widget.setFixedWidth(700)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exit")