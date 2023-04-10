from flask import Flask, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_restful import Api
import pymysql

pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
mi = Migrate(app, db)
ma = Marshmallow(app)
api = Api(app)

from .models import conta_model
from .views import conta_view
