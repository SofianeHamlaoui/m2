Cours de O.Bonneton

# Intro

Cours initialement prévu pour les master finance (MPIF). 

On va bosser avec Python, anaconda et 3 librairies : panda, numpy et scipy. Python est le 2e langage au monde, juste derrière Java. Le prof aime bien R aussi mais pour pas trop en rajouter on va pas en faire. À l'occase on peut installer et tester R (mais sans le dire au père Noël), c'est vraiment chouette.

Le Machine Learning, on est pas précurseurs en la matière : on aurait pu il y a 5/6 ans. Mais à l'époque on avait pas les mêmes capacités techniques et on galérait bien notre maman pour charger des set de data de 1Go

3 grands axes dans le ML : apprentissage non supervisé (clustering, réduction), supervisé (classification/régression) et de renforcement. 

L'IA n'est pas vraiment intelligente, si on regade de près, tout est une affaire de quelques lignes de codes... Un système de recommandation, par exemple, c'est très puissant mais ça fait 10 lignes. Ça se fait même assez rapidement : les entreprises se mettent à exploiter leurs données (genre Darty ou  MAIF). Obtenir les données : pas si difficile aujourd'hui, bcp en open-source.

Le plan est exposé sur la présentation du cours. On va faire la première page ensemble, le contenu de la deuxième devrait être vu avec l'autre prof (F.Baradel).

Environnement technique :

- Python 3.7
- Enthought Canopy // Anaconda
- Apache Spark
- Tensor Flow
- Keras

Affichage d'un plan type plan de métro plutôt riche : le champ est vaste. On ne va faire qu'un cours d'introduction qui va nous donner une vision d'ensemble, à nous d'aller ensuite où on veut. 

Installation d'Anaconda. Revue rapide de R.

# Python

En guerre avec R. Ceux de la finance préfèrent ce dernier. Les deux sont intéressants, mais on ne fera pas de réseau de neurones avec R. Explorer R à l'occasion !

## Types

- int
- float
- str
- bool

## Affichage / Saisie

afficher

`print("foutre")`

saisir :

` v = int(input("insérer une valeur"))` 

## Conditions

```python
if:
	|
    
if:
    |
else:
    |
	
if:
	|
elif:
	|
else:
	|
```



## Boucles

```python
for i in range(0, 10):

for i in range(10):
    if(x is 1):
        continue
    else:
        break

for i in range(0, 10, 2):
```

```python
while ... :
```

## Listes 

```python
list = [1, 2, 3]
tuple = (1, 2, 3)
dict = { "one" : 1, "two": 2, "three": 3}

# permet de tout sélectionner avec un offset correspondant au chiffre
list[:2]
list[2:]
list[-1:]

# fonctions
list.append(4) # une seule valeur ou un tableau
list. extend(5, 6) # plusieurs valeur
list.sort() 
list.sort(reverse=True)

(x, y) = "56,34".split(',') # x = 56 et y = 34

dict.get("key") # revient à dict["key"]
```

## Importation de modules

```python
import numpy as np
from math import random as rd
```

Ne pas fabriquer ses jeux de données : c'est chiant. Il y en a partout, se servir !

## Fonctions

```python
def DoSomething(f, x)
	return f(x)

print(SquareIt, 3)
	
# on utilise lambda pour faire une fonction inline
print(DoSomething)(lambda x: x * x * x, 3)
```

## Biblio

Voir PDF, du plus simple au plus dur. 

Sinon en ligne on a toute la doc de Scipy.

# Pandas

Lancer Anaconda > Jupyter lab

Sur des jeux de data à partir de 2/3 Go, il vaut mieux utiliser Sparks.

De base, `describe()` ne retourne que sur les colonnes calculables (int), mais en faisant un `include='all'` il nous retourne des trucs intéressants aussi, genre "top"  et "freq" qui indiquent l'entrée qui revient le plus souvent et le nombre d'occurences.

Les notebook sont exportables ! Genre en HTML, LaTeX...

Une grosse partie du travail est dans le traitement des données et la normalisation du tableau.



### Nettoyage de données

NaN : la question qui se pose est : qu'en faire ?   
Une solution intéressante est par exemple de calculer la moyenne (sans les NaN), et remplacer les NaN par cette moyenne. On peut aussi faire un tirage au hasard. Il y a vraiment beaucoup de possibilités. Il faut s'adapter au type de colonne auquel on à faire. Supprimer la ligne est pas vraiment la meilleure solution, on vire souvent trop de trucs.