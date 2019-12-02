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

def sol_2(x,y):
    if len(y) == 0:
        y = mots_gaps(len(x))
        return (x,y)

    if len(x) == 0:
        x = mots_gaps(len(y))
        return (x,y)

    if len(x) == 1:
        return align_lettre_mot(x,y)

    i = len(x) // 2
    j = coupure(x,y)

    (x1, y1) = sol_2(x[:i], y[:j])
    (x2, y2) = sol_2(x[i:], y[j:])

    return (x1+x2, y1+y2)

def coupure(x,y):
    prec = []
    m = len(y) + 1

    stop = len(x) // 2
    for j in range(m):
        prec.append(j * c_del)
    for i in range(1,stop+1):
        D = []
        for j in range(m):
            if j == 0:
                D.append(i * c_ins)
                min_c = i * c_ins
                indice_min = j
            else:
                c = prec[j-1] + sub(x[i-1],y[j-1])
                if prec[j] + c_del < c:
                    c = prec[j] + c_del
                if D[j-1] + c_ins < c:
                    c = D[j-1] + c_ins
                D.append(c)
                if c <= min_c:
                    min_c = c
                    indice_min = j
        prec = D
    return indice_min

def mots_gaps(k):
    m = []
    for i in range(k):
        m.append('_')
    return m

def align_lettre_mot(x,y):
    c = -1
    i = 0
    for j in range(len(y)-1):
        if sub(x[0], y[j]) < c or c == -1:
            c = sub(x[0], y[j])
            i = j
    x_ = mots_gaps(i) + x + mots_gaps(len(y)-i-1)
    return (x_,y)

def main():
    (x,y) = lire_mots("Instances_genome/Inst_0000010_7.adn")
    (x,y) = sol_2(x,y)
    print("{}\n{}".format(x,y))

if __name__ == "__main__":
    main()