#!/usr/bin/python 
#coding:utf-8 

import os 
from os.path import join, getsize


### Mostra els noms de tots els arxius de dins de la carpeta 

path="./cartes-i-daus/"

print ""
print "Arxius: "
print ""

for root, dirs, files in os.walk(path):
	for name in files:
		print name

### Mostra els noms dels directoris de dins de la carpeta 

print ""
print "Directoris: "
print ""

for root, dirs, files in os.walk(path):
	for name in dirs:
		print name


 
### Mostra la ruta dels arxius. 
 
print ""
print "Ruta d'arxius: "
print ""

for root, dirs, files in os.walk(path):
    for name in dirs:
        name_path=os.path.join(root, name)
        print(name_path)
        
### Mostra el tamany dels arxius
### Tret de http://www.sromero.org/wiki/programacion/tutoriales/python/recorrer_arbol

print ""
print "Pes d'arxius: "
print ""

for root, dirs, files in os.walk(path):
   print os.path.join(root, name), "pesa",
   print sum(getsize(join(root, name)) for name in files),
   print "bytes"

