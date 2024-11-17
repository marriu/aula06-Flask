from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object('config')
app.secret_key = 'Infinity'

db = SQLAlchemy(app)
migrate = Migrate(app, db)
from models.alunos_model import Aluno