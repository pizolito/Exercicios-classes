
class bichinho:
    def __init__(self,nome,fome,saude,idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude 
        self.idade  = idade
        
    def novoNome(self,novoNome):
        self.nome  = novoNome
        
    def novaFome(self,novaFome):
        self.fome = novaFome
    
    def novaSaude(self,novaSaude):
        self.saude = novaSaude
        
    def novaIdade(self,novaIdade):
        self.idade = novaIdade
        
    def mostrar(self):
        print("O nome é:",self.nome)
        print("A fome é:",self.fome)
        print("A saude é:",self.fome)
        print("A idade é:",self.idade)
 