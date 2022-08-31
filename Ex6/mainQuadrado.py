from quadrado import quadrado

alt = float(input("Digite a altura:"))
larg = float(input("Digite a largura:"))

lados = quadrado(alt,larg)

lados.mostraLados()
lados.mostraArea()

nalt = float(input("Digite a  nova altura:"))
nlarg = float(input("Digite a  nova largura:"))
lados.lados(nalt,nlarg)

lados.mostraLados()
lados.mostraArea()



'''

alt.mostraAtura()
alt1= float(input("Digite a nova altura:"))
alt1.mostraAltura()

larg = float(input("Digite a largura::"))
larg.mostraLargura()
larg1 = float(input("Digite a novaLargura:"))
larg1.mostraLargura()

area = alt * larg
area.mostraArea()
area1 = alt1 * larg1
area1.mostraArea()

'''