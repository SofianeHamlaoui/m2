*07/11/18*

# Introduction

Qu'est-ce que le machine learning ?   
-> Une machine qui apprend. Ça sert de deux façons: 

- comprendre le passé -> amène à de la classification
- déterminer le futur -> aide à la décision

On va surtout s'intéresser au futur. En crypto, on a Bob et Alice, en machine learning on a "Vais-je aller faire du golf ?"

On va utiliser ci-dessous le gros tableau suivant. On va s'en resservir souvent. 

| Jour | Climat | Température | Humidité | Vent | Golf |
| ---- | ------ | ----------- | -------- | ---- | ---- |
| 1    | Pluie  | +           | +        | Non  | Non  |
| 2    | Pluie  | +           | +        | Oui  | Non  |
| 3    | Nuage  | +           | +        | Non  | Oui  |
| 4    | Soleil | ~           | +        | Non  | Oui  |
| 5    | Soleil | -           | ~        | Non  | Oui  |
| 6    | Soleil | -           | ~        | Oui  | Non  |
| 7    | Nuage  | -           | ~        | Oui  | Oui  |
| 8    | Pluie  | ~           | +        | Non  | Non  |
| 9    | Pluie  | -           | ~        | Non  | Oui  |
| 10   | Soleil | ~           | ~        | Non  | Oui  |
| 11   | Pluie  | ~           | ~        | Oui  | Oui  |
| 12   | Nuage  | ~           | +        | Oui  | Oui  |
| 13   | Nuage  | +           | ~        | Non  | Oui  |
| 14   | Soleil | ~           | +        | Oui  | Non  |

À partir de là, on commence par phase d'entrainement  :

Il existe différentes familles de machine learning qui vont avoir besoin de faits plus ou moins conséquents pour s'entraîner. On repère globalement le schéma suivant :

- collecte de faits 
  - trier les faits (nettoyage)
  - entrainer notre système à partir de ces faits

Ensuite on fait tourner tout ça et on contrôle les résultats.

Tout ça est une version simplifiée. Dans la réalité c'est plus complexe. Par exemple on va garder un quart du set de données et le sortir des faits pour les utiliser pour le contrôle.

Attention à ne pas trop verrouiller le système qui ne marcherait plus si on sort du périmètre des données du jeu d'entrainement : on appelle ça l'**overfitting**.

# Les algorithmes

Est-ce que je vais faire golf ?

Pour le déterminer, plusieurs algos 

## One R

Le plus simple : une seule règle. Cherche à définir quel est le paramètre le plus important dans un jeu de données, qui permettra de prendre une décision ? En gros : celui qui aura la plus faible marge d'erreur. 

#### Phase 1 : décompte des cas

Parmi tous les critères, comment savoir quel est celui qui a le plus d'importance ?  
On regarde pour chaque paramètre le résultat final : golf ou pas, et on énumère simplement : sur *n* paramètres, on en a *g* où on pas au golf et *pg* où on y va pas.

#### Phase 2 : trouver la règle générale

Pour chaque décompte, on prend le plus grand entre *g* et *ng* et on se dit "si paramètre, alors {golf | pas golf}"

#### Phase 3 : décompte des aberrations

le problème des règles générales, c'est qu'elle peuvent être aberrantes. on compte donc la sommes des valeurs *g* ou *ng* ne correspondant pas à la règle générale. 

#### Phase 4 : détermination du critère

Reprendre les phases 1 à 3 sur les différents critères restants, et comparer le nombre d'aberrations par système. Le critère avec le plus faibl niveau d'aberrations sera le critère déterminant

#### Exemple 

| Climat | Golf  | Pas golf |
| ------ | ----- | -------- |
| Pluie  | *2*   | **3**    |
| Nuag   | **4** | *0*      |
| Soleil | **3** | *2*      |

En gras, les règles générales, en italique, les aberrations

On fait la suite : 

| Critère             | Golf  | Pas golf |
| ------------------- | ----- | -------- |
| **Température**     |       |          |
| Température chaude  | *2*   | **2**    |
| Température moyenne | **4** | *2*      |
| Température basse   | **3** | *1*      |
| **Humidité**        |       |          |
| Humidité importante | *3*   | **4**    |
| Humidité moyenne    | **6** | *1*      |
| **Vent**            |       |          |
| Vent                | **3** | *3*      |
| Pas de vent         | **6** | *2*      |

aberration climat : 4

aberration température : 5

aberration humidité : 4

aberration vent : 5

En égalité, on prend celui qu'on veut. À choisir, autant prendre celui qui a le plus de cas : granularité plus fine. 

Notre critère déterminant sera donc le **climat**. donc :

```
Si climat == soleil
	golf
sinon si climat == nuage
	golf
sinon si climat == pluie
	golf
```

## Arbre décisionnel

Objectif final : construire un arbre décisionnel. 

Le but de l'arbre est d'établir la suite de critères à interroger pour prendre la meilleure décision 

Le but pour créer l'arbre est de déterminer la quantité d'informations dans une entité. 

