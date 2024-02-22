# + adição
# - subtração
# * multiplicação
# / divisão
# ** Potencia
# // Divisão inteira
# % resto da divisão
# **0.5 raiz quadrada
# contrabarra n para pular a linha 

# Ordem de Precedencia 
# 1 - () parenteses
# 2 - ** potencia
# 3 -  *, /, //, % quem aparecer primeiro
# 4 -  + , - 

n1 = int(input("Digite um valor:"))
n2 = int(input("Digite outro numero:"))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print(f"soma: {s}")
print(f"multiplicação: {m}")
print(f"divisão: {d}")
print(f"Divisão inteira: {di}")
print(f"potencia: {e}")

