# Régressions



R² est un coefficient qui est le coefficient de la variable de corrélation. Il permet de maîtrise et de mesure la part de contribution du paramètre sur les variables. Regression linéaire (en bleu sur slide 1) indique qu'il joue pour 54% de la variable du prix. En gros le prix de la maison dépend à 54% du lower status of the population.

Pour la courbe rouge, regression quadratique (au carré), on monte à 64%, et on peut même monter au cube, à 66%. 

Toute la question est l'overfitting. Et attention, un modèle n'est pas pour expliquer, mais pour modéliser !  Dans notre cas, si on regarde, la verte va passer en dessous de 0, la rouge remonte... ça n'a pas de sens ! 

## Choix de la régression

Schéma qui aide à choisir: 

- Combien de variables de réponse ? 
- Quel type de réponse (continu, qualitatif, évènements rares...)
- Combien de variables de prédiction ?
- Quels type de prédicteurs ?



## Principe de la régression linéaire

En anglais pour l vocabulaire. slope : pente.

La droite de la régression est représentée par ax + b. On pose la droite et on mesure l'écart en le point et la droite pour déterminer un coefficient de corrélation. On fait donc un calcul du "résidu" et elle doit normalement s'aligner sur 0 (correspond au graphique en bas de page) : plus les valeurs s'étalent pas contre, plus on s'écarte d'une prédiction juste. On détermine le R² à partir de ça.

Dans le tableau des "Sales" : observation des ventes en fonction des publicités. À chaque fois qu'on augmente de 1 les ventes, on augmente de 23,42 la pub. On voit que l R² est très important : R² à 0,97 !

## Régression polynomiale

On part de ax + b toujours, et on y ajoute le carré, un cube... jusqu'à un **degré** souhaité.

Attention, sujet à overfitting et underfitting

MSE est difficilement interprétable, il est préférable d'avoir un R. Toute la logique est de trouver le bon degré : clui qui présente le meilleur modèle.

## Régression multiple

À ne pas confondre avec la polynomiale : la première on élève le même x à un degré, là on va prendre différents x (plusieurs variables).

Comme on a plusieurs points (z = ax +by), on se retrouve dans un espace. alors 3 dimensions ça va, mais au dela c'est plus représentable.

$\beta$ = slope. 

Si on regarde la table 3, on put retenir à partir des p les variables à retenir (donc on en retient 4)

Il est difficile de quantifier des variables qualitatives.

## Régression logistique

On a des variables, que l'on va pondérer, pis ça entre dans une "boite noire", t la machine ressort un booléen derrière. La machine vérifie si c'est 0 ou 1, si c'est pas bien elle modifie les poids et donc la pondération et recommence.

Ça rejoint donc le réseau de neurones. on a un exemple de comment 

tableau indiquant le risque d'avoir une crise cardiaque en fonction de plein de paramètres. La pente indique la direction de l'influence : pour l'activité physique elle est négative, donc ça **réduit** les risque ! L'odd ratio  c'est l'influence de la pente : en quoi ça augmente fortement ou non.

## Et python

Graph avec plein de façons de faire de la régression 

curve_fit est intéressant si on veut pas faire du linear, on peut y mettre une fonction. Mais est peu pertinent.

Tableau OLS :  
method least square = moindre carré  
df model = nombre de variables
r square est indiquée
prob = proba du t
const = le $a$ du $ax+b$

# RStudio

Jambon : aucun facteur de corrélation ne semble se démarquer, mais tous ensemble ils représentent presque 70%. On pourrait faire un indice de corrélation pour voir lesquels garder (si on les garde tous c'est overfitté), mais on va plutôt récupérer une librairie pour ça : FactoMineR