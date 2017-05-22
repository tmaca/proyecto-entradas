from funciones import *

# crear artistas
mis_artistas = Artistas()
shakira = Artista('Shakira', 40)
Jason_Derulo = Artista('Jason Derulo', 28)

'''
{
                "zona bronce": 35,
                "zona plata": 50,
                "zona oro": 70
        }
'''

# crear concierto
conciertos = []
concierto_donostia = Concierto()
concierto_donostia.add_artista(shakira)
concierto_donostia.print_artistas()

''' main program '''

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