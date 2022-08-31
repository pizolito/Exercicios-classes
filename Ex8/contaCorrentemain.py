from contaCorrente import contaCorrente
saldo = 0
nome = input("Seu nome:")
num = int(input("Seu numero:"))
saldo = int(input("Saldo:"))


c1 = contaCorrente(num,nome,saldo)
c1.mostrar()
nome = input("Digite um novo nome:")
c1.novoNome(nome)
c1.mostrar()

saque =int(input("valor saque:"))
c1.saque(saque)
c1.mostrar()

deposito =int(input("valor deposito:"))
c1.deposito(deposito)
c1.mostrar()
