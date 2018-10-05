#!/usr/bin/python
# coding: utf8

############################################################################
#                        QUE HACE?
# Apostes
############################################################################


############################################################################
#                        IMPORT
############################################################################
from random import randint
import os

############################################################################
#                               NIVEL 2
############################################################################



def joc(saldo,jugador1,jugador2):
	
	Sortir_carta = False
	J1pal = randint(1,4) 
	J2pal = randint(1,4)

	if (J1pal == 1):
		pal1 = "Piques"
	if (J1pal == 2):
		pal1 = "Cors"
	if (J1pal == 3):
		pal1 = "Diamants"
	if (J1pal == 4):
		pal1 = "Trèbols"

	jugador1 = randint(2,14)

	jugador2 = randint(2,14)
	
	numero1 = jugador1
	if (jugador1 == 11):
		numero1 = "J"
	if (jugador1 == 12):
		numero1 = "Q"
	if (jugador1 == 13):
		numero1 = "K"
	if (jugador1 == 14):
		numero1 = "As"
		
	print "Tu tens un", str(numero1) + " de", pal1


	while (Sortir_carta == False):
		
		if (jugador1 == jugador2 and J1pal == J2pal):
			jugador2 = randint(2,14)
			J2pal = randint(1,4)
			
		if not(jugador1 == jugador2 and J1pal == J2pal):
			Sortir_carta = True
	
	if (J2pal == 1):
		pal2 = "Piques"
	if (J2pal == 2):
		pal2 = "Cors"
	if (J2pal == 3):
		pal2 = "Diamants"
	if (J2pal == 4):
		pal2 = "Trèbols"
				
	numero2 = jugador2
	if (jugador2 == 11):
		numero2 = "J"
	if (jugador2 == 12):
		numero2 = "Q"
	if (jugador2 == 13):
		numero2 = "K"
	if (jugador2 == 14):
		numero2 = "As"
			
	print 
	print "El teu rival te un", str(numero2) + " de", pal2
	print 

	if (jugador1 == jugador2):
		print "Empat de valors... Guanya la màquina."
	
	else:
		#Guanyo jo
		if ( jugador1 > jugador2):
			print "Tu guanyes!!!!"	
			saldo = saldo + apuesta * 2
			print "cogento"
		#Guanya la maquina
		else:
			print "Ets un.... Guanya la maquina!"
	
	return saldo,jugador1,jugador2





def llegir_aposta(saldo,salir,apuesta):
	
	if (saldo<10):
		salir_apuesta=True
		salir=True
		
	else:	
		salir_apuesta=False
		print "Saldo actual:" , saldo
		print "Aposta mínima 10€"
		print "Sortir: -1"
		apuesta=input("Quan vol apostar: ")
		
			
	while (salir_apuesta==False):
		if (apuesta==-1):
			salir_apuesta=True
			salir=True
			print "A tomá pol culo"
		else:
			if (apuesta>=10 and apuesta<=saldo):
				saldo = saldo - apuesta
				salir_apuesta=True
			else:
				print "Aposta incorrecta.... Burro."
				if (apuesta<10):
					print "La aposta mínima es de 10€"
				if (apuesta>saldo):
					print "No es pot apostar més del teu saldo... No vols jugar-te els pantalons no?"
				print "Salir: -1"
				apuesta=input("Introduca su apuesta: ")
	return saldo,salir,apuesta
	
############################################################################
#                               NIVEL 1
############################################################################


saldo=100
apuesta=0
salir=False
jugador2=0
pal2="C"
jugador1=0
pal1="P"

os.system('clear')
# Leer apuesta
saldo,salir,apuesta=llegir_aposta(saldo,salir,apuesta)

while (salir==False):
	#El joc de les cartes + Quien gana 
	joc(saldo,jugador1,jugador2)
		
	# Recalcular Saldo
	if ( jugador1 > jugador2):
		saldo = saldo + (apuesta * 2)
	# Llegir la aposta, que vol fer
	saldo,salir,apuesta=llegir_aposta(saldo,salir,apuesta)
				

# Ni guanya ni perd
if (saldo==100):
	print "\nGracies per venir"
else:
	# Ha perdut diners
	if (saldo<100):
		print "\nEts un pringat, gracies a tu em compraré un Ferrari."
	else:
		print "\nSi tornes a guanyar et trenquem les cames."
