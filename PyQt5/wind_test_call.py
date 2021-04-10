import sys

from PyQt5.QtWidgets import QMainWindow, QApplication

from wind_test import Ui_MainWindow


class MainWin(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.pushButton.clicked.connect(self.click)

    def click(self):
        print('Clickkkkk')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWin()
    main.show()
    sys.exit(app.exec_())
