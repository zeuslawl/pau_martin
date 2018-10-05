#!/usr/bin/python
# coding: utf8

#Això ens permetrà netejar la pantalla

import os
os.system('clear')

#Ara anem a fer el menú de la calculadora

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

if (numero >= "1" and numero <= "4") or (numero == "S") or (numero == "s"):
	print "Molt bé" 
else: 
	print "Esa opción no existe"
