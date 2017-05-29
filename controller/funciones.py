class Artista():
    def __init__(self, name, edad):
        self.name = name
        self.edad = edad
    def __str__(self):
        return self.name

class Artistas():
    def __init__(self):
        self.artistas = []
    
    def add_artista(self,artista):
        self.artistas.append(artista)
    
    def print_artistas(self):
        for x in self.artistas:
            print(x)

class Concierto():

    def __init__(self):
        self.artistas = []
        self.sitios = []
        self.precio = {}
        self.entradas = []
        self.zonas = []

    def __str__(self):
        return self.sitios    

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

    def print_sitios_artista(self, Artista):
        for i in self.artistas:
            if i == Artista:
                sitios_artista = []
                sitios_artista.append(self)

    def add_zona(self, zona):
        self.zonas.append(zona)

    def print_zonas(self):
        for x in self.zonas:
            print(x)
    
    def __str__(self):
        return self.zonas

    def print_precios(self, tipo):
        print(self.precio[tipo])
    

class Conciertos():
    def __init__(self):
        self.conciertos = []
    
    def add_artista(self,concierto):
        self.conciertos.append(concierto)


class Entrada():
    def __init__(self, concierto, tipo):
        self.concierto = concierto
        self.tipo = tipo

