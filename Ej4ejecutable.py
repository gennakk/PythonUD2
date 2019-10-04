from Ej4 import GestorBinario


gestor = GestorBinario

opcion = 0

while opcion != 5:
    print("1. Generar fichero serializable olimpiadas")
    print("2. Añadir edición olímpica")
    print("3. Buscar olimpiadas por sede")
    print("4. Eliminar edición olímpica")
    print("5. Salir")

    opcion = int(input("Introduce opcion"))

    if opcion == 1:
        gestor.crearFichSerializable()
    elif opcion == 2:
        gestor.aniadirEdicion()
    elif opcion == 3:
        gestor.buscarPorSede(input("Introduce sede: "))
    elif opcion == 4:
        gestor.eliminarEdicion(input("Introduce año"), input("Introduce temporada"))
