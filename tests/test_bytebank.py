import classe as cl
import pytest
from pytest import mark

class TestClass:

    def test_quando_idade_recebe_14_04_2000_retorna_24(self):
        #Given
        entrada = '14/04/2000'
        esperado = 24
        
        funcionarioTeste = cl.Pessoa(nome='Vinicius', data_nascimento=entrada, peso=80, altura=1.80, salario=100000)
        
        # When
        resultado = funcionarioTeste.idade()
        
        # Then
        assert resultado == esperado

    def test_quando_sobrenome_recebe_Nome_Sobrenome_retorna_Sobrenome(self):
        #Given
        entrada = 'Vinicius Rodrigues'
        esperado = 'Rodrigues'
        
        funcionarioTeste = cl.Pessoa(nome=entrada, data_nascimento='14/04/2000', peso=80, altura=1.80, salario=100000)
        
        # When
        resultado = funcionarioTeste.sobrenome()
        
        # Then
        assert resultado == esperado
        
    def test_quando_decrescimo_salario_recebe_100000_retorna_90000(self):
        #Given
        entrada_salario = 100000
        entrada_nome = 'Paulo Bragança'
        esperado = 90000
        
        funcionarioTeste = cl.Pessoa(nome=entrada_nome, data_nascimento='14/04/2000', peso=80, altura=1.80, salario=entrada_salario)
        
        # When
        resultado = funcionarioTeste.decrescimo_salario()
        
        # Then
        assert resultado == esperado
        
    @mark.calcularBonus
    def test_quando_calcular_bonus_recebe_1000_retorna_100(self):
        #Given
        entrada = 1000
        esperado = 100
        
        funcionarioTeste = cl.Pessoa(nome='Teste', data_nascimento='14/04/2000', peso=80, altura=1.80, salario=entrada)
        
        # When
        resultado = funcionarioTeste.bonus_salarial()
        
        # Then
        assert resultado == esperado
    
    @mark.calcularBonus
    def test_quando_calcular_bonus_recebe_1000000_retorna_exception(self):
        with pytest.raises(ValueError):
            #Given
            entrada = 1000000
            
            funcionarioTeste = cl.Pessoa(nome='Teste', data_nascimento='14/04/2000', peso=80, altura=1.80, salario=entrada)
            
            # When
            resultado = funcionarioTeste.bonus_salarial()
            
            # Then
            assert resultado
    