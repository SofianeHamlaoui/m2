# Intro

## Le machine learning

### Définition du machine learning

Principalement à titre prédictif aujourd'hui. On utilise des données existantes pour prédire quelles seront les prochaines.

Le ML touche aux :

- Statistiques
- Maths
- Computer science
- Big data
- Intelligence artificielle

Aujourd'hui, le ML c'est de l'informatique avec des outils venus des maths. 

### Historique

#### Machine learning

Alan Turing : début de l'informatique, enigma et surtout test de Turing (qui vise à évaluer une intelligence artificielle en déterminant si l'interlocuteur est une machine ou non).

Dans les années 50, plusieurs découvertes plutôt cool et basiqus, comme Percetron.

Ensuite, le machine learning a changé : concept de rule-based approach : au leu de faire apprendre à une machine, on fait une succession de `if then`. Il existerait même encore aujourd'hui un milliardaire qui, ne croyant pas au ML, continue à employer des tonnes de gens pour écrire tous les `if, then` possibles.

Dans les années 2000 on voit l'arrivée du deep learning avec les résaux de neurones. Aujourd'hui on en sert à toutes les sauces et ne parle plus que ça ! Les réseaux de neurones sont des fonctions très complexes qui s'appuient sur de (très) grosses bdd pour donner des résultats plus précis que ceux des humains

#### Intelligence articifielle

D'abord approche connexionniste puis symbolique, et là on revient sur la première. À creuser pour connaître les tenants et aboutissants de l'un et l'autre.

### Catégories de ML

Le machine learning se découpe en trois parties :

- Apprentissage supervisé (SL) :  
  On a des images, on connaît leur label (genre ce qu'il y a dans img). On fait une fonction qui détermine ce qui est dans l'image et ressort un résultat. C'est assez coûteux et chronophage, genre il faut mettre un label sur les millions d'images.  
  Pour des labels d'images ça va mais si on doit estimer la posture d'un humain, ça devient encore plus galère à déterminer sur des millions d'images.
- Apprentissage non supervisé (UL) :  
  Apprendre à générer des images, juste en regardant des images. On ne dit pas "c'est un chien", il se débrouille à comprendre seul des concepts en analysant des images.  
  La prédiction du futur est égalelement bien à la mode. Savoir à partir d'une vidéo quelles seront les 5 secondes suivantes implique une réflexion et connexion entre objets et environnement
- Apprentissage par renforcement (RL) :  
  On a systématiquement un agent, qui doit comprendre seul les concepts du jeu. au début il ne sait rien à part les actions qu'il peut faire et quand il a perdu. Le programme teste des actions et apprend seul ce qui l'amène à ne pas perdre, devenant de plus en plus performant avec les essais. Exemple d'Alphago : un jeu de go qui joue contre lui-même pour devenir de plus en plus fort. 

### F.Baradel

Doctorant, il travaille sur la compréhension des vidéos et les interactions entre les entités dans cette vidéo. Notamment ce qu'il se passe entre deux instants (exemple des bébés : on se fabrique une histoire où les bébés changent d'attitude en fonction de qui a la télécommande, la machine en est incapable, comment lui faire comprendre ?)

### Strong AI

L'IA d'aujourd'hui est très spécifique : elle peut pas passer du Go au Ping-Pong. Un humain saura s'adapter à un nouveau jeu. La strong IA vise un champ plus large justement. Exemple d'Elon Musk qui a monté une boite allant dans ce sens puis qui s'en est fait virer (haha).

### Applications dans le monde réel

On a par exemple les Tesla : marche très bien, notamment sur autoroute. Y a toujours des accidents, mais moins. À ne pas éprouver dans un centre ville européen.

Google translate : y a 20 ans des linguistes entraient à la main les traductions des enchaînements de termes. Puis Google a appris à des machines à traduire des chaînes en utilisant les données qu'il possédait.

Système de recommandations de Netflix

Criteo : un peu bâtard, récupère les cookies et fait un profil utilisateur à filer au site qu'on visite pour savoir quoi nous vendre.

#### Dans l'industrie

Chez GAFA & co, beaucoup d'investissements et de centres de recherche qui s'ouvrent.

## Le cours

On va utiliser Anaconda et notamment Miniconda car plus léger.

Librairies à la mode en data Science

- SciPy
- NumPy
- IPython
- pandas
- matplotlib
- scikit learn

On aura pas de gros GPU, c'est un peu le nerf de la guerre : elle peuvent faire des calculs très rapides comparé aux CPU.

# Apprentissage supervisé

## Régression linéaire (simple)

On part de données fournies qui se placent sur deux axes, chaque donnée ayant donc des coordonnées (xi, yi). Ces données sont vues comme des caractéristiques t des targets : on veut prédire y en fonction de x. Exemple de la slide : on veut prédire une droite. qui donnera la tendance à partir de toutes ces données.

