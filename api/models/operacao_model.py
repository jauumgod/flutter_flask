from api import db
import enum

class TipoEnum(enum.Enum):
    entrada = 1
    saida = 2

class Operacao(db.Model):
    __tablename__ = 'operacao'
    id = db.Column(db.Integer, primary_key = True, autoincrement=True, nullable=False)
    nome = db.Column(db.String(50), nullable=False)
    resumo = db.Column(db.String(150), nullable=False)
    custo = db.Column(db.Float, nullable=False)
    tipo = db.Column(db.Enum(TipoEnum), nullable=False)