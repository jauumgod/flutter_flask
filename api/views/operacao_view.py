from flask_restful import Resource
from ..schemas import operacao_schema
from flask import request, make_response, jsonify
from ..entidades import operacao
from ..services import operacao_service
from api import api


class OperacaoList(Resource):
    def get(self):
        operacoes = operacao_service.listar_operacoes()
        os = operacao_schema.OperacaoSchema(many=True)
        return make_response(os.jsonify(operacoes), 201)
    
    def post(self):
        os = operacao_schema.OperacaoSchema()
        validate = os.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json["nome"]
            resumo = request.json["resumo"]
            custo = request.json["custo"]
            tipo = request.json["tipo"]
            operacao_nova = operacao.Operacao(nome=nome, resumo=resumo, custo=custo, tipo=tipo)
            resultado = operacao_service.cadastrar_operacao(operacao_nova)
            return make_response(os.jsonify(resultado), 201)

# class OperacaoDetail(Resource):
#     def get(self,id):
#         conta = operacao_service.listar_conta_id(id)
#         if conta is None:
#             return make_response(jsonify("Conta não encontrada"), 404)
#         cs =operacao_schema.ContaSchema()
#         return make_response(cs.jsonify(conta), 200)

#     def put(self, id):
#         conta_bd = operacao_service.listar_conta_id(id)
#         if conta_bd is None:
#             return make_response(jsonify("Conta não encontrada"), 404)

#         cs = operacao_schema.ContaSchema()
#         validate = cs.validate(request.json)
#         if validate:
#             return make_response(jsonify(validate), 404)
#         else:
#             nome = request.json["nome"]
#             resumo = request.json["resumo"]
#             custo = request.json["valor"]
#             tipo = request.json["tipo"]
#             nova_conta = operacao.Operacao(nome=nome, resumo=resumo, custo=custo, tipo=tipo)
#             resultado = operacao_service.atualizar_conta(conta_bd, nova_conta)
#             return make_response(cs.jsonify(resultado), 201)
    
#     def delete(self,id):
#         conta = operacao_service.listar_conta_id(id)
#         if conta is None:
#             return make_response(jsonify("Conta não encontrada"), 404)
#         operacao_service.exclui_conta(conta)
#         return make_response(jsonify(""), 204)


api.add_resource(OperacaoList, '/operacoes')
