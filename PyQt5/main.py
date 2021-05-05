import sys
from datetime import datetime

from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(100, 100, 1000, 700)
        self.setWindowTitle('Minha primeira janela com PyQt5')

        btn1 = QPushButton('Time', self)
        btn1.move(10, 30)
        btn1.resize(150, 100)
        btn1.setStyleSheet('QPushButton { background-color: #0FB123; color:white; font-size:30px }')
        btn1.clicked.connect(self.onLoadTime)

        btn2 = QPushButton('btn2', self)
        btn2.move(10, 150)
        btn2.resize(150, 100)
        btn2.setStyleSheet('QPushButton { background-color: #DDB883; color:white; font-size:30px }')
        btn2.clicked.connect(self.onChangeImage)

        self.lbl1 = QLabel(self)
        self.lbl1.move(180, 30)
        self.lbl1.resize(400, 20)
        self.lbl1.setStyleSheet('QLabel { color:blue; font-size:20px }')
        self.lbl1.setText('Helo world')

        self.lbl_image = QLabel(self)
        self.lbl_image.move(300, 80)
        self.lbl_image.setPixmap(QtGui.QPixmap('naruto.jpg'))
        self.lbl_image.resize(600, 500)

        edt01 = QLineEdit(self)
        edt01.move(300, 10)
        edt01.resize(70, 30)
        self.edt01 = edt01

        btnCalc = QPushButton('Calcular', self)
        btnCalc.move(380, 10)
        btnCalc.clicked.connect(self.onCalc)

    def onLoadTime(self):
        self.lbl1.setText(str(datetime.now()))
        self.lbl_image.setPixmap(QtGui.QPixmap('naruto.jpg'))

    def onChangeImage(self):
        self.lbl_image.setPixmap(QtGui.QPixmap('sasuke-uchiha_46ah.jpg'))

    def onCalc(self):
        num = int(self.edt01.text())
        self.edt01.setText(str(num ** 3))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
