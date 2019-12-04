import sys
c_del = 2
c_ins = 2

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

    return (mot1, mot2)


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


def dist_2(x,y):
    """ Prend en entrée deux mots sous forme de tableau
    et renvoie le tableau D"""
    m = len(y) + 1

    # Remplissage de la première ligne
    prec = [0]
    for j in range(m):
        prec.append((j+1) * c_del)

    # Remplissage des lignes suivantes
    for i in range(1,len(x)+1):
        D = []
        for j in range(m):
            # Première case
            if j == 0:
                D.append(i * c_ins)

            # Test du meilleur coût et ajout dans D
            else:
                c = prec[j-1] + sub(x[i-1],y[j-1])
                if prec[j] + c_del < c:
                    c = prec[j] + c_del
                if D[j-1] + c_ins < c:
                    c = D[j-1] + c_ins
                D.append(c)
        prec = D # La ligne actuelle devient la précédente
    return D

def main():
    (x,y) = lire_mots(sys.argv[1])
    D = dist_2(x,y)
    print(D[-1])

if __name__ == "__main__":
    main()