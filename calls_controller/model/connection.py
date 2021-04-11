import logging

from sqlalchemy import create_engine
from sqlalchemy.orm.session import sessionmaker

from model.tables import Base


class DBConnection:

    def __init__(self):
        self.__session = None

    def connect(self):
        try:
            engine = create_engine(self.builder_url(), pool_timeout=1000, echo=True)
            self.__session = sessionmaker(bind=engine)()
            Base.metadata.create_all(engine)
        except Exception as e:
            logging.error(f'Erro ao conectar ao banco de dados. Erro:{e}')

    @property
    def session(self):
        return self.__session

    def builder_url(self):
        # TODO colocar em arquivo de configuracao
        user = 'root'
        password = 'si411225'
        port = 3306
        host = 'localhost'
        database = 'call_controller'
        charset = 'utf8mb4'
        logging.info(f'Conectando a base dados em {host}')
        return f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}?charset={charset}'

    def test(self, any):
        self.__session.add(any)
        self.__session.commit()