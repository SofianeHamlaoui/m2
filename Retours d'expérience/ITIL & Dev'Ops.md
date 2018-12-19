*30/11/18*

Séance avec Christian Therond

# L'orateur

## ## Formation

Consultant Altran, bac+3 Sciences U, +5 en alternance.

Altran = ESN

ESN : trois grands pôles :

- Conseil : apporte expertise
- Infogérance : supervise systèmes, structures...
- Intégration

## Application

Son travail tourne autour des applications. Dans un SI, une application = un service (genre un BUS entre différents services est une applications car un service). Une application doit apporter de la valeur. Si elle n'en apporte pas on peut la virer. 

Dans un projet, on a un opérateur informatique (OI). Du côté projet, le chef de projet conduit la TMA. Côté OI, il y a l'IPI. on remonte les incidents sur la prod à l'IPI qui remonte à la TMA. 

Son travail est d'être le lien entre TMA et IPI, entre projet et OI. (CA : Chargé d'application)

Son application est liée à la gestion et au traitement des données Linky.



## Les 5 lignes de service

- Gestion du changement
- Conduite des Échanges
  - supervision du run des flucx
- Assistance applicative
- Gestion des accès
  - Sécurisation des accès à

# ITIL

## Stratégie des services

Quel service pour qui ?

- Définition du catalogue de service
- Gestion financière
- Gestion de relation client

LA VALEUR C'EST IMPORTANT

## Conception

Comment faire ? 

- coordination des services
- Gestion des SLA
- Gestion des fournisseurs

Il y a 4 composants à la qualité de service : disponibilité, capacité, continuité, sécurité

## SLA, OLA, UC ... le SLM

SLA : Entende de niveaux de service

OLA : objectif des niveaux de service

UC : Contrat de sous traitance

Le centre de compétences, il est là pour répondre à certaines tâches. 

## Les 4 P

Il faut penser à ces 4 points pour la conception des services.

- Personnes
- Produits
- Processus
- Partenaires



## Gestion du changement

Un changement peut être annulé par un change manager car pas assez bien préparé

E-Cab : emergency Cab. Normalement un changement est prévu. 

Y a 7 R. Je vais pas tous les noter.

Bien checker quelles sont les ressources dont on aura besoin 

## Exploitation

Comment fournir et gérer nos services ?

- Gestion des évènements
- Gestion des incidents
- Gestion des problèmes
- Gestion des requêtes
- Gestion des accès

## Amélioration continue

en 7 étapes : modèle CSI

# Exercice

Voir énoncé, schéma d'architecture

Les Apache contiennent interfaces web, qui contactent les base derrière, tout est répliqué. Ordonnanceur organise comment se fait tout ça.

40 minutes, en groupe de 5 à 6. Présenter une solution pour cette mis en production.

BUDGET I

## Solution

On monte un environnement de préprod identique à la prod mais sans la supervision. Au niveau des bases, réplique de la prod.

### Mise en prod

 Lancement du script permettant de proprifier la base sur la préprod

On déploie la nouvelle IHM sur la préproduction, on fait les vérifications : tout fonctionne, affichage des docs, compatibilité des versions... Pour détecter tous les problèmes. Une semaine de tests, notamment de charge (simulation de nb de personnes qui se connectent).

Une semaine avant migration, communication auprès du client sur migration et nécessité de com pour conduite changement.  
On prévoit comment revenir en arrière si la mise en prod se passe mal. Besoin de quelqu'un dispo chez eux pendant la mise en prod, et identification des points de contacts pour ce projet. 

Une fois les problèmes corrigés et la préprod validée, on migre la préprod sur la prod. Snapshot de la prod avant mise en prod. Migration en heure non ouvrées (à partir 19h jusqu'à 6h du mat'),  en anticipant à partir du temps qu'on a mis à déployer sur la préprod et en comptant large.

Une fois mis en prod : On regarde avec la supervision, comment  le matos tient la charge avec 2000 utilisateurs (surcharge, critique CPU, RAM...). À partir de ça anticipation de la montée de charge pour un x3.

