
import unittest
from app import app, db
from models import Anotacao

class APITestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        app.config['TESTING'] = True
        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.drop_all()

    def test_get_anotacoes(self):
        response = self.app.get('/anotacoes')
        self.assertEqual(response.status_code, 200)

    def test_post_anotacao(self):
        test_anotacao = {
            'classe': 'carro',
            'confianca': 0.9,  # Corrigir para um valor entre 0 e 1
            'centro_x': 150,
            'centro_y': 100,
            'largura': 60,
            'altura': 40
        }
        response = self.app.post('/anotacoes', json=test_anotacao)
        self.assertEqual(response.status_code, 201)
        self.assertIn('mensagem', response.json)
        self.assertEqual(response.json['mensagem'], 'Anotação adicionada com sucesso!')


    def test_update_anotacao(self):
        with app.app_context():
            # Criando uma anotação para atualizar
            anotacao = Anotacao(classe='moto', confianca=80, centro_x=100, centro_y=80, largura=50, altura=30)
            db.session.add(anotacao)
            db.session.commit()
            id = anotacao.id

        updated_data = {'classe': 'caminhão', 'confianca': 85}
        response = self.app.put(f'/anotacoes/{id}', json=updated_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('mensagem', response.json)
        self.assertEqual(response.json['mensagem'], 'Anotação atualizada com sucesso!')

    def test_delete_anotacao(self):
        with app.app_context():
            # Criando uma anotação para teste
            anotacao = Anotacao(classe='bicicleta', confianca=75, centro_x=120, centro_y=90, largura=45, altura=25)
            db.session.add(anotacao)
            db.session.commit()
            id_teste = anotacao.id

        response = self.app.delete(f'/anotacoes/{id_teste}')
        self.assertEqual(response.status_code, 200)
        self.assertIn('mensagem', response.json)
        self.assertEqual(response.json['mensagem'], 'Anotação deletada com sucesso!')

    def test_sinalizar_anotacao(self):
        with app.app_context():
            # Criando uma anotação para sinalizar
            anotacao = Anotacao(classe='pedestre', confianca=65, centro_x=130, centro_y=110, largura=35, altura=45)
            db.session.add(anotacao)
            db.session.commit()
            id_teste = anotacao.id

        response = self.app.put(f'/anotacoes/sinalizar/{id_teste}')
        self.assertEqual(response.status_code, 200)
        self.assertIn('mensagem', response.json)
        self.assertEqual(response.json['mensagem'], 'Anotação sinalizada como errada.')

    def test_get_anotacoes_alteradas(self):
        with app.app_context():
            # Criando uma anotação alterada para teste
            anotacao_alterada = Anotacao(classe='alterada', confianca=70, centro_x=100, centro_y=100, largura=30, altura=30, alterada=True)
            db.session.add(anotacao_alterada)
            db.session.commit()

        response = self.app.get('/anotacoes/alteradas')
        self.assertEqual(response.status_code, 200)
        
    def test_get_anotacoes_sinalizadas(self):
        with app.app_context():
            # Criando uma anotação sinalizada para teste
            anotacao_sinalizada = Anotacao(classe='sinalizada', confianca=50, centro_x=50, centro_y=50, largura=20, altura=20, sinalizada=True)
            db.session.add(anotacao_sinalizada)
            db.session.commit()

        response = self.app.get('/anotacoes/sinalizadas')
        self.assertEqual(response.status_code, 200)
        
if __name__ == '__main__':
    unittest.main()
