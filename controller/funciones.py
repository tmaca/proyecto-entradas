class Artista():
    def init(self, name):
        self.name = name

class Concierto():

    def __init__(self):
        self.artistas = ['Shakira', 'Jason Derulo', 'Rihanna', 'Beyoncé']
        self.sitios = ['Bilbo', 'Barcelona', 'Madrid', 'Valencia', 'Málaga']
        self.precio = {
                "zona bronce": 35,
                "zona plata": 50,
                "zona oro": 70
        }
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

''' main program '''

#s = Artista("Shakira")

concierto = Concierto()

""" seleccion del artista """
concierto.print_artistas()
artista = input("Seleccione artista: "'\n')
print("Ha seleccionado " + artista + '\n')

""" seleccion del lugar """
concierto.print_sitios()
lugar = input("Seleccione lugar del concierto: " '\n')
print("Ha seleccionado el lugar del concierto: " + lugar + '\n')

""" seleccion de entrada """
concierto.print_zonas()
tipo = input("Seleccione el tipo de entrada que desea: " '\n')
print("Ha seleccionado: " + tipo + '\n')

"""dar el precio"""
concierto.print_precios(tipo)

#print(concierto.sitios)

#entradas1[0]["id"]