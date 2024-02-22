a = int(input())
b = int(input())
c = int(input())

if a >= b and a >= c: 
    hip = a
    catb = b
    catc = c
elif b >= a and b >= c:
    hip = b 
    catb = a 
    catc = c
elif c >= a and c >= b:
    hip = c
    catb = a 
    catc = b


if a <= 0 or b <= 0 or c <= 0 :
    print("Valores invalidos.")
elif a >= b + c or b >= a + c or c >= a + b:
    print("Valores nao podem formar um triangulo.")
else:

    if a == b == c:
        print("Triangulo equilatero.")
    elif a == b or b == c or a == c:
        print("Triangulo isosceles.")
    elif a != b and b != c and a != c or (a != b != c):
        print("Triangulo escaleno.")
    
    if hip**2 < (catb**2) + (catc**2) or hip**2 < (catb**2) + (catc**2) or hip**2 < (catb**2) + (catc**2):
        print("Triangulo acutangulo.")
    elif hip**2 == (catb**2) + (catc**2) or hip**2 == (catb**2) + (catc**2) or hip**2 == (catb**2) + (catc**2):
        print("Triangulo retangulo.")
    elif hip**2 > (catb**2) + (catc**2) or hip**2 > (catb**2) + (catc**2) or hip**2 > (catb**2) + (catc**2):
        print("Triangulo obtusangulo.")