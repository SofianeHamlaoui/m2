# Intro

3 scéances ensemble

On va faire de l'hybride : Ionic. À partir des langages web (html/css/js), Ionic va générer du code pour différentes plateformes.

3 méthodes de faire des applis mobiles

- native
  Ultra personnalisable, performances top niveau, accès aux API. Mais plus cher, nécessite plus de maintenance (car une app pour chaque OS), et plus de compétences.
- hybride
  Moins cher, moins long à développer, compétences et maintenance plus accessibles.
- web
  Avantages : coût, temps de dev, maintenance; mais pas d'accès aux API natives, UI/UX bof, performances laissent à désirer.

# IONIC

Basé sur Angular v2(et +) pour la partie logique, HTML5 et Sass (CSS/SCSS)

Angular est basé sur TypeScript (JS avec des types), le tout basé sur du Cordova (qui build l'app pour le tel).

Ionic est juste un framework front, il faudra le connecter avec un backend (API REST / JSON)

## Structure 

- app
- pages : toutes les pages de l'app
- provider : connexion avec le backend
- theme : personnalisation du css

## Installation

- installer nodejs
- npm install -g ionic    
- ionic start _nomprojet_ _template_
- ionic serve --lab 

## Fonctionnalités

Déclarer une variable : `nomVariable:type`

Définir une variable : `nomVariable = valeur`

On peut aussi la déclarer et la définir en même temps.

Afficher une variable dans le html : `{{ nomVariable }}`

Les propriétés html peuvent être définies avec une variable TS : `[propriété]="nomVariable"`  
On appelle ça du binding. Là c'étaut juste dans un sens, mais on peut faire du binding dans les deux sens. : `[(ngModel)]="nomVariable"` puis `name="nomVariable"`. On fait ça grâce à la propriété ngModel

Dans le html, les évènements JS sont indiqués avec des parenthèses.

`*ngIf = "nomVariable"` effectue une action à partir d'un booléen. Peut être sur n'importe quelle balise html, qui s'affichera alors seulement si variable à true.

boucle : `*ngFor="let variable of NomVariable"`

## Application

Ionic DevApp permet de tester l'appli sur son téléphone



