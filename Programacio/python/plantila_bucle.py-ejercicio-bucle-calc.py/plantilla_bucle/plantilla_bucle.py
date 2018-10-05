#!/usr/bin/python
# coding: utf8

################################
#	    Plantilla-Bucle		   #
# Pau Martín Arnau - 21/03/17  #
################################

#Això ens permetrà netejar la pantalla

import os
os.system('clear')

#Ara anem a crear la variable per a poder sortir del bucle

salir = False

#Ara anem a crear el menú principal del bucle

while salir == False:
	print "Hola"
	tecla = raw_input("*. Saludar S. Sortir: ")
	if (tecla == "S" or tecla == "s"):
		print "Vagi bé!!"
		salir = True
	#Aqui acabaria el IF
#Aqui acabaria el While.
