#Conversão do Sistema Decimal Fracionário para o Sistema Binário
#Lucas Correia

from decimal import Decimal

def decimalf_para_binario(num_decimal):
    inteiro = int(num_decimal)
    fracionaria = num_decimal - inteiro
    
    inteira_bin = bin(inteiro)[2:]

    fracionaria_bin = ""

    while fracionaria != 0:
        fracionaria *= 2
        fracionaria_inteira = int(fracionaria)
        fracionaria_bin += str(fracionaria_inteira)
        fracionaria -= fracionaria_inteira

    num_bin = inteira_bin
    if fracionaria_bin:
        num_bin += "." + fracionaria_bin
    
    return num_bin

 
num_decimal = Decimal(input("Digite um numero decimal fracionario: "))
num_bin = decimalf_para_binario(num_decimal)
print("O numero", num_decimal, "em binário é", num_bin)