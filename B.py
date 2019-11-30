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


def dist_1(x,y):
    """ Prend en entrée deux mots sous forme de tableau
    et renvoie le tableau D"""
    D = []
    for i in range(len(x)+1):
        D.append([])
        for j in range(len(y)+1):
            D[i].append(None)

    for i in range(len(x)+1):
        for j in range(len(y)+1):
            if i == 0:
                if j == 0:
                    D[0][0] = 0
                else:
                    D[0][j] = j * c_ins
            else:
                if j == 0:
                    D[i][0] = i * c_ins
                else:
                    c = D[i-1][j-1] + sub(x[i-1], y[j-1])

                    if D[i-1][j] + c_del < c:
                        c = D[i-1][j] + c_del
                    
                    if D[i][j-1] + c_ins < c:
                        c = D[i][j-1] + c_ins

                    D[i][j] = c

    return D

def sol_1(x,y,D):
    """ Prend en entrée deux mots x,y et le tableau déjà remplit des distances
    Renvoie l'alignement minial de (x,y)"""
    """On ne peut ajouter un élément en début de liste en O(1) en python.
    Ainsi, afin de conserver les complexités théoriques du sujet, nous allons
    ajouter les éléments en fin de liste, puis inverser les listes à la fin en O(n),
    ce qui ne changera pas la complexité globale de la fonction."""

    i = len(x) 
    j = len(y) 
    x2=[]
    y2=[]

    while i > 0 and j > 0: 
        if D[i][j] == D[i-1][j-1] + sub(x[i-1],y[j-1]):
            x2.append(x[i-1])
            y2.append(y[j-1])
            i = i - 1
            j = j - 1
        else:
            if D[i][j] == D[i][j-1] + c_ins:
                x2.append('_')
                y2.append(y[j-1])
                j = j - 1
            else:
                x2.append(x[i-1])
                y2.append('_')
                i = i - 1
        

    
    while i > 0:
        x2.append(x[i-1])
        y2.append('_')
        i = i - 1
    
    while j > 0:
        x2.append('_')
        y2.append(y[j-1])
        j = j - 1

    x2.reverse()
    y2.reverse()

    return (x2, y2)

def prog_dyn(x,y):
    D = dist_1(x,y)
    (x2,y2) = sol_1(x,y,D)
    return (x2,y2,D[len(x)][len(y)])

def main():
    (x,y) = lire_mots("Instances_genome/Inst_0000010_7.adn")
    (x2,y2,D) = prog_dyn(x,y)
    print("Distance : {}\n{} \n{}".format(D, x2,y2))

if __name__ == "__main__":
    main()