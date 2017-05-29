from funciones import *


# crear artistas
mis_artistas = Artistas()
shakira = Artista('Shakira', 40)
jason_derulo = Artista('Jason Derulo', 28)
melendi = Artista('Melendi', 38)
maluma = Artista('Maluma', 23)
jennifer_lopez = Artista('Jennifer Lopez', 47)

#añadirlos
mis_artistas.add_artista(shakira)
mis_artistas.add_artista(jason_derulo)
mis_artistas.add_artista(melendi)
mis_artistas.add_artista(maluma)
mis_artistas.add_artista(jennifer_lopez)


# crear concierto
mis_conciertos = Concierto()

# añado artistas y sitios
concierto_donostia = Concierto()
mis_conciertos.add_sitio('Donostia')

concierto_bilbao = Concierto()
mis_conciertos.add_sitio('Bilbao')

concierto_madrid = Concierto()
mis_conciertos.add_sitio('Madrid')

concierto_barcelona = Concierto()
mis_conciertos.add_sitio('Barcelona')

concierto_valencia = Concierto()
mis_conciertos.add_sitio('Valencia')

#crear zonas(prueba)
#mis_zonas = Concierto()
#zona1 = Concierto()
#mis_zonas.add_zona('zona_oro')
#zona2 = Concierto()
#mis_zonas.add_zona('zona_plata')
#zona3 = Concierto()
#mis_zonas.add_zona('zona_bronce')

''' main program '''

concierto = Concierto()

""" seleccion del artista """
mis_artistas.print_artistas()
artista = input("Seleccione artista: "'\n')
print("Ha seleccionado " + artista + '\n''\n')

""" seleccion del lugar """
mis_conciertos.print_sitios()
lugar = input("Seleccione lugar del concierto: " '\n')
print("Ha seleccionado el lugar del concierto: " + lugar + '\n''\n')

""" seleccion de entrada """

mis_conciertos.print_zonas()

tipo = input("Seleccione el tipo de entrada que desea: " '\n')
print("Ha seleccionado: " + tipo + '\n''\n')

"""dar el precio"""

concierto.print_precios(tipo)
