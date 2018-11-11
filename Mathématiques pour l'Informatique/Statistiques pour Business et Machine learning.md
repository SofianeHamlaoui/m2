# Intro

we 'll review everyhting for business et macine learning

Part 1 on statistiques descriptives et probabilité

Stat descr : théorie, pas d'exercice

Propba : 

Partie II (4h aujourd'hui)

tout ce dont on aur abesoin pour coprendre les stats

tes hypothèse : collect data to improve what is right or weong.

Partie III on verra put être plus tard

# I - Statistiques descriptives et probabilité

## 1.

### 1.

sur un même population, on peut collecter sur différents échantillons et obtenir différents données

Nombres discrets vs continus. à redéfinir

la première partie des stats c'st la descriptive > obtnir la data et des conclusions  
seconde partie c'est la déduction > déduire des conclusions sur la population

### 2. Paramètres importants

Différences entre moyenne = valeur moyenne, médiane = valeur du milieu, mode = élément les plus fréquents. On a aussi 1er quartile et 3e quartile, qui sont des médianes correspondant à 25% et 75%.

Donnée aberrante = s'écarte de tout le reste. On peut considérer environ 2% de chaque côté pour les outlier.

Boîte à moustache : façon de représenter ces données (image de gauche), à ne pas confondre avec les chandelles (image de droite).

Variance : se calcule sur échantillon et population à partir de la moyenne t du nombre de personnes. Permet de voir si la moyenne st basée sur des valeurs très différetnes ou plutôt rapporchées. 

Écart type / Cote Z ... à revoir

Covariance  
Quand on vuet voir la corrélation entre deux données. Lz relations entre elles.  

Corrélation  
différetn de la covariance, calculé à partir. difficile d'exploiter la coviarianc,e la corrélation oui. Ça normalise la covariance ! relation de 1 ou -1 relaiton liéaire (mais pas de lien, genre c'st la même chose). 0 au contraire. 

### 3. Interprétation et présentation des données

On voit une tétrachiée de façon de réprésenter les données. Il faut adatper la représentatio aux données. 

Il y a des bons et mauvais échantillons : ils sont représentatifs de la population ou non. 

## 2. Probabilités

### 1.

Voir les probabilités importantes, formules, règle,s tout est sur le slide

### Exercices

#### 1. 

On al'univers suivant du nombre d epsycholgues choisis : {0, 1, 2}

On calcule d'bord la probabilité de n'avoir aucun psychologue

P(x=0). La proba que le premier soit un psychiatre est de 30/54  
La proba que le deuxième en sot un aussi est de 29/54.   
Donc P(x=0) = 30/54 x 29/53

On cherche l'inverse ! Puisque P(x=2) + P(x=1) = 1-P(x=0).

Donc proba = 332/477 ~ 0,70

#### 2.

si possibilités (1/3 x 1/2)

On calcule P(A|B) 

## formule importantes

variable aléatoire

espérance

**Variance**

Bien différencier vairance de population et variance d'une variable aléatoire

Deux formules de variances, deuxième larche que sui X et Y indépendants

Note : 

Si X et Y indépndants

Var(X-Y) = Var(X)+Var(Y)

Cara

Var(X-Y) = Var(1*X + (-1) *Y)

= 1^2*Var(X)+(-1)^2Var(Y)

## Lois de probabilité

discreet disctribution

Loi de bernouilli et binomiale

Fnction de masse:  on a déjà un peu vu avec exo précédent

f est un fonction de masse si f(x) >= 0 t somme f(x) = 1

Loi de bernouilli : seulement deux résultats (genre pile ou face). Trop simple pour trouver souvent dnas la réalité. On va rencontrer plius osuvent la binomiale, qui utilise bernouilli.

binom(n,p) = X1, X2... Xn

Somme de n Bern(p)

Et E(Binom(n,p)) = somme(E(bern(p))) n fois = n*p

Et Var(binom(n,p)) =n.Var(Bern(p)) = n.p(p-1)

http://stattrek.com/online-calcul/binomial.aspx

