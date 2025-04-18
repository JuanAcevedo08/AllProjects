import random

#Generar un numero entero aleatorio
number = random.randint(1,220)
print(number)
#Elegir colores aleatorios
colores =  ['amarillo', 'azul','rojo','naranja' ]
random_color = random.choice(colores)
print(random_color)
#Barajar una lista de cartas
cards = ['az', 'rey', 'reina', 'trebol', '10']
random.shuffle(cards)
print(cards)