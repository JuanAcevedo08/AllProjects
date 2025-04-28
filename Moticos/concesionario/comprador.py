class Comprador:
    def __init__(self, id: int,name: str, age: int, email: str ):
        self.name = name
        self.age = age 
        self.email = email
        self.id = id
        self.motos = []

    def comprar_moto(self, moto):
        self.motos.append(moto)
        print("Moto comprada")


class Concesionario_comprador:
    def __init__(self):
        self.compradores = {}

    def agregar_comprador(self, comprador: object):
        self.compradores[comprador.id] = comprador
        print(f"Comprador {comprador.name} fue agregado")
    
    def consultar_informacion(self, comprador_id: int):
        if comprador_id in self.compradores.keys():
            for k, v in self.compradores.items():
                if k == comprador_id:
                    print(f"Informacion del comprador: Nombre: {v.name} Edad: {v.age} Email: {v.email}")
                    return None
                print("No encontrado")
        else:
            print("ID no valido ")


