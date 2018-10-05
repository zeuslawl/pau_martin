#!/usr/bin/python
# coding: utf8

from random import randint
import os
Sortir = False
while (Sortir == False):

	huma = raw_input("Que quieres jugar?: Piedra, Papel, Tijeras, Lagarto o Spock: ")
	
	machine = randint(1,5)
	
	if machine == 1: 
		maquina = "Tijeras"
	if machine == 2:
		maquina = "Piedra"
	if machine == 3:
		maquina = "Papel"
	if machine == 4:
		maquina = "Lagarto" 
	if machine == 5:
		maquina = "Spock" 
		
	os.system('sleep 1')	
	print "Tu tienes : ", huma 
	print "La maquina juega: ", maquina
	os.system('sleep 1')
	
	if (huma == maquina):
		print "Empate!!!"
	else: 
		if ((huma == "Piedra" and (maquina == "Tijeras" or maquina == "Lagarto")) or
			(huma == "Papel" and (maquina == "Piedra" or maquina == "Spock")) or
			(huma == "Tijeras" and (maquina == "Papel" or maquina == "Lagarto")) or
			(huma == "Lagarto" and (maquina == "Papel" or maquina == "Spock")) or
			(huma == "Spock" and (maquina == "Piedra" or maquina == "Tijeras"))):
			print "Tu ganas!!!!"	
		else: 
			print "Eres un ..... Gana la maquina... "
	if (huma != maquina):
		Sortir = True	
	
