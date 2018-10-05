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

	jugador1 = randint(2,14)

	jugador2 = randint(2,14)
	
	numero = jugador1
	if (jugador1 == 11):
		numero = "J"
	if (jugador1 == 12):
		numero = "Q"
	if (jugador1 == 13):
		numero = "K"
	if (jugador1 == 14):
		numero = "As"
		
	print "Tu tens un", str(numero) + " de", pal1

	numero = jugador2
	if (jugador2 == 11):
		numero = "J"
	if (jugador2 == 12):
		numero = "Q"
	if (jugador2 == 13):
		numero = "K"
	if (jugador2 == 14):
		numero = "As"
	
		
	print "El teu rival te un ", str(numero) + " de", pal2

		
	if (jugador1 == jugador2):
		print "Empat de valors!!!"
		
	else:
		if ( jugador1 > jugador2):
			print "Tu guanyes!!!!"	
		else:
			print "Ets un.... Guanya la maquina!"
	
	if (jugador1 != jugador2):
		Sortir = True
