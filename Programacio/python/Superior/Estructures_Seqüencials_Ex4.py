#!/usr/bin/python3
# -*-coding: utf8-*-

# Pau Martín Arnau
# isx46420653
# 05/10/18
# Falten corregir els minuts, poden passar de 60

# Que demani una hora amb valors enters, transformar l'hora donada a un format correcte,
# en cas de que no ho sigui, i mostrar per pantalla l'hora correcte que ha introduit 
# l'usuari. Exemple:  3h 118m 195s --> 5h 1m 15s.

# S'ha de llegir una hora amb valors enters i amb el format: hh mmm sss
# Mostrara per sortida el format correcte de l'hora en cas de que estigui malament. 

# Variables on entra l'usuari l'hora.
segons = int(input("Quants segons vols? "))

minuts = int(input("Quants minuts vols? "))

hores = int(input("Quantes hores vols? "))

# Calcularem l'excès de segons, es a dir, que passin de 60 per a després 
# poder augmentar-los als minuts

augment_segons = (segons // 60)

# Fem la operació per a saber quants segons en queden, en cas de tenir més de 60
# s'hauran de restar la quantitat sobrant per a que quedi un numero inferior a 60 i 
# despres afegir aquest numero als minuts totals. 

segons_totals = segons - augment_segons*60

# Calcularem l'excès de minuts, es a dir, que passin de 60 per a després 
# poder augmentar-los a les hores

augment_minuts = (minuts // 60)

# Fem la operació per a saber quants minuts en queden, en cas de tenir més de 60
# s'hauran de restar la quantitat sobrant per a que quedi un numero inferior a 60 i 
# despres afegir aquest numero a les hores totals, a més també afegim els segons que 
# em calculat anteriorment que superaven els 60.  

minuts_totals = minuts - augment_minuts*60 + augment_segons

# Les hores no les hem de calcular, ja que podem posar més de 24, el que si que hem de fer
# es afegir-les el numero d'augment dels minuts.

hores_totals = hores + augment_minuts

# Fem un print de les variables. 
print ("")
print ("El total de temps introduit és:",hores_totals, "hores,", minuts_totals, "minuts i", segons_totals, "segons")
print ("")
