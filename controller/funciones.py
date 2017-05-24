class Artista():
    def __init__(self, name, edad):
        self.name = name
      #  self.edad = edad

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

class Conciertos():
    def __init__(self):
        self.conciertos = []
    
    def add_artista(self,concierto):
        self.conciertos.append(concierto)

    def find_artista(self):
        #buscar en self.conciertos si existe
        #for
        pass

class Artistas():
    def __init__(self):
        self.artistas = []
    
    def add_artista(self,artista):
        self.artistas.append(artista)

    def find_artista(self):
        #buscar en self.artistas si existe
        #for
        pass
        
    #def print_art(self):
     #   for x in self.artistas:
      #      print(x)

class Entradas():

    def __init__(self, concierto, tipo):
        self.concierto = concierto
        self.tipo = tipo
