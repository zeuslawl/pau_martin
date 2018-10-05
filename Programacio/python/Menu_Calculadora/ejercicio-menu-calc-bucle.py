#!/usr/bin/python
# coding: utf8

#Això ens permetrà netejar la pantalla

import os
os.system('clear')

#Ara anem a definir la variable que crea el bucle

sortir=False 

#Ara anem a fer el menú de la calculadora

while sortir == False:
	 
	os.system('clear')
	print "Bon dia, que desitja fer el meu amo?: "
	print ""
	print "1.- Sumar"
	print "2.- Restar" 
	print "3.- Multiplicar" 
	print "4.- Dividir" 
	print "5.- Sortir"
	print ""
	
	numero=raw_input("Quina acció vols realitzar? ")
	
	if numero == "1": 
		print "Ara has d'introduir els 2 nombres que vols sumar: "
		print ""
		x=input("Quin és el 1r factor? ")
		y=input("Quin és el 2n? ") 
		print ""
		print "El resultat de la suma dels dos factors és: ", x+y 
		print ""
		tecla=raw_input("Prem una tecla per a continuar")
		
	if numero == "2": 
		print "Ara has d'introduir els 2 valors que vols restar: "
		print ""
		x=input("Quin és el 1r factor? ")
		y=input("Quin és el 2n? ") 
		print ""
		print "El resultat de la resta dels dos factors és: ", x-y 
		print ""
		tecla=raw_input("Prem una tecla per a continuar")
		
	if numero == "3": 
		print "Quins són els dos nombres que vols multiplicar? "
		print ""
		x=input("Quin és el 1r factor? ")
		y=input("Quin és el 2n? ") 
		print ""
		print "El resultat de la multiplicació dels dos factors és: ", x*y 
		print ""
		tecla=raw_input("Prem una tecla per a continuar")
		
	if numero == "4": 
		print "Quins són els dos nombres que vols dividir? "
		print ""
		x=input("Quin és el 1r factor? ")
		y=input("Quin és el 2n? ") 
		print ""
		print "El resultat de la divisió dels dos factors és: ", x/y 
		print ""
		tecla=raw_input("Prem una tecla per a continuar")
		
	if numero == "5": 
		print ""
		print "Adéu amo!!" 
		print ""
		sortir=True
	
	if (numero < "1" or numero >= "6"):
		print ""
		print "No és un valor vàlid senyor meu, torni a posar un correcte sisplau "
		print ""
		tecla=raw_input("Prem una tecla per a continuar")
	else: 
		print "No és un valor vàlid senyor meu, torni a posar un correcte sisplau "

