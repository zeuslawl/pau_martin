#!/usr/bin/python3
# -*-coding: utf8-*-

# Pau Martín Arnau
# isx46420653
# 11/10/18
# Primera versió

# Convertir un nombre binari de 3 xifres a un nombre decimal. 

# Entrar un numero enter que sigui 0 o 1. El resultat serà
# el nombre en format decimal. 

a_binari = int(input("Primer dígit? "))
b_binari = int(input("Segon dígit? "))
c_binari = int(input("Tercer dígit? "))
d_binari = int(input("Quart dígit? "))
e_binari = int(input("Cinqué dígit? "))
f_binari = int(input("Sisè dígit? "))
g_binari = int(input("Setè dígit? "))
h_binari = int(input("Vuitè dígit? "))

h_decimal = h_binari * 2**7
g_decimal = g_binari * 2**6
f_decimal = f_binari * 2**5
e_decimal = e_binari * 2**4
d_decimal = d_binari * 2**3
c_decimal = c_binari * 2**2
b_decimal = b_binari * 2**1
a_decimal = a_binari * 2**0

resultat = a_decimal+b_decimal+c_decimal+d_decimal+e_decimal+f_decimal+g_decimal+h_decimal

print ("El teu nombre binari a decimal és el:", resultat)
