# Introduction

# Qu'est-ce que l'urbanisation des SI ?

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