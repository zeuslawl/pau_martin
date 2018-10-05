#!/usr/bin/python
# coding: utf8

from random import randint
import os

########################## --> Variables 

Sortir_aposta = False
Sortir_tot = False 
saldo = 100 
aposta = 0

######################## --> Nivell 2

def opcio_menys1(opcio,Sortir_aposta,Sortir_tot):
		
	if (opcio == -1):
		Sortir_aposta = True
		Sortir_tot = True
		print "Que vagi bé!!"
		
	return Sortir_aposta, Sortir_tot

def sense_saldo(saldo,Sortir_aposta,Sortir_tot): 
	
	if (saldo < 10): 
		Sortir_aposta= True
		Sortir_tot = True
		print "Tens menys de 10€, a carré"
	
	elif (saldo >= 1000):
		Sortir_aposta = True
		Sortir_tot = True
		print "Felicitats, has guanyat!!!"
		
	return Sortir_aposta, Sortir_tot
	

def control_apostes(aposta, saldo,Sortir_control):

	while Sortir_control == False: 
		if (aposta > saldo):
			print "No pots fer apostes superiors al teu saldo, atontao"
			print 
			aposta=input("Quan vols apostar? ")
			
		else: 
			if (aposta < 0):
				print "No pots apostar menys de 0, subnormal"
				print
				aposta=input("Quan vols apostar? ")
			
			else: 
				Sortir_control = True

def menu(saldo):
	
	os.system('clear')
	print "Bon dia! Que vols fer?"
	print 
	print "1 --> Jugar" 
	print 
	print "-1 --> Sortir" 
	print 
	print "Ara mateix tens", str(saldo) + " €"
	print 
	opcio=input("Que vols fer? ")
	print 
	
	return opcio

def variables():
	Sortir_menu = False
	Sortir_aposta = False
	Sortir_control = False

	return Sortir_menu, Sortir_aposta, Sortir_control

