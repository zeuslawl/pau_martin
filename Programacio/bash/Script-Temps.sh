#!/bin/bash

#Pau Martín Arnau (Col·laboració amb Jorge Pastor)

#Ara farem un script que et dirà el temps que ha passat des de que vas nèixer.

#Ara crearem el dia actual com a variable

AVUI_DIA=`date +"%d"`

#Ara ho farem igual però amb els mesos

AVUI_MES=`date +"%m"`

#I finalment amb els anys 

AVUI_ANY=`date +"%Y"`

clear

#Ara farem el qüestionari per a saber l'edat de la persona.

#Tots els echo buits són per a un tema més estètic.

#El read llegeix el que introdueix l'usuari i ho assigna com a variable

echo "Bon dia! Vols veure la teva edat exacte? " 
echo 
echo "Quin dia vas nèixer? "
echo 
read dia
echo
echo "Quin mes vas nèixer? (Format 00) "
echo
read mes
echo 
echo "De quin any? "
echo
read any 

#Ara farem la resta de variables, la del temps actual menys la data de quan va nèixer.
#Per a que surti la seva edat
 
edat_dia=`expr $AVUI_DIA - $dia`

edat_mes=`expr $AVUI_MES - $mes`

edat_any=`expr $AVUI_ANY - $any`

#Si la resta de dies dona negatiu el multiplicarà per -1 per a que el mostri positiu.

if [ $edat_dia -lt 0 ]; then 
	edat_dia=`expr $edat_dia \* -1`
fi 

#Si la resta de mesos dona negatiu el multiplicarà per -1 per a que el mostri positiu.

if [ $edat_mes -lt 0 ]; then 
	edat_mes=`expr $edat_mes \* -1`
fi

#Si el mes que dona l'usuari és major al mes d'avui. Li resta -1 al any actual,
#igual amb els dies, això ho fem per a que no doni 1 any més del compte.

if [ \( $mes -gt $AVUI_MES \) -o  \( $mes -eq $AVUI_MES  -a  $dia -ge $AVUI_DIA \) ]; then
	edat_any=`expr $edat_any - 1`
fi

#Ara mostrem un text i l'edat de la persona.

echo
echo "Ara mateix tens $edat_any anys, $edat_mes mesos i $edat_dia dies."
