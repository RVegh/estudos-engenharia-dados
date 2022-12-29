class Pessoa:
    
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade
        
    def cadastro_pessoa(self):
        pessoas = []
        pessoas.append(Pessoa())
        print(pessoas)

pessoa_1 = Pessoa('Ricardo', 25)
print(pessoa_1)
print(pessoa_1.cadastro_pessoa)