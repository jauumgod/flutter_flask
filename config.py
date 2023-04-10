DEBUG = True

USERNAME = 'jmnd1'
PASSWORD = 'A1h2q4v1'
SERVER = 'localhost'
DB = 'gerenciamento_contas'

SQLALCHEMY_DATABASE_URI = f'mysql://{USERNAME}:{PASSWORD}@{SERVER}/{DB}'
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = '2h1hesoyam2j5uzumymw2m3'