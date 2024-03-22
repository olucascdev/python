#Conversão do Sistema Binários Fracionario para o Sistema Decimal
#Lucas Correia
def binariof_para_decimal(num_bin):
    partes = num_bin.split(".")
    inteiro = int(partes[0],2)

    fracionaria = 0
    if len(partes) > 1:
        fracionaria_str = partes[1]
        for i in range(len(fracionaria_str)):
            fracionaria += int(fracionaria_str[i]) * (2  **-( i + 1 ))

        return inteiro + fracionaria
    
num_bin = input("Digite um número binário fracionário: ")
num_decimal = binariof_para_decimal(num_bin)
print("O número", num_bin, "em decimal é: ", num_decimal)

