import numpy as np


def lire_mots(filename):
    """ Prend en entrée le nom d'un fichier de type adn
        et renvoie les 2 mots associés à ce fichier sous
        forme de tableau numpy """

    with open(filename, 'r') as f:
        #Supression des deux premières lignes
        f.readline()
        f.readline()

        #Lecture des deux mots sous forme de chaine de caractères
        mot1 = f.readline()
        mot2 = f.readline()

    #Conversion des mots en liste
    mot1 = mot1.split(' ') 
    mot2 = mot2.split(' ')

    #Suppression du \n terminal
    del mot1[-1]
    del mot2[-1]

    #Conversion des listes en tableau
    mot1 = np.asarray(mot1)
    mot2 = np.asarray(mot2)

    return (mot1, mot2)


def dist_naif(x,y):
    """ Prend en entrée deux mots sous forme de tableau numpy
        et lance le premier appel de dist_naif_rec.
        Renvoie la distance d'édition minimale entre x et y """

    return dist_naif_rec(x,y,-1,-1,0,-1)

def dist_naif_rec(x,y,i,j,c,dist):
    """ Prend en entée deux mots sous forme de tableau numpy,
        deux indices entiers i et j,
        c coût de l'alignement de x[:i],y[:j]
        dist le coût du meilleur alignement de (x,y) avant appel
        Renvoie le coût du meilleur alignement après appel """
    if i == x.size-1 and j == y.size-1 :
        if dist == -1 or c < dist :
            return c
    
    if i < x.size-1 and j < y.size-1:
        dist = dist_naif_rec(x,y,i+1,j+1,c+sub(x[i+1], y[j+1]), dist)

    if i < x.size-1:
        dist = dist_naif_rec(x,y,i+1,j,c+2, dist)

    if j < y.size-1:
        dist = dist_naif_rec(x,y,i,j+1,c+2, dist)

    return dist


def sub(a,b):
    """ Prend en entrée deux lettres et
        renvoie le coût de substition """

    if a == b:
        return 0

    if a in ['A', 'T']:
        if b in ['A', 'T']:
            return 3
        return 4

    if b in ['G', 'C']:
        return 3

    return 4


def main():
    (x,y) = lire_mots("Instances_genome/Inst_0000010_44.adn")
    dist = dist_naif(x,y)
    print("Distance : {}".format(dist))

if __name__ == "__main__":
    main()