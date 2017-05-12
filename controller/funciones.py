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
            print(x)

    def add_sitio(self, sitio):
        self.sitios.append(sitio)

    def print_sitios(self):
        for x in self.sitios:
            print(x)
    
    def add_precio(self, precio):
        self.precios.append(precio)

    def print_precios(self):
        for x in self.precios:
            print(x)

    

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

#print(concierto.sitios)
""" seleccion del artista """
concierto.print_artistas()
artista = input("Seleccione artista: ")
print("Ha seleccionado " + artista)

""" seleccion del lugar """
concierto.print_sitios()
lugar = input("Seleccione lugar del concierto: ")
print("Ha seleccionado el lugar del concierto: " + lugar)

""" seleccion de entrada """
concierto.print_precios()
entradas = input("Seleccione el tipo de entrada que desea: ")
print("Ha seleccionado: " + entradas)