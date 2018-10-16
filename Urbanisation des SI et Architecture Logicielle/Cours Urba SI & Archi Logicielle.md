# Introduction

## Qu'est-ce que l'urbanisation des SI ?

Urbanisation : amélioration/optimisation/agencement d'un système pour ses membres.

BPM = Business Process Management.  
C'est un concept qu'on retrouve dans l'urbanisation des SI, qui touche à la transformation digitale. C'est l'urbanisation, pour les petites entreprises. On reviendra souvent dessus dans le cours  
BPMN : système de notation du BPM.

Pour le gérer un SI (max couverture, max taux de couv), il faut faire du management des SI.   
À l'intérieur du management on a la gouvernance des SI, pour en contrôler et piloter l'évolution (ITIL, COBIT...)  
Mais pour pouvoir le contrôler il faut mettre en place des bonnes pratiques. C'est là qu'arrive le sous-domaine **urbanisation des SI**. Elle est toujours centrée métier donc centrée process, donc c'est un BPM.  
Elle permet d'apporter plus d'information pour la gouvernance. 

Max couverture : besoin fonctionnel  
Max DI : Taux de couverture = chaque besoin fonctionnel de l'entreprise doit être couvert.

L'idée de l'urba est d'utiliser la métaphore avec l'urbanisation des villes pour l'appliquer au SI, car on a une complexité similaire entre un SI et une ville.

En urba, 2 mots clefs : **cohérence** et **agilité**.  
Le but est de rendre le SI **cohérent** par rapport à la stratégie de l'entreprise.  Il faut aussi le rendre **agile** par rapport au besoin du marché

## Plan

- L'urbanisation des SI
  - Architecture d'entreprise
  - Notion d'urbanisation
  - Métamodèle de concepts
- Le processus d'urbanisation
- Le management des processus



## Partiel

- Étude de cas
- TD

# I - L'urbanisation des SI

## Contexte stratégique

Les contextes sont les occasions de regarder nos process métiers et de les reprendre.

3 phénomènes font pression sur le besoin d'urbanisation du SI. Également d'autres éléments de contexte poussent vers l'urbanisation. (p4pdf)  
La montée des nouvelles technologies peut rendre un système obsolète en 3 ans. >> Il faut faire une veille fournie et constante.

Le contexte dans les entreprises, c'est plusieurs besoins (p5pdf) :

- besoin d'adapter la stratégie pour que l'entreprise devienne meilleure.
- pour ça il faut analyser les processus, la chaine (voir BPM). KPM = clé d'indications de performances. C'est le process qui fait ça.
- process étendu = qui touche plusieurs flux/logiciels. Qui part du fournisseur et qui va jusqu'au client. Ex : la chaine logistique. C'est souvent complexe à gérer, il faut donc des process bien optimisé, un plan d'action (BPM).

Contexte stratégique : on retrouve dans l'entreprise une demande croissante d'évolution. S'ajoute à ça le gros bordel de l'entreprise : des versions différentes, des langages diférents, logiciels différents. Ça rend le système rigide, l'acquis est lourd. On peut pas tout changer en partant du principe que c'est pourri, il faut tenir compte de l'ancienneté de la boite et effectuer une évolution, pas une révolution. Faire une refonte complète a trop de désavantages : cher, risqué, manque de valeur ajoutée. 

L'objectif est d'améliorer l'adaptabilité du SI et de son parc applicatif. On ne réagit pas directement face à un besoin, mais on évolue de façon permanente. On est dans le progessif. Simplification maximum de l'architecture, optimisation de la valeur ajouté, rendre le SI plus flexible.

Dans ce contexte stratégique on retrouve les mots clefs :

- **évolutivité**
- **performance**
- **alignement stratégique**

## L'architecture d'entreprise - EA

Le lean management se retrouve imbriqué dans l'EA (lean management : voir cours de Marketing **numérique** (et pas digital parce que digital c'est les doigts, putain))

L'EA est un cadre commun qui permet la communication entre le comité pilotage et les exécuteurs et responsables métiers. C'est le seul moyen de communication qui permet ça. **C'est le socle de l'urba des SI**. Sans EA on arrive pas à mettre en place (d'un point de vue pratique) les lignes et objectifs de l'entreprise.

L'EA met les différentes visions de l'architecture en synergie avec archi métier (c'est ça l'alignement statégique)

### Comment établir l'EA ? 

On commence par établir l'architecture existante, puis on définit l'architecture cible. Pour faire l'existante, voir p11pdf

L'EA va établir une feuille de route, dans laquelle on retrouve entre autres (p12pdf) le schéma directeur informatique (consultable en ligne, chaque boite doit la publier tous les 3 ans. cf. celle de la caisse de retraite).

C'est donc un travail autour du SI, dans lequel on fait intervenir tous les acteurs (DSI, MOE, MOA, archi d'entreprise, urbaniste... p13pdf).

