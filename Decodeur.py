#!/usr/bin/env python3
## Decodeur.py for mastermind in /home/laloge_h/Documents/ISN/Mastermind
##
## Made by Hugo Laloge
## Login   <laloge_h@epitech.net>
##
## Started on  Fri Feb 20 18:03:29 2015 Hugo Laloge
## Last update Fri Feb 20 18:56:09 2015 Hugo Laloge
##

#-----------Import des modules---------#

from tkinter import *
from random import randint
from IA import *


#-------Definition des fonctions-------#

def changerCouleur(event):
    global couleurs, canevas, grille, tour
    x = int((event.x - 20) / 20)
    if x >= 0:
        couleur = couleurs[(reponse[x] + 1) % 6]
        reponse[x] = (reponse[x] + 1) % 6
        canevas.create_oval(x*20+20, 220, x*20+40, 240, fill=couleur)

def afficherEval(hypot, reponse):
    global tour
    couleurCorrect = 0
    couleurPlace = 0
    recoCode = []
    for i in range(4):  #On recopie le code
        recoCode.append(reponse[i])

    for i in range(4):
        if grille[tour][i] == '':
            nbPion = False

    for essai in hypot:  #Boucle pour vérifier les couleurs
        for i in range(len(recoCode)):
            if essai == recoCode[i]:
                couleurCorrect += 1
                recoCode.pop(i)
                break

    for i in range(4):  #Boucle pour vérifier les couleurs bien placées
        if reponse[i] == hypot[i]:
            couleurPlace += 1
    afficherRep(couleurCorrect, couleurPlace)

def valider():
    global grille, reponse, score, tour, couleurs
    while (tour < 10) :
        hypot = hypothese(tour, grille, score)
        print(hypot, reponse)
        grille.append(hypot)
        for x in range(4):
            canevas.create_oval(x*20+20, tour*20, x*20+40, tour*20 + 20, fill=couleurs[hypot[x]])
        score.append(evaluer(hypot, reponse))
        afficherEval(hypot, reponse)
        if (hypot == reponse):
            break
        tour += 1
    print('Fini')

def afficherRep(couleurCorrect, couleurPlace):
    global canevas, tour
    for i in range(couleurCorrect):
        if i == 0:
            canevas.create_oval(0, tour*20, 10, tour*20+10, fill ='white')
        if i == 1:
            canevas.create_oval(10, tour*20, 20, tour*20+10, fill ='white')
        if i == 2:
            canevas.create_oval(0, tour*20+10, 10, tour*20+20, fill ='white')
        if i == 3:
            canevas.create_oval(10, tour*20+10, 20, tour*20+20, fill ='white')

    for i in range(couleurPlace):
        if i == 0:
            canevas.create_oval(0, tour*20, 10, tour*20+10, fill ='black')
        if i == 1:
            canevas.create_oval(10, tour*20, 20, tour*20+10, fill ='black')
        if i == 2:
            canevas.create_oval(0, tour*20+10, 10, tour*20+20, fill ='black')
        if i == 3:
            canevas.create_oval(10, tour*20+10, 20, tour*20+20, fill ='black')
            terminer()

def terminer():
    global canevas, valider
    canevas.unbind('<Button-1>')
    valider.destroy()

score = []
grille = []
reponse = [0,0,0,0]
tour = 0
couleurs = ['ivory', 'black', 'blue', 'red', 'green', 'yellow']

#---------Création de la fenetre-------#

fenetre = Tk()
fenetre.wm_title('Master Mind - Codifieur')

canevas = Canvas(fenetre, width=100, height=240, bg='dark grey')
canevas.bind('<Button-1>', changerCouleur)
for i in range(10):
    canevas.create_line(0, (i+1)*20, 100, (i+1)*20, fill='black')
canevas.create_rectangle(0, 200, 100, 215, fill='black')
canevas.create_line(20, 0, 20, 200, fill='black')
canevas.pack(side=LEFT)

valider = Button(fenetre, text='Valider reponse', command=valider)
valider.pack(side=TOP)

quitter = Button(fenetre, text='Quitter', command=fenetre.destroy)
quitter.pack(side=BOTTOM)

for i in range(4):
    canevas.create_oval(i*20+20, 220, i*20+40, 240, fill='ivory')

fenetre.mainloop()
