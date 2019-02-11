# Intro

On va bosser sur la Big data, Python, Hadoop, Spark

Objectif principal : améliorer les performances. 

## Examen final

- 1e partie : examen écrit (1h, relatif aux slides)
- 2e partie : code (plus simple que ce qu'on a fait en TP) sur jupyter notebook (2h)

# Big Data

## Réviser Big data

Les données sont représentées comme un réseau : connexions entre points.

On peut avoir une liste de clients, il n'y a pas de relations entre eux. Mais on peut les foutre sur un graphique et tirer de l'information, par exemple à partir de l'espace entre les points. 

On a donc un réseau à comprendre et dont on doit tirer de l'information. Exemple de Google PageRank : chaque node est un website, et il y a des liens entre les sites > réseau. Un site avec beaucoup de liens vers lui sera plus important  qu'un avec moins. 

## 1.2 - Modélisation des réseaux

$$
C_T = ( V, E)
$$

Où V est un jeu de noeuds et E un jeu de relations

On modélise les noeuds et les relations comme sur le PDF

Ça peut être dirigé ou non  : dirigé on a un sens dans le réseau, c'est le cas du PageRank.  On peut aussi avoir du poids sur les réseaux (graphe pondéré)

Réseau est un terme technique, graph un terme pratique pour représenter la même chose

On réprésente V = {a, b, c, d, e} et E = {ab, bd, bc, cd}

d la distribution des degrès des noeuds. d : {1,2, 2,1,2} . 

d(b) = somme du poids total des relations

$d^+(b) =$  nombre de relations sortantes de b (=2)

$d^-(b) =$ nombre de relations entrantes vers b (=1)



Composants connectés  : Si on peut aller de a vers b, alors a et b appartiennent au même composant connecté. 

Composants fortement connectés (SCC) :  depuis n'importe quel point on peut aller vers un autre. Toutes les directions existent. 

Entre deux SCC, un noeud/SCC vers lequel un SCC de référence se dirige est un out-compoment. À l'inverse, si il se dirige vers le SCC de référence c'est un in-component

À partir des graphes on génère des matrices (voir pdf), on peut compter le nombre de connexions entre les points et tout et tout. Dans un truc non dirigé, M[a,b] = M[b,a]. Si on a une relation M(a,b) = 1, sinon 0. Dans un graph pondéré, M[a,b] = le poids de la relation.

coût : n²

Liste des relations : n*degré moyen (a peu égal à log(n))

Si on a pas le réseau (donc la totalité des données), on va générer un réseau artificel, similaire au réseau réel. Trois méthodes communes qu'on va aborder rapidement.

On connait le nombre de noeuds (1000), pas toutes les relations. On peut étalir le réseau à partir de la probabilité d'avoir une relation entre un noeud et un autre. p.e, chaque nœud a environ 20 connexion. 
$$
degre_a \approx p*n = \frac{20}{1000}*1000 = 20
$$


P : probabilité
$$
P(ab\ is \ an \ edge) \approx Bern(p)  \\
P(degre\ of\ a) \approx Binom(p*n) \approx poisson\ law
$$
Le fait que la plupart des noeuds aient un degrés proche de p*n n'est pas correct dans la réalité. Ces réseaux ne sont donc pas corrects dans la réalité, mais utiles. 

### Réseaux sans échelle

n : nombre de noeuds

$\lambda$ : power parameter ($2 \leqslant \lambda \leqslant 3$)
$$
Nb\ edge = \sum_adegre(a) \\
= \sum i*\frac{n(\lambda-1)}{\lambda^{i+1}}
$$

### Réseaux petit monde 

Les noeuds ne s'atteingnant pas directement, mais sont à une très faible distance les uns des autres (genre moins de 6 étapes pour aller de a vers b)

## Analyse des modèles : Google page Rank

Problématique du spam de mot clef contournée grace au système de PageRank qui donne de l'importance à la page, indépendamment du nombre du mots-clefs.

L'importance du site et donc la probabilité qu'on veuille aller sur celui là se calcule à partir d'une matrice. De cette matrice, on divise toutes les valeurs 1 de sorte à ce que chaque colonne fasse un total de 1.

|      | a    | b    | c    | d    | e    |
| ---- | ---- | ---- | ---- | ---- | ---- |
| a    | 0    | 1    | 1    | 0    | 0    |
| b    | 0    | 0    | 0    | 1    | 0    |
| c    | 1    | 1    | 0    | 0    | 0    |
| d    | 0    | 0    | 0    | 0    | 1    |
| e    | 0    | 0    | 0    | 1    | 0    |

devient

|      | a    | b             | c    | d             | e    |
| ---- | ---- | ------------- | ---- | ------------- | ---- |
| a    | 0    | $\frac{1}{2}$ | 1    | 0             | 0    |
| b    | 0    | 0             | 0    | $\frac{1}{2}$ | 0    |
| c    | 1    | $\frac{1}{2}$ | 0    | 0             | 0    |
| d    | 0    | 0             | 0    | 0             | 1    |
| e    | 0    | 0             | 0    | $\frac{1}{2}$ | 0    |

on obtient une matrice conditionnelle. Chaque ligne est 1/5, on fait la somme en fractions de la ligne et on a la matrice. La somme des éléments de la matrice donne 1. 

Une affaire de V ensuite. $V_0$ est la probabilité d'accéder à un point depuis n'importe  quel point de départ. 



## TP: Python pour Data Science

Installer Anaconda

Copier la database soccer et la metttre dans le dossier "python"

finir TP 0 et 1

----

*26/11/18*

À faire : 

1. Les Pandas notebook week1
2. Puis ls TP week 2. Pour chaque exercice :
   - Example = comment faire l'exo
   - exercice = à faire : remplir les champs
   - hint = résultat
3. Une fois fini :  envoyer à tien-nam.le@ens-lyon.fr

---

*20/12/18*

## Memory latency

Pbatique en big data : le volume de données augmente. Avant on gérer ça en ajoutant juste de a mémoire (RAM). Mais maintennat on fait plutôt des clusters avec plusieurs ordis pour de l'analyse parallèle de données. Différents ordis avec différentes mémoires qui aprtagent la même data. 

DONC : qu'est ce qui rend le calcul lent ? Pourquoi on a besoin de plusieurs ordis ? 

### CPU computation

Dux grandes parties dans un ordi : 

- CPU
- Stokage

l'ordi lit A et B selon leur emplacment sur le disque, et calcule par exmple C à partir de A et B, puis inscrit C sur le disuqE. Le temps de lecture et d'écrtirue est plus long que celui de calcul. 

### Memory hierarchy

Le CPU contient plusieurs core avec chacun une section register. Chaque core est relié à des blocs de cache (L1, L2) et un bloc de cache global (L3). L3 st relié à la mémoire principalke (RAM) qui est reliée au disque dur.

### Questions

- Performing CPU operation has the lowest latency
- False
- A computation just done is stocked in the register

### Trade off

Cache est petit et rapide, mémoire principale grande et lente.

### Cache

le CPU récupère blocs stockées en cache pour calculer. 

Si bloc n'est pas en cache, on vire un bloc ancien plus utile, et hop on le remplace par celui nécessité. 

La performance du cache vaut :

$perf = \frac {cache\ hits}{cache\ miss}$

miss : recherche bloc qui n'est pas en cache

Pour avoir plus de cache hits (besoin d'un bloc déjà en cache) , on garde en cache données souvent utilisées. quand on overwrite des données en cache on écrase tjrs celle la moins utilisée du cache : **temporal locality**

Il copie un bloc entier (64kb), même si seuleent 10kb sont utilisés dedans, car temps pour bouger 10kb ou 64kb sont très proches.

Exemples de temporal locality :

on calcul à partir d'un élément W fixe et d'un élément x qui change tout le temps. si w rentre dans le cache, on le réutilise tout le temps : c'est plus rapide. Si trop grand pour cache : c'est bcp plus lent. 

Exmple de spacial locality : 

on veut calculer la somme d'opérations sur x pour x de 1 à n : chaque nouveau x est proche de ses voisins : on gagne plus de temps que si il était stocké aléatoirement. 

### Questions

1 - On a pas besoin de garder A car trop grand, et juste besoin de garder sum dans la mémoire. Par contre on itère avec des valeurs qui s suivent : il est plus efficace de faire un spatial locality. (Au pire répondre "both" est acceptable)

2 - 64 bytes (the block size)

3 - la dernière réponse

### Conclusion

Pourquoi est-ce important de g&rer la memory latency en big data ? 

clock rate semble plafonner à 3gh

Les ordis plus rapides sont très chers, 

Il vuat mieux vaec pleins d'ordis pas chers en lcluster, chacun ayant une petit partie du calcul. Donc :

**comment diviser la data** ?

## Clustering Data

Combien de clusters faut-il ? Le moins possible mais avec la plus grande similitude entre les données possible par rapport à la courbe d'efficacité : quand elle commence à devenir similaire d'un cluster à l’autre, on a notre nombre idéal. Il faut essayer pour trouver le nombre idéal de clusters.

### Types de techniqus de clustering

on peut tous les déclarer en même temps "flat techniques"

ou bien répéter des clusters basés sur clusters prédents : "hierarchical techniques"

### K-means clustering example

technique très simple

étape 0 : choisir K ( genre K = 3)

étape 1 : choisir 3 entiers au hasard. ils sont placés dans un sorte de graphique, et par rapport à un point (un vrai) on repère celui qui est le plus proche.

étape 2 : on détermine une zone par point et tous les points de cette zone sont raccordés à ce point. Ensuite on bouge le point de référence à la position optimal : proche du plus de points possible

Ensuite chaque cluster fait les calculs autour de là ou il est.

L'avantage c'est que c'est simple et efficace. Par contre il faut définir la distance, et c'est très sensible aux "outlier" : points éloignés des clusters.

----

*25/01/19*

# Distributed and cloud computing

## Distributed computing

Les problèmes posés sont par exemple un SUM SQL sur une base contenant trop d'entrées pour être comptées une à une par le système. Ou bien en ML : la régression linéaire, ou trouver le voisin le plus proche

Objectif : comment aller plus vite ?

### Hadoop

Créé par Google en 2004. Ça distribue le stockage, mais aussi le calcul et a une bonne tolérance aux erreurs. Utilise le map reduce et le HDFS

### Map reduce 

Fonctionnement : les map sont des "escalves", qui récupère l'input d'un disque dur, font le calcul niveau 1 renvoient aux maîtres, et les reduce sont les maîtres qui font le calcul niveau 2, et renvoient le résultat sur un autre disque dur.

Si par exemple on a 30 produits, on veut calculer la somme (exemple 1), on va diviser les 30 en plusieurs parties envoyées au mappers, qui vont chacun effectuer le calcul sur leur set de data. Ils renvoient ensuite tous leur résultat au même reducer qui va additionner le tout et renvoyer le résultat.

Si on a $k$ mappers ça permet d'aller $k$ fois plus vite. 

Un autre exemple : trouver le plus proche voisin k  
on a deux mappers, le 1 sont les points verts et le 2 les marrons.   
avec un point d'entrée "query point" il faut trouver les 3 points les plus proches. le mapper 1 va envoyer les 3 points verts les plus proches et le 2 les 3 points marrons aux reducers, ce ne seront pas les mêmes. Le reducer renvoie les 3 points les plus proches parmi les 6 récupérés

### HDFS

Hadoop Distributed File system. Son objectif c'est la tolérance aux pannes.

On a plusieurs PC avec chacun un disque. Certains sont des mappers, d'autres des reducers. Ce sont des data nodes. On va avoir à côté un name node, à  qui chaque data node envoie ses métadonnées : il garde une trace de tout ce qui se passe. si un noeud tombe, le name node le réplique ailleurs.

- Si il y a un prolème de réseau, ce n'est pas résolu.
- Si un data node a un problème de disque, le name node peut recover la data
- Si la taille des blocs diffère ce n'st pas un problème
- Si tout les data nodes ne sont pas utilisés, ce n'est pas un problème.
- Si on a une panne de disque sur le name node, c'est un plus gros problème.

Comment récupérer la data si un nœud tombe ? Chaque bloc de données est répliqué 3 fois et envoyé sur des nœuds aléatoires. Si un nœud tombe, il sait quels blocs sont tombés, mais il sait aussi qu'il peut les retrouver ailleurs, et le nœud qui prendra le relai récupérera les blocs depuis les nœuds qui ont une version répliquée.

Si le name node tombe, tout est perdu, on le duplique donc pour que le second prenne le relai si le premier tombe.

### Avantages de Hadoop

- Gratuit et open source

- architecture distribuée : les données sont stockées dans plusieurs noeuds différents

- tolérance au pannes (3 répliques de chaque bloc)

- Viable : réparation automatique en cas de panne

- Haute disponibilité

- Modulable : on peut ajouter facilement de nouveaux ordis et données


### Inconvénients de Hadoop

Efficace dans les algorithmes qui n'effectuent qu'un calcul dans une direction. Mais si ils utilisent la data de façon répétéé (descente de gradient, k-means, deep learning, graph algorithm (shortest path)), il se révèle inefficace. En effet, en hadoop à la sorite des reducers la data est stockée en disque et non en RAM avant d'être réutilisée pour les calculs. C'est de la redondance ! L'étape la plus coûteuse en temps est l'écriture et la lecture sur le disque, non le calcul.

C'est pour ça que dans ces cas on va se pencher plutôt vers Spark.

## Spark

Au lieu d'écriture la data sur le disque dur à chaque fois, il la stocke en mémoire vive.

Spark créé en 2012, est opensource, et bien plus rapide que Hadoop.

Mais il a deux problèmes :

- La RAM, c'est cher, bien plus que la mémoire dure.
- La RAM est plus efficace mais mois *stable* : moins tolérante aux pannes. si l'ordinateur tombe, la data est perdue.

Le challenge est de rendre Spark tolérant aux pannes. 

Dupliquer la data sur les nœuds est très cher puisque la RAM est chère.  
Garder une trace de chaque changement est aussi cher car il y en a beaucoup.

La solution :  **Resilient Distributed Datasets**. Ils gardent une trace des changement sur chaque bloc (plusieurs éléments)

Un exemple : la régression linéaire. 



En conclusion : on utilise Hadoop si le calcul se fait dans un seul sens et qu'on a peu de budget, et Spark quand le calcul est itératif et qu'on priorise la vitesse.

## Cloud computing

Face au problème de la big data, deux solution, on a v la première : architecture distribuée, maintenant on va voir le cloud computing, deuxième solution.

C'est un peu similaire à l'architecture distribuée, mais pas complètement.

Les problématiques des entreprises sont de bien estimer les besoins, et implique de sacrées infrastructures. La solution idéale st de ne pas avoir à anticiper ces besoins et leurs couts, d'avoir de l'adaptabilité, de ne pas se préoccuper de la sécurité ... L'infra cloud apporte tout ça : les services sont accessibles à distance. Nombreux avantages et l'inconvénient de devoir trouver un fournisseur de confiance.

AWS est le plus représenté ajd à 50%

### Technologies

Deux technos : la virtualisation et le high broadband Internet

La virtualisation permet de partager une large ressource entre plusieurs clients.

### Types

Trois types de clouds : 

- public. Le plus populaire, B to C. Ex : Dropbox. Partagé par énormément de clients. Peu cher, pas de maintenance, haute disponibilité, extrêmement modulable.
- privé. L'accès est exclusif et non partagé.
- hybride. les données et apps peuvent passer du privé au public pour plus de flexibilité.

### Niveau de services cloud 

On en a trois : 

PaaS, Platform as a Service. Fournit des ressource,s des platformes, sur lesquelles les développeurs peuvent construire des applications.

IaaS, Infrastructure as a Service. Fournit serveur, réseeau, stockage, et la maintenance est à charge du client.

SaaS, Software as a Service. Fournit le logiciel final

