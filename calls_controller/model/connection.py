from sqlalchemy import create_engine
import logging

class DBConnection:

    def __init__(self):
        # TODO colocar em arquivo de configuracao
        self.user = 'root'
        self.password = 'si411225'
        self.host = 'localhost'
        self.database = 'world'
        self.charset = 'utf8mb4'

    def connectar(self):
        try:
            engine = create_engine(
                f'mysql+pymysql://{self.user}:{self.password}@{self.host}/{self.database}?charset={self.charset}')
            connect = engine.connect()
            logging.info(f'Conectado a base dados em {self.host}')
        except Exception as e:
            print(e)
