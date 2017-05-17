class Artista():
    def __init__(self, name):
        self.name = name

class Concierto():

    def __init__(self):
        self.artistas = []
        self.sitios = []
        self.precios = []

    def add_artista(self, artista):
        self.artistas.append(artista)

    def print_artistas(self):
        for x in self.artistas:
            return x

    def add_sitio(self, sitio):
        self.sitios.append(sitio)

    def print_sitios(self):
        for x in self.sitios:
            return x
    
    def add_precio(self, precio):
        self.precios.append(precio)

    precio = {
                "zona bronce": [35],
                "zona plata": [50],
                "zona oro": [70]
    }

    entradas1 = [
        {"id": 1, "zona":"zona bronce", "precio": 15 },
        {"id": 2, "zona":"zona plata", "precio": 30 },
        {"id": 3, "zona":"zona oro", "precio": 50 }
    ]

    def print_precios(self):
        for x in self.precio:
            for y in self.precio:
                return self.precio


class Entradas():

    def __init__(self):
        self.entradas = self

  
''' main program '''

#s = Artista("Shakira")

concierto = Concierto()
#concierto.add_artista(s)
concierto.add_sitio("Donostia")
concierto.add_sitio("Bilbo")
concierto.add_artista("Shakira")
concierto.add_artista("Jason Derulo")
concierto.add_precio("30 euros")
concierto.add_precio("50 euros")

""" seleccion del artista """
concierto.print_artistas()
artista = input("Seleccione artista: ")
print("Ha seleccionado " + artista)

""" seleccion del lugar """
concierto.print_sitios()
lugar = input("Seleccione lugar del concierto: ")
print("Ha seleccionado el lugar del concierto: " + lugar)

""" seleccion de entrada """
entradas = input("Seleccione el tipo de entrada que desea: ")
print("Ha seleccionado: " + entradas)

"""dar el precio"""
print(concierto.print_precios())

#print(concierto.sitios)

#entradas1[0]["id"]