#### Entropie et Shannon

Quelle est la quantité d'information dans une entité ?  
C'est une question que c'est posé Shannon, qui pose la base de la théorie de l'information. 

En philo, l'entropie est une mesure du chaos. Shannon s'st planté dans son interprétation : il a fait une mesure de l'ordre.   
Shannon va adapter l'entropie au domaine IT pour déterminer quelle quantité d'information est présente dans un postulat. 

Pour cela, on a une formule :


$$
E = \sum{i}-p_i log_2(p_i)
$$
Rappel :
$$
log_b(x) = \frac{ln_x}{ln_b}
$$


#### Exemples

**"C'est l'anniversaire de machin" ou "ce n'est pas l'aniversaire de machin"**
$$
Proba_{anniversaire} = \frac{1}{365}
$$
$$
Proba_{non anniv}= \frac {364}{365}
$$

$$
E_{anniv} = - \frac{1}{365} log_2(\frac{1}{365} ) - \frac{364}{365}log_2(\frac{364}{365}) \\
=  \frac{1}{365} . \frac{ln(\frac{1}{365})}{ln(2)} - \frac{364}{365} . \frac{ln(\frac{364}{365})}{ln(2)} \\
= 0,027
$$

La quantité d'information portée par la phrase "C'est l'anniversaire de x" ou "Ce n'est pas l'anniversaire de x" est de 0,027.

On était là dans un cas où il y a peu de chance que ce soit son anniversaire. Voyons celui d'une équiprobabilité.

**Je suis à l'équateur et je dis "il fait jour" ou "il fait nuit"** 
$$
E_{jour/nuit} = - \frac{1}{2} . log_2(\frac{1}{2}) - \frac{1}{2} . log_2(\frac{1}{2}) \\
= 0,5 + 0,5 \\
= 1
$$
On écarte ici beaucoup plus de possibilités. On apporte donc plus d'information à l'interlocuteur lorsqu'on permet d'écarter des possibilités qui ont les même probabilités d'occurence. 

On maximise donc l'entropie quand on trouve une information plus importante à transmettre.

##### Comment appliquer ça au golf ?

Il faut calculer l'entropie de chaque critère, puis déterminer le critère avec le plus d'entropie. Cela permet de déterminer un noeud dans l'arbre décisionnel. Ensuite pour chaque possibilité liée au noeud, création d'un sous tableau et répétition des calculs dans ce sous-tableau jusqu'à obtenir l'arbre complet

À savoir pour cela  :
$$
E_S = \sum_i - P_i log_2(p_i) \\
E_{T,x} = \sum_{C \in x } P_C. E_C \\
E_{T,x} étant "E de T sachant x"
$$


On calcule donc l'entropie de golf (total oui, total non, total des occurences ) : 0,94

puis pour le climat on va calculer l'entropie de golf sachant climat (connaissant le climat, quelle est la quantité d'information dans "je vais au golf"/"je ne vais pas au golf")

| Climat | Golf | Golf | Total |
| ------ | ---- | ---- | ----- |
| Pluie  | 2    | 3    | 5     |
| Nuage  | 4    | 0    | 4     |
| Soleil | 3    | 2    | 5     |


$$
E_{golf, climat} = P_{pluie} . E_{2,3 (pluie)} + P_{nuage} . E_{4,0 (nuage)} + P_{soleil} . E_{3,2 (soleil)} \\
= \frac{5}{14} . (-\frac{2}{5} . log_2(\frac{2}{5}) - \frac{3}{5} . log_2(\frac{3}{5})) + ...
$$
On finit par obtenir 0,693

En connaissant le climat, le fait de savoir si je vais au golf m'apporte 0,693 unité d'information.

On va ensuite calculer le **gain d'information**. c'est lui qui nous intéresse au final.
$$
G_{(golf, climat)} = E_{golf} - E_{(golf, climat)} \\
= 0,940 - 0,693
= 0,247
$$
On gagne donc 0,247 unité d'information en sachant le climat. Le critère climat vaut 0,247.



On calcule ça pour tous les critères : c'est le plus important qui sera à la racin de mon arbre. On recommencera ensuite en subdivisant le tableau d'orgine en n sous-tableau à partir des différentes proba du critère racine. (voir sur feuille). 

L'arbre permet d'avoir exactement les bonnes questions à poser pour faire la classification.

## Bayes

Filtres bayésiens naïfs :
$$
P_{C|_x} = \frac{P_{x|_C}.P_C}{P_x}
$$
On regarde ce qui existe, et à partir de là on détermine la probabilité pour qu'il se passe un truc. 

| Climat | Golf | Pas golf |
| ------ | ---- | -------- |
| pluie  | 2    | 3        |
| nuage  | 4    | 0        |
| soleil | 3    | 2        |

$$
P_{golf} = 9/14 = 0,64\\
P_{pas golf} = 5/14 = 0,36
$$

On peut réécrire le tableau avec des probas

