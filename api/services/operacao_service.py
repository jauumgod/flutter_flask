from api import db
from ..models import operacao_model, conta_model
from ..services import conta_service

def listar_operacoes(usuario):
    operacoes = operacao_model.Operacao.query.join(conta_model.Conta).filter_by(usuario_id=usuario).all()
    return operacoes

def listar_operacoes_id(id):
    operacao = operacao_model.Operacao.query.filter_by(id=id).first()
    return operacao

def cadastrar_operacao(operacao):
    operacao_db = operacao_model.Operacao(
    nome=operacao.nome, 
    resumo=operacao.resumo, 
    custo=operacao.custo, 
    tipo =operacao.tipo, 
    conta_id=operacao.conta)
    db.session.add(operacao_db)
    db.session.commit()
    conta_service.alterar_saldo_conta(operacao.conta, operacao, 1)

def atualizar_operacao(operacao,nova_operacao):
    valor_antigo = operacao.custo
    operacao.nome = nova_operacao.nome
    operacao.resumo = nova_operacao.resumo
    operacao.custo = nova_operacao.custo
    operacao.tipo = nova_operacao.tipo
    operacao.conta = nova_operacao.conta
    db.session.commit()
    conta_service.alterar_saldo_conta(nova_operacao.conta,nova_operacao, 2, valor_antigo)
    return operacao

def excluir_operacao(operacao):
    db.session.delete(operacao)
    db.session.commit()
    conta_service.alterar_saldo_conta(operacao.conta_id, operacao, 3)