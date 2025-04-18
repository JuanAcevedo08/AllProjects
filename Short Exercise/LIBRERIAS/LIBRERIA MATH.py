import math

#Hallar el are y perimetro de un circulo
radius = 5
area = math.pi * radius**2
perimetro = 2 * math.pi * radius
print(f"El area es {area} y el perimetro es {perimetro}")

#Hayar el area de un cuadrado // Usar math nos sirve para que la constante de pi , sea mucho mas exacta y el rusltado sea mas exacto
lado = 10
area = lado * lado
#Hayar el lado de un cuadrado usando math para raiz que es sqrt
area1 = 100
lado2 = math.sqrt(area)
print(lado2)