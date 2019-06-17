# Plan

1. Data mining (web mining)
2. GAN
3. Auto encoder
4. Recommender systems

Ces 3 derniers points sont de l'apprentissage non supervisé : il n'y a pas de catégories définies.

# 1. Data mining - web mining

Le web mining intervient quand on a pas les donnés, pour un projet perso par exemple.  
On y retrouve trois principaux outils :

## 1. Beautiful soup 4

La librairie python "Beautiful soup 4" // outils en découlant : Scrapy; Selenium.

Travaille avec le code source de base de la page (HTML). Extrait la plupart des informations (tables, images...)  
Se trouve sur Internet; Utilise Python : tout est automatisé.
Tourne plusieurs jours pour extraire toutes les données  
Enregistre les données : genre dans un CSV. Doit les enregistrer régulièrement  
Exploitable avec pandas...

Peut par exemple s'exploiter avec un vieil ordi, qu'on fait tourner chaque jour pour recueillir chaque jour des données.

S'utilise dans un jupiter notebook par exemple

## 3. Scrapy

Dans un terminal

Même fonction que BS4, mais tourne plus vite car mis en parallèle. Par contre écrire en scrapy est plus compliqué.

## 2. Selenium 

Peut faire des trucs que BS4 et Scrapy ne peuvent pas faire :  
Le code source qu'on a habituellement côté client n'est pas le code source complet. Si on enregistre le fichier HTML depuis la page web, là on a le code source complet.

Selenium a la capacité d'interagir :  
Ouvrir une page web depuis un vrai navigateur, scroller, entrer username et pswd, cliquer sur des boutons...



Il y a une "éthique" du web mining :

1. Ne pas surcharger le serveur : pas plus d'un accès  / seconde
2. Respecter la demande de certains sites de ne pas utiliser à but commercial (genre whois.net)
3. Certains site interdisent carrément le téléchargement d'informations de façon automatisée (genre unsplash)



# Systèmes de recommandation

Genre Amazon, Netflix...

On part d'une liste de *m* films et *n* utilisateurs

Les données peuvent se présenter sous forme de liste (en colonne : user, film, note) ou bien de matrice (colonnes = m; lignes : n ; en entrées les notes.)

L'objectif à partir de ces données est de trouver 10 films à recommander pour chaque utilisateur, qu'il serait susceptible d'apprécier le plus.

## Technique classique

Multiplication de la matrice. en gros à partir de la data, on multiplie n par k et m par k et on obtient une prédiction. Rien compris.

TD : plusieurs exemples et techniques issues de Microsoft : 

- Fast-AI notebook
- Wide-deep notebook

# GAN

C'est du "future faking everything". Ce qu'ils savent faire de mieux : de faux visage humains ! Impossible de distinguer un vrai humain d'un généré par GAN.  
On s'attaque à la vidéo dans le jupyter notebook ?  

Pour commencer à apprendre le "fake"

- news articles
- research articles

Petit schéma dur à refaire, mais globalement : un bruit aléatoire entre dans un générateur, ce qui génère de la fake data. Celle ci est comparée avec de la true data par un discriminateur (réseau de neurones), qui détermine la précision du réel vs fake.

En gros, c'est une compétition entre le générateur, qui essaye de produire la meilleure donnée pour tromper le discriminateur : le fraudeur ; et le discriminateur qui essaye de distinguer le vrai du faux : la police.

# Auto encoder

Encore un schéma. La data entre dans un compresseur, qui en fait une data bien plus petite, qui ensuite passe dans un décompresseur, qui ressort exactement la même donnée. Tout ceci constitue un réseau de neurones.

Ses utilisations sont pour compresser des données et enlever le bruit de données.

# TP9

# Reinforcement learning

On a donc apprentissage non supervisé, supervisé et par renforcement.

On y trouve deux acteurs : un agent, et l'environnement. L'agent effectue une action sur l'environnement, qui renvoie une récompense, ainsi qu'un feedback (une maj de l'état de l'environnement).

Ses applications sont par exemple : entraîner une IA à jouer à Dota2 ; robot qui ramasse les merdes das la maison ; construire un "stock portfolio" (portefeuille d'actions)

Ses différences :

- Pas de catégorisation de la data
- La récompense peut être repoussée : si on a besoin d'attendre de savoir si une décision était bonne ou mauvaise
- Le feedback est séquentiel : il faut attendre pour avoir plus de data : plus de puissance de calcul, un meilleur CPU n'aideront pas.
- L'action peut influencer sur l'environnement de façon presque certaine. Il n'y a pas de distribution statique comme en supervisé/ non supervisé.

Se jour principalement, pour le modèle, à trouver le meilleur compromis entre epxloration t exploitation.  
exploration : Trouver une nouvelle action jamais essayée avant, sans connaitre le feedback/la reward.  
exploitation : répéter un bon mouvement déjà appris auparavant. Feedback et reward connues.

# TP 10

