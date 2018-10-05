# Sistemes RAID  

* * *  
  
1. Resum de sistemes RAID fent servir una taula com la vista a classe.  
  
    
| Nivells | Nº mínim de discs | Nº màxim de discs fallats | Capacitat | Read | Write | 
| :------ | :---------------: | :-----------------------: | :-------: | :--: | ----: | 
| Raid 0 | 2 | 0 | 100 % | Excel·lent | Excel·lent |
| Raid 1 | 2 (Max) | 1 | 50 % | Molt bona | Bona | 
| Raid 5 | 3 | 1 | 67% ~ 94% | Molt bona | Bona |
| Raid 6 | 4 | 2 | 50% ~ 98% | Bona | Bona |
| Raid 10 | 4 | 1/mirror | 50 % | Molt bona | Bona |

* * *

2. Descripció de la metodologia utilitzada a classe per a fer proves amb màquines virtuals.  
  

   * Utilitzarem la màquina de Fedora 24 per a realitzar la pràctica. 
   * Afegirem dos o ms discs durs a la màquina, depenent de la Raid que volguem fer.
   * Un cop comprovats els discs i integrats a la màquina haurem de crear la Raid.
   * Crearem el Raid amb les comandes mdadm.
   * També hi montarem un sistema de fitxers, en aquest cas un EXT4, amb la comanda mkfs.ext4
   * Finalment montem la Raid dins de la carpeta que ens vagi bé, nosaltres ho hem fet a /mnt.
   * Quan realitzem un **lsblk** sortirà el disc de tipus "Raid X" i muntat a /mnt
   * Ara realitzarem la comprobacío del funcionament de la Raid. 
   * A les configuracions de la màquina hi eliminarem un dels discs durs, en calent, simulant que ha donat un error.
   * Si mirem informació sobre la Raid a l'arxiu /proc/mdstat sortirà que la Raid ha donat un error.
   * Depen de la Raid seguirà en funcionament o s'haurà aturat. 
   * Ara tornariem a afegir un altre disc, per a suplir les funcions del disc dur que ha donat error. (Ha estat eliminat)
   * Insertem un altre disc dur a les configuracions de la maquina virtual.
   * L'afegim a la Raid amb **mdadm "Raid" --add "Nou disc"**
   * Si ara comprovessim l'arxiu /proc/mdstat hauria de funcionar tot correctament. 
   
* * *
     
3. Comandes i descripció de les mateixes per tal de crear un sistema RAID1

+ **mdadm --create md1 --level=1 --raid-devices=2 /dev/vda /dev/vdb**  
Crearà una raid 1 amb el nom "md1" amb els discs *vda* i *vdb*  

  --create: Crea una Raid amb el nom que adjuntes.   
  --level: Crea la Raid amb el nivell que li diguis.  
  --raid-devices: Numero de discs durs que hi vols afegir a la Raid.   
  /dev/vda: Localització del disc dur que vols introduir al Raid.  

+ **mkfs.ext4 /dev/md1**  
Monta un sistemes de fitxers ext4 per el RAID md1  
+ **mount /dev/md1 /mnt**   
Monta el RAID md0 al directori 'mnt'  

* * *

4. Comandes i descripció de les mateixes per tal de crear un sistema RAID  

+ **mdadm --create md5 --level=5 --raid-devices=3 /dev/vda /dev/vdb /dev/vdc**  
Crearà una raid 5 amb el nom "md5" amb els discs *vda*, *vdb* i *vdc*  

  --create: Crea una Raid amb el nom que adjuntes.   
  --level: Crea la Raid amb el nivell que li diguis.  
  --raid-devices: Numero de discs durs que hi vols afegir a la Raid.   
  /dev/vda: Localització del disc dur que vols introduir al Raid.  

+ **mkfs.ext4 /dev/md5**  
Monta un sistemes de fitxers ext4 per el RAID md5  
+ **mount /dev/md5 /mnt**   
Monta el RAID md5 al directori 'mnt'  

* * *

5. Comandes i descripció de les mateixes per tal de crear un sistema RAID6  

+ **mdadm --create md6 --level=6 --raid-devices=4 /dev/vda /dev/vdb /dev/vdc /dev/vdd**    
Crearà una raid 6 amb el nom "md6" amb els discs *vda*, *vdb*, *vdc* i *vdd*  

  --create: Crea una Raid amb el nom que adjuntes.   
  --level: Crea la Raid amb el nivell que li diguis.  
  --raid-devices: Numero de discs durs que hi vols afegir a la Raid.   
  /dev/vda: Localització del disc dur que vols introduir al Raid.  

+ **mkfs.ext4 /dev/md6**  
Monta un sistemes de fitxers ext4 per el RAID md6  
+ **mount /dev/md6 /mnt**   
Monta el RAID md6 al directori 'mnt'  

* * *

6. Comandes i descripció de les mateixes per tal de crear un sistema RAID10  
+ **mdadm --create md0 --level=1 --raid-devices=2 /dev/vda /dev/vdb**    
  
Crearà una Raid 1 amb el nom "md0" amb els discs *vda* i *vdb*.  
  
+ **mdadm --create md1 --level=1 --raid-devices=2 /dev/vdc /dev/vdd**  
  
Crearà un Raid 1 amb el nom "md1" amb els discs *vdc* i *vdd*.    
    
  Després hi haurem de crear el Raid 10, ja que ara només hi tenim 2 Raids 1. Ho farem amb la mateixa comanda.  
  
+ **mdadm --create md10 --level=0 --raid-devices=2 /md0 /md1**  
  
   Ara ja tindriem la Raid 10 montada, amb 4 discs.   

+ **mkfs.ext4 /dev/md10**  
Monta un sistemes de fitxers ext4 per el RAID md10
+ **mount /dev/md10 /mnt**   
Monta el RAID md10 al directori 'mnt'  

* * *

Pau Martín Arnau
