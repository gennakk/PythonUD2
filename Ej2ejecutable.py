from Ej2 import GestorCSV

gestor = GestorCSV

opcion = 0

while opcion != 5:
    print("1. Generar fichero CSV")
    print("2. Buscar deportista")
    print("3. Buscar por deporte y olimpiada")
    print("4. Añadir deportista")
    print("5. Salir")

    opcion = int(input("Introduce opcion"))

    if opcion == 1:
        gestor.generarCSV()
    elif opcion == 2:
        gestor.buscarDeportista(input("Introduce deportista"))
    elif opcion == 3:
        gestor.buscarDeporteOlimpiada(input("Introduce deporte"), input("Introduce año"), input("Introduce olimpiada"))
    elif opcion == 4:
        gestor.aniadirDeportista()

