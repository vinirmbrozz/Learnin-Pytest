from pydantic import BaseModel
from datetime import date

class Pessoa(BaseModel):
    nome: str
    data_nascimento: str
    peso: float
    altura: float
    salario: float

    def idade(self):
        return date.today().year - int(self.data_nascimento.split('/')[2])
    
    def sobrenome(self):
        return self.nome.split(' ')[-1]
    
    def _socio(self):
        sobrenomes = ['Bragança', 'Windsor', 'Bourbon', 'Yamato', 'Al Saud', 'Khan', 'Tudor', 'Ptolomeu']
        return self.salario >= 100000 and self.sobrenome() in sobrenomes
    
    def decrescimo_salario(self):
        if self._socio():
            return self.salario * 0.9
        
    def bonus_salarial(self):
        valor = self.salario * 0.1
        if valor > 10000:
            raise ValueError('Salário muito alto para receber bônus.')
        return valor

    def __str__(self):
        ano = int(self.data_nascimento.split('/')[2])
        return f'Nome: {self.nome}, Idade: {date.today().year - ano}, Peso: {self.peso}, Altura: {self.altura}'