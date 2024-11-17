from app_config import db

class Aluno(db.Model):
    __tablename__ = "alunos"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    curso = db.Column(db.String(150), nullable=False)
    nota = db.Column(db.Float, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "idade": self.idade,
            "curso": self.curso,
            "nota": self.nota
        }