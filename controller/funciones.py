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
        self.precio = {
                "zona_bronce": 35,
                "zona_plata": 50,
                "zona_oro": 70
        }
        self.entradas = []
        

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

    def print_zonas(self):
        for x in self.precio:
            print(x)

    def print_precios(self, tipo):
        for titulo, precio in self.precio.items():
            print(titulo + ": " + str(precio))
    

class Conciertos():
    def __init__(self):
        self.conciertos = []
    
    def add_artista(self,concierto):
        self.conciertos.append(concierto)


class Entrada():
    def __init__(self, concierto, tipo):
        self.concierto = concierto
        self.tipo = tipo