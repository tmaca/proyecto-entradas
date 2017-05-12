class Artista():
    def __init__(self, name):
        self.name = name

class Concierto():

    def __init__(self):
        self.artistas = []
        self.sitios = []

    def add_artista(self, artista):
        self.artistas.append(artista)

    def add_sitio(self, sitio):
        self.sitios.append(sitio)

    def print_sitios(self):
        for x in self.sitios:
            print(x)

''' main program '''

s = Artista("Shakira")

concierto = Concierto()
concierto.add_artista(s)
concierto.add_sitio("Donostia")
concierto.add_sitio("Bilbo")

#print(concierto.sitios)

concierto.print_sitios()