Il faut avoir un cadre de référence. Dedans on retrouve plusieurs visions (p14pdf)

### Cadre Zachman

Le premier c'est le cadre Zachman. il fonctionne avec des problématiques (p15pdf).  
Pour lui l'entreprise est modélisée comme un ensemble de briques. Il faut répondre à ces problématiques pour chaque brique. Il ne s'agit pas d'un référentiel (= comment faire) mais d'un cadre de référence (= que regarder). Dedans on a différentes visions sur l'entreprise (p16pdf). Ce n'est pas un référentiel il n'y a donc pas bcp de choses (p17pdf), c'est un ensemble de briques élémentaires qui vont définir l'entreprise et son outil. 

### Cadre TOGAF

Plusieurs références, éléments, à regarder. On passe rapidement dessus, c'est utile pour ceux qui veulent faire de la transformation digitale. TOGAF est, lui, un réferentiel. 

### De l'EA vers l'urbanisation

On part d'un truc vers un autre j'ai pas tout suivi.  
Urbanisation = vision centrée métier. On va mettre en place différents éléments (p24pdf)

## Notions d'urbanisme

### La métaphore de l'urbanisme.

On utilise des modèles de l'urbanisme pour adapter le SI. 

Ce qu'on peut assurer avec l'urbanistation du SI c'est :

- Gagner en souplesse et en réactivité
- Réussir l'ouverture du SI à de multiples et même nouveaux acteurs
- Assurer la capitalisation et la valorisation des acquis de l'expertise métier

### Définitions

p27pdf.  
Urbanisation = application d'un plan d'urbanisation sur le SI.

Comment fonctionne l'urbanisation ?  
On part d'une architecture non organisée, et on applique les règles d'urbanisation pour arriver à une architecture cible, qui sera, elle, organisée. 

La nouvelle architecture urbanisée participe au dispositif de gouvernance. Elle est évolutive, peut accueillir de nouveaux composants.

### Apports 

L'urbanisation est un apport dans gestion des risques parce qu'on peut les établir et les régler très rapidement grâce à elle.

### L'outil cartographique

Sans outil de cartographie, on peut rien faire. On a besoin de l'architecture actuelle et de l'architecture cible, c'est pour ça qu'on a besoin de l'outil de cartographie. Il faut établir 4 cartographies (p34pdf). 

p34pdf : liste des étapes du bon déroulement d'un plan d'urbanisation.

L'urbanisation des SI est la solution au RGPD  
Il y a différentes motivations à l'urbanisation des SI (p36pdf)

## Métamodèle

Il y a un métamodèle de l'urbanisation des SI. Il faut remplir les trous de Barhi avec les concepts de base de l'urbanisation des SI.
Le métamodèle est basé sur concepts de base de l'urbanisme : zones, quartiers, îlots... avec une notion de hiérarchie et d'appartenance.
Voir metamodele.png (Ressources)

![metamodèle des concepts](Ressources/metamodele.png)

Le métamodèle permet d'organiser la vue fonctionnelle et applicative de notre urbanisation. C'est un référentiel : un guide de bonnes pratiques. 

## TD 1

1. L'urbanisme est un cadre d'évolution des SI. Ce cadre là met en valeur les différentes actions à entreprendre pour améliorer les SI. Tandis que l'urbanisation est un cadre pratique de bonnes pratiques
2. Il y a 5 composantes : stratégique, métier, fonctionnelle, applicative et technique.  
   Le process d'urbanisation c'est passer d'une EA existante à une EA cible. Pour ça 4 vues : métier, fonctionnelle, applicative et technique
3. Il est impératif de cartographier les 4 vues du système. Également avoir une carto existante et une cible.
4. Modularité : permise par le découpage en briques. On a ainsi une architecture très modulaire pour permettre l'évolutivité (pour ça qu'on parle de quartiers, d'îlots de blocs).
   Subsidiarité : Car on découpe en zones, en quartiers, en îlots, en blocs. Il y a une hiérarchie forte entre des éléments. Ça permet d'être agile, réactif.
   Progressivité : car il s'agit d'une plateforme d'échange (ou collaborative, ou bus d'intégration entre les différents modules)

_16/10/18_

# II - Le processus d'urbanisation 

L'urbanisation des SI est en complément de la gouvernance des SI.

## Introduction au processus d'urbanisation

Ce process d'urbac'est l'ensemble des activité nécessaires pour otnir syst d'info urbanisé.  C'est pas un process figé : il est continu, on a un cerlce de transformation. Au bout de 3 ans, le schéma directeur est remis à jour et remet à jour carto de process. >> Processus permanent, pas limité dnas le tmeps.

