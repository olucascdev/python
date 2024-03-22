#Conversão do Sistema Decimal para o Sistema Binário
#Lucas Correia

def decimal_para_Binario(num_decimal):
    num_binario = bin(num_decimal)
    return num_binario[2:]

num_decimal = int(input("Digite um número decimal: "))
num_binario = decimal_para_Binario(num_decimal)
print("O numero ", num_decimal, "em binário é: ", num_binario)