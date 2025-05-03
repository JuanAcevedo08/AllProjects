import random

def contraseña():
    letras = ["@", "*", "#", "&", "/", "a", "c"]
    numeros = random.randint(1,100)
    pw = []
    for n in range(10):
        n = random.choice(letras)
        pw.append(n)
        n = numeros
        pw.append(n)
    print(pw)
contraseña()