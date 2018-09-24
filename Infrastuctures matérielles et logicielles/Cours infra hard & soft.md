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