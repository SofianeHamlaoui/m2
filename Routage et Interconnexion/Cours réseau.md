# Réseau

*06/09/18*

## OSPF

Les opérateurs sont divisés en tiers 1, 2 et 3. 

- 1 porte réseaux et est international
- 3 front avec le client
- 2 fait la liaison avec 1 et front avec client.

OSPF est un protocole de base utilisé par les opérateurs. On le retoruve sur des architectures de type campus, grosses structures.   
Pour OSPFv3 il faut de l'IPv6. l'IPv6 est obligatoire au moins en interne chez les opérateurs (ils sont au moins en double IP).  
En IPv6 on peut envoyer des paquets 3x fois gros qu'en ipv4, mais il faut une archi full IPv6.

MPLS : sous-couche. C'est interne. Ça carbure mais ça fait pas le job d'OSPF.

## EIGRP

Propriétaire (Cisco). Se retrouve dans les très grosses structure type hôpital.

Protocole utilisé : RTP. 

`show ip eigrp neighbors` permet d'afficher les voisins : routeurs avec qui on travaille

