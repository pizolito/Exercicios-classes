
class dados:
    def __init__(self,nome,idade,end):
        self.nome=nome
        self.idade=idade
        self.end=end

    def mostrar(self):
        print(self.end)

    def novoEnd(self,novoEnd):
        self.end = novoEnd

    def novaIdade(self,novaIdade):
        self.idade = novaIdade

    def novoNome(self,novoNome):
        self.nome = novoNome
        