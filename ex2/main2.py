import re
from CLASS.BOLA.BANCO.entrada import entrada
from CLASS.BOLA.BANCO.saida import saida
from CLASS.BOLA.BANCO.relatorio import relatorio

saldo = 0
while True:
    print("Banco")
    print("1 - Entrada")
    print("2 - saida")
    print("3 - relatorio")
    print("4 - Saldo")
    print("5 - Sair")
    op = int(input("Digite a op:"))
    if op == 1:
        print("Entrada")
        E = float(input("valor:"))
        soma(E)
        print(soma)
    elif op == 2:
        print("Saida")
        S  = float(input("Valor:"))
        sub = (S - saldo)
        print(sub)
        saida(S - saldo)
    elif op == 3:
        print("Relatorio")
        print(saldo)
        relatorio(print,saldo)
    elif op == 5:
        print("cabou :(")
        break










               

