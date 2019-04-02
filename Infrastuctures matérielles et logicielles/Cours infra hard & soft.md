# Introduction

Principe du cours : par groupes de 3-4, on passe l'année sur un sujet, avec des présentations régulières au reste de la classe.

# Présentations

## Anti virus

L'antivirus est un logiciel en charge de détecter les logiciels malveillants et douteux (malware), via diverses méthodes 

Plusieurs types de malwares :

- Programmes simples (trojan, spywares, backdoors...)
- Programmes auto-reproducteurs (virus, vers)
- Botnet (IoT, DDOS, cryptomining)
- PUP (adwares)
- Autres (rootkit...)

Fonctionnement :

- Analyses scantime et runtime
- Principes on-demand scanners et/ou On-Access Scanners
- Dictionnaire de données
- Monitoring
- Contrôle d'intégrité
- Analyse spectrale
- Analyse heuristique



## SGBD

Principaux éléments du SGBD :

- Structure mémoire - Mémoires physiques et logiques du serveur
- Processus - Chargement des données en mémoire, gère l'écriture en mémoire des fichiers
- Instances - Créées par les users lorsqu'ils se connectent à la bdd

Il y a plusieurs types de SGBD :

- Relationnels : PostgreSQL, s'inspire d'Oracle, très complet
- autres types : noSQL, MongoDB, neo4J...

SGBD VS Feuille de calcul : pourquoi c'est mieux ?

- Haute disponibilité et répartition des charges
- Multi utilisateurs
- Vérifie l'intégrité des données

## Pare-feu

But : se protéger des intrusions malveillantes et des fuites de sécurité / de données

Intervient sur les couches 3 et 4 du OSI, plus la 7 pour le filtrage applicatif

Le filtrage peut être :

- Stateless : couche 3-4, se fait en fonction du paquet
- Stateful : couche 7, se fait en fonction de l'état de la connexion

Trois types de pare feu :

- Logiciel, le plus répandu, déjà intégré à l'OS/au noyau
- Matériel, lié à la machine réseau (routeur), pas flexible
- Bridge

## OS

Bootloader avant l'OS

1965 : Multies par MIT  
1980 : DOS  
1990 : OS sous licence (Linux)

5 générations : 

- Par lots
- Multitâches
- Temps partagé
- Temps réel
- Systèmes distribués

Les _system calls_ sont des appels système via le shell, possibles une fois l'OS lancé

Les couches :

- Hardware
- Kernel
- Shell
- Applications

Ne pas confondre shell et terminal ! Ce dernier exécute le shell mais n'en est pas un !



## Driver

Permet de faire fonctionner le matériel. Il est souvent embarqué avec l'OS, ou sinon est distribué autrement. **Tout périphérique** en a besoin ! Pour le matos de base (carte graphique, ...) c'est le BIOS qui prend la main.

Les pilotes évitent que l'OS ait à reconnaitre tous les matos, et évite ainsi beaucoup de mises à jour... Ils sont codés par les constructeurs. 

Plug & play : contiennent un BIOS qui communique les infos à l'OS.

Chaque protocole a des pilotes (IP, TCP...)

Types :

- Drivers de masse
- Texte (GPS)
- Spécifiques (vidéo)
- USB (mix plug and play)



## Compilateur

Le compilateur traduit du texte >> il le convertit.

Types ?

- Interpréteurs
- Formateurs de texte
- Préprocesseurs

Fonctionnement :

1. Analyse lexicale : scan du texte qui est regroupé pour former des mots, des blocs, et garde ce qui l'intéresse
2. Syntaxe (backend) : regarde comment sont formés les mots pour en déduire la "grammaire", la structure du texte. Création d'un arbre syntaxique, ou arbre de dépendance.
3. Analyse sémantique : vérifie que la syntaxe est OK puis checke le sens. Regarde le contexte, voit la globalité : est-ce **logique** ?

L'optimisation passe 

- Par la vitesse d'exécution 
- Par la taille du code (minify)

Le code est généré d'abord dans un langage intermédiaire, puis en code binaire pour la machine. À chaque fois il est généré puis optimisé.

*20/12/18*

# Deuxième vague

## OS : La mémoire

J'ai oublié. De. Noter.

### Noël

Avant, pas plus de 640 kilooctets. Du coup les gars se sont dit "bon, bah on prend une page de cette taille, on la rempli, pis si ça fait plus on fait une deuxième page".

