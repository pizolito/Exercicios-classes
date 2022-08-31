class quadrado:
    def __init__(self,altura,largura):
        self.altura = altura
        self.largura = largura
        self.area = self.altura*self.largura
        self.perimetro = self.altura * 2 + self.largura * 2
        
    def lados(self,novaAltura,novaLargura):
        self.altura = novaAltura
        self.largura = novaLargura
        self.area = self.altura*self.largura
        self.perimetro = self.altura * 2 + self.largura * 2
        
    def mostraLados(self):
        print("A altura é:",self.altura,"A largura é:",self.largura)
        
    def mostraArea(self):
        print("A area é:",self.area,"O perimetro é:",self.perimetro)
        