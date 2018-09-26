# Introduction

Urbanisation : amélioration/optimisation/agencement d'un système pour ses membres.

BPM : à l'intérieur de l'urbanisation des SI = transformation digitale, urbanisation, pour les petites entreprises.  
Business Process Management

BPMN : système de notation du BPM. Seimann fait ça dans sa merde qui lui sert d'entreprise.

On a un SI. Pour le gérer, il faut faire du management des SI.   
À l'intérieur on a la gouvernance des SI, pour contrôler et piloter l'évolution SI (ITIL, COBIT...)  
Mais pour pouvoir le contrôler il faut mettre en plce des bonnes pratiques. C'est là qu'arrive le sous-domaine **urbanisation des SI**. Elle est toujours centrée métier donc centrée process, donc c'est un BPM.  
Permet d'apporter plus d'information pour la gouvernance. 

Max couverture : besoin fonctionnel  
Max DI : Taux de couverture = chaque besoin fonctionnel de l'entreprise doit être couvert.

L'idée de l'urba est d'utilisar la métaphore avec urbanisation ds villes pour l'appliquer au SI, car on a une complexité silmilaire. 

- SSIS 
- modélisation de données - cube olap multidimentionnel) DataVault. On commence par de l'intégration (ETL). On va  y aller par couches.
- deep learning & machine leardning // clustering supervisé ou non
- tuning bdd : big data. NoSQL. Système de recommandation.

En urba, 2 mots clefs : cohérence et agilité.  
Le but est de rendre le SI cohérent par rapport à la stratégie de l'entreprise.  Il faut aussi le rendre agile par rapport au besoin du marché

## Plan

- L'urbanisation des SI
  - Architecture d'netreprise
  - Notion d'urbanisation
  - Métamodèle de concepts
- Le processus d'urbanisation
- Le management des processus



## Partiel

- Étude de cas
- TD

# I - L'urbanisation des SI

## L'architecture d'entreprise - EA

### Contexte stratégique

Les contextes sont ls occasions de regarder nos process métiers et de reprendre ça.

La montée des nouvelles technologies peut rendre un système obsolète en 3 ans. Il faut faire une veille fournie et constante.

3 phénomène font un pression sur besoin d'urbanistion du SI. Également d'autres  éléments de contexte poussent vers l'urbanisation.

Le contexte dnas ls entreprises, c'est plusieurs besoins : 

- besoin d'adapter la stratégie pour que l'entreprise devienne meilleure.
- pour ça il faut analyser les processus, la chaine (voir BPM). KPM = clé d'indications de performances. C'est le process qui fait ça.
- process étendu = qui touche plusieurs flux/logiciels. qui part du fournisseur et qui va jusqu'au client. Ex : la chaine logistique. C'est souvent complexe à gérer, il faut donc des process bien optimisé, un plan d'action (BPM).

contexte stratégique : on retrouve dnas l'entreprise une demande croissante d'évolution. s'ajoute à ça le gros bordel de l'entreprise : des versions différentes, des langages diférents, logiciels différnts. Ca rend le système rigide, l'acquis est lourd. On peut pas tout changer en partant du principe que c'est pourri, il faiut tenir compte de l'ancienneté de la boite et effectuer une évolution, pas une révolution. Fair une refonte complète a torp de désavantages : cher, risqué, manque de valuer ajoutée. 

L'objectif est d'améliorer l'adaptabilité du SI et de son parc applicatif. On ne raéagit pas directmeent fac eà un besoin, mais on évolue de façon permanente. On est dnas le progessif. simplification max de l'architecture, optimisation de la valeur ajouté, rendre le SI plus flexible.

Dans ce contexte stratégique on retrouve ls mots clefs :

- évolutivité
- performance
- alignement stratéigque

Le lean management se retrouve imbriqué das l'EA

L'EA est un cadre commun qui permet la comm en comité pilotage et exécuteurs et responsables métiers. C'est le seul moyezn de comm qui permet ça.  c'est le socle de l'urba des SI. Sans Ea on arriv epas à mettre en place (d'un pt de vue pratique) les lignes et objectifs de l'entreprise.

L'EA met les différntes visions de l'archi ne synergie vec archi métier ( = alignement statégiue)

Comment établir ? on commence par établir archi xistante, puis on définit archi cible. Pour faire l'existante, voir pdf

l'EA va établir une feuille de route => schéma directeur informatique (à regarder, chaque boite doit la publier, tous les 3 ans. cf celle de la caisse de retraite)

C'est donc un travail autour du SI, dnas lequel on fait intervenir tous les acturs (DSI, OE, Ma, archi d'entreprise, urbaniste). 

