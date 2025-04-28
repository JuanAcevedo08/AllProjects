import asyncio
from concesionario.motos import Motos, MotosConcesionario
from concesionario.comprador import Comprador, Concesionario_comprador
from concesionario.procesos import transaccion

async def main():

    #Creamos concesionario
    concesionario_motos = MotosConcesionario()
    concesionario_compradores = Concesionario_comprador()

    #Creamos motos
    Kawasaki = Motos(101, "Kawasaki", "H2-R", 56.000)
    Aprilia =  Motos(202, "Aprilia", "RS 660", 15.000)
    Triumph =  Motos(303, "Kawasaki", "SPEED TRIPLE 1200 RS", 36.000)
    Duke  =  Motos(404, "Kawasaki", "SuperDuke 1390", 56.000)

    #Creamos compradores
    comprador1 = Comprador(105347132, "Juanda", 17, "Juanda@gmail.com")
    comprador2 = Comprador(105347132, "Lucia", 17, "Lucia@gmail.com")

    #Agregar motos al concesionario
    concesionario_motos.agregar(Kawasaki)
    concesionario_motos.agregar(Aprilia)
    concesionario_motos.agregar(Triumph)
    concesionario_motos.agregar(Duke)

    if concesionario_motos.revisar_disponibilidad(101) == True:
        concesionario_motos.mostrar_moto(101)
        await transaccion("Juanda", 56.000)
        comprador1.comprar_moto(Kawasaki)
        concesionario_motos.eliminar(Kawasaki)
        concesionario_compradores.agregar_comprador(comprador1)

    print("Moto comprada")

    if concesionario_motos.revisar_disponibilidad(202) == True:
        concesionario_motos.mostrar_moto(202)

        await transaccion("Lucia", 15.000)

        comprador2.comprar_moto(Aprilia)
        concesionario_motos.eliminar(Kawasaki)
        concesionario_compradores.agregar_comprador(comprador2)

    concesionario_motos.mostrar_motos


if __name__ == "__main__":
    asyncio.run(main())
