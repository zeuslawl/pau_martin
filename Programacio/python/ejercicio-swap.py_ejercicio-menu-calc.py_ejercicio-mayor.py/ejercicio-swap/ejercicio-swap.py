#!/bin/python
# coding: utf8

####################################
#          Exercici Swap           #
#	Pau Martín Arnau - 16-3-17	   #
####################################		

import os
os.system('clear')

#Primer hem de definir les variables

mano_derecha = "movil"
mano_izquierda = "bocadillo"

#Mostrem el que contenen 

print mano_derecha + " --> Esta és la mano derecha!"
print mano_izquierda + " --> Esta és la mano izquierda!"
print ""

#Ara les intecanviarem amb una variable temporal que direm "mano_extra"

mano_extra = mano_derecha
mano_derecha = mano_izquierda
mano_izquierda = mano_extra

#Ho mostrarem per pantalla per a que l'usuari sàpiga el que fem
print "Ahora hacemos las operaciones... "
print ""
print "mano_extra = mano_derecha"
print "mano_derecha = mano_izquierda"
print "mano_izquierda = mano_extra"
print "" 

#I ara mostrarem el resultat

print "El resultado és...." 
print ""
print "Ahora el " + mano_derecha + " esta en la derecha..."
print "Y el " + mano_izquierda + " en la izquierda!"
print "" 
