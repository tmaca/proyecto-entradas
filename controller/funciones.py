class Artista():
    def init(self, name, edad):
        self.name = name

class Concierto():

    def __init__(self):
        self.artistas = []
        self.sitios = []
        self.precio = {}
        self.entradas = []

    def add_artista(self, artista):
        self.artistas.append(artista)

    def print_artistas(self):
        for x in self.artistas:
            print(x)

    def add_sitio(self, sitio):
        self.sitios.append(sitio)

    def print_sitios(self):
        for x in self.sitios:
            print(x)

    def print_zonas(self):
        for x in self.precio:
            print(x)

    def print_precios(self, tipo):
        print(self.precio[tipo])

class Entradas():

    def __init__(self, concierto, tipo):
        self.concierto = concierto
        self.tipo = tipo
