p_agua = 0
p_terra = 0
p_fogo = 0
p_ar = 0
element = input()

while element != "FIM":
    p = int(input())

    if element == "AGUA":
        p_agua += p
        p_fogo -= p/2
        if p_fogo < 0:
            p_fogo = 0
            
    if element == "TERRA":
        p_terra += p 
        p_ar -= p/2
        if p_ar < 0:
             p_ar = 0
        
    if element == "FOGO":
        p_fogo += p
        p_agua -= p/2
        if p_agua < 0:
            p_agua = 0
        
    if element == "AR":
        p_ar += p
        p_terra -= p/2
        if p_terra < 0:
            p_terra = 0
     
    element = input()

print("Pontuacao Final")
print(f"Agua: {p_agua:.1f}")
print(f"Terra: {p_terra:.1f}")
print(f"Fogo: {p_fogo:.1f}")
print(f"Ar: {p_ar:.1f}")

if (p_agua > 0) and (p_terra > 0) and (p_fogo > 0) and (p_ar > 0):
    print("Treinamento realizado com sucesso.")
else:
    print("Realize mais treinamentos.")