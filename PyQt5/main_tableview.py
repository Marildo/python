import logging
import operator
import sys
from datetime import datetime

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QMainWindow

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

        data = list(map(lambda x: [x.id, x.description, datetime.strftime(x.init, "%d/%m/%Y %H:%M")], actions))

        for item in data:
            print(item)

        header = ['Id', 'Descrição', 'Inicio', 'col_3', 'col_4']
        tablemodel = MyTableModel(data, header, self)
        self.tv_tarefas.setModel(tablemodel)


class MyTableModel(QAbstractTableModel):
    def __init__(self, datain, headerdata, parent=None):
        QAbstractTableModel.__init__(self, parent)
        self.arraydata = datain
        self.headerdata = headerdata

    def rowCount(self, parent):
        return len(self.arraydata)

    def columnCount(self, parent):
        if len(self.arraydata) > 0:
            return len(self.arraydata[0])
        return 0

    def data(self, index, role):
        if not index.isValid():
            return QVariant()
        elif role != Qt.DisplayRole:
            return QVariant()
        return QVariant(self.arraydata[index.row()][index.column()])

    def setData(self, index, value, role):
        pass  # not sure what to put here

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return QVariant(self.headerdata[col])
        return QVariant()


if __name__ == "__main__":
    try:
        app = QApplication(sys.argv)
        MainWindow = MainWindowControll()
        MainWindow.show()
        sys.exit(app.exec_())
    except Exception as error:
        logging.error(error)
