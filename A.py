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
        # Même lettre : coût nul
        return 0

    if a in ['A', 'T']:
        if b in ['A', 'T']:
            # Paire concordante
            return 3
        return 4

    if b in ['G', 'C']:
        # Paire concordante
        return 3

    return 4


def dist_naif(x,y):
    """ Prend en entrée deux mots sous forme de tableau
        et lance le premier appel de dist_naif_rec.
        Renvoie la distance d'édition minimale entre x et y """
        # Il faut faire le premier appel avec les indices -1, car à l'itération on remplit la ligne i+1
    return dist_naif_rec(x,y,-1,-1,0,-1)

def dist_naif_rec(x,y,i,j,c,dist):
    """ Prend en entée deux mots sous forme de tableau,
        deux indices entiers i et j,
        c coût de l'alignement de x[:i],y[:j]
        dist le coût du meilleur alignement de (x,y) avant appel
        Renvoie le coût du meilleur alignement après appel """

    # Traduction du pseudo-code donné dans l'énoncé en python
    if i == len(x)-1 and j == len(y)-1 :
        if dist == -1 or c < dist :
            return c
    
    if i < len(x)-1 and j < len(y)-1:
        dist = dist_naif_rec(x,y,i+1,j+1,c+sub(x[i+1], y[j+1]), dist)

    if i < len(x)-1:
        dist = dist_naif_rec(x,y,i+1,j,c+c_del, dist)

    if j < len(y)-1:
        dist = dist_naif_rec(x,y,i,j+1,c+c_ins, dist)

    return dist


def main():
    (x,y) = lire_mots("Instances_genome/Inst_0000010_44.adn")
    dist = dist_naif(x,y)
    print("Distance : {}".format(dist))

if __name__ == "__main__":
    main()