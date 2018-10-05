#!/usr/bin/python3
# -*-coding: utf8-*-

# Pau Martín Arnau
# isx46420653
# 05/10/18
# Versió acabada

# Que demani una hora amb valors enters, transformar l'hora donada a un format correcte,
# en cas de que no ho sigui, i mostrar per pantalla l'hora correcte que ha introduit 
# l'usuari. Exemple:  3h 118m 195s --> 5h 1m 15s.

# S'ha de llegir una hora amb valors enters i amb el format: hh mmm sss
# Mostrara per sortida el format correcte de l'hora en cas de que estigui malament. 

segons = int(input("Quants segons vols? "))

minuts = int(input("Quants minuts vols? "))

hores = int(input("Quantes hores vols? "))

if (segons < 60):

	segons = segons + (segons % 60)

minuts = segons = segons + (segons % 60)

hores = hores + (hores % 60)

print ("")
print ("El total de temps introduit és: ",hores, "hores, ", minuts, "minuts i ", segons, "segons")
print ("")
