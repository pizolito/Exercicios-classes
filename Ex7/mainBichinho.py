from bichinho import bichinho

nome  = input("nome:")
fome = int(input("qual nível de fome:"))
saude = int(input("Nivel de saude:"))
idade  = int(input("qual a idade:"))

bixo = bichinho(nome,fome,saude,idade)

soma  = (fome + saude)/2
if soma <=5:
    print("Mal Humor")
elif soma >5:
    print("Bom humor")
    

bixo.mostrar()



Nnome  = input("novo nome:")
bixo.novoNome(Nnome)
    
Nfome = int(input("qual nível de fome:"))
bixo.novaFome(Nfome)
        
Nsaude = int(input("Nivel de saude:"))
bixo.novaSaude(Nsaude)
        
Nidade  = int(input("qual a idade:"))
bixo.novaIdade(Nidade)
        

Nbixo = bichinho(Nnome,Nfome,Nsaude,Nidade)

Nsoma  = (Nfome + Nsaude)/2
if Nsoma <=5:
    print("Mal Humor")
elif Nsoma >5:
    print("Bom humor")
    

Nbixo.mostrar()



