#!/usr/bin/python
# coding: utf8

from random import randint

Sortir = False

while (Sortir == False):

	pal = randint(1,4)

	if (pal == 1):
		pal1 = "Piques"
	if (pal == 2):
		pal1 = "Cors"
	if (pal == 3):
		pal1 = "Diamants"
	if (pal == 4):
		pal1 = "Trèbols"

	pal = randint(1,4)
		
	if (pal == 1):
		pal2 = "Piques"
	if (pal == 2):
		pal2 = "Cors"
	if (pal == 3):
		pal2 = "Diamants"
	if (pal == 4):
		pal2 = "Trèbols"

	jugador1 = randint(1,13)

	jugador2 = randint(1,13)

		
	if (jugador1 == jugador2):
		print "Empat de valors!!!"
		
	else:
		
		if (jugador1 > jugador2):
			if (jugador1 == 11):
				jugador1 = "J"
			if (jugador1 == 12):
				jugador1 = "Q"
			if (jugador1 == 13):
				jugador1 = "K"
			
			print "Tu tens un", str(jugador1) + " de", pal1
			print "El teu rival te un ", str(jugador2) + " de", pal2
			print "Tu guanyes!!!!"	
		
		else:
			
			if (jugador2 == 11):
				jugador2 = "J"
			if (jugador2 == 12):
				jugador2 = "Q"
			if (jugador2 == 13):
				jugador2 = "K"
			
			print "Tu tens un ", str(jugador1) + " de", pal1
			print "El teu rival te un ", str(jugador2) + " de", pal2
			print "Ets un.... Guanya la maquina!"
	
	if (jugador1 != jugador2):
		Sortir = True
