#Conversão do Sistema Binário para o Sistema Decimal
#Lucas Correia

def binario_para_decimal(num_binario):
    num_decimal = int(num_binario, 2)
    return num_decimal


num_binario = input("Digite o número binário: ")
result_decimal = binario_para_decimal(num_binario)
print("O número decimal equivalente é:", result_decimal)
