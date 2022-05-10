class Pessoa:

    def __inti__(self,nome,idade):
        self.nome = nome
        self.idade = idade
    
    def fala_algo(self):
        return f'Oi meu nome é {self.nome}'