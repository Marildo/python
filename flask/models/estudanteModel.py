from flask_sqlalchemy import Model
from sqlalchemy import Column, String, Integer

class Estudante(Model):
    id = Column(Integer, primary_key=True)
    nome = Column(String(150))
    idade = Column(Integer)

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
