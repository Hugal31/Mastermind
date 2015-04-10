def geneCouleur(gene, nbCouleur=6):
    """Retourne un tableau de couleur à partir d'un numero de gene"""
    couleur = []
    for i in range(4):      #Il génère un tableau de couleur
        couleur.append(gene % nbCouleur)
        gene = gene // nbCouleur
    return couleur

def couleurGene(couleur, nbCouleur=6):
    gene = 0
    for i in range(4):
        gene += couleur[i]*nbCouleur**(i)
    return gene

def inverseFitness(fitness):
    score = [0, 0]
    score[0] = fitness / 6
    score[1] = fitness % 6
    return score

print(couleurGene([0,1,2,3]))
print(couleurGene([2,1,0,0]))
print(couleurGene([2,0,2,1]))
print(couleurGene([0,4,3,1]))
