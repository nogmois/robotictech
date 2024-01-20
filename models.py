from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Anotacao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    classe = db.Column(db.String(80))
    confianca = db.Column(db.Float)
    centro_x = db.Column(db.Integer)
    centro_y = db.Column(db.Integer)
    largura = db.Column(db.Integer)
    altura = db.Column(db.Integer)

    sinalizada = db.Column(db.Boolean, default=False)
    alterada = db.Column(db.Boolean, default=False)
