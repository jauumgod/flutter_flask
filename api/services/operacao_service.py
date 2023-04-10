from api import db
from ..models import operacao_model

def listar_operacoes():
    operacoes = operacao_model.Operacao.query.all()
    return operacoes

def listar_operacoes_id(id):
    operacao = operacao_model.Operacao.query.filter_by(id=id).first()
    return operacao

def cadastrar_operacao(operacao):
    operacao_db = operacao_model.Operacao(nome=operacao.nome, resumo=operacao.resumo, custo=operacao.custo, tipo =operacao.tipo, conta_id=operacao.conta)
    db.session.add(operacao_db)
    db.session.commit()

def atualizar_operacao(operacao,nova_operacao):
    operacao.nome = nova_operacao.nome
    operacao.resumo = nova_operacao.resumo
    operacao.custo = nova_operacao.custo
    operacao.tipo = nova_operacao.tipo
    operacao.contsa = nova_operacao.conta
    db.session.commit()
    return operacao

def excluir_operacao(operacao):
    db.session.delete(operacao)
    db.session.commit()