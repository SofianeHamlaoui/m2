# Anti virus

## Présentation

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

## L'Algorithme AHO-CORASICK

### 1 - Qu'est-ce que Aho Corasick ?

- Algorithme de recherche de mot (String-searching algorithm). Qui sert à rechercher toutes les occurrences d’un nombre arbitraire de motifs (ou mots-clés) dans un flux d’information (un texte).
- Inventé par Alfred Aho & Margaret J.Corasick en 1975 - "Efficient string matching: An aid to bibliographic search".
- Usage :
  -  Signature based anti-virus.
  -  Deep Packet Analyzer (DPA - détection / prévention d'intrusion).
  - GPU (GTX 285 – optimisation accès mémoire).
  - Fuzzification (Tentative d'implémentation dans un "système flou").
  - Détection d'attaque par injection.
- Automate fini non déterministe
  - Automate : c'est une machine abstraite au fonctionnement programmé passant par des changements d'état
  - Fini : il contient un nombre fini d'états, sa mémoire a des limites. Il part d'un état initial et passe par une succession d'états pour aboutir sur un état final.
  - Non-déterministe : parce qu'il n'est pas déterministe : à chaque état il peut y avoir une à plusieurs transitions. Un déterministe n'en aura qu'une seule : en partant d'un état et pour une lettre, il n'y a qu'un seul chemin possible.

### 2 - Fonctionnement

C'était tout à l'oral, si personne a pris de note pendant nos exposés vous êtes dans la merde les gars. Nous on sait comment ça marche.

## Offuscation et Polymorphisme

### Qu'est-ce que l'offuscation et le polymorphisme ?

#### Offuscation

- Procédé pour rendre du code impénétrable (raison malveillante ou éviter rétro-ingénierie).
- Difficilement compréhensible pour un humain.
- Mais, compilable pour un ordinateur.

Le code impénétrable d'un programme informatique est un code dont la compréhension est très difficile pour un humain tout en restant parfaitement compilable par un ordinateur.

Plusieurs raisons :

- protéger les investissements de développement d'un logiciel par des techniques de génération de code objet rendant plus difficile la rétro-ingénierie. 
- Code malveillant.

Deux formes : 

- le code objet généré à fin de distribution d'un programme
- le code source. 

#### Polymorphisme

- Sens propre : capacité à se présenter sous différentes formes.
- Virus : modifie sa représentation lors de sa réplication.

Modification du code d'un virus sans modifier son fonctionnement. La plupart des logiciels antivirus tentent d'identifier un virus en recherchant sa signature. Le polymorphisme de certains virus empêche la définition de telles signatures. Car il n'existe plus de séquence invariable suffisamment longue pour être spécifique au virus. Le code viral dispose d'un moteur de codage et de décodage en fonction de la technique employée afin de varier son code. 

Cependant, ce moteur constitue en lui-même une invariance généralement utilisée par les éditeurs d'antivirus afin de donner une signature sur les code viraux, ce problème est alors traité par une catégorie spécifique appelée virus métamorphes.

###  Le polymorphisme

- Le virus polymorphe :  ninja des bases virales
- La mutation, cette inconnue
  - Par chiffrement
  - Par métamorphisme

### Fonctionnement d'un RunPE

#### Problématique des ‘black-hats’

- La problématique d’un utilisateur malicieux est d’exécuter son code malveillant sans éveiller les soupçons de l’antivirus
- Bypasser les méthodes de scans des antivirus :
  - Scantime : éviter la détection par l’AV du fichier sur le disque dur
  - Runtime : éviter la détection par l’AV du malware en tant que processus actif

#### Objectifs d’un RunPE

Buts :

- bypass scantime : chiffrement du code malveillant sur disque
- bypass runtime : injection du code malveillant dans un processus légitime (calc.exe, svchost.exe…)

Problèmes :

- Un code chiffré est ininterprétable par l’OS
- Nécessite un ‘loader’ (le RunPE) pour l’injection

#### Structure d'un fichier Portable Executable

- Un fichier Portable Exécutable est un fichier .exe
- Permet au système d'exploitation (ici Windows) de :
  - Charger l'executable
  - Charger les librairies nécessaires (user32.dll, gdi.dll...)
  - Naviguer entre les différentes sections de code qu'il contient, organisées lors de la compilation du programme

#### Workflow d’un RunPE

1. Lecture du malware.exe chiffré
2. Déchiffage, via clé de déchiffrement, directement en RAM
3. Analyse du fichier malware.exe au format PE (toujours en mémoire)
4. Récupération des sections et leur taille du malware.exe (toujours en mémoire)
5. Lancement de calc.exe en mode suspendu
6. Récupération des registres processeur du processus calc.exe
7. Récupération de l’adresse mémoire de base de calc.exe
8. Unmapping des sections de code de calc.exe
9. Allocation d’espace mémoire de la taille de malware.exe, dans calc.exe
10. Ecriture des sections de code malware.exe dans calc.exe
11. Modification d’AddressOfEntryPoint de calc.exe pour pointer sur les nouvelles sections de code (malveillant) 
12. Modification de calc.exe pour passer de l’état suspended à running
13. Le code du malware.exe a été injecté en mémoire dans calc.exe et fait ses affaires

### Résumé

- On charge en mémoire RAM le malware chiffré
- On le déchiffre en RAM
- On l’analyse en RAM (sections de code, taille en bytes…)
- On lance un logiciel légitime non suspicieux par les AV (explorer.exe, calc.exe…) en suspendu 
- On supprime le code du logiciel quand il a été chargé en RAM
- On remplace le code légitime par le code du malware
- On ‘dé-suspend’ l’état du processus légitime (running) et son exécution va continuer… en chargeant le code du malware

### Problèmes d’un RunPE

- Un RunPE embarque souvent lui-même le code du malware, chiffré en AES-256, 3DES…
- AV sensibles aux fichiers .exe embarquant avec eux un payload chiffré
- Tip (testé par moi-même) : leurrer les antivirus en modifiant le code chiffré, par exemple en ajoutant un fakeheader JPEG au code…
  - Code du malware chiffré en hexa : 49 46 FF DB E4 A6 => Un .exe qui embarque des données chiffrées ?! ALERTE
  - Code du malware avec entête JPEG : FF D8 FF 49 46 FF DB E4 A6 => Mouais c’est une tête JPEG, c’est OK !

## Virus par cavité et par recouvrement

### Qu'est-ce qu'un virus par cavité et par recouvrement ?

#### 1 – Virus par recouvrement

- Technique archaïque utilisée par virus et vers
- Infecte les fichiers exécutables
- Destructeur (un vrai verre de lait....)
- Vole le travail du programme infecte - "they took our job"
- One shot
- N'est pas dans la ram de la machine
- Faible contre du contrôle d'intégrité

#### 2 – Virus par cavité

- Technique utilisé par virus et vers
- Infecte les fichiers exécutables
- Fourbe (pas destructeur)
- Développement parallèle avec 32bits
- Connait d'avance la structure des programmes
- Morcelle son code là où il y a des zéros binaires
- Faible contre du contrôle d'intégrité

### Fonctionnement du recouvremment

1. Se met a la place du code de l'exe
2. Le virus pourri l'exe
3. L'utilisateur lance l'exe
4. Le virus se lance
5. L'exe se lance pas
6. L'utilisateur clique 20 fois sur l'exe
7. Il dit que rien marche et l'informatique c'est caca

### Exemple de recouvrement

- BadGuy: les 264 premiers octets des fichiers com sont tous ecrasés
- W32/HLL.ow.Jetto: les 7170 premiers octets de chaque fichier sont ecrasés
- Linux/Radix.ow:comme w32/hll.ow.Jetto mais pour les pingouins
- Tri reboot,trivial.88.D,VBS/Entice.ow

### Fonctionnement de la cavité

1. Cherche des programmes pouvant l'accueilir chaudement
2. Modifie le point d'entrée du programme
3. Insère son code dans les partie 'libre' ou 'a vide'
4. Se morcelle dans le programme
5. N'altere pas le fonctionnement du programme
6. L'utilisateur l'exécute

## Analyse comportementale et mode sandbox

### Analyse comportementale (généralité)

- Cherche à aller au-delà des limites du Pattern-Matching (qui recherche des signatures au sein des fichiers).
- Basé sur un processus d'apprentissage (Machine Learning). 
- Deux types :
  - Analyse comportementale des virus ou code malveillant.
  - Analyse comportementale des utilisateurs (User Behavior Analytics).

#### Analyse comportementale (utilisateurs)

- Détection des comportements anormaux ou susceptible de générer un contexte de vulnérabilité.
- Idée d'analyser "l'historique de vie" après l'infection du système afin de minimiser les risques futurs. 
- Idée aussi de corriger les défaillances liées aux utilisateurs (système de Dashboard / d'alerte). 

### Analyse comportementale (virus)

- Idée de détecter et de supprimer la menace avant qu'elle ne s'exécute. 
- Basé sur l'analyse du fichier, le moyen de transport et toutes autres informations disponibles sur ce fichier. 
- Système de détection et de classification des virus.

- Exemple de la solution "VPS" d'ISS : 
  - Le code malveillant va s'exécuter sur une machine virtuelle, sans causer de dommage (sandbox). 
  - L'algorithme de la solution VPS va analyser le comportement du code malveillant en profondeur.
  - Va comparer le comportement à des scénarios d'attaque et générer une signature dynamique.
  - La prochaine fois que ce code malveillant ou une variante se présentera, il sera supprimé avant de pouvoir s'exécuter. 

### Mode sandbox

- Environnement virtuel contrôlé pour évaluer les risques
- Piège passif : le code exécuté ne se rend (idéalement) compte de rien
- Principale limite : si le malware s'en rend compte, c'est foutu
- Le mode Sandbox selon ISS : logs et machine learning

### Cukoo

- Framework d'analyse automatisé de fichiers
- Python !  pip install -U cuckoo
- Environnement sandboxé mais réaliste
- Analyse plusieurs types de fichiers (.exe, .pdf, .docx...) sous plusieurs environnement virtualisés (Windows, Mac OS et Android)
- Trace les appels aux API (LowLevelKeyboardProc, ZwUnmapViewOfSection…)
- Dump et analyse le trafic réseau, avec MITM pour SSL/TLS. Peut transmettre le trafic réseau sur une interface réseau
- Analyse RAM avec YARA
- malwr.com : site basé sur Cuckoo mais en rework depuis des  mois...
- https://cuckoo.cert.ee en moins bien


#  SGBD

##  Présentation

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

## Verrouillage 

### ACID 

- Atomicité
- Cohérence
- Isolation
- Durabilité

### Verrouillage pessimiste 

- Verrouille l'enregistrement au moment de son édition
- Libéré après validation des changements

Avantages

- Permet d'éviter les conflits
- Utilisé lorsqu'il y a beaucoup de monde

Inconvénients

- Possibilité de verrous mortels 
- Moins rapide que les verrous Optimistes

Méthode simple qui empêche la modification simultanée des enregistrements. Dit que lorsqu'une transaction se déclenche, on applique un verrouillage explicite sur les ressources touchées par les transactions. Verrouillage très restrictif : on ne peut pas lire les éléments en cours de modifs. 

Empêche que les transactions se "croisent" : elles s'interbloquent. On appelle ça un "verrou mortel".

### Verrouillage optimiste

Principe : laisser les conflits se produire puis les résoudre

Ordonnancement par estampillage : 

- Conservation de la dernière estampille du dernier écrivain et plus jeune lecteur
- Effectue les accès dans l'ordre croissant des estampilles (lecture / écriture)

Avantages : 

- Contrôle simple par ordonnancement des accès
- Reprise à partir de la transaction ayant créé le désordre

Inconvénients :

- l'ordonnancement des transactions provoque beaucoup trop de reprises
- Les possibilités d’amélioration sont difficiles à mettre en place

Piste d'amélioration :

- Conservation d'anciennes version des objets pour les accès en lecture

Laisse les conflits se faire, puis les résout. Pose une sorte de "tag" (une estampille) sur éléments modifiés, et effectue les accès dans l'ordre croissant des accès aux ressources. Lorsqu'il y a conflit, utilise l'ordonnancement. Ce verrouillage est plus rapide mais provoque trop de "reprises" et donc gourmand en ressources.

### 2PL : 2 Phase Locking

L'objectif d'un SGBD c'est que les transactions soient sérialisables. 

Fonctionnement : Une transaction suit le protocole 2PL si le verrouillage peut être effectué en 2 phases :

- Growing phase
- Shrinking phase

Protocole 2PL va permettre à deux entités t1 et t2 d'accéder à une ressources.

Deux types de verrous : un verrou partagé et un verrou exclusif.  
L'exclusif intervient quand on veut faire une modif en écriture sur une ressource : la ressource est alors complètement inaccessible, il faut que l'entité relâche son verrou pour laisser les autres accéder. 2PL est là pour poser les verrous sur toutes les ressources nécessaires et ne les relâche pas jusqu'à ce que le traitement soit terminé. Pendant ce temps les autres attendent.

### Noël

- optimiste implique du rollback, donc utile quand peu de congestion sur les donnés
- pessimiste utilisé quand beaucoup de transactions sur données en même temps (forte congestion sur les données)

C'est au niveau du commit que tout se gère : opti/pessi encadre le commit

## Structures mémoire

### Sommaire

- Les structures en mémoire vive
  - SGA (System Global Area)
  - PGA (Program Global Area)
  - Les processus en mémoire
- Algorithme LRU
- Le stockage sur disque
  - Les fichiers de données
  - Les journaux de transaction
- Synchronisation entre mémoire vive et mémoire persistante

### SGA : Global System Area

Zones de mémoire les plus imporante : shared pool et 

### PGA  : process global area

Zone ou on stocke informations sur tout ce qui est SQL : le curseur... zone de travail pour executer le SQL.

Elle est alloué à chaque process, il y a une PGA pour tout ce qu'on veut travailler en mémoire

Comment fonctionnent ces processus ?  Ils sont effectués en mémoire RAM puis synchronisés ensuite via le SGA.

### Noël

Un user qui se connecte crée un UGA, puis ses opérations des PGA dans le UGA. Ces PGA se connectent au SGA.

## Systèmes d'indexation

### Définition

Aide à retrouver facilement et rapidement les données.

Exemple des panneaux dans un supermarché : permet de retrouver plus vite où sont les produits.

L'index indique donc où on peut trouver une donnée.

" Un index est une structure de données utilisée et entretenue par le système de gestion de base de données (SGBD) pour lui permettre de retrouver rapidement les données. L'utilisation d'un index simplifie et accélère les opérations de recherche, de tri, de jointure ou d'agrégation effectuées par le SGBD.    "

### Quand utiliser un index

Il faut calculer la **Sélectivité**, si elle est inférieure à 15% des lignes, c'est intéressant, sinon ça prendra plus de temps de faire un index.

$ sélectivité\ = \frac{Cardinalité (ldx)}{Nombre\ total\ de\ lignes}$ 

- Si sélectivité de la requête < 15 % des lignes 
- Tables de gros volume
- Beaucoup de valeurs NULL
- Colonne souvent utilisée dans WHERE ou en tant que pivot de jointure
- 2 colonnes ou plus utilisées ensemble dans un WHERE ou pivot de jointure

**L'optimiseur** : pour une requête, regarde et retient toutes les actions qu'il a fallu faire pour obtenir la données, et calcule un coût pour la requête. Ensuite, quand on l'interroge, il dit comment on peut optimiser le coût de la requête, en mettant un index sur certaines colonnes par exemple. Attention, il peut aussi se tromper (rarement), on peut alors le forcer à utiliser un autre index.

- L'optimiseur aide à définir des index performants 
  - Ce n'est cependant pas une parole d'évangile !
  - On peut utiliser les "hint" pour guider l'optimiseur
- Créer un index mal choisi est nuisible aux performances
- Un index doit être maintenu (usable / unusable , mises à jour...)
- Un index augmente la charge des mises à jour, l'espace de stockage nécessaire
- Les SGBD créent des index automatiquement sur PRIMARY KEY, CONTRAINTES UNIQUE

### Différents types d'index

#### Le B tree

C'est un arbre hiérarchique équilibré. Par rapport à un arbre normal, se base plutôt sur un concept de "racine + branche" et de "feuilles"

- Arbre B hiérarchique équilibré
- Notion de taille maximale
- Stock un pointeur vers l'enregistrement RowID

#### Le bitmap

Destiné aux colonnes avec peu de valeurs distinctes et beaucoup d'enregistrement.   
Codé sur un bit (vrai ou faux) pour chaque entrée

Donc chacun est plus ou moins efficace en fonction de la cardinalité. 

### Index basés sur les fonctions

- Index B-Tree et bitmap peuvent être basés sur des fonctions
- Index sur des fonctions / expressions (pas directement sur un champ)
  - Fonction :   UPPER(champs)
  - Expression :  12 * salaire * commission 
- Valeurs précalculées donc gain de temps à la sélection (CLAUSE WHERE) 

#### Index par hashage

- Utilisation d'un tableau ne comportant pas d'ordre
- Accède à la valeur par la clé (fonction de hashage)

Avantages :

- Index par hashage est très performant pour les recherches d’égalité (= ou <>)
- Permet un accès direct à un enregistrement dans le cas des valeurs uniques

Inconvénients :

- Collision possible entre les clés de hashage
- Deux valeurs peuvent donner la même clé

Préconisations :

- Bien choisir sa fonction de hashage : rapidité de calcul, espace réservé au hashage, réduction de risque de collision
- Mise en place d'un système de résolution de collision ( stockage de la paire clé-valeur)

on accède à la valeur par la clé , construction d'un tableau sans ordre. Il peut y avoir collision entre les clés de hashage, il faut donc mettre en place un système de résolution de collision pour gérer ces cas. Et bien choisir sa fonction de hashage pour pas se niquer en temps de calcul.

## Exécutions des requêtes

1. ### Parcourir le texte

D'abord, ordre donné. Avant de l'exécuter, le moteur vérifie la syntaxe, puis la sémantique (l'utilisateur a t il le droit?...), enfin si l'ordre a déjà été exécuté : la requête a t elle déjà un plan d'exécution (dans le SGA) ?

2. ### Optimisation : les bind variables

SQL sensible à la casse, et pour une mêùme variable en min et maj, il est obligé de faire un hard pass ce qui est très couteux. Les bind variables font un truc qui permet d'économiser des ressources  
Elle permet de créer un seul et unique arbre de résolution de requête qui va être actualisé avec les nouvelles valeurs, autrement SQL créerait un nouvel arbre à chaque fois.

Génération de plusieurs plans d'exécution :

- Parcours approfondi au moins une fois de chaque requête 
- Les ordres DDL ne comportant pas de composants DML ne sont jamais optimisés
- La génération des différents plans à lieu à cette étape
- Depuis la V7 d'Oracle : CBO : Cost Based Optimizer
  - Ne privilégie pas un type de jointure particulier
  - Ne s'occupe pas de l'existence d'index

Puis sélection du plan d'exécution

3. ### Exécution du plan sélectionné.

### Compléments

hints = Syntaxe spécifique qui va permettre d'exécuter d'une façon spécifique, par exemple en demande un parcours complet de la table.  

Plusieurs listes et jointures possibles :

- Séquentiel : FULL SCAN
- Adresse mémoire de la ligne : BY INDEX ROW ID
- Lecture index: INDEX RANGE SCAN
- Jointure de HASHAGE : HASH JOIN
- Jointure de fusion : MERGE JOIN

l'optimiseur : il aide et assiste. SQL TUNING ADVISOR donne des indications sur comment opti sa bdd

### Noël

Le CBO a de meilleures perfs mais a besoin de métadonnées sur les tables utilisées. Pour cela, Oracle a des tables cachées de stats sur les tables utilisables. Avant c'était RBO : rule-based organisation

# Pare-feu

## Présentation

But : se protéger des intrusions malveillantes et des fuites de sécurité / de données

Intervient sur les couches 3 et 4 du OSI, plus la 7 pour le filtrage applicatif

Le filtrage peut être :

- Stateless : couche 3-4, se fait en fonction du paquet
- Stateful : couche 7, se fait en fonction de l'état de la connexion

Trois types de pare feu :

- Logiciel, le plus répandu, déjà intégré à l'OS/au noyau
- Matériel, lié à la machine réseau (routeur), pas flexible
- Bridge

## Gestion des paquets

Paquet : données envoyées sur le réseaux découpées en pitits morcaux

Socket : Permet au développeur de manier les outils réseaux. Un socket contient ce qu'il faut pour les protocoles de la couche.

Communication peu être en TCP ou UDP  (connecté / non connecté)  
TCP : socket, bind, listen, accept, recv, send  
UDP : socket, bind, recvfrom

Lorsque le paquet arrivé, il est mis en tampon, ou rejeté. Puis il y a génération ou interruption, on lui alloue le SK_buffer, appelle la fonction et on le met en file d'attente du CPU. Il est ensuite traité au niveau processeur, t c'est ici que le pare feu intervient pour filtrer les paquets : il peut lire ce qui se passe dans le processeur, et en fonction de ses règles il l'accepte ou le rejette.

SK_buffer conserve les données sur les paquets. c'est un objet qui permet à l'OS de se "représenter" le paquet : toutes les données (dont entête, tout ça) qui sont inscrite dedans. 

## Netfilter

### Définition

- C’est un module noyau
- C’est le pare-feu de linux
- Il fonctionne de paire avec sk_buffer
- Netfilter = filtrage et routage des paquets

Ne pas confondre avec IP table, une interface de netfilter

S'organise en couches la plus haute : utilisateur, puis les règles (tables), en dessous netfilter, le oyau, qui fait analyse pure du paquet, et enfin matérielle

### tables 

ce sont les entités qui définissent le comportement de netfilter : des chaînes qui sont un ensemble de règles

- Filter : permet le rôle de pare-feu en supprimant ou acceptant le paquet
- Nat : permet le rôle de passerelle en masquant les adresses des paquets
- Mangle : permet de faire de la QoS en marquant les paquets
- Raw : permet de contourner le suivi de connexion

### Chaines

Les chaînes sont des ensembles de règles que nous allons écrire dans chaque table. 
Ces chaînes vont permettre d'identifier des paquets qui correspondent à certains critères.

- INPUT : Connexions à destination du pare-feu
- OUTPUT : Connexions depuis le pare-feu
- FORWARD : Connexions transitant entre deux interfaces réseau
- PREROUTING : Modification de l'adresse de destination (DNAT)
- POSTROUTING : Masquage d'adresse par modification de l'adresse source (SNAT)

### Cibles

- DROP : Détruit le paquet
- ACCEPT : Autorise le paquet
- REJECT : Refuse le paquet et le signale à son expéditeur
- MASQUERADE : Masque l'origine du paquet pour lui permettre de circuler d'un réseau à un autre
- LOG/ULOG : Les caractéristiques du paquets sont journalisé dans un fichier ou vers le processus ulogd
- MARK : marque le paquet en y ajoutant une information

### Hooks

Cinq points d'accroche :

- NF_IP_PRE_ROUTING  Chaînes PRESROUTING 

- NF_IP_LOCAL_IN  Chaînes INPUT

- NF_IP_FORWARD  Chaînes FORWARD

- NF_IP_LOCAL_OUT  Chaînes OUTPUT

- NF_IP_POSTROUTING  Chaînes POSTROUTING

### Cheminement

Le paquet est d’abord inspecté pour savoir sa source et sa destination. Le firewall confronte ces informations avec ses propres règles et détermine s’il s’agit d’un paquet « en transit » ou directement pour lui.

Si le paquet lui est adressé il est confronté au filtre INPUT sinon il passera dans le filtre FORWARD.

Si le paquet sort du firewall c’est la chaîne OUTPUT qui est concernée.

### Les règles

- Par iptables
- Permet de d'ajouter, supprimer, modifier et afficher les règles utilisée par Netfilter 

## IDS

Intrusion Detection System

Logiciel qui fait de la détection d'intrusion : sniffe le réseau et détermine si qqch de suspect dessus. Utilisé en complément du pare feu et des antivirus.

### Ce qu'il fait

- Surveille : 
  - Routeur
  - Pare-feu
  - Tout service de prévention des cyberattaques.
- Rendre plus clair, faciliter le paramétrage, organiser les processus d’audit et logs des système d’exploitation.
- Signaler quand certains fichiers ou données sont modifiées.
- Signaler quand la sécurité d’un système est violée
- Réagir aux intrusions en les  bloquant par exemple.

### Avantages

- Visibilité
- Facilité de sécurisation de son SI
- Automatisation
- Surveillance d’application, de réseau (LAN), internet (WAN)

donne de la visibilité, automatise des tâches de surveillance, surveille les applications et les réseaux 

### 3 familles, 2 techniques

Les grandes familles :

- NIDS  : Network tournent en mode passif en utilisant de sports miroir
- HIDS : Host ids surveillent réseau pour voir si compromis
- Hybrides : regardent sur machines plus que réseau

Les 2 types d'IDS :

- Approche par signature
- Approche heuristique

### Techniques

- L'analyse de signatures :
  - Similaire aux antivirus
  - Utilise une base de signatures
  - Nécessite des mises à jours régulières
- L'analyse heuristique :
  - Analyse comportementale
  - Nécessite un temps d'apprentissage
  - Sujet aux faux positifs

Comme celles des antivirus : scanne le réseau, vérifie si signatures correspondent à ses règles. Lance alertes en fonction de ce qu'il a trouvé. Nécessite d'avoir une base ultra à jour, pas méga fiable.

Combiné donc avec analyse heuristique, l'IDS apprend en fonction du comportement du réseau, ce qui est normal et ce qui ne l'est pas. Gros travail d'origine à fournir pour indiquer ce qui est normal et ce qui ne l'est pas. 

### Les systèmes de détection d'intrusions « réseau » (NIDS)

- Objectif : analyser de manière passive les flux en transit sur le réseau et détecter les intrusions en temps réel.
- Un NIDS écoute donc tout le trafic réseau, puis l'analyse et génère des alertes si des paquets semblent dangereux.
- Les NIDS étant les IDS plus intéressants et les plus utiles du fait de l'omniprésence des réseaux dans notre vie quotidienne.

Analyse de manière passive les flux entrant et détecter intrusions en temps réel. Écoute tout le trafic réseau. Le NIDS est une machine à parti qui rajoute pas de la charge. Très efficace.

### Les systèmes de détection d'intrusions de type hôte (HIDS)

- Un HIDS se base sur une unique machine, n'analysant cette fois plus le trafic réseau, mais l'activité se passant sur cette machine. Il analyse en temps réel les flux relatifs à une machine ainsi que les journaux.
- Un HIDS a besoin d'un système sain pour vérifier l'intégrité des données. Si le système a été compromis par un pirate, le HIDS ne sera plus efficace. Pour parer à ces attaques, il existe des KIDS (Kernel Intrusion Detection System) et KIPS (Kernel Intrusion PreventionSystem) qui sont fortement liés au noyau. Ces types d'IDS sont décrits un peu plus loin.

Analyse plus le trafic réseau mais uniquement le flux sur une machine. Vérifie intégrité des données mais a besoin d'un système sain. 

### IDS Software 

IDS Réseau : (nids ?)

- Snort
- Bro
- Suricata
- Check Point 

IDS Système : (hids ?)

- Fail2Ban
- Rkhunter
- Chkrootkit

### Les systèmes de détection d'intrusions « hybrides »

- Généralement utilisés dans un environnement décentralisé, ils permettent de réunir les informations de diverses sondes placées sur le réseau. Leur appellation « hybride » provient du fait qu'ils sont capables de réunir aussi bien des informations provenant d'un système HIDS qu'un NIDS.
- L'exemple le plus connu dans le monde Open-Source est Prelude. Ce framework permet de stocker dans une base de données des alertes provenant de différents systèmes relativement variés. Utilisant Snort comme NIDS, et d'autres logiciels tels que Samhain en tant que HIDS, il permet de combiner des outils puissants tous ensemble pour permettre une visualisation centralisée des attaques.

### Les systèmes de prévention d'intrusions « kernel » (KIDS/KIPS)

- Nous l'évoquions précédemment dans le cadre du HIDS, l'utilisation d'un détecteur d'intrusions au niveau noyau peut s'avérer parfois nécessaire pour sécuriser une station.
- Le KIPS peut reconnaître des motifs caractéristiques du débordement de mémoire, et peut ainsi interdire l'exécution du code. Le KIPS peut également interdire l'OS d'exécuter un appel système qui ouvrirait un shell de commandes.
- Puisqu'un KIPS analyse les appels systèmes, il ralentit l'exécution. C'est pourquoi ce sont des solutions rarement utilisées sur des serveurs souvent sollicités.
- Exemple de KIPS : SecureIIS, qui est une surcouche du serveur IIS de Microsoft.

Encore plus sécurisé et complémentaire à l'IDS. Peuvent faire pas mal de trucs mais solution rares qui utilisent des serveurs, des machines à part. 

### Les technologies complémentaires

Dans l'objectif de décourager le hacker.

- Les scanners de vulnérabilités : systèmes dont la fonction est d'énumérer les vulnérabilités présentes sur un système. Ces programmes utilisent une base de vulnérabilités connues (exemple : Nessus).
- Les systèmes de leurre : le but est de ralentir la progression d'un attaquant, en générant des fausses réponses telles que renvoyer une fausse bannière du serveur Web utilisé.
- Les systèmes de leurre et d'étude (Honeypots) : le pirate est également leurré, mais en plus, toutes ses actions sont enregistrées. Elles seront ensuite étudiées afin de connaître les mécanismes d'intrusion utilisés par le hacker. Il sera ainsi plus facile d'offrir des protections par la suite.
- Les systèmes de corrélation et de gestion des intrusions (SIM - Security Information Manager) : centralisent et corrèlent les informations de sécurité provenant de plusieurs sources (IDS, firewalls, routeurs, applications…). Les alertes sont ainsi plus faciles à analyser.
- Les systèmes distribués à tolérance d'intrusion : l'information sensible est répartie à plusieurs endroits géographiques, mais des copies de fragments sont archivées sur différents sites pour assurer la disponibilité de l'information. Cependant, si un pirate arrive à s'introduire sur le système, il n'aura qu'une petite partie de l'information et celle-ci lui sera inutile.

### Conclusion

- IDS est une couche supplémentaire de sécurité bien à part d’un pare-feu ou d’un antivirus.
- Ils sont complémentaires 
- Peut même les « superviser »
- Permet de clarifier, mettre à plat les flux, les comportements, les évènements d’une infrastructure.
- Permet de notifier un changement d’état, une violation de sécurité, un comportement suspect

### Noël ?

Pour le temps d'apprentissage en heuristique, faut bien compter 3 mois (commencer en IDS, pis au bout de 3 mois passer en IPS)

## Filtrage applicatif

### Définition 

- Wikipédia : Dernière génération de pare-feu, ils vérifient la complète conformité du paquet à un protocole attendu. Par exemple, ce type de pare-feu permet de vérifier que seul le protocole [HTTP](https://www.wikiwand.com/fr/Hypertext_Transfer_Protocol) passe par le port [TCP](https://www.wikiwand.com/fr/Transmission_Control_Protocol) 80.
- La parfaite : Le filtrage applicatif permet de filtrer les communications application par application. Il opère au niveau 7 du modèle osi « APPLICATION ».

### Avantages

- Contrôle complet sur chaque service 
- Permet l’installation de procédures d’authentification extrêmement poussées.
- Bien plus faciles à configurer et à tester que pour un firewall filtre de paquets.

### Inconvénients

- Augmentent considérablement le coût du firewall, ce coût étant principalement lié à celui de la plate-forme matérielle de la passerelle, des services proxy et du temps et des connaissances requises pour configurer cette passerelle.
- Les filtres au niveau application ont tendance à réduire la qualité du service offert aux utilisateurs tout en diminuant la transparence du système.
- Une analyse fine des données applicatives requiert une grande puissance de calcul et se traduit donc souvent par un ralentissement des communications . 
- De plus, collecter et analyser  demande aussi une expertise humaine et la mise en place de processus

### Pourquoi ?

Les pare-feu classiques, «réseau » et « UTM », sont pour la plupart totalement aveugles et inefficaces face à ces attaques.

Les nouveaux risques encourus sont les suivants :

- Le déni de service : attaque massive provoquant une indisponibilité de votre site,
- Les tentatives d’intrusion,
- Les vols et remplacement de données sensibles : fichiers clients, données RH, données comptables,…
- L’altération des sites Web, 
- L’utilisation frauduleuse de données bancaires,
- etc.

### Filtrage applicatif type proxy

- Niveau 7 du modèle OSI (Application)
- Requêtes traitées par des processus dédiés.
- Rejet de toutes les requêtes qui ne sont pas conformes aux spécifications d’un protocole (http, https …)

### Solution WAF

Web application Firewall

- Permet de définir et d’appliquer des politiques de sécurité correspondant aux applications web
- Un WAF inspecte chaque paquet de données HTML, HTTPS, SOAP et XML-RPC.
- Généralement déployé via un proxy

D’un point de vue configuration, un WAF pourra opérer suivant deux modes : logging ou blocking.
Dans le mode logging, les requêtes suspectes seront enregistrées, mais pas bloquées. Ce type de configuration est généralement adopté lors de l’installation d’un WAF, pour éviter dans un premier temps les “faux positifs” et donc éviter de bloquer du traffic légitime.​
Dans le mode blocking, les attaques détectées sont bloquées, et le traffic dangereux ne parvient pas à l’application web.

Chaque demande envoyée est d'abord examinée par le WAF avant qu'elle n'atteigne l'application Web. Si cette demande est conforme avec l'ensemble de règles du pare-feu, ce dernier peut alors transmettre la demande à l'application

Les WAF peuvent être installés comme un équipement autonome sur le réseau, comme un logiciel, ou encore connectés à partir d’un service disponible sous forme de service cloud.

### Conclusion

- C’une véritable barrière entre un réseau de confiance et d'autres réseaux de confiance nulle
- Mais ne dispense pas d’ajouter d’autres outils de sécurité :
- ANTIVIRUS
- IDS
- Supervision
- Logs

Mettre en place un firewall applicatif demandera du temps, des compétences et la mise en place de processus pour qu'il soit efficace et ne pénalise pas les utilisateurs.

# OS

## Présentation

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

## La mémoire

### Le Gestionnaire de mémoire

- Un sous-ensemble du système d'exploitation
- Son rôle est de partager la mémoire entre l'OS et les diverses applications
- Le terme "mémoire" fait surtout référence la mémoire principale = la RAM

- La gestion de celle-ci demande la contribution de la :
  1. mémoire auxiliaire (mémoire de masse, spacieuse mais lente)
  2. mémoire cache (rapide mais de taille restreinte).

### Les fonctions du gestionnaire de mémoire 

L'allocation de la mémoire aux processus

- Répertorier les emplacements libres de la mémoire
- Allouer la mémoire nécessaire aux nouveaux processus
- Récupérer la mémoire des processus qui s'achèvent

La protection

- Garantir l’intégrité du Système d’exploitation et des processus
- Utilisation simultanée

La segmentation de l'espace d'adressage

- Pouvoir coder les segments séparément et les paramétrer en fonction de l'application
- Permettre des degrés de protection différents selon les segments ( lecture seule, exécution...)
- Accepter le partage de certains segments.

La mémoire virtuelle

- Elle offre aux applications une mémoire de taille supérieure à celle de la mémoire principale.
- L'espace d'adressage qu'offre la mémoire centrale est parfois insuffisant. 
- Les disques suppléent à cette insuffisance en fournissant une mémoire auxiliaire (plus vaste mais plus lente) 

### Gestion de la mémoire pour systèmes multi-tâches

Partitions fixes

- Les partitions sont de différentes tailles pour éviter que de grandes partitions ne soient occupées que par de petits processus.
- Une file d'attente est associée à chaque partition.
- Une autre solution est de créer une file unique

Partitions variables

Au fur et à mesure que les processus se créent et se terminent, des partitions s'allouent et se libèrent laissant des zones mémoires morcelées et inutilisables. 

### La Pagination

- La mémoire physique est découpé en morceaux linéaires de mêmes taille, appelés case.
- La mémoire virtuelle est divisée en unités de même taille, appelées pages.
- La taille d’une case est égale à la taille d’une page.
- Cette taille est définie par le matériel, en puissance de 2, entre 512 octets et 8192 octets.

Lorsqu’un programme tente d’accéder à une page dans la mémoire virtuelle, le MMU fait correspondre celle-ci au cadre de page correspondant.

### Conversion adresse logique - adresse physique

- L’espace d’adressage du processus est découpé en pages, formé par le couple <numéro de page p, déplacement d>
- Pour faire correspondre une adresse logique en adresse physique, le MMU utilise une structure particulière, la tables des pages.
- Chaque processus a sa propre table de page.

### La Segmentation

- Partage les processus en segments bien spécifiques.
- Chaque objet logique sera désigné par un segment.
- Traduction du couple d'adressage en adresse mémoire par le biais d’une table de segments.
- Adressage de la mémoire par déplacement.

- Les segments sont des entités logiques que le programmeur connaît et manipule.
- Chaques composantes du processus (pile, code, tas, données …) peut avoir son propre segment.
- Gestion des droits sur l’accès aux segments.
- Un segment peut être partagé par plusieurs processus.
- Chaque segment est un espace linéaire.

- La base est l’adresse de début du segment.
- La limite est la dernière adresse du même segment.
- La limite définit la taille de l’adresse de départ.
- L’adresse logique est constituée du numéro de segment et d’un offset.
- Le numéro de segment sert d’index pour retrouver l’adresse du début du segment.
- L’offset ajouté à l’adresse de début de segment pour former l’adresse physique.

Segmentation avec pagination: schéma de la mort.

### Noël

Avant, pas plus de 640 kilooctets. Du coup les gars se sont dit "bon, bah on prend une page de cette taille, on la rempli, pis si ça fait plus on fait une deuxième page".

Le problème c'est que si quelqu'un arrive à percer le code il a accès à tout. Donc ils ont définit un espace mémoire, et dedans des blocs, qui sont des "segments". chacun avec ses propres règles et des tailles différentes. On a donc du paginé + segmenté.

## Les processus sous Linux

Processus : Du latin pro (“vers l’avant”) et cessus, cedere(“aller , marcher”) 

On peut le définir : 

- N'importe quel exécutable exécuté ( tâche en cours d'exécution)
- L’image de l’état du processeur et de la mémoire au cours de l'exécution d’un programme

Au niveau technique:

- Référencés par un identifiant unique, le PID. (utile pour changer la priorité ou arrêter un processus)
- Si le processus 2 a été lancé par le processus 1, on l'appelle un processus fils. Le processus qui l'a lancé est appelé processus parent.
- 3 Etats: Prêt, Élu et Bloqué 

### L'ordonnancement

La fonction d’ordonnancement gère le partage du processeur entre les différents processus en attente pour s’exécuter.

Pour passer de l’état pret à l’état élu l’ordonnanceur utilise l’opération d’élection.

Mode préemptif et non préemptif:

- Non préemptif, transition de l’état élu vers l’état prêt est interdite
- Préemptif, transition de l’état élu vers l’état prêt est autorisé. 

### Politiques d'ordonnancement

- Premier arrivé, premier servi : pas le meilleur
- Plus court d'abord : le processus le plus court passe en prio. Assez efficace mais nécessite de savoir le temps du process, ce qui peut être copliqué
- Par priorité : l'OS détermine une prio par process
- Tourniquet (round Robin) : marche pour les OS à temps partagé

### Fork

Fonction système permettant la création dynamique d’un nouveau processus.

- Division cellulaire
- Le père et le fils
- Principe d’héritage
- processus INIT

Permet la création dynamique de nouveau processus par le système. Sort de division cellulaire : process père génère un process fils. Notion d'héritage présente : les attributs systèmes sont transmis du parent à l'enfant. Var globales t statiques ne sont pas transmises dans le fork. 

Fonctionnement :

- getpid( ) 
- getppid( )
- Allocation d’une entrée à la table des processus
- Allocation d’un PID unique au nouveau processus
- Duplication du contexte
- PID du processus créé 
- retourne 0

Au démarrage du syst unix, le process INIT arrive et tous les autres process découlent de celui-ci : arborescence.

### Sémaphore

Outil système disposant d'une file d'attente, et d'un système de jetons. Initialement il distribue des jetons par processus, et consomme ces jetons, lorsqu'il n'a plus de jetons ils s'arrête. Il peut aussi réveiller des process.

Outil  / structure système composée d’une file d’attente L de processus et d’un compteur K, appelé niveau du sémaphore et contenant initialement une valeur Val.

3 opérations possibles : 

-  INIT (Sem, Val)
- P (Sem) 
- V (Sem) 

Gestion des réveils effectuée en lide FIFO

### Thread

Proche du fork, mais cette fois ci le parent partage variables globales, statiques locales et descripteurs de fichiers avec l'enfant.  C'est finalement un fork avancé.

Le père partage avec son fils :
​    Les variables globales​
​    Les variables statiques locales​
​    Les descripteurs de fichiers (file descriptors)​

Utilisation de méthode pour la synchronisation et le partage des données :

- MUTEX (MUTual EXclusion)
- Sémaphores POSIX 1003.1b...

### Noël

Le fork crée un autre process parallèle.

Le thread a un flux d'activité (maître), fait une copie avec la data du flux : reprise de l'exécution à partir de là ou s'ne était arrêté la première. Ce qui est intéressant c'est que le thread, une fois fini, peut potentiellement revenir sur la branche maître. 

## Le kernel Linux

### Introduction

- Logiciel libre
- Coeur du système
- Un peu d’histoire
  - Le créateur
  - Architecture de processeur
- Caractéristiques principales 
  - Multi-fonction
  - Normes
  - Fonctionnalités

Développé en C et en assembleur. Fait l'interface entr la couche software et la couche hardware. fournit une interface de programmation pour le matériel. 

Créateur : L. Torvald en 1991. À la base pour une seule archi puis porté sur d'autres type ARM. Multi utilisateur, respecte les normes posix, certaines fonctionnalités peuvent être ajoutées ou envelvées à lavolée. 

### Fonctions du noyau

Excécution des processus, gstion mémoire, gestion du matériel...

Assure le chargement et l’exécution des processus, gère les entrées/sorties et propose une interface entre l’espace noyau et les programmes de l’espace utilisateur.

### Développement du noyau

Développé par la communauté originellement, puis de grosse boite s'y sont mises : Red Hat, Intel, IBM...

Sous licence GNU.

- A la base
- Réseau de développement étendu 
- Licence du noyau Linux
- Esprit collaboratif d’évolution
- Gestion de versions

### Les types de noyaux

Le monolithique : conception ancienne et considérée comme obsolète. Un seul gros bloc qui contient toutes les fonctions et pilotes et de quoi les compiler. Concept simple, excellente vitesse d'exécution. Mais forte augmentation de taille avec l temps (ajout de fonctionnalités). 

- Conception ancienne (obsolète)
- Fonctions et pilotes en 1 seul bloc de code compilé
- Concept simple et excellente vitesse d'exécution
- Au fur et à mesure des développement, ils ont augmenté en taille => Problème d’évolution et maintenabilité 

### Monolithique Modulaire

Pour contrer ce dernier point, création des monolithiques modulaires : noyau avec fonctionnalités principales, et plein de services différnts sous formes de modules. Tout est centralisé dans un seul noyau, donc une seul erreur dans un service facultatif peut mettr en péril toute la sécurité du système. Meilleures possiiblités de configuration et améliore temps de chargement mais encore des défauts.

- Répondre aux problèmes des noyau monolithiques
- Partie principale monolithique
- Autres fonctions (pilotes) sous forme de modules
- Simple mais un inconvénient reste (une erreur met en péril la stabilité du système)

Le modularité du noyau permet le chargement à la demande de fonctionnalité et augmente les possibilité de configuration 

### Micro-noyaux

Du coup invention des micronoyaux dans les années 90. Le nombre de fonctions principales et les dépendances du noyau est fortement réduite. Donc minimisation des risques d'erreurs pour meilleure robustesse, fiabilité, évolutivité et maintenance. Nécessite par contre un protocole de communication netre les processus (IPC), assez lourd qui finalement réduit les performances.

- Minimiser les fonctionnalité dépendantes du noyau en plaçant les service d’exploitation hors du noyau
- Un petit nombre de fonctions principales conservée dans un noyau minimaliste = Le micro noyau
- Eloigner les services à risque des parties critique du noyau => Plus de robustesse / fiabilité et on facilite la maintenance/évolutivité
- IPC : protocole de communication entre processus (fondamentaux => Particulièrement  lourd donc réduit les performance

### Noyaux-hybrides

Enfin on ne arrive au noyau hybride qui combine avantages de monolithique et micronoyaux

- Combiner noyau monolithiques et micro-noyaux pour combiner les avantages
- Réintégrer des fonctionnalités non principales pour gagner en performance
- Les micro noyaux “pur” = échec

### Caractéristiques techniques

le noyau doit être compilé pour être compris en binaire. On a donc besoin des sources et de GCC (Gnu Compiler Collection) qui embarque tous les outils nécessaires. 

On place les sources dans `/usr/src/linux-(version)`, à partir de ces sources on peut compiler le noyau dans `/boot`, et les modules quant à eux sont placés dans `/lib/modules` 

Compilation du noyau :

- les sources sont nécessaires
- compilation avec GCC

Interfaces : Interfacé avec le matériel grâce aux modules

Portabilité : Drivers dit “génériques”

### Les modules

Code ajoutant des fonctionnalités au noyau. Ils sont exécutés dans l'espace mémoire du noyau : contrôle total sur la machine. Depuis version 2, il n'est plus nécessaire de recompiler le noyau pour chagrer un module (chargement dynamique), via `insmod` ou `modprobe`.

Un module est un morceau de code permettant d’ajouter des fonctionnalités au noyau: pilotes de périphériques matériels, protocoles réseaux, etc..

Les modules sont exécutés dans l'espace mémoire du noyau :

- Ils possèdent le contrôle total de la machine
- Ils peuvent détourner ou créer un appel système

Depuis la version 2.0  du noyau , il n’est pas nécessaire de recompiler le noyau linux quand on ajoute un périphérique.

### Les commandes

 Les modules peuvent être chargé dynamiquement sans avoir besoin de recompiler le noyau ou de redémarrer le système:

-  insmod ou modprobe

Lister les modules actifs: 

- lsmod

Information sur un module -> modinfo

## Gestion des péripériques

### Introduction

Udev est un gestionnaire de périphériques remplaçant devfs dans le noyau Linux depuis la version 2.6.  
Sa fonction principale est gérer les périphériques dans le répertoire /dev.  
En général une règle s’écrit en quelques lignes dans un fichiers .rules qui se trouve dans /etc/udev/rules.d

### Concepts

- /dev : sert à contenir les périphériques sous forme de fichier, les “nodes”, qui se rapportent aux périphériques système.
- Nodes: Chaque “node” se réfère à un périphérique, les applications peuvent utiliser ces nodes pour interagir avec les périphérique.
- Udev: est le nouveau système pour gérer le répertoire /dev, conçu pour repousser les limites mises en avant pas les précédentes versions de /dev
- Sysfs: officialisé avec le noyaux 2.6. Il est géré par le noyau pour exporter les informations basiques sur les périphériques connectés au système. Udev utilise ces informations pour créer les “nodes”.

### Les règles Udev

Les règles udev sont flexibles et très puissantes:

- changer le nom assigné par défaut à un périphérique;
- donner un nom alternatif ou permanent à un périphérique en créant un lien symbolique;
- nommer un périphérique en fonction de la sortie d'un programme;
- changer les permissions et les propriétés d'un périphérique;

### Fichiers de règles et syntaxes

- Udev se sert de différent fichiers qui se trouvent dans le répertoire /etc/udev/rules.d  
  Extension .rules

- Les règles udev sont par défaut crées dans le fichier /lib/udev/rules.d/50-udev-default.rules  
  Trié par ordre alphabétique, et ordres de prise en compte /etc/udev/rules.d/10-local.rules

- Pour info udev, essaie d’appliquer toutes les règles qu’il trouve,  

  "#":  commentaire et les règles s’écrivent sur une seule ligne. Enfin un périphérique peut-être contrôlé par plusieurs règles

### Syntaxe d'une règle

On retrouve un ensemble de clefs de correspondances et de clefs d'assignation, séparées par des virgules. 

- Les clefs de correspondances sont les conditions utilisées pour identifier le périphérique sur lequel la règle agit. 
- Chaque règle doit se composer d'au moins une clef de correspondance et d'une clef d'assignation.

KERNEL=="hdb", NAME="my_spare_disk"  
La clef de correspondance (KERNEL) et une clef d'assignation (NAME).

### Règles basiques  `man udev`

Les clefs les plus communes:

- KERNEL : le nom du périphérique donné par le noyau;
- SUBSYSTEM : le nom du sous système contenant le périphérique;
- DRIVER :  le nom du pilote du périphérique.

Les clefs d'assignation les plus communes:

- NAME : nom du périphérique "node";
- SYMLINK : liste des liens symboliques, ceux-ci étant les noms alternatifs pour le périphérique..

On peut avoir plein de fichiers d'extension .rules  
Un périphérique peut être contrôlé par plusieurs règles

### Utilisation de sysfs - Organisation de sysfs

- Outil servant à écrire des règles.
- Structure très simple
- La commande suivante permet de lister les périphériques :  
  find /sys -name dev
- La commande suivante permet de trouver un périphérique tout juste branché :  
  find /dev/bus/usb/ '!' -type d -mmin -5

Sysfs quand Gaulène le dit in dirait qu'il dit "si ses fesses". Exemple : "si, ses fesses on peut faire plein de choses avec".

### Permissions et propriétés

Udev vous permet de gérer dans vos règles les propriétés et les permissions de chaque périphérique.

La clef d'assignation GROUP vous permet de définir à quel groupe appartient un périphérique "node". Dans cet exemple, les périphériques framebuffer appartiennent au groupe Video :  
`KERNEL=="fb[0-9]*", NAME="fb/%n", SYMLINK+="%k", GROUP="video"`

Dans cet exemple, l'utilisateur John sera mis comme propriétaire pour les lecteurs de disquettes :  
`KERNEL=="fd[0-9]*", OWNER="john"`

Cet exemple définit que le périphérique peut être utilisé par tout le monde :  
`KERNEL=="inotify", NAME="misc/%k", SYMLINK+="%k", MODE="0666"`

Il est par exemple possible grâce aux règles udev de faire un script qui se déclenche en fonction du numéro de série d'un périph branché. Mais ça marche pas toujours.

# Driver

## Présentation

Permet de faire fonctionner le matériel. Il est souvent embarqué avec l'OS, ou sinon est distribué autrement. **Tout périphérique** en a besoin ! Pour le matos de base (carte graphique, ...) c'est le BIOS qui prend la main.

Les pilotes évitent que l'OS ait à reconnaitre tous les matos, et évite ainsi beaucoup de mises à jour... Ils sont codés par les constructeurs. 

Plug & play : contiennent un BIOS qui communique les infos à l'OS.

Chaque protocole a des pilotes (IP, TCP...)

Types :

- Drivers de masse
- Texte (GPS)
- Spécifiques (vidéo)
- USB (mix plug and play)

## Modules, utilité, fonctionnalités

### Qu’est-ce qu’un module?

Modules = morceau de code qui ajoutent fonctionnalité au noyau. On y retrouve différentes fonctions.

- morceau de code permettant d'ajouter des fonctionnalités au noyau : pilotes de périphériques matériels, protocoles réseaux, etc…
- chargé dynamiquement sans avoir besoin de recompiler le noyau (insmod ou modprobe) ou de redémarrer le système.
- exécutés dans l'espace mémoire du noyau :
- possèdent contrôle total de la machine
- peuvent détourner ou créer un appel système

Un module doit contenir deux fonctions particulières :

- int init_module(void) : appelée au démarrage du module. Son principal but est d'initialiser le périphérique et d'installer le driver
- void cleanup_module(void) : appelée lorsque le module est déchargé de la mémoire par la commande rmmod.

On parle uniquement des non plug and play.

Le noyau linux appelle différents modules :

- modules de base : protocoles réseau, système de fichier
- modules périphériques : carte mère, vidéo, son réseau
- modules supplémentaires : carte vidéo (non-libre), cartes peu utilisées.

### Chargement/Déchargement d'un module

commande `modprobe`

- Charger `$ sudo modprobe-a 3c59x`
- Décharger `$ sudo modprobe -r 3c59x`
- Lister `lsmod`

### Options d'un module

Certains modules possèdent des options ("parm") qui permettent un plus grand contrôle sur le module en lui-même. Ces options se chargent de plusieurs manières. 

`modprobe snd_ens1371 joystick_port=1`

- les "parm" vous indique quoi mettre : int = entier,  bool = booléen (0 ou 1) , array of int = plusieurs entier, array of bool = plusieurs bits 

- Pour que cela soit pris en compte directement au lancement il faut éditer le fichier /etc/modprobe.d/option et y ajouter une ligne.

On peut spécifier les modules à charger au lancement du noyau. La liste des fichiers à charger est dans /etc/module . On peut aussi l'empêcher d'en charger : /etc/mprob/blacklist.conf

### La structure file_operations 

Permet de s'y retrouver dans l'orga communautaire de Linux

Cette structure dont le type est décrit dans le fichier  permet de définir les méthodes du pilote.  
La tradition veut que l’on préfixe le nom de la structure et des méthodes par le nom du pilote (ici mydriver).  

De part la nécessité de définir les symboles correspondant aux méthodes, on placera la déclaration de la structure après la définition des méthodes. De ce fait, l’architecture générale du pilote sera la suivante :

1. Déclaration des en­têtes.
2. Déclaration des macro-instructions identifiant le pilote
3. Déclaration des variables. 
4. Définition des méthodes. 
5. Définition de la structure file_operations.
6. Définition des points d’entrée module_init() et module_exit() du module. 

### Module du noyau

Les fichiers contenant le code compilé des modules se trouvent dans un des sous répertoires de /li/modules/<version-du-noyau>/kernel/ et porte l'extension .ko

Les fichiers dont l'extension est .KO sont des fichiers de type Linux Kernel Module Format

Manipulation des modules du noyau :

- Lsmod
- Insmos
- Rmmod

Les fichiers .ko sont des Kernel Objects chargeables parle noyau. plusieurs commandes permettent d'agir sur les modules chargés par le noyau.

### Cas particulier de Linux

Dans le cas de LINUX, le pilotes de périphériques sont ajoutés de deux manières: 

- de manière statique: dans ce cas la, le code source du pilote est  ajouté à l'arborescence des sources du noyau LINUX. Le pilote sera  chargé même en l'absence du périphérique à controler. Ce type de pilote  était utilisé systématiquement jusqu'à la version 1.2 du noyau LINUX. 
- de manière dynamique: dans ce cas la, on peut ajouter dynamiquement à  un noyau LINUX existant un pilote dont le code source ne sera pas  contenu dans l'arborescence du noyau. Le pilote constitue alors un  module chargeable. Dans la suite de l'article nous étudierons  exclusivement ces pilotes. 

L'utilisation des modules chargeables  permet aussi de limiter la mémoire utilisée par les pilotes car ceux-ci  sont chargés uniquement lorsqu'un programme utilisateur ou un autre  module en fait la demande. Les programmes kerneld ou kmod sont destinés à  gèrer le chargement/déchargement automatique des modules chargeables.  

### Loadable Kernel Module

Dans un système d'exploitation, un module est une partie du noyau qui  peut être intégrée pendant son fonctionnement. Le terme anglais  généralement employé pour les désigner est Loadable Kernel Module,  abrégé LKM, ou (en français : « module de noyau chargeable »). Cette  fonctionnalité existe dans les noyaux Linux et les noyaux BSD. C'est une  alternative aux fonctionnalités compilées dans le noyau, qui ne peuvent  être modifiées qu'en relançant le système. Les modules du noyau Linux  sont généralement placés dans /lib/modules. Ils utilisent l'extension  .ko depuis la version 2.6. 

### Noël

Le lien entre le fichier de code et le matériel se fait par un BUS qui va donner une adresse physique de périphérique. IRQ (Interrupt ReQuest), DMA (Direct Memory Access, zone de mémoire attribuée à un périphérique). Le kernel interagit avec le matériel via ces éléments là.

## USB

### Driver USB structure

Il existe 2 modes différents, le mode noyau et le mode utilisateur.

- Espace noyau : tout est permis même le pire, on peut vite tout casser.
- Espace utilisateur : tout est protégé, les possibilités sont bridées.

Par défaut, tous les pilotes de périphérique tournent en mode "noyau".   
En mode noyau, le code d'exécution dispose d'un accès complet et illimité au matériel sous-jacent. Il  peut exécuter toute instruction de la CPU et référencer toute adresse  de mémoire. Le mode noyau est généralement réservé aux fonctions les plus fiables et de niveau inférieur du système d'exploitation.  
Les accidents en mode noyau sont catastrophiques; ils vont arrêter le PC entier.

### Mode noyau

- Possibilité d'exécuter tout type d’instruction

Potentiellement dangereuses pour la sécurité du système, comme, par exemple, les instructions qui permettent l’accès direct à la mémoire ou aux périphériques.

En mode utilisateur, le code d'exécution ne permet pas d'accéder directement au matériel ni à la mémoire de référence.  Le code exécuté en mode utilisateur doit déléguer aux API système pour accéder au matériel ou à la mémoire.   
En raison de la protection offerte par ce type d’isolement, les collisions en mode utilisateur sont toujours récupérables. La plupart du code exécuté sur votre ordinateur s'exécutera en mode utilisateur.

### Mode utilisateur

Certaines instructions sont interdites, Pas d’accès aux périphériques, Accès à l’espace mémoire virtuel du processus

2 types de périphériques :

- Type caractère  
  Un périphérique caractère représente un dispositif matériel qui lit ou écrit en série un flux d’octets. Les ports série et parallèle, les lecteurs de cassettes, les terminaux et les cartes son sont des exemples de périphériques caractères.

- Type bloc  
  Un périphérique bloc représente un dispositif matériel qui lit ou écrit des données sous forme de blocs de taille fixe. Contrairement aux périphériques caractère, un périphérique bloc fournit un accès direct aux données stockées sur le périphérique. Un lecteur de disque est un exemple de périphérique bloc.

### Numéro de périphériques

Les pilotes sont accessibles à travers des fichiers spéciaux appelés également nœuds (nodes). Ces fichiers sont localisés sur le répertoire /dev et sont caractérisés par deux valeurs numériques :

- Le MAJEUR (MAJOR) qui identifie le pilote
- Le MINEUR (MINOR) qui représente une sous-adresse en cas de présence de plusieurs périphériques identiques, contrôlés par un même pilote.

Pour créer une nouvelle entrée dans le répertoire /dev, on utilisera la commande mknod: mknod /dev/monpilote c majeur mineur  
Le c indique que l'on crée un noeud pour un pilote en mode caractère.  
A partir du moment où le noeud est créé et le pilote installé, on peut accèder au périphérique en utilisant les commandes standards de LINUX

### Implémentation d'un driver

- Structure d'implémentation
- Méthode open et release
- Allocation de la mémoire
- Méthodes read and write
- Méthode ioctl
- Gestion d'interruptions

### Que ce passe t’il lorsque l’on branche un périphérique ?

Chaîne d’opérations lors de l’insertion d’un périphérique USB

-  Le 'chargeur de module' du noyau est appelé lorsqu’un nouveau périphérique est détecté.
  - Il identifie de manière unique le type de périphérique, le modèle et la marque
  - Il interroge le périphérique pour connaître les fonctionnalités
  - Il cherche est charge le pilote offrant les capacités de prise en charge du pilote branché et il associera le pilote au périphérique
- Transfert des données

Lorsque  l'on branche un périphérique USB, l'ordinateur le détecte grâce à une  tension, constante entre D- et D+ lorsque rien n’est branché, et qui chute dès que l'on branche quelque chose.   
Ainsi, dès que le périphérique est connecté, l'ordinateur envoie un courant d'initialisation pendant 10 millisecondes. Dès  lors, il lui attribue l'adresse "0". Après, le PC questionne tous les  périphériques USB déjà connectés pour connaître leur adresse, puis en attribue une non utilisée (codée sur 7 bits) au nouveau périphérique, ce qui laisse 127 possibilités !   
Les  principes de l'USB, pour communiquer avec les périphériques, c'est que  chacun a la parole à son tour, personne ne parle en même temps, et l'ordinateur indique au préalable qui doit parler. Ce système est appelé anneau à jeton ou "token ring"  
Ainsi, le PC envoie ce qui s'appelle un jeton, qui contient l'adresse du périphérique qui doit parler. Ce jeton circule de périphérique en périphérique, jusqu'à ce que le périphérique se reconnaisse et écrive à l'intérieur. Le PC finit par recevoir le jeton et le décode. 

## Protocoles de communication

SPI : Sans Protocole d'Interface

Le noyau contient un genre 

### MIDI

Format de fichier lié à la mudsique et utilisé comme potocole pour les instruments

Le Musical Instrument Digital Interface ou MIDI est un protocole de communication et un format de fichier dédiés à la musique et utilisés pour la communication entre instruments électriques, contrôleurs, séquenceurs et logiciels de musiques

### OSC

Contrôle en temps réel, successeur du MIDI. Open Sound Control

L'Open Sound Control est un format de transmission de données entre ordinateurs, synthétiseurs, robots ou tout autre matériel ou logiciel compatible, conçu pour le contrôle en temps réel. Il utilise le réseau au travers des protocoles UDP ou TCP et apporte des améliorations en termes de rapidité et flexibilité par rapport à l'ancienne norme MIDI.

### RS-232

Norme ultra standard : le port série. N'est plus trop d'actualité, enfin si, enfin ça dépend des matos.

RS-232 est une norme standardisant une voie de communication de type série. Disponible sur presque tous les PC depuis 1981 jusqu'au milieu des années 2000, il est communément appelé le « port série »

### DMX

Protocole pour le raccordement des lumières. Avant 86 c'était de l'analogique.

Le DMX 512 est une norme destinée à faciliter le raccordement des gradateurs sur les consoles lumières. En définissant les contraintes techniques, le type de câble et les conditions d’utilisation, il permet de rendre compatible des produits de différentes marques. 

### SPI

Différents protocoles de communication selon le SPI. Master/slave, ou via l'horloge, peut être généré par le maître ou l'esclave. Le kernel dit au matos/logiciel où trouver l'info, ou dit à un truc de donner l'info au matos/logiciel

SCLK — Serial Clock, Horloge (généré par le maître)  
MOSI — Master Output, Slave Input (généré par le maître)  
MISO — Master Input, Slave Output (généré par l'esclave)  
SS — Slave Select, Actif à l'état bas (généré par le maître)

### Avantages SPI

-  Communication Full duplex
- Débit plus important qu'un bus I2C
- Flexibilité du nombre de bits à transmettre ainsi que du protocole en lui-même
- Simplicité de l'interface matérielle
  - Aucun arbitre nécessaire car aucune collision possible
  - Les esclaves utilisent l'horloge du maître et n'ont donc pas besoin d'oscillateur propre
- Partage d'un bus commun pour l'horloge, MISO et MOSI entre les périphériques

### Inconvénients SPI

- Monopolise plus de broches d'un boîtier que l'I2C ou une UART qui en utilisent seulement deux.
- Aucun adressage possible, il faut une ligne de sélection par esclave en mode non chaîné.
- Le protocole n'a pas d'acquittement. Le maître peut parler dans le vide sans le savoir.
- Ne tolèrent pas la présence que d'un seul maître SPI sur le bus. Néanmoins, on trouve des circuits intégrés supportant le mode "multi-master", permettant de partager le bus SPI entre plusieurs maîtres.
-  Ne s'utilise que sur de courtes distances contrairement aux liaisons RS-232, RS-485 ou bus CAN. 

## Drivers Windows, signatures et certificats

C'est maintenant obligatoire sous Windows depuis Vista.

La signature vérifie si tout est approuvé, le logiciel, l'éditeur, et si y a 0 modifs depuis la certification.Pour obtenir un certif, on se rapproche d'une autorité de certif. Les certifs et centre approuvés sont regroupé dans une bibliothèque gérée par Windows.

- À partir de Windows Vista, les versions x64 de Windows nécessitaient la signature numérique de tous les logiciels s'exécutant en mode noyau, y compris les pilotes, pour pouvoir être chargés.
- À compter de Windows 8 et des versions ultérieures de Windows, l'installation ne sera pas poursuivie à moins que ces packages de pilotes ne soient également signés..
- L'installation de périphérique Windows utilise des signatures numériques pour vérifier l'intégrité des packages de pilotes et l'identité du fournisseur (éditeur de logiciels) qui fournit les packages de pilotes. 

### Présentation des signatures numériques

- Les signatures numériques sont basées sur la technologie d'infrastructure à clé publique Microsoft, basée sur Microsoft Authenticode, associée à une infrastructure d'autorités de certification approuvées. 
- Authenticode, basé sur les normes du secteur, permet aux fournisseurs, ou aux éditeurs de logiciels , de signer un fichier ou une collection de fichiers (un package de pilote, par exemple) à l'aide d'un certificat numérique de signature de code émis par une autorité de certification .

Windows utilise une signature numérique valide pour vérifier les éléments suivants :

- Le fichier, ou la collection de fichiers, est signé.
- Le signataire est approuvé.
- L'autorité de certification qui a authentifié le signataire est approuvée.
- La collection de fichiers n'a pas été modifiée après sa publication.

### Processus de signature 

- Un éditeur obtient un certificat numérique X.509 auprès d'une autorité de certification. Un certificat de signature est un ensemble de données identifiant un éditeur. 
- Les certificats qui identifient les éditeurs approuvés et les autorités de certification approuvées sont installés dans des magasins de certificats gérés par Windows.
- Le certificat de signature comprend une clé privée et une clé publique, appelée paire de clés . La clé privée est utilisée pour signer le fichier catalogue d'un package de pilotes ou pour incorporer une signature dans un fichier de pilotes. La clé publique est utilisée pour vérifier la signature du fichier de catalogue d'un package de pilotes ou une signature incorporée dans un fichier de pilotes
- Pour signer un fichier de catalogue ou incorporer une signature dans un fichier, le processus de signature génère d'abord un hachage cryptographique, ou empreinte numérique , du fichier. Le processus de signature chiffre ensuite l'empreinte numérique du fichier avec une clé privée et ajoute l'empreinte numérique au fichier.
- Le processus de signature ajoute également des informations sur l'éditeur et l'autorité de certification ayant émis le certificat de signature. La signature numérique est ajoutée au fichier dans une section du fichier qui n'est pas traitée lors de la génération de l'empreinte de fichier.
- Pour vérifier la signature numérique d'un fichier, Windows extrait les informations relatives à l'éditeur et à l'autorité de certification et utilise la clé publique pour déchiffrer l'empreinte numérique du fichier crypté.
- Windows n'accepte l'intégrité du fichier et l'authenticité de l'éditeur que si les conditions suivantes sont vraies:
- L'empreinte numérique décryptée correspond à l'empreinte numérique du fichier.
- Le certificat de l'éditeur est installé dans le magasin de certificats des éditeurs approuvés .
- Le certificat racine de l'autorité de certification qui a émis le certificat de l'éditeur est installé dans le magasin de certificats des autorités de certification racines de confiance .

### Certifier un pilote

- Certifiez votre pilote auprès de Microsoft et Microsoft lui fournira une signature. Lorsque votre package de pilotes réussit les tests de certification, il peut être signé par Windows Hardware Quality Labs (WHQL). Si votre package de pilotes est signé par WHQL, il peut être distribué via le programme Windows Update ou d'autres mécanismes de distribution pris en charge par Microsoft.
- Les fournisseurs ou les développeurs de pilotes peuvent obtenir un certificat de publication de logiciels (SPC) auprès d’une autorité de certification autorisée par Microsoft et l’utiliser pour signer eux-mêmes des fichiers binaires en mode noyau et en mode utilisateur.

### Visualiser la signature d’un pilote

- Fichier .cat du driver
- On voit ici que le pilote a été signé le 24 Juin 2013 et que la date de signature est garantie par le serveur de temps de Microsoft.

### Certifier un pilote

- Certifiez votre pilote auprès de Microsoft et Microsoft lui fournira une signature. Lorsque votre package de pilotes réussit les tests de certification, il peut être signé par Windows Hardware Quality Labs (WHQL). Si votre package de pilotes est signé par WHQL, il peut être distribué via le programme Windows Update ou d'autres mécanismes de distribution pris en charge par Microsoft.
- Les fournisseurs ou les développeurs de pilotes peuvent obtenir un certificat de publication de logiciels (SPC) auprès d’une autorité de certification autorisée par Microsoft et l’utiliser pour signer eux-mêmes des fichiers binaires en mode noyau et en mode utilisateur.



# Compilateur

## Présentation

### Qu’est-ce qu’un compilateur ?

Compilateur = vérificateur et traducteur 

### Cousins

- Interpréteurs  
  Diffèrent d'un compilateur par l'intégration de l'exécution et de la traduction. Utilisés pour les langages de commande
- Formateurs de texte  
  Traduit le code source dans le langage de commande d'une imprimante
- Préprocesseurs  
  Effectuent des substitutions de définitions, des transformations lexicales, des définitions de macros, etc.

Fonctionnement :

1. Analyse lexicale : scan du texte qui est regroupé pour former des mots, des blocs, et garde ce qui l'intéresse
2. Syntaxe (backend) : regarde comment sont formés les mots pour en déduire la "grammaire", la structure du texte. Création d'un arbre syntaxique, ou arbre de dépendance.
3. Analyse sémantique : vérifie que la syntaxe est OK puis checke le sens. Regarde le contexte, voit la globalité : est-ce **logique** ?

### Analyse lexicale (scanners) 

- Rôle : grouper les lettres pour former des mots. 
- Au passage : 
  - reconnaît et signale les mots mal orthographiés
  - peut supprimer les commentaires. 
  - peut préprocesser le texte : expansion de macros.

#### Lex : un outil pour construire un analyseur lexical

Fonctionnement :

- On décrit un ensemble de mots par une expression.
- On associe à chaque expression une action.
-  L'exécutable produit par lex lit le fichier d'entrée et pour chaque mot reconnu, effectue une action précisée par l'utilisateur.   
    expression -> action  
    Exemple : transformer tous les 'A' en 'a’ 

### Analyse syntaxique 

Vise à reproduire une représentation (arbre) des relations grammaticales entre les mots.

- La syntaxe est l’étude de la façon avec laquelle les mots sont composés pour construire des phrases.
- La syntaxe ne s’interesse pas à la sémantique des mots.
- Parcontre, une analyse syntaxique peut apporter de l’information utile à la compréhension d’une phrase
- (utile en traduction automatique, système de réponse automatique..)
- L’analyse syntaxique va permettre d’exposer et de manipuler de nouveaux concepts linguistiques utiles :
- Les constituants qui sont des groupes de mots agissant comme une unité à part entière, tels les noun phrases.
- Les relations grammaticales telles les relations d’objet et de sujet d’un verbe
- D’autres propriétés sur la relation entre les mots d’une phrase telle les relations de dépendance.

### Analyse sémantique

À la sortie de l’analyse syntaxique, on se trouve avec un arbre syntaxique (abstrait) qui contient toutes les informations pertinentes sur la structure syntaxique du programme   
On a donc vérifié qu’il est syntaxiquement correct. . . . . . ce qui ne veut pas dire qu’il est sémantiquement correct !   
De même, on a compris sa structure syntaxique. . . . . . ce qui ne veut pas dire qu’on a compris sa signification !

### Optimisation de code

Le code est généré d'abord dans un langage intermédiaire, puis en code binaire pour la machine. À chaque fois il est généré puis optimisé.

L’optimisation de code peut être soit par :

1. #### Optimisations de la vitesse d'exécution

Un compilateur peut optimiser plusieurs choses :

- la taille du programme 
- la vitesse d’exécution 
- la consommation énergétique du programme.

Si les compilateurs sont très bons pour optimiser la vitesse d’exécution, il n’en est pas vraiment de même pour la taille du code ou la consommation énergétique. Quoiqu’il en soit, il existe plusieurs façons pour optimiser la vitesse d’exécution :

- utiliser au mieux les instructions du processeur ;
- diminuer le temps processeur passé à faire des calculs ;
- virer des branchements et fonctions pour obtenir un code le plus linéaire possible ;
- utiliser au mieux la hiérarchie mémoire, que ce soit au niveau des registres, du cache ou de la DRAM.

2. #### Optimisations de la taille du code

Si la vitesse des programmes peut être optimisée, les compilateurs peuvent aussi jouer sur la taille du programme. La taille d’un programme en elle-même n’est pas importante pour des programmes PC puisque la majorité d’entre eux possèdent plusieurs gibioctets1 de RAM, ce qui laisse une grande marge. Par contre, diminuer la taille du code a des effets indirects sur les performances en économisant de la mémoire cache. Mais dans la réalité, les optimisations de la taille du code entrent souvent en conflit avec les optimisations de vitesse d’exécution et on a :

- Choix des instructions
- Jonction de branchements 
- Abstraction de procédure
- Suppression de code mort

### Génération de code

Se passe en plusieurs étapes : 

1. Génération du code intermédiaire 
2. Optimisation du code intermédiaire
3. Génération du code machine 
4. Optimisation du code machine

### Pile d’execution

Zone de mémoire supposée très grande.  
Le registre traditionnellement utilise pour le haut de pile s’appelle $sp.

Par convention, il pointe vers le mot (4 octets) le plus en haut.  
Attention, on compte a l’envers en MIPS ! On augmente la pile en​
diminuant $sp 

### Appel de fonction

Les fonctions (et procédures) en assembleur sont simplement des adresses dans le code.  
le passage des arguments se fait a la main, la récupération du résultat aussi, il n’y a pas de “variable locale”.

On utilise la pile pour stocker

- le résultat,
- les arguments,
- les variables locales

### Arbre d’activation

A n’importe quel moment, une seule fonction est active  
Elle est representée par une trame de pile ou trame d’activation  
Les activations successives forment un arbre d’activation  
Une trame de pile est crée lors d’un appel  a fonction   
La trame est ecrasée quand la fonction finit son activation   

### Outils logiciels

- Générateurs d’analyseurs lexicaux  
  Engendrent un analyseur lexical (scanner, lexer) sous forme d’automate fini à partir d’une spécification sous forme d’expressions rationnelles  
  Flex, Lex

- Générateurs d’analyseurs syntaxiques  
  Engendrent un analyseur syntaxique (parser) à partir d’une grammaire  
  Bison, Yacc

- Générateurs de traducteurs  
  Engendrent un traducteur à partir d’un schéma de traduction (grammaire + règles sémantiques)  
  Bison, Yacc

## Analyse lexicale

Analyse lexical = Transformation d’une suite de caractères en une suite de mots.  
C'est la première partie de la compilation, le point d'entrée, juste après le source code.  
Un analyseur lexical est un automate fini

### Les enjeux 

- La production d’un arbre (de syntaxe abstraite) à partir de caractères 
- Création des automates finies à partir des expressions régulières qui sont utilisés souvent dans les éditeurs des textes et les grep d'Unix .

### Les langages formels 

On se donne un ensemble Σ appelé alphabet, dont les éléments sont appelés caractères. Un mot (sur Σ) est une séquence de caractères (de Σ). On note є le mot vide, uv la concaténation des mots u et v (la concaténation est associative avec є pour élément neutre). On note Σ∗ l’ensemble des mots sur Σ.

Un langage sur Σ est un sous-ensemble L de Σ∗. On se donne quelques opérations sur les langages. Si U et V sont des langages sur Σ, on note U V l’ensemble des mots obtenus par la concaténation d’un mot de U et d’un mot de V; U∗ (resp. U +), l’ensemble des mots obtenus par la concaténation d’un nombre arbitraire, éventuellement nul (resp. non nul) de mots de U.

### Les expressions régulières  (regex) :

Rôle : permettent de représenter des modèles de chaînes de caractère. Ce sont des outils très puissants et très utilisés.

Syntaxe : 

- Une lettre de l’alphabet a désigne le langage {a}.
- Epsilon є désigne le langage {є}
- Concaténation : M N désigne le langage [[M]] [[N]].
- Alternative : M ∣ N désigne le langage [[M]] ∪ [[N]].
- Répétition : M∗ désigne le langage [[M]] ∗.
- Autres constructions tel que a ou b : a|b , un ou plus a+ , a?, $,^, etc
- Exemple:  Adresse email : `^[a-zA-Z-]+@[a-zA-Z-]+\.[a-zA-Z]{2,6}$`

### Les automates

#### DFA automate fini déterministe

Nombre fini d'états et un état ne peut aller que vers un autre état (ex: feu tricolore)

#### NFA fini non déterministe

La définition est la même que celle de automates déterministes, compte tenu des deux détails suivants :

1. Les transitions sont définies par une relation et non plus par une fonction, c’est à dire que plusieurs transitions issues d’un état donné peuvent porter la même étiquette.
2. Il existe des transitions « spontanées » qui portent une étiquette spéciale, classiquement є.

## Analyse syntaxique

Analyse syntaxique = fait suite à l’analyse lexical et qui permet de connaître la structure syntaxique d’un énoncé et par suite expliciter les relations de dépendances entre les différents lexèmes et de construire la représentation du sens d'énoncé   
Vise à reproduire une représentation (arbre) des relations grammaticales entre les mots.

Il définit ce qu'est un sujet, un verbe.. donc un objet, une classe... ?

### Le rôle de l’analyseur syntaxique  

prépare la traduction : si des mots sont pas compwris, communication possible via la table des symboles.

Rôle central de la partie frontale :

1. active l’analyseur lexical;
2. vérifie la conformité syntaxique;
3. construit l’arbre d’analyse ;
4. prépare ou anticipe la traduction ;
5. gère les erreurs communes de syntaxe.  
6. Traitement des erreurs :
   - diagnostic (messages) ;
   - redémarrage : mode panique, jusqu’à resynchronisation ;  
     correction, difficile si l’erreur est antérieure à sa détection ;  
     règles d’erreurs, intégrées à la grammaire.  

### Grammaires

Syntaxe spécifiée par des règles de grammaire.

- Symboles terminaux (= unités lexicales) alphabet A ;
- Symboles intermédiaires ou variables (= catégories
  grammaticales) alphabet X ;
- Règles de grammaire x ® w , où x Î X et où w Î (AÈ X)*
  w est un mot quelconque, même vide.

Exemples :  
instr ⇾ si expr alors instr sinon instr  
phrase ⇾ gsujet gverbe gcomplément  

Axiome (= programme)  
Langage engendré = mots terminaux dérivant de l’axiome

### L’analyse descendante  

Une procédure par terme.  
Problème : récursivité directe à gauche ;​ nécessité d’une transformation pour l’éliminer.

Procédures correspondantes : deux procédures supposées éc

- prévision retourne l’unité lexicale suivante sans l’enlever ;
- correspond(x) lit l’unité lexicale suivante, l’enlève et signale erreur si elle ne vaut pas x. Ici plus, nombre, etc. sont les​ codes d’unités lexicales renvoyés par l’analyseur lexical

### L’analyse ascendante  

On utilise une pile, et une table de transition entre états. (Automate déterministe à une pile)

En fonction du symbole de prévision, 

- on empile un état en lisant un caractère de l’entrée (décalage)
- on dépile autant de symboles que la longueur de la règle qu’on a reconnue, et on empile un nouvel état (réduction)  

## Analyse sémantique

La sémantique est l’étude du sens des mots, dans une phrase et dans le contexte de cette phrase. L’analyse sémantique d’un texte consiste à établir sa signification en utilisant le sens des éléments du texte ; a contrario, les analyses lexicales ou grammaticales ne font que décomposer le message à l’aide d’un lexique (dictionnaire) ou d’une grammaire

Un programme peut être syntaxiquement correct mais contenir des erreurs “sémantiques” :

- Variables/fonctions non déclarées
-  Fonctions avec mauvais nombre/type de paramètres 
- Opérateurs appliqués à des types incompatibles (int + string) 
- Pas de return alors que la fonction n’est pas void (ou vice-versa) 
- Pas de main 

### Système de types

Les variables, fonctions et expressions ont des types associés 

- Types : déclarés ou inférés ? modifiables ?   
  - Déclarés : identificateurs déclarés avec un type (C, Java)  	
  - Inférés : types sont inférés selon leur utilisation (Perl, Python, PHP) 
  - Modifiables : changement de type dans la même portée (Python) 

- Vérifications : statiques (compilation) ou dynamiques (exécution) ? 
  - Statiques : compatibilité types utilisés/déclarés des variables 
  - Dynamiques : dépassement des bornes d’un tableau 
- Conversions de types 
  - Implicites (coercitions) : x = 1 + 5.3 
  - Explicites (cast) : x = (int)y + 1 
  - Polymorphisme (fonctions, opérateurs, types complexes)

### Table des symboles

- Elle rassemble toutes les informations utiles concernant les variables et les fonctions du programme. Pour toute variable, elle garde l’information de : son nom son type sa portée son adresse en mémoire.
- Pour toute fonction, elle garde l’information de : son nom sa portée le nom et le type de ses arguments, ainsi que leur mode de passage le type du résultat qu’elle fournit La table des symboles est construite lors du parcours de l’arbre abstrait. 
- Elle grandit pendant la compilation des parties déclaratives : déclaration de variables, définition de fonctions. Elle est consultée pendant la compilation des parties exécutables : appel de fonction, référence à une variable. La table des symboles doit être réalisée avec soin : on estime qu’un compilateur passe la moitié de son temps à la consulter