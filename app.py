from flask import Flask, request, jsonify, redirect
from models import db, Anotacao

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///anotacoes.db'
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return redirect('/anotacoes')

# Rotas da API

# POST
@app.route('/anotacoes', methods=['POST'])
def add_anotacao():
    dados = request.json

    # Verifica se todos os campos obrigatórios estão presentes no corpo da requisição
    campos_obrigatorios = ['classe', 'confianca', 'centro_x', 'centro_y', 'largura', 'altura']
    for campo in campos_obrigatorios:
        if campo not in dados:
            return jsonify({'erro': f'O campo "{campo}" é obrigatório.'}), 400

    # Validações adicionais, por exemplo, se a confiança está dentro do intervalo de 0 a 1
    if not 0 <= dados['confianca'] <= 1:
        return jsonify({'erro': 'A confiança deve estar entre 0 e 1.'}), 422

    # Resto do código para adicionar a anotação
    anotacao = Anotacao(classe=dados['classe'], confianca=dados['confianca'],
                        centro_x=dados['centro_x'], centro_y=dados['centro_y'],
                        largura=dados['largura'], altura=dados['altura'])
    db.session.add(anotacao)
    db.session.commit()
    return jsonify({'mensagem': 'Anotação adicionada com sucesso!'}), 201


# GET
@app.route('/anotacoes', methods=['GET'])
def get_anotacoes():
    anotacoes = Anotacao.query.all()
    return jsonify([{'id': anot.id, 'classe': anot.classe, 'confianca': anot.confianca, 'centro_x': anot.centro_x, 'centro_y': anot.centro_y, 'largura': anot.largura, 'altura': anot.altura} for anot in anotacoes])

@app.route('/anotacoes/<int:id>', methods=['GET'])
def get_anotacao(id):
    anotacao = Anotacao.query.get_or_404(id)
    return jsonify({'id': anotacao.id, 'classe': anotacao.classe, 'confianca': anotacao.confianca, 'centro_x': anotacao.centro_x, 'centro_y': anotacao.centro_y, 'largura': anotacao.largura, 'altura': anotacao.altura})

@app.route('/anotacoes/alteradas', methods=['GET'])
def get_anotacoes_alteradas():
    anotacoes = Anotacao.query.filter_by(alterada=True).all()
    if not anotacoes:
        return jsonify([])
    return jsonify([{
        'id': anot.id, 
        'classe': anot.classe, 
        'confianca': anot.confianca, 
        'centro_x': anot.centro_x, 
        'centro_y': anot.centro_y, 
        'largura': anot.largura, 
        'altura': anot.altura,
        'sinalizada': anot.sinalizada
    } for anot in anotacoes])

@app.route('/anotacoes/sinalizadas', methods=['GET'])
def get_anotacoes_sinalizadas():
    anotacoes = Anotacao.query.filter_by(sinalizada=True).all()
    if not anotacoes:
        return jsonify([])
    return jsonify([{
        'id': anot.id, 
        'classe': anot.classe, 
        'confianca': anot.confianca, 
        'centro_x': anot.centro_x, 
        'centro_y': anot.centro_y, 
        'largura': anot.largura, 
        'altura': anot.altura,
        'alterada': anot.alterada
    } for anot in anotacoes])



# PUT

@app.route('/anotacoes/<int:id>', methods=['PUT'])
def update_anotacao(id):
    anotacao = Anotacao.query.get_or_404(id)
    dados = request.json
    anotacao.classe = dados.get('classe', anotacao.classe)
    anotacao.confianca = dados.get('confianca', anotacao.confianca)
    
    db.session.commit()
    return jsonify({'mensagem': 'Anotação atualizada com sucesso!'})

@app.route('/anotacoes/sinalizar/<int:id>', methods=['PUT'])
def sinalizar_anotacao(id):
    anotacao = Anotacao.query.get_or_404(id)
    anotacao.sinalizada = True
    db.session.commit()
    return jsonify({'mensagem': 'Anotação sinalizada como errada.'})


# DELETE

@app.route('/anotacoes/<int:id>', methods=['DELETE'])
def delete_anotacao(id):
    anotacao = Anotacao.query.get_or_404(id)
    db.session.delete(anotacao)
    db.session.commit()
    return jsonify({'mensagem': 'Anotação deletada com sucesso!'})


if __name__ == '__main__':
    

    # Importe a classe Anotacao do seu modelo
    from models import Anotacao

    # Crie as 5 anotações automaticamente
    with app.app_context():
        for i in range(5):
            classe = f"Classe de Anotação {i}"
            confianca = 0.9  # Confiança (float)
            centro_x = 50   # Centro X (int)
            centro_y = 50   # Centro Y (int)
            largura = 100   # Largura (int)
            altura = 100    # Altura (int)
            
            # Defina alterada e sinalizada com base no índice i
            alterada = True if i % 2 == 0 else False
            sinalizada = True if i % 3 == 0 else False
            
            anotacao = Anotacao(
                classe=classe,
                confianca=confianca,
                centro_x=centro_x,
                centro_y=centro_y,
                largura=largura,
                altura=altura,
                alterada=alterada,
                sinalizada=sinalizada
            )
            db.session.add(anotacao)
        
        db.session.commit()

    app.run(debug=True)