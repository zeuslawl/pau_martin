#!/usr/bin/python
# coding: utf8

from random import randint
import os

Sortir_menu = False
Sortir_aposta = False
Sortir_joc = False
saldo = 100 
aposta = 0


while (Sortir_menu == False):
	
	os.system('clear')
	print "Bon dia! Que vols fer?"
	print 
	print "1 --> Jugar" 
	print 
	print "-1 --> Sortir" 
	print 
	opcio=input("Que vols fer? ")
	
	if (opcio == 1):
		
		while (Sortir_aposta == False):
			
			Sortir_aposta = False
				
			print "Ara mateix tens", str(saldo) + " €"
			print 
			aposta=input("Quan vols apostar? ")
			
			if(aposta >= 10 and aposta <= saldo):
				while (Sortir_joc == False):	
					
					Sortir_joc = False
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
						print "Empat de valors... Guanya la banca."
						saldo = saldo - aposta

					else:
						if ( jugador1 > jugador2):
							print "Tu guanyes!!!!"
							saldo = (saldo - aposta) + (aposta * 2)	
							
						
						else:
							print "Ets un.... Guanya la maquina!"
							saldo = saldo - aposta
							
					print "Ara mateix tens", str(saldo) + " €"
					tecla=raw_input("Prem una tecla per a continuar")
					Sortir_joc = True
					Sortir_aposta = True
			else:
				print 
				print "No pots apostar menys de 10 ni més del teu saldo... Melón"
				print 
	
	
	if (opcio == -1 or saldo < 10):
		print "A tomá pol culo"
		Sortir_menu = True
		
