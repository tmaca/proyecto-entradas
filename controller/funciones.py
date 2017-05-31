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

    def comprobar_artista(self, artista):
        for x in self.artistas:
            if artista == x.name:
                return True
        print('No hay conciertos para ese artista')
        return False

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
        self.zonas = []

    def __str__(self):
        return self.sitios    

    def add_artista(self, artista):
        self.artistas.append(artista)

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
            if titulo == tipo:
                print(titulo + ": " + str(precio))
                return True
        print('No existe esa zona')        
        return False
    
    def coger_precio_tipo(self,tipo):
        for titulo, precio in self.precio.items():
            if titulo == tipo:
                return str(precio)
        
    def comprobar_sitio(self, sitio):
        for x in self.sitios:
            if sitio == x:
                return True
        print('No hay conciertos en esa ciudad')
        return False
            

class Conciertos():
    def __init__(self):
        self.conciertos = []
    
    def add_artista(self,concierto):
        self.conciertos.append(concierto)


class Entrada():
    def __init__(self, concierto, tipo):
        self.concierto = concierto
        self.tipo = tipo