def joc():				
	
		J1pal_pal1 = randint(1,4) 
		J1pal_pal2 = randint(1,4)
		J1pal_pal3 = randint(1,4)
		J2pal_pal1 = randint(1,4)
		J2pal_pal2 = randint(1,4)
		J2pal_pal3 = randint(1,4)
		
		if (J1pal_pal1 == 1):
			J1pal_1 = "Piques"
		if (J1pal_pal1 == 2):
			J1pal_1 = "Cors"
		if (J1pal_pal1 == 3):
			J1pal_1 = "Diamants"
		if (J1pal_pal1 == 4):
			J1pal_1 = "Trèbols"
			
		if (J1pal_pal2 == 1):
			J1pal_2 = "Piques"
		if (J1pal_pal2 == 2):
			J1pal_2 = "Cors"
		if (J1pal_pal2 == 3):
			J1pal_2 = "Diamants"
		if (J1pal_pal2 == 4):
			J1pal_2 = "Trèbols"
			
		if (J1pal_pal3 == 1):
			J1pal_3 = "Piques"
		if (J1pal_pal3 == 2):
			J1pal_3 = "Cors"
		if (J1pal_pal3 == 3):
			J1pal_3 = "Diamants"
		if (J1pal_pal3 == 4):
			J1pal_3 = "Trèbols"
			
	############## Pals del J1


		if (J2pal_pal1 == 1):
			J2pal_1 = "Piques"
		if (J2pal_pal1 == 2):
			J2pal_1 = "Cors"
		if (J2pal_pal1 == 3):
			J2pal_1 = "Diamants"
		if (J2pal_pal1 == 4):
			J2pal_1 = "Trèbols"
		
		if (J2pal_pal2 == 1):
			J2pal_2 = "Piques"
		if (J2pal_pal2 == 2):
			J2pal_2 = "Cors"
		if (J2pal_pal2 == 3):
			J2pal_2 = "Diamants"
		if (J2pal_pal2 == 4):
			J2pal_2 = "Trèbols"
			
		if (J2pal_pal3 == 1):
			J2pal_3 = "Piques"
		if (J2pal_pal3 == 2):
			J2pal_3 = "Cors"
		if (J2pal_pal3 == 3):
			J2pal_3 = "Diamants"
		if (J2pal_pal3 == 4):
			J2pal_3 = "Trèbols"

	################# Pals del J2

		jugador1_carta1 = randint(2,14)
		jugador1_carta2 = randint(2,14)
		jugador1_carta3 = randint(2,14)
		jugador2_carta1 = randint(2,14)
		jugador2_carta2 = randint(2,14)
		jugador2_carta3 = randint(2,14)
		
		jugador1_numero1 = jugador1_carta1
		jugador1_numero2 = jugador1_carta2
		jugador1_numero3 = jugador1_carta3
		jugador2_numero1 = jugador2_carta1
		jugador2_numero2 = jugador2_carta2
		jugador2_numero3 = jugador2_carta3
				
		
		if (jugador1_carta1 == 11):
			jugador1_numero1 = "J"
		if (jugador1_carta1 == 12):
			jugador1_numero1 = "Q"
		if (jugador1_carta1 == 13):
			jugador1_numero1 = "K"
		if (jugador1_carta1 == 14):
			jugador1_numero1 = "As"
			
		if (jugador1_carta2 == 11):
			jugador1_numero2 = "J"
		if (jugador1_carta2 == 12):
			jugador1_numero2 = "Q"
		if (jugador1_carta2 == 13):
			jugador1_numero2 = "K"
		if (jugador1_carta2 == 14):
			jugador1_numero2 = "As"
			
			
		if (jugador1_carta3 == 11):
			jugador1_numero3 = "J"
		if (jugador1_carta3 == 12):
			jugador1_numero3 = "Q"
		if (jugador1_carta3 == 13):
			jugador1_numero3 = "K"
		if (jugador1_carta3 == 14):
			jugador1_numero3 = "As"
			
	############# Cartes del J1

		if (jugador2_carta1 == 11):
			jugador2_numero1 = "J"
		if (jugador2_carta1 == 12):
			jugador2_numero1 = "Q"
		if (jugador2_carta1 == 13):
			jugador2_numero1 = "K"
		if (jugador2_carta1 == 14):
			jugador2_numero1 = "As"
			
		if (jugador2_carta2 == 11):
			jugador2_numero2 = "J"
		if (jugador2_carta2 == 12):
			jugador2_numero2 = "Q"
		if (jugador2_carta2 == 13):
			jugador2_numero2 = "K"
		if (jugador2_carta2 == 14):
			jugador2_numero2 = "As"
			
			
		if (jugador2_carta3 == 11):
			jugador2_numero3 = "J"
		if (jugador2_carta3 == 12):
			jugador2_numero3 = "Q"
		if (jugador2_carta3 == 13):
			jugador2_numero3 = "K"
		if (jugador2_carta3 == 14):
			jugador2_numero3 = "As"
			
	################ Carta del J2

		print "Tens un", str(jugador1_numero1) + " de", J1pal_1
		print "Tens un", str(jugador1_numero2) + " de", J1pal_2
		print "Tens un", str(jugador1_numero3) + " de", J1pal_3
		print 
		
#		return jugador1_carta1, jugador1_carta2, jugador1_carta3, jugador2_carta1,jugador2_carta2,jugador1_carta3
		
	

######################## --> Nivell 1 

while (Sortir_tot == False):
	
	######## Funció que reestableix les variables
	Sortir_menu,Sortir_aposta, Sortir_control=variables()
	
	####### Funció del menú principal	
	opcio=menu(saldo)

	####### Funció de la opció -1 del menú
	Sortir_aposta,Sortir_tot=opcio_menys1(opcio,Sortir_aposta,Sortir_tot)
			
	###### Funció de l'usuari senses saldo 
	Sortir_aposta,Sortir_tot=sense_saldo(saldo,Sortir_aposta,Sortir_tot)

	###### Bucle que genera la tirada
	while (Sortir_aposta == False):
			
		joc()
		
		############### Apostes ################
		print "L'aposta mínima és de 10 €"
		print "No pots apostar més del teu saldo total"
		aposta=input("Quan vols apostar? ")
		
		##### Funció que controla l'aposta de l'usuari
		control_apostes(aposta, saldo, Sortir_control)
		
		saldo = saldo - aposta
		
							
			

				
					
				
				
				
				
				
				
				
				

	
	
