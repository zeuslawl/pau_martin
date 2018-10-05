#!/usr/bin/python
# coding: utf8

####################################
#     Calculadora amb Bucle        #
#	Pau Martín Arnau 22-3-17   #
####################################	


#Això ens permetrà netejar la pantalla

import os

#Ara anem a crear la variable per a poder sortir del bucle

sortir = False

#Ara anem a fer el menú de la calculadora, amb un bucle

while sortir == False:

	os.system('clear')
	print "Bon dia, que desitja fer el meu amo?: "
	print ""
	print "S.- Sortir"
	print "1.- Sumar"
	print "2.- Restar" 	
	print "3.- Multiplicar" 
	print "4.- Dividir" 
	print ""

#Ara anem a crear la variable que detectarà el que hi posa l'usuari

	numero=raw_input("Quina acció vols fer?: ") 

#Ara crearem totes les opcions que realitzarà el menú, incluit el control d'errors.
	if (numero == "1"):
		print ""
		print "Has triat la opció de sumar!"
		print
		tecla=raw_input("Prem una tecla per a continuar")
		
	if (numero == "2"):
		print ""
		print "Has triat la opció de restar!"
		print 
		tecla=raw_input("Prem una tecla per a continuar")
		
	if (numero == "3"):
		print ""
		print "Has triat la opció de multiplicar!"
		print
		tecla=raw_input("Prem una tecla per a continuar")
		
	if (numero == "4"):
		print ""
		print "Has triat la opció de dividir!"
		print
		tecla=raw_input("Prem una tecla per a continuar")
		
	if (numero == "S") or (numero == "s"):
		print ""
		print "Que vagi bé!!" 
		sortir = True
	
	if not((numero <= "4" and numero >= "1") or (numero == "s") or (numero == "S")):
		print
		print "No existeix aquesta opció"
		print
		tecla=raw_input("Prem una tecla per a continuar")
