x = int(input("Cual es tu primer numero "))
y = int(input("Cual es tu segundo numero "))

def Calcutator (x,y):
    suma = x + y
    resta = x - y
    multiplicacion = x * y
    if y != 0:
        division = x / y
    else:
        division = "Error: No se puede dividir entre 0"

    return{
        "Tu suma es :": suma,
        "Tu resta es :": resta,
        "Tu multiplicacion es :": multiplicacion,
        "Tu division es :": division
        }

Resultados = Calcutator(x,y)
for operacion, resultado in  Resultados.items():
    print(operacion, resultado)
