from api import db
from ..models import conta_model

def listar_contas():
    contas = conta_model.Conta.query.all()
    return contas

def cadastrar_conta(conta):
    conta_bd = conta_model.Conta(nome=conta.nome, resumo=conta.resumo, valor=conta.valor)
    db.session.add(conta_bd)
    db.session.commit()
    return conta_bd

