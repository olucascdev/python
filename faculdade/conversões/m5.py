#Conversão do Sistema Binário para o Sistema Hexadecimal
#Lucas Correia

def binario_para_hexa(num_binario):
    num_decimal = int(num_binario, 2)
    num_hexa = hex(num_decimal)[2:]
    return num_hexa.upper()
 
num_binario = input("Digite um número binário: ")
num_hexa = binario_para_hexa(num_binario)

print("O numero ", num_binario, "em Hexadecimal é: ", num_hexa)