L'objectif est de simplifier et optimiser la valeur ajoutée du SI, rendre SI plus adaptable et flexibl, saisir les nouvelles opportunité technologiques pour mettre à jour SI. Aussi participer à la gouvernance des SI : une fois le SI performant, il faut le contrôler et le piloter. Le managmenet permet de le rendre efficac,e la gouvernance de le piloter.

Urba SI : vision orientée process. On en a des microscopiques et des macroscopiques : polusoieurs vues dans urba SI.

Il s'agit d'un projet du SI. C'edst donc colplexe à g&rer. Il faut donc en premier lieu penser au pilotage. Grace à ça on réduit l pourcentage d'échec du projet. On va donc rapidmeent ragerder quels process prioriser pour l'optimisation. 

## Les processus opérationnels

qu'est-ce qui a de la valeur dans le SI ? Le cervice. quand on vuet optimiser, il faut aller direct sur ls process qui ont de la valeur, donc l sprocess opérationnels, donc ls process métierS. p6pdf pour quoi faire. 

Il faut un chef d'orchestre pour tout ça : c'est l'urbaniste. Il doit avoir une connaissance métier. il doit être fonctionnel, technique, et un peu de business/stratégie >> vision urbanistique. Urbanisation évite les projets "d'urgence" : c'est anticipé avant qu'on arrive sur une arhci obsolète. 

## Support et communicaiton

déconcentré

## Temporalité

C'est un process permanent, il va donc être prospectif par rapport à l'évolution du SI. Attention à la cohérence par rapport à la strat d'entreprise, il doit aussi etre stabl,e modulaire, et se baser tjrs sur process métier entreprisE. 

L'aspct cadastral : faire des carto par couche. On obtien des carte de ref de l'actuel, ancien et ce qu'on veut fairE.

Aspect opérationnel : impact, scnenarii du projet, lien avec équipe opé.

## Acteurs

dans un process d'urba des SI :