Le problème c'est que si quelqu'un arrive à percer le code il a accès à tout. Donc ils ont définit un espace mémoire, t dedans des blocs, qui sont des "segments". chacun avec ses propres règles et des tailles différentes. On a donc du paginé + segmenté.

## SGBD : ACID 

- Atomicité
- Cohérence
- Isolation
- Durabilité

Verrouillage pessimiste : méthode simple qui empêche la modification simultanée des enregistrements. Dit que lorsqu'une transaction se déclenche, on applique un verrouillage explique sur les ressources touchées par les transactions. Verrouillage très restrictif : on ne peut pas lire les éléments ne cours de modifs. Ça peut être problématique si les transactions se "croisent" : elles s'interbloquent. On appelle ça un "verrou mortel".

Verrouillage optimiste : laisse les conflits se faire, puis les résout. Pose une sorte de "tag" (une estampille) sur éléments modifiés, et effectue les accès das l'ordre croissant des accès aux ressources. Lorsqu'il y a conflit, utilise l'ordonnancement. Ce verrouillage est plus rapide mais provoque trop de "reprises" et donc gourmand en ressources.



L'objectif d'un SGBD c'est que les transactions soient sérialisables. Protocole 2PL va permettre à deux entités t1 et t2 d'accéder à une ressources. Deux types de verrous : un verrou partagé et un verrou exclusif. L'exclusif intervient quand on veut faire une modif en écriture sur une ressource : la ressource est alors complètement inaccessible, il faut que l'entité relâche son verrou pour laisser les autres accéder. 2PL est là pour poser les verrous sur toutes les ressources nécessaires et ne les relâche pas jusqu'à ce qu le traitement soit terminé. Pendant ce temps les autres attendent.

### Noël

- optimiste implique du rollback, donc utile quand peu de congestion sur les donnés
- pessimiste utilisé quand utilisé quand beaucoup de transactions sur données en même temps (forte congestion sur les données)

C'est au niveau du commit qu tout se gère : opti/pessi encadre le commit

## Pare-feu : comment voit et gère-t-il les paquets ?

Paquet : données envoyées sur le réseaux découpées en pitits morcaux

Socket : Permet au développeur de manier les outils réseaux. Un socket contient ce qu'il faut pour les protocoles de la couche.

Communication peu être en TCP ou UDP  (connecté / non connecté)  
TCP : socket, bind, listen, accept, recv, send  
UDP : socket, bind, recvfrom

Lorsque le paquet arrivé, il est mis en tampon, ou rejeté. Puis il y a génération ou interruption, on lui alloue le SK_buffer, appelle la fonction et on le met en file d'attente du CPU. Il est ensuite traité au niveau processeur, t c'est ici que le pare feu intervient pour filtrer les paquets : il peut lire ce qui se passe dans le processeur, et en fonction de ses règles il l'accepte ou le rejette.

SK_buffer conserve les données sur les paquets. c'est un objet qui permet à l'OS de se "représenter" le paquet : toutes les données (dont entête, tout ça) qui sont inscrite dedans. 

## Drivers : modules, utilité, fonctionnalités

Modules = morceau de code qui ajoutent fonctionnalité au noyau. On y retrouve différentes fonctions.

On parle uniquement des non plug and play.

Le noyau linux applle différents modules :

- modules de base : protocoles réseau, système de fichier
- modules périphériques : carte mère, vidéo, son réseau
- modules supplémentaires : carte vidéo (non-libre), cartes peu utilisées.

On peut spécifier les modules à charger au lancement du noyau. La liste des fichiers à charger est dans /etc/module . On peut aussi l'empêcher d'en charger : /etc/mprob/blacklist.conf

Il y a une structure file_operation qui permet de s'y retrouver dans l'orga communautaire de Linux

Les fichiers .ko sont des Kernel Objects chargeables parle noyau. plusieurs commandes permettent d'agir sur les modules chargés par le noyau.

### Noël

Le lien entre le fichier de code et le matériel se fait par un BUS qui va donner une adresse physique de périphérique. IRQ (Interrupt ReQuest), DMA (Direct Memory Access, zone de mémoire attribuée à un périphérique). Le kernel interagit avec le matériel via ces éléments là.

## Compilateur : analyse lexicale

