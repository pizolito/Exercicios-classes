class contaCorrente:
    def __init__(self,numero,nome,saldo):
        self.numero = numero
        self.nome = nome
        self.saldo = saldo
        
    def novoNome(self,novoNome):
        self.nome = novoNome
        
    def deposito(self,deposito):
        self.saldo += deposito
       
       
    def saque(self,saque): 
        self.saldo -= saque
        
    def mostrar(self):
        print("seu nome:",self.nome,"numero",self.numero,"saldo",self.saldo)
        