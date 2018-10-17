#!/usr/bin/python3
# -*-coding: utf8-*-

# Pau Martín Arnau
# isx46420653
# 11/10/18
# Primera versió

# Un programa que rebi un nombre enter que representin segons i transformi 
# la xifra a una hora en format H:M:S 

# Entrar un numero enter positiu que seran els segons, el resultat serà
# l'hora en un format correcte.

segons = int(input("Quants segons vols? "))

# Calcularem l'excès de segons, es a dir, que passin de 60 per a després 
# poder augmentar-los als minuts

augment_segons = (segons // 60)

# Fem la operació per a saber quants segons en queden, en cas de tenir més de 60
# s'hauran de restar la quantitat sobrant per a que quedi un numero inferior a 60 i 
# despres afegir aquest numero als minuts totals. 

segons_totals = segons - augment_segons*60

# Calcularem l'excès de minuts, es a dir, que passin de 60 per a després 
# poder augmentar-los a les hores

minuts = augment_segons

augment_minuts = (minuts // 60)

# Fem la operació per a saber quants minuts en queden, en cas de tenir més de 60
# s'hauran de restar la quantitat sobrant per a que quedi un numero inferior a 60 i 
# despres afegir aquest numero a les hores totals, a més també afegim els segons que 
# em calculat anteriorment que superaven els 60.  

minuts_totals = minuts - augment_minuts*60

# Les hores també les calcularem, dividirem les hores totals en 24 per a saber si sumen algun dia.

hores = augment_minuts

# Finalment farem un print: 

print ("")
print ("El total de temps introduit és:",hores, "hores,", minuts_totals, "minuts i", segons_totals, "segons")
print ("")
