
class tv:
    def __init__(self,canal,volume):
        self.canal = canal
        self.volume = volume
    def volume (self,novoVolume):
        self.volume  = novoVolume
        
    def canal (self,novoCanal):
        self.canal = novoCanal
    
    def mostrar(self):
        print("canal:",self.canal,"Volume:",self.volume)