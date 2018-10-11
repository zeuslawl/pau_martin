#!/usr/bin/python3
# coding: utf8

# Pau Martín Arnau
# isx46420653
# 05/10/18
# Versió acabada

# Calcular el sou de 3 treballadors augmentant-lo en percentatges concrets. 
# Entrar 3 nombres Float més grans que 0

Sou1 = 5
Sou2 = 10
Sou3 = 15

Sou1_Augment = (Sou1 * 10/100) + Sou1
Sou2_Augment = (Sou2 * 15/100) + Sou2
Sou3_Augment = (Sou3 * 15/100) + Sou3

print ("")
print ("Els 3 treballadors guanyen: ", str(Sou1), "€, ", str(Sou2), "€ i ", str(Sou3), "€ respectivament.")
print ("")
print ("Els aplicarem un augment del 10%, 12% i 15% respectivament.")
print ("")
print ("El sou final del primer treballador són: ", str(Sou1_Augment))
print ("El sou final del segon treballador són: ", str(Sou2_Augment))
print ("El sou final del tercer treballador són: ", str(Sou3_Augment))
