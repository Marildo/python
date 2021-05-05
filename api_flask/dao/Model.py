
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine, MetaData, Column, Table, INTEGER, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from flask_marshmallow import Marshmallow

engine = create_engine('sqlite:///test_api.db', echo=True)

session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
session.configure(bind=engine)
metadata = MetaData(bind=engine)
Base = declarative_base()
metadata.create_all()

ma = Marshmallow()

def configureMash(app):
    ma.init_app(app)

class User(Base):
    __tablename__ = 'user'

    id = Column(INTEGER, primary_key=True)
    name = Column(String, nullable=False, default='')
    update_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())

class UserSchema(ma.Schema):
    class Meta:
        model = User
        fields = ('id', 'name','update_at')

