class Usuario:

    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        #print(nome, idade,altura)

    def vddnome(self):
        print(self.nome)

    def vddidade(self):
        print(self.idade)

    def vddaltura(self):
         print(self.altura)
    
    

usuario1 = Usuario('anastacia','4', '1.10')
usuario2 = Usuario('susy','34','1.78')

usuario1.vddnome()
usuario2.vddaltura()
