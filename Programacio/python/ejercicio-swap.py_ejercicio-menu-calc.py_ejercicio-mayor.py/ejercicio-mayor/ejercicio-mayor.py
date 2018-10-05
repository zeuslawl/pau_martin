#!/usr/bin/python
# coding: utf8

import os 
os.system('clear')

print ""
Var1=raw_input("Digues un nombre: ")
print ""
Var2=raw_input("Digues un altre nombre: ") 
print ""

if ( Var1 > Var2 ):
	print str(Var1) + " és més gran que " + str(Var2)
	print "" 
	
else: 
	if ( Var1 == Var2 ):
		print str(Var1) + " és igual a " + str(Var2)
		print ""
	
	else: 
		print str(Var2) + " és més gran que " + str(Var1)
		print ""
	
