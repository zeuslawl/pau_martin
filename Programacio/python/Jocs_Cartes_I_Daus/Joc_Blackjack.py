#!/usr/bin/python
# coding: utf8

################# Import ##############

import random
import os 

################# Variables ###########
 
opcio = ""
Sortir_menu = False
Sortir_Fase2 = False
Sortir_joc = False
Sortir_banca = False
Saldo = 100


################# Llibreries ##########

numero=[2,3,4,5,6,7,8,9,10,10,10,11]

pal=[1,2,3,4]

################# Nivell 1 ############

##### Menu de quan torna a treure una carta

def menu_Fase2():
	print "Que vols fer? "
	print 
	print "1 --> Treure carta"
	print 
	print "0 --> Plantar-se"
	print 
	opcio_Fase2=raw_input('Que vols fer ara? ')
	return opcio_Fase2


#Aquest és el menú que apareix només veure'l

def menu():
	
	os.system('clear')
	print "BENVINGUT!!"
	print "Vols fer una partideta al BLACKJACK? "
	print 
	print "1 --> Jugar" 
	print 
	print "0 --> Sortir" 
	print 
	opcio=raw_input("Que vols fer? ")	
	
	return opcio
	
# Cartes del Jugador 
def generar_carta_jugador(): 

	numero_jugador=random.choice(numero)
	pal_jugador=random.choice(pal)
	numero_jugador1 = numero_jugador
	
	
	#El nom dels pals
	if (pal_jugador == 1):
		pal_jugador = "Diamants"
	if (pal_jugador == 2):
		pal_jugador = "Cors"
	if (pal_jugador == 3):
		pal_jugador = "Trébols"
	if (pal_jugador == 4):
		pal_jugador = "Piques"
		
	#El nom dels numeros
	if numero_jugador == numero[8]:
		numero_jugador1 = "J"
	if numero_jugador == numero[9]:
		numero_jugador1 = "Q"
	if numero_jugador == numero[10]:
		numero_jugador1 = "K"
	if numero_jugador == numero[11]:
		numero_jugador1 = "A"
		
	print "Tens un ", str(numero_jugador1) + " de ", pal_jugador
	
	return pal_jugador, numero_jugador

				
# Cartes de la banca
def generar_carta_banca(): 

	
	numero_banca=random.choice(numero)
	pal_banca=random.choice(pal)
	numero_banca2 = numero_banca

#### El nom dels pals
	if (pal_banca == 1):
		pal_banca = "Diamants"
	if (pal_banca == 2):
		pal_banca = "Cors"
	if (pal_banca == 3):
		pal_banca = "Trébols"
	if (pal_banca == 4):
		pal_banca = "Piques"
		
#### El nom dels numeros
	if numero_banca == numero[8]:
		numero_banca2 = "J"
	if numero_banca == numero[9]:
		numero_banca2 = "Q"
	if numero_banca == numero[10]:
		numero_banca2 = "K"
	if numero_banca == numero[11]:
		numero_banca2 = "A"

#### Mostrem el que te el jugador

	print "Tens un ", str(numero_banca2) + " de ", pal_banca

	return pal_banca, numero_banca

#################### Joc #######################

# Aquest mostra el menú

opcio=menu()

#Aquest es per a sortir del programa
if opcio == "0": 
	Sortir_joc = True
	print "Que vagi bé!"
	
# Comença a jugar

while (Sortir_joc == False):
	
#### Genera la tirada del jugador 1
	pal_jugador,numero_jugador=generar_carta_jugador()
	carta1 = numero_jugador

#### Genera un menú per a treure més cartes o plantar-se.
	opcio_Fase2=menu_Fase2()
	
#### Per si es vol plantar, no entrar al bucle de mes de 2 cartes
	if opcio_Fase2 == "0":
		Sortir_Fase2 = True
	
#### Bucle per treure més d'una carta
	while (Sortir_Fase2 == False):
				
		if opcio_Fase2 == "1": 
			
#### Genera més cartes i ensenya el valor
			
			pal_jugador,numero_jugador=generar_carta_jugador()
			carta1 = carta1 + numero_jugador
			
			print 
			print "Tens un valor total de", str(carta1)
			print 
			
#### Si es passa el fot fora	
			if carta1 > 21:
				print "No pots passar de 21... Has perdut."
				Sortir_Fase2 = True
				Sortir_joc = True
				
			if Sortir_Fase2 == False:
				opcio_Fase2=menu_Fase2()
		else: 
			if opcio_Fase2 == "0":
				Sortir_Fase2 = True
		
########### Genera la tirada de la banca
			
	pal_banca,numero_banca=generar_carta_banca()
	carta2 = numero_banca
	
#### Per a que la banca tregui més de 15. Més ajustat
	
	while (Sortir_banca == False):
		if carta2 < 15: 
			pal_banca,numero_banca=generar_carta_banca()
			carta2 = carta2 + numero_banca
		else: 
			Sortir_banca = True
#### Si el jugador no s'ha passat evalua les opcions

	if carta1 < 22:
		print "Tens un valor total de", str(carta1)
		print
		print "La banca te un valor total de", str(carta2)
		print
		print "per tant... "
		print 

#### Evalua les diferents situacions... Empats i victories
#### Ho fa comparant la suma de totes les cartes tretes.
		if (carta1 == carta2):
			if carta1 == 21 and carta2 == 21: 
				print "Doble BLACKJACK!!!! "
				
			else: 
				print "Empat de valors!!!"
			
		else: 
			if (carta1 > carta2):
				if carta1 == 21:
					print "BLACKJACK!!!!!"
					print "Tu guanyes!!!!"
					
				else:
					print "Has guanyat!!!!"
				
			else: 
				if carta2 > 21:
					print "La banca s'ha passat! Tu guanyes!!"
					
				else:
					if carta2 == 21:
						print "BLACKJACK DE LA BANCA!!!!"
						
					else: 
						print "Has perdut..."
						
		Sortir_joc = True		
