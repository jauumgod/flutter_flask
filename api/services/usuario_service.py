from api import db
from ..models import usuario_model



def listar_usuarios():
    usuarios = usuario_model.Usuario.query.all()
    return usuarios

def listar_usuario_id(id):
    usuario = usuario_model.Usuario.query.filter_by(id=id).first()
    return usuario

def listar_usuario_email(email):
    usuario = usuario_model.Usuario.query.filter_by(email=email).first()
    return usuario

def cadastrar_usuarios(usuario):
    usuario_db = usuario_model.Usuario(nome=usuario.nome, email=usuario.email, senha=usuario.senha)
    usuario_db.cripto_senha()
    db.session.add(usuario_db)
    db.session.commit()

def exluir_usuario(id):
    usuario = usuario_model.Usuario.query.filter_by(id=id).first()
    db.session.delete(usuario)
    db.session.commit()
