# !/usr/bin/python
# coding:utf-8

import os
 
ruta_a_explorar="../cartes-i-daus/"
 
 
for ruta, directorios, archivos in os.walk(ruta_a_explorar):
    for nombre in archivos:
        ruta_completa=os.path.join(ruta, nombre)
        print(ruta_completa)
        print "Segons: ",
        print os.path.getatime(ruta_completa) 
 
    for nombre in directorios:            
        ruta_completa=os.path.join(ruta, nombre)
        print(ruta_completa)
        print "Segons: "
        print os.path.getatime(ruta_completa) 
