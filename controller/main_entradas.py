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

# crear escenarios
mis_escenarios = Escenarios()
donostia = Escenario('Donostia', 'Ilunbe', 'Kursaal')
bilbao = Escenario('Bilbao', 'BBK', 'Kafe Antzoki')
madrid = Escenario('Madrid', 'Bernabeu', 'Puerta del sol')
bcn = Escenario('Barcelona', 'Palau Sant Jordi', 'Camp nou')
valencia = Escenario('Valencia', 'Kokos beach', 'la castellana')

#añadirlos
mis_escenarios.add_escenario(donostia)
mis_escenarios.add_escenario(bilbao)
mis_escenarios.add_escenario(madrid)
mis_escenarios.add_escenario(bcn)
mis_escenarios.add_escenario(valencia)



# crear concierto
mis_conciertos = Concierto()

# añado artistas y sitios
concierto_donostia = Concierto()
mis_conciertos.add_escenario(donostia)

concierto_bilbao = Concierto()
mis_conciertos.add_escenario(bilbao)

concierto_madrid = Concierto()
mis_conciertos.add_escenario(madrid)

concierto_bcn = Concierto()
mis_conciertos.add_escenario(bcn)

concierto_valencia = Concierto()
mis_conciertos.add_escenario(valencia)


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

""" seleccion de la ciudad """
comprobar = False
while comprobar == False:
    mis_escenarios.print_escenarios()
    ciudadNombre = input("Seleccione lugar del concierto: " '\n')
    comprobar = mis_conciertos.comprobar_escenario(ciudadNombre)
    if comprobar == True:
        print("Ha seleccionado el lugar del concierto: " + ciudadNombre + '\n''\n')

"""seleccion del escenario"""
comprobar = False
while comprobar == False:
    mis_escenarios.print_escenarios_edificios(ciudadNombre)
    escenario = input('Seleccione escenario: ' '\n')
    comprobar = mis_conciertos.comprobar_escenario_edificios(escenario)
    if comprobar == True:
        print("Ha seleccionado el escenario: " + escenario + '\n''\n')


""" seleccion de entrada """
enc=False
tipo = ""
while not enc:
    mis_conciertos.print_zonas()
    tipo = input("Seleccione el tipo de entrada que desea: " '\n')
    print("Ha seleccionado: " + tipo + '\n')
    enc=concierto.print_precios(tipo)

print('Compra finalizada.''\n')
print('Ha seleccionado: '+artista+'\n'
'En: '+ciudadNombre+'\n''Escenario: '+escenario+'\n'+
'Zona: '+tipo+'\n'+'Precio: '+concierto.coger_precio_tipo(tipo))
