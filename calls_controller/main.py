import logging
import sys
from datetime import datetime

from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem

from model.connection import DBConnection
from model.dao.actionDao import ActionDao
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
        connection = DBConnection()
        connection.connect()

        dao = ActionDao(connection)
        """
        action = Action()
        action.description = 'Qualquer coisa vale'
       
        dao.save(action)
      

       
        print(type(actions))
             data = map(lambda x:[ x.id ], actions )
        print(data)
        
          """
        actions = dao.load()

        header = ('Id', 'Descrição', 'Inicio')
        data = list(map(lambda x: (x.id, x.description, datetime.strftime(x.init, "%d/%m/%Y %H:%M")), actions))


        self.tw_actions.setRowCount(len(data))
        self.tw_actions.setColumnCount(len(header))

        for i in range(0, len(data)):
            for j in range(0, len(header)):
                self.tw_actions.setItem(i, j, QTableWidgetItem(str(data[i][j])))


if __name__ == "__main__":
    try:
        app = QApplication(sys.argv)
        MainWindow = MainWindowControll()
        MainWindow.show()
        sys.exit(app.exec_())
    except Exception as error:
        logging.error(error)
