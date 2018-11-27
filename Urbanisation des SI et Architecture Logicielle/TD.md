# TD

## TD 2 : Renault

### 1. Enjeux

Améliorer le temps de réponse des requêtes entre fournisseurs, partenaires, clients.  
On va assurer la cohérence et la qualité d'échange.  
Gain de productivité derrière.   
Fonctionnement du SI plus performant.

### 2. Attentes

**Pour direction métier :**

description de l'existant en termes de process (carto)  
Description de la vision cible (carto qui va permettre réegeninring) 
Oriente les responsables ver sla refonte ud SI

**Pour direction informatique :**

Vue applicative  
Avoir une vision tehcnique sur c qu'il doit aborder comme technologie et mettre à niveau  

### 3. Démarche

La démarche mise en œuvre a déjà été rodée sur des chantiers précédents. C'est une démarche de type **urbanisme**, en deux étapes.
La première étape vise à faire un état des stratégies **métier**, des stratégies **SI** et des dysfonctionnements par rapport à ces stratégies. Elle conduit avec une approche **macroscopique** sur un champ limité, essentiellement sur l'ingénierie et la logistique. L' **existant** et la **cible** sont décrits, la demande est formalisée. Les **résultats** sont publiés et font l'objet de discussions avec les interlocuteurs concernés. Cette étape permet de comprendre la problématique de l'étude. À la différence des études **métier** classiques, l'étude n'est pas un chantier métiers. Elle ne concerne pas un métier en tant que tel ; le **B2B **n'est pas un métier. L’étude ne peut pas embrasser l'ensemble des métiers concernés mais il faut faire partager les classiques, résultats et les **recommandations** par tout le monde.
La deuxième étape a comme objectif d'établir un **plan** d'action, en priorisant les actions en fonction de leur valeur métier, de leurs **risques** informatiques et des difficultés ou des **schémas directeur** à faire. Ici, le champ de l'étude est élargi et approfondi, sans être ciblé sur un métier. Cette étape produit un ensemble de recommandations. Pour s'assurer de la **complétude** est croisée avec les domaines **fonctionnels** et **applicatifs** de ses recommandations, la liste des activités de l'entreprise est réalisée. La deuxième étape produit également une **méthode** et une analyse des **données** utilisable dans les études d'urbanisation des relations directions métiers avec les **fournisseurs**. (Comment l'entreprise peut concevoir le travail avec les fournisseurs ? Quel support mettre en œuvre ? Quels outils utiliser...)

------

_17/10/18_

On va retrouver toujours les mêmes questions dans les études de cas : quel est le process métier ? Est-ce un process métier ou support ? Comment on va l'optimiser ?

Au partiel on va nous demander soit une archi fonctionnelle, soit une archi applicative.

### 4. Schéma d'infrastructure

![schéma d'infrastructure d'échange](/run/media/aveias/data/Documents/Cours/Sciences%20U/Notes/m2/Urbanisation%20des%20SI%20et%20Architecture%20Logicielle/Ressources/TD2-4.jpg)

Plusieurs blocs dans des blocs. La plus petite unité de blocs représente les blocs fonctionnels. On les regroupe ensuite  en sections et les relie aux différents acteurs / entités (les blocs de premier niveau).

La meilleure solution était de dissocier les blocs par domaine (métier, support et fonctionnel). 

On peut en savoir plus en cherchant "Renault urbanisation" sur Internet, y a un article qui détaille tout.

## TD 3 : Société générale

_// TODO : Choper une vraie correction de ce TP, j'ai pris ça vraiment à l'arrache. Si quelqu'un passe par là et me corrige c'est cool._

### 1

Qu'est ce qu'on va gagner à avoir la direction impliquée ? 

1. On va prioriser le projet et augmenter le degré d'importance. 
2. Implication et mobilisation de tous les acteurs de l'entreprise car le projet est poussé par la direction
3. Un financement, car la direction alloue un budget au projet
4. L'implication de la direction dans le pilotage du projet. 

### 2

La réforme permet de sécuriser le (... ? j'ai entendu "FO" mais je sais que c'est pas ça.)

### 3 

Renforcer la cohérence des investissements et les rationnaliser par le process de normes d'investissements.

Capactié à livrer/modéliser plus rapiement les nouveaux process des normes

Optimiser le process : plus de réactivité par rapport aux besoins métier.

### 4

1. Lancement
2. Formalisation des objectifs métier
3. Cartographie bilan de l'existant
   Carto applicative existant
   Carto fonctionnelle existant
   Carto process existant
4. Définition de la cible alignée sur les obj métier
   Carto appli cible
   Carto fonctio cible
   Carto process clé cible
5. Scénario de convergence vers la cible

### 5

Rôles marqués dans la diapo (p20pdf) :

- Conseil
- Contrôle
- Validation
- +1 je crois

### 6

Dit en fin de cours mais mon esprit était déjà au bar. Et mon ordi rangé.

------

*09/11/18*

Dans deux semaine, truc à faire à rendre pour première note.

Deuxième note la smeaine suivante, un bpmn à suivre et à montrer. 

## AXA : urbanisme et gouvernance

### Contexte

#### 1 

réglementaire (AXA est une multinationale, elle va dépendre de son emplacement, et donc des règles locales en fonction, de là où elle est implantée) => contexte de conformité règlementaire (rappel : norme BAL2 la dernière fois, ici on dépend de l'emplacement)

- transverse (peu importe ce qu'elle fait : elle gère tout ce qui est risque, peu importe le cœur de métier.)
- 
- 
- couts
- unité
- transnationale
- infrastructures
- applications
- contractualisés
- service (SLA = contrat de service)
- processus
- changement
- conception
- oeuvre
- ouvrage
- vers le holding
- cycle de vie

DONC l'objectif stratégique d'AXA actuellement est de réduire les coûts. Ils font des développements spécifiques par continent, c'est cher, ils créent donc AXA tech pour mettre à plat les process, normaliser tout les process, standardiser, et ajouter la couche règlementaire nécessaire par continent. 

Pour urba des SI : fusion, rachat, mise à niveau. 

### Grandes phases d'urbanisme 

#### 2 

1. Cartographie existant
2. Carto de la cible (process)
3. Lister les opportunités et les solutions qui existent (prioriser les projets)
4. Proposer les projets et un plan de migration

### Conduite d'urbanisme

#### 3

L'intérêt pour le département archi, c'est qu'il représente le pilier du process. Il aura donc une gestion de projet stratégique : un pilier stratégique pour maîtriser tous les process, les mettre à plat et les étudier (on fait une archi existant et cible). Ce département en plus d'être l'acteur pilier ce qui va donner une influence stratégique, une maîtrise des process et permet de prendre les décisions. C'est ce départment qui va prendre les décisions et déterminer les solutions adéquates. Il devient le centre du process. Il devient donc acteur stratéiguqe pour la réalisation du projet. 

#### 4

Ils sont à leur 5e projet. Ils maitrisent toutes les phases de process d'urbanisation, ils auront plus de crédibilité financière, pour la direction notamment, il y aura plus de budget. 

#### 5

Car agile et cohérent. On va trouver des process cohérents, et du point de vue technique ça va être agile, donc s'adapter aux besoins de l'entreprise. C'est donc ces deux termes à mettre en avant auprès de la direction pour la convaincre. 

## AXA : Application Portfolio Management

Outiller la gouvernance du parc applicatif

### 1

- Enjeux métier :
- Coût : maîtrise des risques, exploration et infra, 
- 
- Adéquation : adéquation fonctionnelle, projet

### 2, 3

La carte permet de prioriser les SA. On laisse par exemple de côté le SA3. Il faut améliorer le SA5

### 4, 5

Par rapport à la couche infra et les enjeux métiers, on voit si l'app tourne avec un bon support technique derrière. 

le SA5 a un problème : il est pas hyper pérenne. c'est comme ça qu'on peut l'améliorer. 

Après directement on commence l'architecture des process métier. 

## Conclusion

### 6

- nord : marché et client
- est : organisation efficace
- sud : résultat et profit
- ouest : personnes mobilisées

### 7

- nord : améliorer l'accès aux informations et produits et donc améliorer l'interface homme/machine. Avantage concurrentiel et valoriser le client.
  Tableaux de bord pour évaluer le marché. Orienter la stratégie de l'entreprise.
- est : valoriser les outils de communication . chaque acteur peut donner son avis. 
  documentation 
- sud :  les 4 couches répondent à la stratégie de l'entreprise. Le SI doit être évolutif et répondre à la stratégie qui change toujours.
  On rend le SI homogène et on harmonise
- ouest : plans de communication, réunion
  responsabiliser chaque acteur
  acteur doit pas seulement être principal et rendre cohérente toute la communication et le mouvement doit être global, en réseau. 