import csv


class GestorCSV:

    @staticmethod
    def generarCSV():
        diccionario_olimpiadas = {}
        with open("/home/dm2/PycharmProjects/UD2/Datos_Olimpiadas/athlete_events.csv") as file_athlete:
            reader = csv.DictReader(file_athlete)

            for linea in reader:
                for juegos in linea:
                    if juegos == "Games":
                        if not diccionario_olimpiadas.__contains__(juegos):
                            diccionario_olimpiadas.update(
                                {linea[juegos]: [linea["Year"], linea["Season"], linea["City"]]})

        with open("/home/dm2/PycharmProjects/UD2/olimpiadas.csv", "w+") as file_olimpiadas:
            writer = csv.DictWriter(file_olimpiadas, fieldnames=["Games", "Year", "Season", "City"])
            writer.writeheader()
            for key in diccionario_olimpiadas:
                year = diccionario_olimpiadas[key][0]
                season = diccionario_olimpiadas[key][1]
                city = diccionario_olimpiadas[key][2]

                writer.writerow({"Games": key, "Year": year, "Season": season, "City": city})

    @staticmethod
    def buscarDeportista(deportista):

        cont = 0

        with open("/home/dm2/PycharmProjects/UD2/Datos_Olimpiadas/athlete_events.csv") as file_athlete:
            reader = csv.DictReader(file_athlete)

            for linea in reader:
                if linea["Name"] == deportista:
                    if cont == 0:
                        print("Nombre: ", linea["Name"],
                              ", Sexo :", linea["Sex"],
                              ", Altura :", linea["Height"],
                              ", Peso: ", linea["Weight"])
                        cont += 1
                    print(linea["Games"],
                          linea["Year"],
                          linea["Season"],
                          linea["City"],
                          linea["Sport"],
                          linea["Event"])

    @staticmethod
    def buscarDeporteOlimpiada(deporte, anio, temporada):

        cont = 0
        with open("/home/dm2/PycharmProjects/UD2/Datos_Olimpiadas/athlete_events.csv") as file_athlete:
            reader = csv.DictReader(file_athlete)

            for linea in reader:
                if linea["Sport"] == deporte and linea["Year"] == anio and linea["Season"] == temporada:
                    if cont == 0:
                        print(linea["Games"],
                              linea["City"],
                              linea["Sport"])
                        cont += 1
                    print(linea["Name"],
                          linea["Event"],
                          linea["Medal"])
        if cont == 0:
            print("No se ha encontrado ningún deportista")

    @staticmethod
    def aniadirDeportista():
        with open("/home/dm2/PycharmProjects/UD2/Datos_Olimpiadas/athlete_events.csv") as file_athlete:
            fieldnames = ['ID',
                          'Name',
                          'Sex',
                          'Age',
                          'Height',
                          'Team',
                          'NOC',
                          'Games',
                          'Year',
                          'Season',
                          'City',
                          'Sport',
                          'Event',
                          'Medal']
            writer = csv.DictWriter(file_athlete, fieldnames=fieldnames)

            id = input("id")
            name = input("nombre")
            sexo = input("sexo")
            edad = input("edad")
            altura = input("altura")
            equipo = input("equipo")
            noc = input("NOC")
            juegos = input("juegos")
            anio = input("año")
            temporada = input("temporada")
            ciudad = input("ciudad")
            deporte = input("deporte")
            evento = input("evento")
            medalla = input("Medalla")

            writer.writerow({"ID": id,
                             "Name": name,
                             "Sex": sexo,
                             "Age": edad,
                             "Height": altura,
                             "Team": equipo,
                             "NOC": noc,
                             "Games": juegos,
                             "Year": anio,
                             "Season": temporada,
                             "City": ciudad,
                             "Sport": deporte,
                             "Event": evento,
                             "Medal": medalla})
