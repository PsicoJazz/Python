class Pessoa:
    def __init__(self, nome, idade, genero, falando=False):
        self.nome = nome
        self.idade = idade
        self.genero = genero
        self.falando = falando

    def falar(self, fofoca):
        print(f'{self.nome} está fazendo {fofoca}')
        self.falando = True

p1 = Pessoa('Daniel',32,'Masc')
p1.falar('fofoca')
print(p1)