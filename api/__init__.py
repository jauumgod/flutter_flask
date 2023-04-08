from flask import Flask, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import pymysql

pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
mi = Migrate(app, db)

from .models import conta_model