from django.test import TestCase
from .models import InformacoesSensiveis, Pessoas

class PessoasTestCase(TestCase):
    
    
    def test_model_pessoas_existe(self):
        dados = Pessoas.objects.count()
        self.assertEqual(dados, 0)
        
    def test_model_informacoesSensiveis_existe(self):
        informacoes = InformacoesSensiveis.objects.count()
        self.assertEqual(informacoes, 0)