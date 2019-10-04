import os


class GestorFich:

    @staticmethod
    def crearDirectorio():
        ruta = input("Introduce la ruta")
        nomb_dir = input("Introduce el nombre de fichero")

        os.mkdir(ruta + "/" + nomb_dir)

    @staticmethod
    def listarDirectorio():

        nomb_dir = input("Introduce la ruta")

        lista = os.listdir(nomb_dir)

        for nombre in lista:
            if nombre.__contains__("."):
                print(nombre + ", Archivo")
            else:
                print(nombre + ", Directorio")

    @staticmethod
    def copiarArchivo():

        rutaoriginal = input("Introduce la ruta original")

        rutadestino = input("Introduce la ruta de destino")

        os.popen("cp " + rutaoriginal + " " + rutadestino)

    @staticmethod
    def moverArchivo():

        rutaoriginal = input("Introduce la ruta original")

        rutadestino = input("Introduce la ruta de destino")

        os.popen("mv " + rutaoriginal + " " + rutadestino)

    @staticmethod
    def borrar():

        ruta = input("Introduce la ruta")

        if ruta.__contains__("."):
            os.remove(ruta)
        else:
            try:
                os.rmdir(ruta)
            except Exception:
                print("El directorio no está vacío.")
