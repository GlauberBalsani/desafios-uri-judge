sami = input().split()
A = float(sami[0])
B = float(sami[1])
C = float(sami[2])

area_triangulo = (A*C)/2
area_circulo = (3.14159*C*C)
area_trapezio = (A+B)*C/2
area_quadrado = (B*B)
area_retangulo = (A*B)

print(f"TRIANGULO: {area_triangulo:.3f}\nCIRCULO: {area_circulo:.3f}\nTRAPEZIO: {area_trapezio:.3f}\nQUADRADO: {area_quadrado:.3f}\nRETANGULO: {area_retangulo:.3f}")
