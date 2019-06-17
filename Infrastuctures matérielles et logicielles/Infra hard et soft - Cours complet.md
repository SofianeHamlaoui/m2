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

### Structures mémoire

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

### Comment voit et gère-t-il les paquets ?

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

## Protocoles de communication

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

## Drivers Windows, signatures et certificats

C'est maintenant obligatoire sous Windows depuis Vista.

La signature vérifie si tout est approuvé, le logiciel, l'éditeur, et si y a 0 modifs depuis la certification.Pour obtenir un certif, on se rapproche d'une autorité de certif. Les certifs et centre approuvés sont regroupé dans une bibliothèque gérée par Windows.

# Compilateur

## Présentation

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

## Analyse lexicale

C'est la première partie de la compilation, le point d'entrée, juste après le source code.

Un analyseur lexical est un automate fini

### Les REGEX

...explique ce que c'est.

### Les automates

DFA automate fini déterministe

NFA fini non déterministe

## Compilateur : Analyse syntaxique

Après l'analyse lexicale

Construit un arbre des relations grammaticales entre les mots. 

Il définit ce qu'est un sujet, un verbe.. donc un objets, une classe... ?

### Rôle

prépare la traduction : si des mots sont pas compwris, communication possible via la table des symboles.

### Grammaires



