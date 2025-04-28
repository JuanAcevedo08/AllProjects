import time
import random

class Motos:
    def __init__(self, moto_id: int,marca: str, modelo: str, precio: float):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
        self.moto_id = moto_id
        self.disponibilidad = True     

class MotosConcesionario:
    def __init__(self):
        self.motos = {}

    def agregar(self, moto: object):
        self.motos[moto.moto_id] = moto
        print("Agregando moto...")
        time.sleep(random.randint(1,3))
        print(f"Moto agregada al concesionario {moto.modelo}")

    def eliminar(self, moto: object):
        if moto.moto_id in self.motos:
            del self.motos[moto.moto_id]
            print("Elminando moto")
            time.sleep(random.randint(1,3))
            print(f"Moto {moto.marca} {moto.modelo} eliminada , con exito")
            return 
        print("Moto no encontrada")

    def mostrar_motos(self):
        for moto in self.motos.values():
            print(f"Motos: - Marca: {moto.marca}  Modelo: {moto.modelo} Precio: {moto.precio}")
    
    def revisar_disponibilidad(self, moto_id: int) -> bool:
        print("Buscando moto...")
        time.sleep(1.5)
        for i in self.motos.keys():
            if i == moto_id:
                print(f"Moto disponible. Buscando informacion...")
                return True
            else:
                print("Moto no dispónible")
                return False
    
    def mostrar_moto(self, moto_id:object):
        print("Mostrando moto...")
        time.sleep(2)
        for k, v in self.motos.items():
            if k == moto_id:
                print(f"Marca: {v.marca} Modelo: {v.modelo} Precio: {v.precio}")
            

            

moto1 = Motos(1,"Susuki", "GSXR-R 1000R", 40.000)
#moto2 = Motos(2,"kawasaki", "Z900", 43.000)
#concesionario = MotosConcesionario()
#concesionario.agregar(moto1)
#concesionario.agregar(moto2)
#concesionario.mostrar_motos()
#concesionario.revisar_disponibilidad(2)
        