from api import api
from flask_restful import Resource
from ..schemas import login_schema
from ..services import usuario_service
from flask import request, make_response, jsonify
from ..models.usuario_model import Usuario
from flask_jwt_extended import create_access_token, create_refresh_token
from datetime import timedelta

class LoginList(Resource):
    def post(self):
        ls = login_schema.LoginSchema()
        validate = ls.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            email = request.json['email']
            senha = request.json['senha']
            
            usuario_bd = usuario_service.listar_usuario_email(email)
            
            if usuario_bd and usuario_bd.decripto_senha(senha):
                access_token = create_access_token(
                    identity=usuario_bd.id,
                    expires_delta=timedelta(seconds=120)
                )
                refresh_token = create_refresh_token(
                    identity=usuario_bd.id
                )
                return make_response(jsonify({
                    'access_token': access_token,
                    'refresh_token': refresh_token,
                    'mensagem': 'Login realizado com sucesso!'
                }), 200)
            
            return make_response(jsonify({
                "mensagem":"credenciais estão invalidas"
            }), 400)
            
api.add_resource(LoginList, "/login")