# -*- coding: utf-8 -*-
"""
Exercice 1 du cours 2 de machine learning avec F.Baradel
"""
import matplotlib

matplotlib.use("TkAgg")

import matplotlib.pyplot as plt
import numpy as np

from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression

boston = load_boston()

boston

X = boston['data']
Y = boston['target']
X.shape

n_train = 300

crim = X[:, 0].copy()

""" 4. Right now we will be using only the first features called CRIM for 
 modelling the target variable. Plot CRIM vs target with and without normalizing your data. 
 What do you observe?
"""
# plot target VS CRIM
plt.scatter(crim, Y)
plt.show()

# c'est inexploitable, on log 
plt.scatter(np.log(crim), Y)
plt.show()

# C'est mieux
#on écrit la fonction de normalisation

def normalize (y):
    return (y - np.min(y)) / (np.max(y) - np.min(y))

"""5. Use LinearRegression() for modelling target with CRIM on the training set and compute the predicted
values for the validation set."""



model = LinearRegression().fit(crim[:n_train].reshape(-1, 1), Y[:n_train])


w, b = model.coef_, model.intercept_

print(w, b)


""" 6. Plot the predictions and the actual ground-truth for the training and the validation set."""
print("entrainement")
preds = model.predict(crim[:n_train].reshape(-1, 1))
plt.scatter(crim[:n_train], preds, color="green")
plt.scatter(crim[:n_train], Y[:n_train], color="red")
plt.show()

n_valid = 400

print("validation")
valids = model.predict(crim[n_train:n_valid].reshape(-1,1))
plt.scatter(crim[n_train:n_valid], valids, color="green")
plt.scatter(crim[n_train:n_valid], Y[n_train:n_valid], color="orange")
plt.show()

# On utilise maintenant le log . Je m'a planté et ait cru que c'était la normalisation d'ou les noms fallacieux.
# Ne pas oublier de caler l'exponentielle (réciproque de log) pour remettre valeur dans le bon champ

print(" avec log")
normY = np.log(Y)

model = LinearRegression().fit(crim[:n_train].reshape(-1, 1), normY[:n_train])
print("entrainement")
normPreds = np.exp(model.predict(crim[:n_train].reshape(-1, 1)))
plt.scatter(crim[:n_train], normPreds, color="green")
plt.scatter(crim[:n_train], np.exp(normY[:n_train]), color="red")
plt.show()

print("validation")
normValids = np.exp(model.predict(crim[n_train:n_valid].reshape(-1,1)))
plt.scatter(crim[n_train:n_valid], normValids, color="green")
plt.scatter(crim[n_train:n_valid], np.exp(normY[n_train:n_valid]), color="orange")
plt.show


"""
7. Implement a function which is computing the Root-Mean-Square-Error (RMSE). What is the RMSE on
the training set and on the validation set?

 On veut calculer un score, pour savoir si le modèle est bon ou non
 on définit une fonction qui prend mes prédiciton,s mes valeurs, et retourne le mean square error
(ŷi-yi)²
 à calculer sur le trainig set et le validation set
 
 Ensuite modéliser log(target) = w +b.CRIM et MSE train/val
"""

def mse(preds, vals):
    return np.mean((preds - vals)**2)
    
mse(preds, Y[:n_train])
mse(valids, Y[n_train:n_valid])

# meme chose avec log   
mse(normPreds, Y[:n_train])
mse(normValids, Y[n_train:n_valid])


# Ensuite, faire la meme chose avec une deuxièm variabl du tableau X : ZN
crimZn = X[:, :2]

model = LinearRegression().fit(crimZn[:n_train].reshape(-1, 2), Y[:n_train])


w, b = model.coef_, model.intercept_

print(w, b)

print("entrainement")
preds = model.predict(crim[:n_train].reshape(-1, 2))
plt.scatter(crimZn[:n_train], preds, color="green")
plt.scatter(crimZn[:n_train], Y[:n_train], color="red")
plt.show()

n_valid = 400

print("validation")
valids = model.predict(crim[n_train:n_valid].reshape(-1,1))
plt.scatter(crim[n_train:n_valid], valids, color="green")
plt.scatter(crim[n_train:n_valid], Y[n_train:n_valid], color="orange")
plt.show()