C'est la première partie de la compilation, le point d'entrée, juste après le source code.

Un analyseur lexical est un automate fini

### Les REGEX

...explique ce que c'est.

### Les automates

DFA automate fini déterministe

NFA fini non déterministe

# Troisième vague

## Antivirus

J'ai rien noté, c'est nous qu'on est passés

## OS : l'ordonnancement

### Politiques d'ordonnancement

- Premier arrivé, premier servi : pas le meilleur
- Plus court d'abord : le processus le plus court passe en prio. Assez efficace mais nécessite de savoir le temps du process, ce qui peut être copliqué
- Par priorité : l'OS détermine une prio par process
- Tourniquet (round Robin) : marche pour les OS à temps partagé

### Fork

Permet la création dynamique de nouveau processus par le système. Sort de division cellulaire : process père génère un process fils. Notion d'héritage présente : les attributs systèmes sont transmis du parent à l'enfant. Var globales t statiques ne sont pas transmises dans le fork. 

Au démarrage du syst unix, le process INIT arrive et tous les autres process découlent de celui-ci : arborescence.

### Sémaphore

Outil système disposant d'une file d'attente, et d'un système de jetons. Initialement il distribue des jetons par processus, et consomme ces jetons, lorsqu'il n'a plus de jetons ils s'arrête. Il peut aussi réveiller des process.

### Thread

Proche du fork, mais cette fois ci le parent partage variables globales, statiques locales et descripteurs de fichiers avec l'enfant.  C'est finalement un fork avancé.

### Noël

Le fork crée un autre process parallèle.

Le thread a un flux d'activité (maître), fait une copie avec la data du flux : reprise de l'exécution à partir de là ou s'ne était arrêté la première. Ce qui est intéressant c'est que le thread, une fois fini, peut potentiellement revenir sur la branche maître. 

## SGBD 

Le SGA : Global System Area

Zones de mémoire les plus imporante : shared pool et 

### PGA  : process global area

Zone ou on stocke informations sur tout ce qui est SQL : le curseur... zone de travail pour executer le SQL.

Elle est alloué à chaque process, il y a une PGA pour tout ce qu'on veut travailler en mémoire

Comment fonctionnent ces processus ?  Ils sont effectués en mémoire RAM puis synchronisés ensuite via l SGA.

### Noël

Un user qui se connecte crée un UGA, puis ses opérations des PGA dans le UGA. Ces PGA se connectent au SGA.

## Pare feu : Netfilter

S'organise en couches la plus haute : utilisateur, puis les règles (tables), en dessous netfilter, le oyau, qui fait analyse pure du paquet, et enfin matérielle

### tables 

ce sont les entités qui définissent le comportement de netfilter : des chaînes qui sont un ensemble de règles

Il y a des hooks, avec 5 points d'accroche : prerouting, inpout, forward, output, postrouting

# Quatrième vague

## Antivirus



## OS : Le kernel

### Introduction

Développé en C et en assembleur. Fait l'interface entr la couche software et la couche hardware. fournit une interface de programmation pour le matériel. 

Créateur : L. Torvald en 1991. À la base pour une seule archi puis porté sur d'autres type ARM. Multi utilisateur, respecte les normes posix, certaines fonctionnalités peuvent être ajoutées ou envelvées à lavolée. 

### Fonctions

Excécution des processus, gstion mémoire, gestion du matériel...

### Développement

Développé par la communauté originellement, puis de grosse boite s'y sont mises : Red Hat, Intel, IBM...

Sous licence GNU.

### Les types

Le monolithique : conception ancienne et considérée comme obsolète. Un seul gros bloc qui contient toutes les fonctions et pilotes et de quoi les compiler. Concept simple, excellente vitesse d'exécution. Mais forte augmentation de taille avec l temps (ajout de fonctionnalités). 

Pour contrer ce dernier point, création ds monolithiques modulaires : noyau avec fonctionnalités principales, et plein de services différnts sous formes de modules. Tout est centralisé dans un seul noyau, donc une seul erreur dans un service facultatif peut mettr en péril toute la sécurité du système. Meilleures possiiblités de configuration et améliore temps de chargement mais encore des défauts.