Il faut avoir un cadre de référence. Dedans  plusieurs visions (voir pdf)

Le premier c'est le cadre Zachman. il fonctionne avec des pbiques (voir pdf). Pour lui 'st un concept d'ensemble de briques. Il faut répondre à ces question pour chauqe bvrique. Il ne s'agit pas d'un référentiel (comment faire) mais d'un cadre de référence (que regarder). Dedans on a différentes visions sur l'entreprise (pdf). ce n'est pas un référentiel il n'y a pas bcp de choses (pdf), c'est un ensemble de birque élémentaires qui vont définir l'entrepris eet son outil. 

TOGAF : plusieurs références, éléments, à regarder. on passe rapidement dessus, pour ceux qui vuemnt faire de la transformation digitale. TOGAF est un réfzrntiel. 

EA vers urbanisation : on part d'un truc vers un autre j'ia pas tout suivi. Urbanisation = vision centrée métier. On va mettre en place (voir pdf)

La métaphore de l'urbanisme. On utilise de smodèles de l'urba pour adapter le SI. mots clefs (pdf) sous objectif de refonte. Ca résume ce qu'on peut assurer avec urba du SI.

4 définitions sur PDF. urbanisation = application d'un plan d'urbanisation sur le SI.



comment fonctionne l'urba ?

on part d'une archi non organisée, on applique les règles d'urba pour arriver à une archi cible, qui ser aorganisée. 

Nouvelle archi urbanisée, participe au dispositif de gouvernance. elle est évolutive, peut accueilli de nouvaux composants.

URba est un apport dans gstion des risque parce qu'on peut les étblir et régler très rapidement. 

Sans outil de cartopgraphie, on peut rien faire. on a besoin de l'archi actuelle et du cible, c'est pour ça qu'on a besoin de l'outil de cartopgrahie. Besoin de 4 carto  (pdf). PDF : bon déroulement du'n plan d'urba.

Pouruqoi on utilise les outils cartographiques ? 

urba SI est solution au RGPD  
diff"retnes motivations au urba SI voir PDF

Il y a un méta modèle de l'urba des SI. Il fat remplir les trous de barhi. et ce avec concepts de base de l'U SI. Basé sur concepts de base de l'urbanisme : base fonctionnel, quartiers, ilots...  
Voir metamodele.png

Ca permet d'organiser la vue fonctionnelle et applicative de notre urba. Le métamodèl est un référentiel : un guide de bonnes pratiques. 

## TD 1

1. Urbanisation implique une action, urbanisme est un domaine d'expertise.
   
   L'urbanisme est un cadre d'évolution des SI. Ce cadre là met en valeur les différentes actions à entreprendre pour améliorer les SI. Tandis que l'urbanisation est un cadre pratique de bonnes pratiqus

2. décomposition en zones, quartiers et ilots? ou en opérations. Il en découle une vue métier, fonctionnelle, applicative et techniuqe.

   Il y a 5 composantes : strategique, metier, fonctionnelle, applicative et technique. Le process d'urba c'est passer d'une EA existante à une EA cible. Pour ça 4 vues : metier, fonctionnelle, applicative et technique

3. il faut établir l'EA (alignemetn stratégique), en adoptant un cadre de référnce (Zachman). Etablir archi existante puis définir archi cible. Faire feuille de route (schema directeur info). Avoir une vision centrée métier.

   Il est impératif de cartopgraphier les 4 vues du système. Également avoir une carto existante et une cible.

4. modularité car l'urbanisation doit permettre de s'adapter à la nouveauté, se faire en évolution. subsidiarité car implication de tous les membres de l'entreprise (directif, executif). progressivité car ne pas faire table rase de ce qui existe maisévluer à partir de l'existant, sinon c'est couteux, risqué et n'apporte rien.

   Modularité : découpage en brique permet modularité. Architecture très modulaire pour permetttre évolutivité.(pour ça qu'on parle de quartiers, d'ilots de blocs)
   Subsidiarité : Car découpe en zones, en quartiers, en îlots, en blocs. Hierarchie forte entre des éléments. Ça permet d'être agile, réactif.
   Progressivité : car plate forme d'échange (ou collaborative, ou bus d'intégration entre les différents modules)