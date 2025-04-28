import asyncio
import random
import time

async def transaccion(name: str, cantidad: int):
    print("Procesando compra...")
    time.sleep(1)
    print(f"Accediendo a cuenta de {name} ...")
    time.sleep(2)
    print(f"Cantidad a pagar {cantidad}")
    await asyncio.sleep(random.randint(1,3))
    print("Transaccion Realizada con exito")

async def agregar_motos(moto):
    print("Agregando motos...")
    await asyncio.sleep(random.randint(1,3))
    print("Motos agregadas")
    