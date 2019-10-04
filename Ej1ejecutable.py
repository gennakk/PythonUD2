from Ej1 import GestorFich

gestor = GestorFich

opcion=0

while opcion != 6:
    print("1. Crear directorio")
    print("2. Listar directorio")
    print("3. Copiar archivo")
    print("4. Mover archivo")
    print("5. Eliminar archivo/directorio")
    print("6. Salir")

    opcion = int(input("Introduce opcion"))

    if opcion == 1:
        gestor.crearDirectorio()
    elif opcion == 2:
        gestor.listarDirectorio()
    elif opcion == 3:
        gestor.copiarArchivo()
    elif opcion == 4:
        gestor.moverArchivo()
    elif opcion == 5:
        gestor.borrar()




