#!/usr/bin/env python3
## Codifieur.py for mastermind in /home/laloge_h/Documents/ISN/Mastermind
##
## Made by Hugo Laloge
## Login   <laloge_h@epitech.net>
##
## Started on  Fri Feb 20 18:01:57 2015 Hugo Laloge
## Last update Fri Feb 20 18:02:07 2015 Hugo Laloge
##

#-----------Import des modules---------#

from tkinter import *
from random import randint


#-------Definition des fonctions-------#

def genererCode():
    global couleurs, code, grille
    couleurs = ['ivory', 'black', 'blue', 'red', 'green', 'yellow']   # 6 Couleurs possibles, tableau de 0 à 5
    grille = []
    reponse = []
    tour = 0
    for i in range(10):
        grille.append(['', '', '', ''])
        reponse.append(['', '', '', ''])
    code = []

    for i in range(4):
        code.append(couleurs[randint(0,5)])

def afficherCode():
    global code, canevas, codeAffiche
    for i in range(4):
        couleur=code[i]
        canevas.create_oval(i*20+20, 220, i*20+40, 240, fill=couleur)

def changerCouleur(event):
    global couleurs, canevas, grille, tour
    x = int((event.x-20)/20)
    if x >= 0:
        couleurSuivante = {'ivory':'black', 'black':'blue', 'blue':'red', 'red':'green', 'green':'yellow', 'yellow':'ivory', '':'ivory'}
        couleur = couleurSuivante[grille[tour][x]]
        grille[tour][x] = couleur
        canevas.create_oval(x*20+20, tour*20, x*20+40, tour*20+20, fill=couleur)

def valider():
    global tour, grille, code, reponse
    nbPion = True
    couleurCorrect = 0
    couleurPlace = 0
    recoCode = []
    for i in range(4):  #On recopie le code
        recoCode.append(code[i])

    for i in range(4):
        if grille[tour][i] == '':
            nbPion = False

    for essai in grille[tour]:  #Boucle pour vérifier les couleurs
        for i in range(len(recoCode)):
            if essai == recoCode[i]:
                couleurCorrect += 1
                recoCode.pop(i)
                break

    for i in range(4):  #Boucle pour vérifier les couleurs bien placées
        if grille[tour][i] == code[i]:
            couleurPlace += 1

    afficherRep(couleurCorrect, couleurPlace)
    print('couleurCorrect =', couleurCorrect, 'et couleurPlacé =', couleurPlace)

    if tour < 9 and nbPion:
        tour += 1
    elif tour == 9:
        terminer()

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
    afficherCode()
    canevas.unbind('<Button-1>')
    valider.destroy()


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

valider = Button(fenetre, text='Valider ligne', command=valider)
valider.pack(side=TOP)

afficher = Button(fenetre, text='Afficher code', command=afficherCode)
afficher.pack(side=TOP)

generer = Button(fenetre, text='Recommencer', command=genererCode)
generer.pack(side=TOP)

quitter = Button(fenetre, text='Quitter', command=fenetre.destroy)
quitter.pack(side=BOTTOM)

genererCode()
for i in range(4):
    canevas.create_oval(i*20+20, 220, i*20+40, 240, fill='grey')

tour = 0

fenetre.mainloop()
