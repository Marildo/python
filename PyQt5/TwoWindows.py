from PyQt5 import uic, QtWidgets

def loadSecond(self):
   secondWind.show()

def loadFirst(self):
   fisrtWind.show()

app = QtWidgets.QApplication([])
fisrtWind = uic.loadUi("firstWindows.ui")
secondWind = uic.loadUi('secondWindow.ui')

fisrtWind.pushButton.clicked.connect(loadSecond)
secondWind.pushButton.clicked.connect(loadFirst)






fisrtWind.show()
app.exec()