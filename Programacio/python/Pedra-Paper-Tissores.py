#!/usr/bin/python
# coding: utf8

# Variables i funcions utilitzades

from random import randint
import os
import time

print
print "Vols fer una partida de pedra paper i tissores contra la máquina? Endavant! "
print "--------------------------------------------------------------------------- "
print

# Crearé una funció per a que en cas d'haver-hi empat es pugui desempatar 
# tornant a fer tot el procediment d'una manera molt més neta i còmode.
# Simplement tornem a cridar la funció al final si hi ha empat.

def Joc():
		
	Control_error = False
	Control_empat = False
	
	# Aqui s'estableix les respostes de l'usuari i el resultat aleatori de la màquina. 

	jugada_usuari = raw_input("Quina opció vols jugar? (Ex. Pedra, Paper, Tissores): ")

	opcio_maquina = randint(1,3)

	# Ara farem el control d'errors per a la resposta de l'usuari, s'activarà en cas
	# de que cap de les respostes siguin aptes per al joc. 

	while Control_error == False: 
		
		if (jugada_usuari != "Pedra" and jugada_usuari != "Paper" and jugada_usuari != "Tissores"):
			
			print "No és una resposta correcte, posa una correcte com s'indica a l'exemple. "
			print ""
			jugada_usuari = raw_input("Quina opció vols jugar? (Ex. Pedra, Paper, Tissores) ")
		
		elif (jugada_usuari == "Pedra" or jugada_usuari == "Paper" or jugada_usuari == "Tissores"):
		
			Control_error = True
					
	# Ara decidim les respostes de la màquina segons el número aleatori que surti.

	if opcio_maquina == 1:
			
		jugada_maquina = "Pedra" 
		
	if opcio_maquina == 2:

		jugada_maquina = "Paper" 

	if opcio_maquina == 3:

		jugada_maquina = "Tissores"
		
	# Direm quina jugada vol fer cada jugador:

	print
	print "Has jugat: ", jugada_usuari
	print
	print "La màquina ha jugat: ", 
	print jugada_maquina
	print
	time.sleep(1)
	# Ara anem amb el joc com a tal, ja sabem que les respostes són correctes.

	while Control_empat == False:
		
		if ( jugada_usuari == "Pedra" and jugada_maquina == "Tissores"):
			print "Has guanyat!!"
			Control_empat = True
		
		if (jugada_usuari == "Paper" and jugada_maquina == "Pedra"):
			print "Has guanyat!!"
			Control_empat = True
			
		if (jugada_usuari == "Tissores" and jugada_maquina == "Paper"):
			print "Has guanyat!!"
			Control_empat = True

		if (jugada_usuari == "Tissores" and jugada_maquina == "Pedra"):
			print "Has perdut de manera humil·liant..."
			Control_empat = True
		
		if (jugada_usuari == "Pedra" and jugada_maquina == "Paper"):
			print "Has perdut de manera humil·liant..."
			Control_empat = True
		
		if (jugada_usuari == "Paper" and jugada_maquina == "Tissores"):
			print "Has perdut de manera humil·liant..."
			Control_empat = True
		
		if (jugada_usuari == jugada_maquina): 
			print "Empat! Altre ronda! "
			print
			Joc()
			Control_empat = True
			


# A jugar!

Joc()
