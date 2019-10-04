from Ej3 import GestorXML

gestor = GestorXML

opcion = 0

while opcion != 4:
    print("1. Crear fichero XML de olimpiadas")
    print("2. Crear fichero XML de deportistas")
    print("3. Listado de olimpiadas")
    print("4. Salir")

    opcion = int(input("Introduce opcion"))

    if opcion == 1:
        gestor.crearXMLOlimpiadas()
    elif opcion == 2:
        gestor.crearXMLDesportistas()
    elif opcion == 3:
        gestor.crearListadoOlimpiadas()
