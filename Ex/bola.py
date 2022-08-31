
class bola:
    def __init__(self,cor,circuferencia,material):
        self.cor = cor
        self.circuferencia = circuferencia
        self.material = material

    def trocaCor(self,novaCor):
        self.cor = novaCor
    
    def mostraCor(self):
        print("A cor é:",self.cor)
    
    def novaCircuferencia(self,novaCircuferencia):
        self.circuferencia = novaCircuferencia
        
    def mostraCircuferencia(self):
        print("A circuferencia é:",self.circuferencia)
        
    def novoMaterial(self,novoMaterial):
        self.material = novoMaterial
        
    def mostraMaterial(self):
        print("O material é:",self.material)
        