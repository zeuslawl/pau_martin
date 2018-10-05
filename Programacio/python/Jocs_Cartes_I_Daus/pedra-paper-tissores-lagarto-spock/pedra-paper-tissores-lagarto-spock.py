#!/usr/bin/python
# coding: utf8

from random import randint
import os

jugador = raw_input("Que vols jugar?: Pedra, Paper, Tissores, Lagarto o Spock?: ")

maquina = randint(1,5)

if (maquina == 1):
	rival = "Pedra"
	
if (maquina == 2):
	rival = "Paper"
	
if (maquina == 3):
	rival = "Tissores"
	
if (maquina == 4):
	rival = "Lagarto"
	
if (maquina == 5):
	rival = "Spock"
	
os.system('sleep 1s')
print "Tu tens: ", jugador
print "El teu rival té: ", rival 
os.system('sleep 1s')

if (jugador == rival):
	print "Empat"
else:
	if 	((jugador == "Pedra")  and (rival == "Lagarto" or rival == "Tissores") or 
		  (jugador == "Paper")   and (rival == "Pedra" or rival == "Spock") or
		  (jugador == "Tissores")  and (rival == "Paper" or rival == "Lagarto") or
		  (jugador == "Lagarto") and (rival == "Paper" or rival == "Spock"   ) or
		  (jugador == "Spock")   and ( rival == "Pedra" or rival == "Tissores")):
		
		print "Has guanyat!!!"
	else:
		print "Ets un.... Has perdut"
