import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from view.mainWindow import Ui_MainWindow


class MainWindowControll(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.setup_actions()

    def setup_actions(self):
        self.pushButton.clicked.connect(self.on_click)

    def on_click(self):
        print('Eu fui clicado')


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = MainWindowControll()
    MainWindow.show()
    sys.exit(app.exec_())
