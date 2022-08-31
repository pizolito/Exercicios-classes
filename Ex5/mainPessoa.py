from pessoa import Pessoa

n  = input("Seu nome:")
id1= int(input("Sua idade:"))
pes1 = float(input("Seu peso:"))
alt1 = float(input("Sua altura:"))

carac = Pessoa(n,id1,pes1,alt1)

carac.mostrar()

id1= int(input("Sua idade:"))
pes2= float(input("seu novo peso:"))
alt2 = float(input("Sua nova altura:"))

carac.mostrar()

