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
        self.escenarios = []
        self.precio = {
                "zona_bronce": 35,
                "zona_plata": 50,
                "zona_oro": 70
        }
        self.entradas = []
        self.zonas = []

    def add_artista(self, artista):
        self.artistas.append(artista)

    def add_escenario(self, escenario):
        self.escenarios.append(escenario)


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
        
    def comprobar_escenario(self, ciudadNombre):
        for x in self.escenarios:
            if ciudadNombre == x.ciudadNombre:
                return True
        print('No hay conciertos en esa ciudad')
        return False
    
    def comprobar_escenario_edificios(self, escenario):
        for x in self.escenarios:
            if x.escenarioNombre1 == escenario or x.escenarioNombre2 == escenario:
                return True
        print('No hay conciertos para ese escenario')
        return False

class Escenario():
    def __init__(self, ciudadNombre, escenarioNombre1, escenarioNombre2):
        self.ciudadNombre= ciudadNombre
        self.escenarioNombre1 = escenarioNombre1
        self.escenarioNombre2 = escenarioNombre2

    def __str__(self):
        return self.ciudadNombre

class Escenarios():
    def __init__(self):
        self.escenarios = []
    
    def add_escenario(self,escenario):
        self.escenarios.append(escenario)
    
    def print_escenarios(self):
        for x in self.escenarios:
            print(x)
        
    def print_escenarios_edificios(self, ciudadNombre):
        for x in self.escenarios:
            if x.ciudadNombre == ciudadNombre:
                print(x.escenarioNombre1)
                print(x.escenarioNombre2)

    def comprobar_escenario(self, escenario):
        for x in self.escenarios:
            if escenario == x.ciudadNombre:
                return True
        print('No hay conciertos para esa ciudad')
        return False
    
    def comprobar_escenario_edificios(self, escenario):
        for x in self.escenarios:
            if x.escenarioNombre1 == escenario or x.escenarioNombre2 == escenario:
                return True
        print('No hay conciertos para ese escenario')
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
