from dados import dados

nome = input("novo seu nome:")
idade =int(input("Digite sua idade:"))
end = input("Digite seu endereco:")
p1 = dados(nome,idade,end)


p1.mostrar()
novoEnd = input("digite o novo endereco:")
p1.novoEnd(novoEnd)
p1.mostrar()


novoEnd = input("digite nova idade:")
p1.novaIdade(novaIdade)
p1.mostrar()