Du coup invention des micronoyaux dans les années 90. Le nombre de fonctions principales et les dépendances du noyau est fortement réduite. Donc minimisation des risques d'erreurs pour meilleure robustesse, fiabilité, évolutivité et maintenance. Nécessite par contre un protocole de communication netre les processus (IPC), assez lourd qui finalement réduit les performances.

Enfin on ne arrive au noyau hybride qui combine avantages de monolithique et micronoyaux

### Caractéristiques techniques

le noyau doit être compilé pour être compris en binaire. On a donc besoin des sources et de GCC (Gnu Compiler Collection) qui embarque tous les outils nécessaires. 

On place les sources dans `/usr/src/linux-(version)`, à partir de ces sources on peut compiler le noyau dans `/boot`, et les modules quant à eux sont placés dans `/lib/modules` 

### Les modules

Code ajoutant des fonctionnalités au noyau. Ils sont exécutés dans l'espace mémoire du noyau : contrôle total sur la machine. Depuis version 2, il n'est plus nécessaire de recompiler le noyau pour chagrer un module (chargement dynamique), via `insmod` ou `modprobe`.

## Drivers :  Protocoles de communication

SPI : Sans Protocole d'Interface

Le noyau contient un genre 

### MIDI

Format de fichier lié à la mudsique et utilisé comme potocole pour les instruments

### OSC

Contrôle en temps réel, successeur du MIDI. Open Sound Control

### RS-232

Norme ultra standard : le port série. N'est plus trop d'actualité, enfin si, enfin ça dépend des matos.

### DMX

Protocole pour le raccordement des lumières. Avant 86 c'était de l'analogique.

### SPI

Différents protocoles de communication selon le SPI.  Master/slave, ou via l'horloge, peut être généré par le maître ou l'esclave. Le kernel dit au matos/logiciel où trouver l'info, ou dit à un truc de donner l'info au matos/logiciel

## SGBD : Systèmes d'indexation

Dans les SGBD relationnels

### Définition

Aide à retrouver facilement et rapidement les données.

Exemple des panneaux dans un supermarché : permet de retrouver plus vite où sont les produits.

L'index indique donc où on peut trouver une donnée.

### Quand utiliser un index

Il faut calculer la Sélectivité, si elle est inférieure à 15% des lignes, c'est intéressant, sinon ça prendra plus de temps de faire un index.

$ sélectivité\ = \frac{Cardinalité}{Nombre\ total\ de\ lignes}$ 

L'optimiseur : pour une requête, regarde et retient toutes les actions qu'il a fallu faire pour obtenir la données, et calcule un coût pour la requête. Ensuite, quand on l'interroge, il dit comment on peut optimiser le coût de la requête, en mettant un index sur certaines colonnes par exemple. Attention, il peut aussi se tromper (rarement), on peut alors le forcer à utiliser un autre index.

### Différents types d'index

#### Le B tree

C'est un arbre hiérarchique équilibré. Par rapport à un arbre normal, se base plutôt sur un concept de "racine + branche" et de "feuilles"

#### Le bitmap

Destiné aux colonnes avec peu de valeurs distinctes et beaucoup d'enregistrement. Codé sur un bit (vrai ou faux) pour chaque entrée

Donc chacun est plus ou moins efficace en fonction de la cardinalité. 

#### Index par hashage

on accède à la valeur par la clé , construction d'un tableau sans ordre. Il peut y avoir collision entre les clés de hashage, il faut donc mettre en place un système de résolution de collision pour gérer ces cas. Et bien choisir sa fonction de hashage pour pas se niquer en temps de calcul.

## Pare-feu : IDS

Intrusion Detection System

Logiciel qui fait de la détection d'intrusion : sniffe le réseau et détermine si qqch de suspect dessus. Utilisé en complément du pare feu et des antivirus.

### Ce qu'il fait

Surveille routeur, pare feu et les services

Permet de rendre plus clair des trucs via une interface.

Signale quand sécurité est violée, peut bloquer des intrusions.

### avantages

donne de la visibilité, automatise des tâches de surveillance, surveille les applications et les réseaux 

### 3 familles, 2 techniques

NIDS : Network tournent en mode passif en utilisant de sports miroir

HIDS : Host ids surveillent réseau pour voir si compromis

Hybrides : regardent sur machines plus que réseau

Deux types d'approches : soit par signature soit par huristique, comme antivirus

### techniques

