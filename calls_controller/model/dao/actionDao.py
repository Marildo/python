from model.connection import DBConnection
from model.tables import Action


class ActionDao(object):
    def __init__(self, connection: DBConnection):
        self.__connection = connection

    def save(self, action: Action):
        try:
            session = self.__connection.session
            session.add(action)
            session.commit()
        except Exception as e:
            print(f'Erro ao conectar ao banco de dados. Erro:{e}')

    def load(self):
        session = self.__connection.session
        return session.query(Action).all()
