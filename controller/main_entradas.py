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

''' main program '''

concierto = Concierto()

""" seleccion del artista """
comprobar = False
while comprobar == False:
    mis_artistas.print_artistas()
    artista = input("Seleccione artista: "'\n')
    comprobar = mis_artistas.comprobar_artista(artista)
    if comprobar == True:
        print("Ha seleccionado " + artista + '\n''\n')

""" seleccion del lugar """
comprobar = False
while comprobar == False:
    mis_conciertos.print_sitios()
    sitio = input("Seleccione lugar del concierto: " '\n')
    comprobar = mis_conciertos.comprobar_sitio(sitio)
    if comprobar == True:
        print("Ha seleccionado el lugar del concierto: " + sitio + '\n''\n')


""" seleccion de entrada """
enc=False
tipo = ""
while not enc:
    mis_conciertos.print_zonas()
    tipo = input("Seleccione el tipo de entrada que desea: " '\n')
    print("Ha seleccionado: " + tipo + '\n')
    enc=concierto.print_precios(tipo)

print('Compra finalizada.')
print('Ha seleccionado: '+artista+'\n''En: '+sitio+'\n'+'Zona: '+tipo+'\n'+'Precio: '+concierto.coger_precio_tipo(tipo))