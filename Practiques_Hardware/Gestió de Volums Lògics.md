# Volums Lògics  

* * *  

### Què són?   
  
Els volums lògics són unitats de disc virtualitzades que permeten fer més funcions que les clàssiques 
particions
  
### Com estan formats?  
  
Estan formats per a 3 tipus de volums, cada un d'ells té unes funcions:  
  
PV --> Phisical Volum -->  Identificació de disc  
VG --> Volum Group --> El grup dels discs  
LV --> Logical Volum --> Particionatge  
  
El PV és el pas de transformar el disc dur a volum lógic. Comandes útils --> **pvcreate, pvs**  
El VG és el conjunt de PV que formen un tipus de disc dur virtual. Comandes útils --> **vgcreate, vgs, vgextend**  
El LV són les particions del VG, ampliables en calent. Comandes útils -->  **lvcreate, lvs, lvextend**  

* La comanda **pvcreate** permet crear un volum lògic d'un disc, podrem veure tots amb la comanda **pvs**  
* **vgcreate** permet crear volumns lògics amb PV, els llistem tots amb **vgs** i l'hi augmentem de tamany amb el **vgextend**  
* La comanda **lvcreate** permet crear volums lògics partint dels VG, les llistem amb **lvs** i l'hi podem augmentar de tamany en calent amb **lvextend**
    
* * *

### Entorn de pràctiques:  
  
Realitzarem la gestió de volums amb el programa VirtManager, el qual permet posar discs VirtIO, 
discs que es poden treure i posar en calent. Afegirem 3 de 200 M. 

![](https://github.com/pmartinarnau/m01-2016-2017/blob/master/M01/fotos-lvm/maquina.png)
* * * 

### Pràctica 1:  
  
Per a crear un PV de la capacitat total del disc farem:  
**pvcreate /dev/vda**  
Després hi crearem el VG on hi afegirem el PV:  
**vgcreate practica1 /dev/vda**  
Tot seguit hi crearem el VL, de tota la dimensió del disc, amb: 
**lvcreate -l +100%free -n dades practica1**   
D'aquesta manera agafarem tota la dimensió del disc amb un sol LV.  

![](https://github.com/pmartinarnau/m01-2016-2017/blob/master/M01/fotos-lvm/pvs%2C%20lvs%2C%20pratica1.png)

* * *

### Pràctica 2: 
  
Per a crear un sistema de fitxers xfs al volum lògic dades farem la següent comanda: 
**mkfs.xfs /dev/practica1/dades**  
Aleshores el muntem a /mnt.  
**mount /dev/practica1/dades /mnt**  
Tot seguit hi muntarem un arxiu de prova ple de zeros.  
**dd if=/dev/zero of=test.img bs=180M**  
Ja tindriem muntat el VL amb un arxiu de prova dins seu.  
  
![](https://github.com/pmartinarnau/m01-2016-2017/blob/master/M01/fotos-lvm/xfs.png)

* * *

### Pràctica 3:  
  
Ara crearem un RAID 1 amb els dos discs sobrants, vdb i vdc. Ho farem amb: 

**mdadm --create /dev/md0 --level=1 --raid-device=2 /dev/vdb /dev/vdc**  


![](https://github.com/pmartinarnau/m01-2016-2017/blob/master/M01/fotos-lvm/raid1-millor.png)

* * *

### Pràctica 4: 
  
Primer transformem el Raid 1 a un PV, ho fem amb:  
**pvcreate /dev/md0**  
Després extenem el tamany del VG, amb la comanda:  
**vgextend practica1 /dev/md0**  
I finalment extenem el tamany de dades amb:   
**lvextend -l +100%free /dev/practica1/dades**  
  
![](https://github.com/pmartinarnau/m01-2016-2017/blob/master/M01/fotos-lvm/raid1.png)

* * *
  
### Pràctica 5: 
  
Per a ampliar el sistema de fitxers realitzarem la següent comanda, com es xfs no cal desmuntar-lo:  
**xfs_growfs /dev/practica1/dades**  
ja tindriem el LV amb el màxim tamany de 400 M, 1 disc de 200 i un Raid 1 de 200M també. 

![](https://github.com/pmartinarnau/m01-2016-2017/blob/master/M01/fotos-lvm/xfs-aument.png)

* * *

Pau Martín Arnau
