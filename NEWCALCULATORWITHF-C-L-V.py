user = input("Cual es tu usuario? ")
def suma(a,b):
    return a+b

def resta(a,b):
    return a-b

def multiplicacion(a,b):
    return a*b

def division(a,b):
    return a/b

def calculator():
    print(f"Bienvenido al sistema de calculadora user {user}")
    while True:
        print("Opciones del 1 al 5")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicacion")
        print("4. Division")
        print("5. Salir")

        opciones = input("Cual es tu opcion? (1,2,3,4,5) : ")

        if opciones == "5":
            print("Saliste de la computadora")
            break
        if opciones in ["1","2","3","4"]:
            Numero1 = float(input("Ingrese Primer Numero: "))
            Numero2 = float(input("Ingrese Segundo Numero: "))
            
            if opciones == "1":
                print("🔥La suma es: ", suma(Numero1,Numero2))
            elif opciones == "2":
                print("🔥 resta es: ", resta(Numero1,Numero2))
            elif opciones == "3":
                print("🔥 multiplicacion es: ", multiplicacion(Numero1,Numero2))
            elif opciones == "4":
                print("🔥 Division es: ", division(Numero1,Numero2))
        else:
            print("😭 Ese Valor No Esta Acá")
         
calculator()