Là c'est un simple produit scalaire. Notre droite $y = ax +b$. En l'occurence ici on va parler de $w$ et non de $a$

À patir de cet exemple simple qui vient des maths, on part en informatique. En informatique, l'objectif d'optimisation est toujours présent. Pour optimiser, on va avoir besoin de déterminer une fonction de coût : elle représente l'écart de la valeur prédite par rapport à la vraie valeur. Le but final est de définir une droite qui s'approche le plus possible des valeurs réelles à partir de la moyenne des fonctions de coût.  
On représente une prévision avec un chapeau : $\hat y$. On note $l$ le coût (loss) pour un point, et $L$ le coût total :
$$
l(\hat y_i, y_i) = ((wx_i + b) - y_i)² \\

L(_{w, b, x_i, y_i}) = min\frac{1}{N}\sum_{i=1...N} (w * x_i+b) - y_i)²
$$


En gros on attribue des valeurs w et b complètement aléatoires et on voit la valeur du coût. Ensuit la machine tâche de minimiser le plus possible ce coût avec des valeurs différentes de w et b.

### Solution closed-form

Pour appliquer cette solution on fait des matrices pour chaque point de 1 à N, puis des opérations sur ces matrices. On pose :
$$
beta =  \begin{bmatrix}w & b\end{bmatrix} \\
\\
X = \begin{bmatrix}
	1 & w_1 \\
	\cdots & \cdots \\
	1 & x_i
	\end{bmatrix} \\
\\
Y = \begin{bmatrix}y_1 \\ y_i\end{bmatrix}
$$
Avec ça, on peut réécrire notre fonction de coût en quelque chose de matriciel, et obtenir la solution optimale à partir d'opérations de transformation, d'inverse et de multiplication de matrices. Et on trouve les meilleurs cas grâce à ce calcul. Mais ça ne marche que dans des cas précis, car le calcul de la matrice inverse est parfois trop chiadé pour être réalisable.

Solution optimale : $\beta * = \hat \beta = (X^T. X)^{-1}.X^T.Y$

À cause de cette complexité on cherche parfois des solutions qui vont être "à peu près similaire" à ce résultat pour quand on a des matrice énormes.

### Régression linéaire avec descente de gradient

La descente de gradient donne une courbe montrant la valeur du coût en fonction de la valeur du $\theta$ . La solution optimale est au creux de la courbe, quand on a une valeur minimale et qu'on peut pas aller plus bas. 

Voici les étapes : 

1. On sait pas où est le minimum. On choisit un $\theta_0$ aléatoire
2. On détermine un "learning rate", on reviendra dessus
3. On choisit ensuite le nombre d'itérations (genre 1000), et pour chaque on met à jour les paramètres en cherchant à aller dans le sens de la pente.

C'est là qu'intervient la dérivée, qui est le gradient, qui indique l'inverse de la pente. On va donc prendre le sens contraire : on soustrait la dérivée à la valeur actuelle de $\theta$

Il y a la problématique de l'initialisation, si on tombe direct sur le le mini ou bien sur les courbes problématiques qui ont des parties horizontales. Une solution est de prendre plusieurs points d'initialisation. 

Comment trouver w et b à partir de cet algo d'optimisation ? Et bien on dit que $J(\theta) = J(w,b)$. On initialise donc w et b et on calcule les gradients pour w et pour b.

En gros, c'est le calcul de la dérivée qui permet de savoir le sens de la pente : puisqu'en fonction de son signe, la dérivée de $f(x)$ indique si $f$ est croissante ou décroissante, connaitre cette dérivéepermet de connaitre le sens de la pente pour $x_i$

### Descente de Gradient stochastique

Comme dans la réalité on a beaucoup trop de données pour s'appuyer sur toutes, on fait une descente de gradient stochastique : on estime les gradients d'un échantillon des données seulement.

### Exemple

Nous sommes de charmants vendeurs de gales ambulants. On se pose la question : "Quand température est de $x$, combien je vais vendre de glace ?". On s'appuie sur plusieurs expériences de cas réels où on a vendu $y$ glaces alors que la température était de $x$.

On va résoudre le problème en partant du principe qu'on va vendre $wx + b$ glaces, où x est la température. Si $x = 0$ on va vendre $b$ glaces. $b$ est appelé l'intercepte, et $w$ la pente.

### Notes en vrac

$$
\hat \theta = argmin\ J(\theta)
$$
Se comprend comme "le paramètre $\theta$ qui minimise $J(\theta)$"

Le chapeau indique la prédiction. Pour trouver le coût moyen (de tous les points), donc l'écart entre prédiction et réalité, on va chercher à déterminer $\hat w$ et $\hat b$.

À la fin des exercies on mate un graph avec trois méthodes : closed-form, gradient descend et stochastic gradient descent. On remarque que les 3 sont très proches.

On voit ensuite comment faire une descente de gradient en 3 lignes de code : scikit-learn