Urbanisates (ou architecte d'netreprise)

direction SI

direction métier

responsable domaine fonctionnel

responsable projrnt( couche exécutif et fonctionnel)

mais aussi architecte technique, consultant BPR, expert en conduite du changement (pour réfractaires à nouveau SI), expert métier (donnent besons). BPR =  Business Process Reengineering

trois types de reenginering : 

- radical : on rase tout, on repart de 0. Coute ultra cher
- opportuniste : profite de sprojets qui arrivnent, dnas l'urgent
- progressiste, par évolution, la meileur version.

## Instances

on vint de voir les ressources humaines, mais onva toucher aussi les départements de l'entrreprise, on appelle ça des instanceS. Plus un acteur, mais une équipe, une unité organisationnelle. p11pdf

## Compétences

Liste des compétences p12pdf

- analyse risque : doit etre auditeur avant tout, car il doit analyser l'existant pour faire architecture cible.
- connaissance stratétique car c'est un architecte.
- qualité rédac : notamment en anflais si internationale

L'urbanisate est donc une perle rare.

## Indice d'urbanisation 

### Introduction 

c'est l'établissement de l'état de l'urba du SI actuellement. pour tout ou partie de la boite. 

définition et suivi des actions menées. c'est un outil de gouvernance. 

### Axes d'analyse

Ce sont ls axes qu'on retrouve dans référentiel TOGAF. 

1. Connaitre SI existant et cible
2. pour ensuite réger référentiel entreprise
3. Voir carto entreprise
4. accompagner projets
5. maitriser la complexité des flux d'échange (carto des process)
6. piloter urba des SI
7. faire communication sur urab et developper compétences

Pour chaque axe, il faut donner criète entre 2 et 8, et noter chauqe criète entre 0 t 4. on a une grille prédifinie et on se base sur un radar. 

Il y a un lien étroit entre indice et process. 

## Influence de l'orga sur les projets SO

### Les proijets dans le processus

p17pdf : 3 composantes, et ls autres.

Pour pouvoir gérer ces 3 composantes, l'urba doit être impliqué et communiquant. 

### apport de l'urbanisation aux projets

pouruqoi on fait de l'urba ? le process prmet plusieurs apports en externe de la moerniasation du SI. 

- Srtout dans le dev applicatif. Car la couche applicative est impacté pr urba
- dans choix du logiciel, y a souvent derrière un progiciel un erp qui va évoluer
- la maintenance va être améliorée
- l'architecture va être plus modulaire et dépoussiérée

Avantages :

- limiter projets redondants
- simplifier les intégrations en limitant les impact : meileure solution = microservices. (on maitris eles ipacts)
- maitrise périmètre de projet : pas d'effet tunnel. 
- garantir cohérence, eolutivité, flexibilité applicative et technie : on est sur meme technoi langages...
- arbitrer choix progiciel et techinque: meilleure solution pour prjets
- prioriser projets

On limite donc coutrs liés aux projet, on maitris ele sporjets

### Couts de l'urbanisme

les couts = tousls efofrts qui vont être faits pour mettre en place projet. Il faut voir retour sur investissmeent qu'on va faire. Tache pour après (voutivité ?) sont pas chiffrables, mais doivent être quand même prise se compte. 

## Lerôle de l'urbnaiste

risques : trop impliqué ou trop peu comuniquant, as assez dedans prjet. l'iurba doit trouver positionnement correct entre trop d'iplication et pas assez.

## Les èlges d'rubanisme

### Définition

Les rèlges permettentde formuler ce qui est interdit et exigé. 

doivent être définies dès le dpéart, validée, acceptées, controlés, par direction notamment

### typologie des règles

on en trouve pour les pahses en amont du projet et pour les phases de la suite. n en trouve pour chauqe. Ces règles sont parfois assimilées à des bonnes pratiqus

ce qu'on va y faire p23 pdf

## L'urbanisme VS COBIT/ITIL

### COBIT

Pourquoi ajouter des règles d'urba à es merdes comme cobit et itil ? 

on retrouve l'urba dans PO et AI de Cobit. donc l'urba participe à ces deux domaines du référentiel de cobit. 

On a donc des liens entre les composants des process de ces deux approches : pas en conflit. 

### ITIL

Couche serice, pas process. Pas de lien direct avec urba. Mais lrosuq'n utilise ITL, on va avoir besoib d'inices de process, qui sont de sindicateurs d'urbanisme. Lien indirect donc, ura donne moyne pour optimiser services d'itil. Ubra peut servir de support à ITIL.



## Synthèse

chercher acteurs

3 composantes dnas process:  pilotage, étude en amont, pilter/prioriser porjet

pour ça, de l'aide : grace à support, référentiels (données/servcie), proposer architecture

## TD 2 : Renault

### 1. Enjeux

Les enjeux de l'étude d'urbanisation sont d'optimiser les process à  plusieurs niveaux. Unifier les différents échanges, les tehcnos utilisés pour cela, et les logiciels ASP/ERP ainsi que leurs rapports interne/externe. Améliorer le SI pour le rendre évolutif. 

Améliorer le temps de réponse des requêtes entre fournisseurs, partenaires, clients.  
On va assurer la cohérence et la qualité d'échange.  
Gain de productivité derrière.   
Fonctionnement du SI plus performant.

### 2. Attentes

**Pour direction métier :**

Optimiser les process en lien avec les partnaires externes afin d'atteindre plus d'efficacité. 

description de l'existant en termes de process (carto)  
Description de la vision cible (carto qui va permettre réegeninring) 
Oriente les responsables ver sla refonte ud SI

**Pour direction informatique :**

Unifier les outils et technologies utilisées dnas les différents types de d'échanges.

Vue applicative  
Avoir une vision tehcnique sur c qu'il doit aborder comme technologie et mettre à niveau  

### 3. Démarche

La démarche mise en œuvre a déjà été rodée sur des chantiers précédents. C'est une démarche de type **urbanisme**, en deux étapes.
La première étape vise à faire un état des stratégies **métier**, des stratégies **SI** et des dysfonctionnements par rapport à ces stratégies. Elle conduit avec une approche **macroscopique** sur un champ limité, essentiellement sur l'ingénierie et la logistique. L' **existant** et la **cible** sont décrits, la demande est formalisée. Les **résultats** sont publiés et font l'objet de discussions avec les interlocuteurs concernés. Cette étape permet de comprendre la problématique de l'étude. À la différence des études **métier** classiques, l'étude n'est pas un chantier métiers. Elle ne concerne pas un métier en tant que tel ; le **B2B **n'est pas un métier. L’étude ne peut pas embrasser l'ensemble des métiers concernés mais il faut faire partager les classiques, résultats et les **recommandations** par tout le monde.
La deuxième étape a comme objectif d'établir un **plan** d'action, en priorisant les actions en fonction de leur valeur métier, de leurs **risques** informatiques et des difficultés ou des **schémas directeur** à faire. Ici, le champ de l'étude est élargi et approfondi, sans être ciblé sur un métier. Cette étape produit un ensemble de recommandations. Pour s'assurer de la **complétude** est croisée avec les domaines **fonctionnels** et **applicatifs** de ses recommandations, la liste des activités de l'entreprise est réalisée. La deuxième étape produit également une **méthode** et une analyse des **données** utilisable dans les études d'urbanisation des relations directions métiers avec les **fournisseurs**. (Comment l'entreprise peut concevoir le travail avec les fournisseurs ? Quel support mettre en œuvre ? Quels outils utiliser...)