| Climat | Golf                               | Pas golf      | Probabilité                 |
| ------ | ---------------------------------- | ------------- | --------------------------- |
| Pluie  | $\frac{2}{9}$                      | $\frac{3}{5}$ | $\frac{5}{14} = P_{pluie}$  |
| Nuage  | $\frac{4}{9}$                      | $\frac{0}{5}$ | $\frac{4}{14} =P_{nuage}$   |
| Soleil | $\frac{3}{9} = P_{soleil|_{golf}}$ | $\frac{2}{5}$ | $\frac{5}{14} = P_{soleil}$ |

Maintenant on peut calculer la probabilité de golf sachant soleil :
$$
P_{golf|_{soleil}} = \frac{P_{soleil|_{golf}} . P_{golf}}{P_{soleil}} \\
= \frac{\frac{3/9}{9/14}}{\frac{5}{14}} \\
= 0,6
$$
Sachant qu'il y a du soleil aujourd'hui, il y a 0,6 (60%) de chances que j'aille au golf.

Les filtres antispam utilisent des filtres bayésiens.

## Chaînes de Markov

En 1905, Markov déclare qu'en ayant une connaissance parfaite d'un système à un état *n*, il peut déterminer l'état *n+1*

Donc :

$P_x = \prod_{i=1}^np_{x|_{n-1}}$

S je peux établir un automate à état et renseigner les règles de passage entre les états (et les probabilités d'occurence), je peux anticiper l'état futur.

Exemple d'automate à état : feu tricolore, vert puis orange puis rouge, puis vert.... ou bien vert, puis orange, puis rouge, puis orange, puis vert,puis orange... dans d'autres pays. 

Dans ces deux cas on aura dans les proba de changement d'état :

Vert > 1 orange  
Orange > 1 rouge  
Rouge > 1 Vert

et 

Vert > 1 Orange  
Orange > O,5 Vert, 0,5 Rouge  
Rouge > 1 Orange

Donc $P_{O->V} = 0,5$ en Pologne et $1$ en France.

### Exemple

Par rapport au tableau, on considère que chaque ligne est un jour. On compte donc les changement d'état d'un jour à un autre :

Pluie vers pluie : 2 (40%) 
Pluie vers nuage : 2 (40%)
Pluie vers soleil : 1 (20%)

Nuage vers pluie : 1 (25%)  
N vers N : 1 (25%)  
N vers S : 2 (50%)

S vers P : 1 (25%)  
S vers N : 1 (25%) 
S vers S : 2 (50%) 

On peut donc faire un diagramme (voir feuille)

À partir de ce diagramme, on peut voir le changement à un état n+1 directement. 

 Si on veut déterminer un état à n+2, ça suppose de connaitre tous les chemins intermédiaires possibles et d'estimer leur probabilités. On calcule chaque proba en le multipliant :
$$
P_{n_{nuage} -> n+2_{soleil}} = P_{N>N>S} + P_{N>P>S} + P_{N>S>S} \\
= (0,25*0,5) + (0,25*0,2) + (0,5*0,5) \\
= 0,125 + 0,05 + 0,25 \\
= 0,425
$$
On a ici une chaine de Markov d'ordre 2, car il y a deux passages.

La chaine de Markov ne marche que si tous les facteurs sont prévus, mais **c'est très rarement le cas**. C'est le gros point faible : aucun intervention extérieure ne doit pouvoir intervenir sur le système. Ça fonctionne bien dans certains cas cependant, c'est notamment utilisé dans l'autocomplétion. C'est plutôt pratique comme système car les maths se font toutes seules.

C'est donc très utile pour devnir un état futur proche, mais attention au fort impact des phénomèes non anticipés.   
Plus l'ordre de la CM est élevé, moins la chaîne est fiable.

## Exercice

| Nom             | Cape | Argent | Tech | Pouvoir | Héro |
| --------------- | ---- | ------ | ---- | ------- | ---- |
| Spiderman       | N    | N      | N    | O       | O    |
| Poutine         | N    | O      | O    | ?       | N    |
| Batman          | O    | O      | O    | N       | O    |
| Jocker          | N    | O      | O    | N       | N    |
| Rorschach       | N    | N      | N    | ?       | O    |
| Deadpool        | N    | N      | O    | O       | O    |
| Merckel         | N    | O      | O    | N       | N    |
| D'Artagnan      | O    | N      | N    | N       | N    |
| César           | O    | O      | O    | N       | N    |
| Tesla           | N    | N      | O    | ?       | O    |
| Edison          | N    | O      | O    | N       | N    |
| Homer Simpson   | N    | N      | N    | N       | N    |
| Sherlock Holmes | N    | O      | N    | ?       | O    |
| Moriarty        | N    | O      | O    | ?       | N    |
| ???             | N    | N      | O    | ?       |      |

Créer un système dans un langage qui nous plait qui permet de savoir si la prochaine personne à être ajoutée est un héros ou non.

Vu les outils qu'on a Markov pas utile, Bayes faisable mais trop complexe. Reste One R mais peu pertinent. Donc arbre décisionnel.

Travail à rendre !

