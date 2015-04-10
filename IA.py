#!/usr/bin/env python3
## IA.py for mastermind in /home/laloge_h/Documents/ISN/Mastermind
##
## Made by Hugo Laloge
## Login   <laloge_h@epitech.net>
##
## Started on  Fri Feb 20 18:30:08 2015 Hugo Laloge
## Last update Fri Feb 20 18:37:57 2015 Hugo Laloge
##

#-------Definition des fonctions-------#

def geneCouleur(gene, nbCouleur=6):
    """Retourne un tableau de couleur à partir d'un numero de gene"""
    couleur = []
    for i in range(4):      #Il génère un tableau de couleur
        couleur.append(gene % nbCouleur)
        gene = gene // nbCouleur
    return couleur

def fitness(score, nbCouleur=6):
    """Calcule la 'fitness' d'un score"""
    return (nbCouleur * score[0] + score[1])

def evaluer(hypo, repo):
    """Retourne la M et B de l'hypothèse"""
    hyp = []
    rep = []
    for i in range(4):  #On recopie hyp et rep
        hyp.append(hypo[i])
        rep.append(repo[i])
    valeur = [0, 0]     #Pion bien placé / couleur correct
    for i in range(4):  #Verification des pion bien placés
        if hyp[i] == rep[i]:
            rep[i] = -1
            hyp[i] = -1
            valeur[0] += 1
    for essai in range(4):
        for reponse in range(4):
            if (hyp[essai] == rep[reponse]) and (hyp[essai] != -1):
                valeur[1] += 1
    return valeur

def hypothese(tour, grille, scoreG, nbCouleur = 6):
    """Gener une hypothese de 'puissance' 0"""
    if tour == 0:
        return [0,1,2,3]
    for i in range(nbCouleur ** 4):   #Nombre de possibilité
        hypo = geneCouleur(i, nbCouleur)
        score = 0
        for tr in range(tour - 1):
            score += abs((fitness(evaluer(hypo, grille[tr])) - fitness(scoreG[tr])))
        if score == 0:
            return hypo
    return hypo

if __name__ == '__main__' :
    reponse = [2,3,1,0]
    scoreG = []
    grille = []
    tour = 1
    while 1:
        hypot = hypothese(tour, grille, scoreG, 6)
        print(hypot)
        grille.append(hypot)
        x = input('Blanc :')
        y = input('Noir')
        scoreG.append([x, y])
        if hypot == reponse:
            break
        tour += 1
