from app_config import app, db
from flask import request, jsonify
from models.alunos_model import Aluno

@app.route('/alunos', methods=['POST'])
def add_aluno():
    data = request.get_json()
    novo_aluno = Aluno(
        nome=data['nome'],
        idade=data['idade'],
        curso=data['curso'],
        nota=data['nota']
    )
    db.session.add(novo_aluno)
    db.session.commit()
    return jsonify(novo_aluno.to_dict()), 201


@app.route('/alunos', methods=['GET'])
def listar_alunos():
    alunos = Aluno.query.all()
    return jsonify([aluno.to_dict() for aluno in alunos]), 200

@app.route('/alunos/<int:id>', methods=['GET'])
def get_aluno(id):
    aluno = Aluno.query.get_or_404(id)
    return jsonify(aluno.to_dict()), 200


@app.route('/alunos/<int:id>', methods=['DELETE'])
def delete_aluno(id):
    aluno = Aluno.query.get_or_404(id)
    db.session.delete(aluno)
    db.session.commit()
    return '', 204 # no content


@app.route('/alunos/<int:id>', methods=['PUT'])
def atualizar_aluno(id):
    aluno = Aluno.query.get_or_404(id)
    data = request.get_json()
    aluno.nome = data['nome']
    aluno.idade = data['idade']
    aluno.curso = data['curso']
    aluno.nota = data['nota']
    db.session.commit()
    return jsonify(aluno.to_dict()), 200


if __name__ == '__main__':
    app.run()