Comme celles des antivirus : scanne le réseau, vérifie si signatures correspondent à ses règles. Lance alertes en fonction de c qu'il a trouvé. Nécessite d'avoir une base ultra à jour, pas méga fiable.

Combiné donc avec analyse heuristique, l'IDS apprend en fonction du comportement du réseau, ce qui est normal et ce qui ne l'est pas. Gros travail d'origine à fournir pour indiquer ce qui est normal et ce qui ne l'est pas. 

### NIDS

Analyse de manière passive les flux entrant et détecter intrusions en temps réel. Écoute tout le trafic réseau. Le NIDS est une machine à parti qui rajoute pas de la charge. Très efficace.

### HIDS

Analyse plus le trafic réseau mais uniquement le flux sur une machine. Vérifie intégrité des données mais a besoin d'un système sain. 

### Softwares

NIDS : snort, bro, suricata, check point

HIDS : Fail2ban, rkhunter, chkrootkit

### Hybrides

Généralement utilisés dans envirnnements décentralisés. réunissent infos provenant de NIDS comme HIDS

### KIDS, KIPS

Systèmes de prévention d'intrusion Kernel.

Encore plus sécurisé et complémentaire à l'IDS. Peuvent faire pas mal de trucs mais solution rares qui utilisent des serveurs, des machines à part. 



Nombreuses technologies complémentaires à voir sur PDF, dans l'objectif de décourager le hacker.

Pour le temps d'apprentissage n heuristique, faut bien compter 3 mois (commencer en IDS, pis au bout de 3 mois passer en IPS)

## Compilateur : Analyse syntaxique

Après l'analyse lexicale

Construit un arbre des relations grammaticales entre les mots. 

Il définit ce qu'est un sujet, un verbe.. donc un objets, une classe... ?

### Rôle

prépare la traduction : si des mots sont pas compwris, communication possible via la table des symboles.

### Grammaires



# Cinquième vague

## SGBD : Exécutions SQL

### 

1.

D'abord, ordre donné. Avant de l'exécuter, le moteur vérifie la syntaxe, puis la sémantique (l'utilisateur a t il le droit?...), la requête a t elle déjà un plan d'exécution (dans le SGA) ?

2.

Puis optimisation : bind variables. SQL sensible à la casse, et pour une mêùme variable en min et maj, il est obligé de faire un hard pass ce qui est très couteux. Les bind variables font un truc qui permet d'économiser des ressources.  
Elle permet de créer un seul et unique arbre de résolution de requête qui va être actualisé avec les nouvelles valeurs, autrement SQL créerait un nouvel arbre à chaque fois.

3.

Exécution du plan sélectionné.

En complément :

les hints. Syntaxe spécifique qui va permettre d'exécuter d'une façon spécifique, par exemple en demande un parcours complet de la table.  
Plusieurs listes et jointures possibles listés sur le PDF  
l'optimiseur : il aide et assiste. SQL TUNING ADVISOR donne des indications sur comment opti sa bdd



Le CBO a de meilleures perfs mais a besoin de métadonnées sur les tables utilisées.Pour cela, Oracle a des tables cachées de stats sur les tables utilisables. Avant c'était RBO : rule-based organisation



### OS : Gestion des péripériques

Intro : udev gestionnaire de périph du kernel linux depuis 2.6

Concepts:

- /dev contient les périphériques sous forme de fichier
- udev nouveau système qui permet de les gérer là
- 

Règles :

elles permettent de 

- changer nom périph
- plein d’autres sur pdf

fichiers dans /etc/udev/rules.d

. on peut avoir plein de fichiers d'extension .rules

un périphérique peut être contrôlé par plusieurs règles

Sysfs quand Gaul le dit in dirait qu'il dit "si ses fesses". Exemple : "si, ses fesses on peut faire plein de choses avec".

Il est par exemple possible grâce aux règles udev de faire un script qui se déclenche en fonction du numéro de s"ri d'un périph branché. Mais ça marche pas toujours.

### Pare-feu : WAF WAF

J'étais pas là

### Drivers : Drivers Windows, signatures et certificats

C'est maintenant obligatoire sous Windows depuis Vista.

La signature vérifie si tout est approuvé, le logiciel, l'éditeur, et si y a 0 modifs depuis la certification.Pour obtenir un certif, on se rapproche d'une autorité de certif. Les certifs et centre approuvés sont regroupé dans une bibliothèque gérée par Windows.