#!/usr/bin/python
# coding: utf8

from random import randint

Sortir = False

print "Vols fer una partida als daus? "

while (Sortir == False):
		
	jugador1 = randint(1,6)

	jugador2 = randint(1,6) 

	print 

	print "Tu tens un ", jugador1
	print "El teu rival té un: ", jugador2
	print

	if (jugador1 == jugador2):
		print "Empat!!!"
		print 
		print "Nova ronda!!!!: "
		
	else: 
		if (jugador1 > jugador2):
			print "Tu guanyes!!!"
		else:
			print "Ets un ..... Has perdut!"

	if (jugador1 != jugador2):
		Sortir = True
