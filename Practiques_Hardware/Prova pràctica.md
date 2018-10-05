## PROVA PRÀCTICA UF4

1. [0,5 punts] Desactiveu l'àrea d'intercanvi 'swap'
    Resposta: **swapoff -a**   
  
2. [0,5 punts] Elimineu-ne la partició de swap (Hauria de ser de 3GB)  
    Resposta: **fdisk /dev/vda d 2**  
                  
3. [1 punts] Modifiqueu el fitxer de muntatge en arrencada fstab per tal que ja no carregui mai més la partició swap.  
    Resposta: **vi /etc/fstab** --> Borrem la ultima linea del fitxer  
                  
4. [4 punts] Creeu els següents volums lògics sobre aquesta partició: Abans haurem de fer:  
	**pvcreate /dev/vda2** i **vgcreate prova /dev/vda2**  
    Volum lògic de nom 'documents' i de tamany 1GB  
      Resposta: **lvcreate -L 1G -n documents prova**    
                    
    Volum lògic de nom 'jocs' i de tamany 500MB  
      Resposta: **lvcreate -L 500M -n jocs prova**    
                      
    Volum lògic de nom 'dades1' i de tamany 100MB  
      Resposta: **lvcreate -L 100M -n dades1 prova**       
                      
    Volum lògic de nom 'dades2' i de tamany 100MB  
      Resposta: **lvcreate -L 100M -n dades2 prova**       
                      
5. [0,5 punts] Creeu els directoris /mnt/documents i /mnt/jocs  
    Resposta: **mkdir /mnt/documents** i **mkdir /mnt/jocs**  
                  
6. [0,5 punts] Creeu un sistema de fitxers XFS als volums lògics 'documents' i 'jocs'  
    Resposta: **mkfs.xfs /dev/proves/documents** i **mkfs.xfs /dev/proves/jocs**
                
7. [1 punts] Munteu els volums lògics de la següent manera:  
    lv documents -> /mnt/documents  
      Resposta:  **mount /dev/prova/documents /mnt/documents/** 
                    
    lv jocs -> /mnt/jocs
      Resposta: **mount /dev/prova/jocs /mnt/jocs/** 

8. [2 punts] Creeu un raid 1 sobre els volums lògics 'dades1' i 'dades2'  
    Resposta:  **mdadm --create /dev/md0 --level=1 --raid-devices=2 /dev/prova/dades1 /dev/prova/dades2**
                
