import os
from CLASS.BOLA.CALCULADORAA.soma import soma
from CLASS.BOLA.CALCULADORAA.sub import sub
from CLASS.BOLA.CALCULADORAA.mult import mult
from CLASS.BOLA.CALCULADORAA.divi import divi


print("calculadora")
print("1 - soma")
print("2 - sub")
print("3 - mult")
print("4 - divi")
print("5 - sair")
op = int(input("Digite a opcao:"))
if op == 1:
    print("Menu Soma")
    a = int(input("Digite o valor 1:"))
    b = int(input("Digite o valor 2:"))
    soma(a,b)
    os.system("pause")
elif op == 2:
    print("Menu sub")
    a = int(input("Digite o valor 1:"))
    b = int(input("Digite o valor 2:"))
    sub(a,b)
    os.system("pause")
elif op == 3:
    print("Menu mult")
    a = int(input("Digite o valor 1:"))
    b = int(input("Digite o valor 2:"))
    mult(a,b)
    os.system("pause")
elif op == 4:
    print("Menu divi")
    a = int(input("Digite o valor 1:"))
    b = int(input("Digite o valor 2:"))
    divi(a,b)
    os.system("pause")


