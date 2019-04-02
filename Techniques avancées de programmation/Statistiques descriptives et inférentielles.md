# Introduction

Pour les statistiques descriptives à une variable,

Paramètres de position : 

- moyenne 

- médiane : donnée du "milieu"

- mode


Ces variables sont toutes intéressantes et donnent des informations différentes. La distinction entre moyenne et médiane est intéressante, notamment, en regardant les deux on peut se rendre compte de l’homogénéité ou de l'effet des extrêmes des valeurs (la dispersion). 

Retenir également l'écart-type, et la mustach box.

Pour les statistiques à deux variables, retenir les régressions.



Les statistiques inférentielles reposent sur les inférences. Qu'est-ce qu'une inférence ? Le contraire d'une déduction : à partir d'une observation précise, on en induit que toutes les voitures sont rouges. L'inférence n'a de sens que lorsque l'échantillon est grand. Et cet échantillon doit être représentatif de la population. MAIS pour savoir si l'échantillon de la pop. il faut avoir des infos sur celles-là, hors c'est justement ce qu'on cherche à savoir en faisant de l'inférence.  
Dès qu'on donne un résultat, on donne un pourcentage de chance de se tromper.

Les différents types de variables :

- quantitatives : ça se mesure, des nombres
  - quantatif discret : par paliers ordonnés
  - quantitatif continu : pas de paliers, éventuellement découpé en tranches
- qualitatif : ça se mesure pas, des mots 
  - qualitatif ordinal : peut aussi se quantifier, s'ordonner
  - qualitatif nominal : ne s'ordonne pas, mettre un classement n'aurait aucun sens

Dès qu'on peut, on tâche d'ordonner le qualitatif.

En fonction des variables, on se retrouve avec différents types de graphiques disponibles :

- diagramme à secteurs
- diagramme à bâtons
- histogramme
- ...

Les paramètres de dispersion :

- Étendue
- Interquartile
- Variance
- Écart type
- Kurtosis
- Skewness

L'écart-type permet de quantité la dispersion, on le retrouve sur les courbes suivante la loi normale.

Quand c'est pas symétrique (pas loi normale), on obtient justement un skewness : courbe "poussée" vers la gauche (positive) ou vers la droite (négative). Le kurtosis, lui c'est une courbe de loi normale étirée (leptokurtic) ou aplatie (platykurtic), donc soit avec un pic rapide: gros écart rapide entre données, ou bien l'inverse : toutes les données plutôt proches de la moyenne.

Quand on récupère des données, on regarde donc en premier lieu si leur distribution est normale ou non (skewness, kurtosis). Si elle n'est pas normale, on ne peut pas utiliser les paramètres que l'on connaît. 

Théorie des probabilités s'associe aux lois de probabilités. Les lois de distribution :

- Loi binomiale : loi des jeux (si je joue n fois à ça, combien ai-je de chances de gagner ?)

- Loi de poisson : loi des évènements rares das une durée prévue (trois clients entrent chaque heure dans une boutique. La loi de poisson peut être définie pour décrire chances que 6 personnes entrent dans la boutique dans la prochaine heure). Probabilité de risques de sortir de la moyenne.

- Exponentielle

- Khi-deux : très intéressante car elle gère le qualitatif (les autres ne font que du quantitatif).


Le problème des stats inférentielles, c'est la double flèche : plus on augmente la précision, plus le risque de se planter augmente; moins on est précis plus la confiance en le résultat augmente.

Test d'hypothèse : trouver la frontière à partir de laquelle on considère que la différence est intéressante.  
Le saint Graal : la *p value* : une donnée quantitative qui nous dit oui ou non. C'est elle qui nous permet de dire les chances qu'on a de se tromper par rapport à un résultat donné.

Risques $\alpha$ et $\beta$ : 

Ces lois donnent un résultat mais ne montrent pas la cause. C'est l'expérimentation qui doit être maîtrisée en tous points 



Les tests que l'on devrait à minimum connaître 

Test paramétrique de liaison . Notre distribution suit une loi normale. 

- On fait des corrélations entre deux variables si elles sont quantitatives.
- On fait des Khi-deux si elles sont qualitatives
- Si elles sont les deux : ANOVA. Analyse of Variance. Peut être très compliquée mais on aura un outil pour simplifier.

- Test de comparaison de population indépendantes
  - variances de fisher
  - moyennes de Student

Si ne suite pas une loi normale : non paramétrique :

- 

---

*13/03/19*

# Tests d'hypothèses

On va voir aujourd'hui Chi2, qui permet de travailler sur du qualitatif et non quantitatif. Cette loi va notamment servir en médecine : on compare un échantillon normal et un malade.

Schéma d'analyse univariée : permet de déterminer les outils à utiliser en fonction de ce qu'on veut faire.

Chi2 seulement si on veut bosser sur une distribution. si sur des données, on regarde si ça suit la loi normale. si c'est le cas, on part vers Student, Walsh, randomisation... Il faut aussi regarder si l'échantillon est apparié (même échantillon mais qui a varié dans le temps) ou indépendant

Dans le cas où ça ne suit pas la loi normale, on ne peut pas bosser sur les paramètres ! alors on travaille plutôt avec un système de rang : on classe touts les entrées les unes par rapport aux autres et quand on modifie on voit si elle change de rang.

Schéma d'analyse multivariée : même délire.

hypothèse, observation.. partie du cours perdue crash ordi

Il y a 5 étapes : 

1. 

2. On établit l'hypothèse nulle $H_0$ : "Les paramètres ou les distributions sont identiques"
3. Propose une hypothèse alternative : $H_0$ est rejeté t on considère $H_1$ comme trop importante pour être une simple fluctuation d'échantillonnage. De là on a une hypothèse alternative avec une différence signification, on cherche ensuite le sens de la différence ou non. Si on cherche c'est unilatéral, si non c'est bilatéral.
4. On fait le calcul du test, qui renvoie une p-value, que l'on compare à la valeur du risque d'erreur $\alpha$. La p-value, c'est la probabilité d'être dans la fluctuation d'échantillonnage. Si la p-value est supérieure à $\alpha$  on doit conserver $H_0$, sinon on rejette $H_0$ et on accepte $H_1$. 
5. On conclut. Attention dans le cas d'un test sur une liaison, ça ne prouve pas un lien de causalité.

En gros, la p-value indique la chance que le résultat soit dû au hasard.

En testat une distribution normale, peu importe si la p-value est immense ou non tant qu'elle est supérieure  à 0.05 : c'est binaire, ça n'indiqu pas une meileure distribution normale.