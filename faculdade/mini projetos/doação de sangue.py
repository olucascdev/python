peso = float(input())
print(f"Peso: {peso}")

idade = int(input())
Da = ""

print(f"Idade: {idade}")
if idade >= 16 and idade < 18:
    Da = input()
    print(f"Documento de autorizacao: {Da}")

Bs = input().capitalize()
print(f"Boa saude: {Bs}")

dorgas = input().capitalize()
print(f"Uso de drogas injetaveis: {dorgas}")

Pd = input().capitalize()
print(f"Primeira doacao: {Pd}")
MuD = 0
Du12 = 0
if Pd == "N":
    MuD = int(input())
    print(f"Meses desde ultima doacao: {MuD}")
    Du12 = int(input())
    print(f"Doacoes nos ultimos 12 meses: {Du12}")

Grav = ""
Amame = ""
Mb = 0
sex = input().capitalize()
print(f"Sexo biologico: {sex}")
if sex == "F":
    Grav = input()
    print(f"Gravidez: {Grav}")
    Amame = input()
    print(f"Amamentando: {Amame}")
    if Amame == "S":
        Mb = int(input())
        print(f"Meses bebe: {Mb}")

impedimento = False

if peso < 50:
    print("Impedimento: abaixo do peso minimo.")
    impedimento = True
if idade < 16:
    print("Impedimento: menor de 16 anos.")
    impedimento = True
if (idade >= 16 and idade < 18) and (Da == "N"):
    print("Impedimento: menor de 18 anos, sem consentimento dos responsaveis.")
    impedimento = True
if idade > 60 and idade <= 69 and Pd == "S":
    print("Impedimento: maior de 60 anos, primeira doacao.")
    impedimento = True
if idade > 69:
    print("Impedimento: maior de 69 anos.")
    impedimento = True
if Bs == "N":
    print("Impedimento: nao esta em boa saude.")
    impedimento = True
if dorgas == "S":
    print("Impedimento: uso de drogas injetaveis.")
    impedimento = True
if Pd == "N":   
    if sex == "M":
        if MuD < 2:
            print("Impedimento: intervalo minimo entre as doacoes nao foi respeitado.")
            impedimento = True   
        if Du12 >= 4:
            print("Impedimento: numero maximo de doacoes anuais foi atingido.")
            impedimento = True
    else:
        if MuD < 3:
            print("Impedimento: intervalo minimo entre as doacoes nao foi respeitado.")
            impedimento = True
        if Du12 >= 3:
            print("Impedimento: numero maximo de doacoes anuais foi atingido.")
            impedimento = True
if sex == "F":   
    if Grav == "S":
        print("Impedimento: gravidez.")
        impedimento = True
    if Amame == "S":
        if Mb < 12:
            print("Impedimento: amamentacao.")
            impedimento = True

if not impedimento:
    print("Procure um hemocentro.")           






