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