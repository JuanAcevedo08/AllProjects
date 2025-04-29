import random

opcions = ['Ganaste una moneda', 'Ganaste un cupon', 'Ganaste un chocolote', 'No ganaste nada ', 'Ganaste una mosca']
oselect = random.choice(opcions)
probability = round(random.random() * 100, 2) #random.random = Me da un numero 0 a 1 pero en este caso sin el 1 ntonces
#me daria un 0 con decimales , lo multiplico x 100 y random lo redondea y el 2 genera  dos decimales al final

print(f"Resultado: {oselect} (Probabilidad: {probability}%)")