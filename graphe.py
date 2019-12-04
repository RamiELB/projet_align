import matplotlib.pyplot as plt
import sys

def read_data(filename):
    taille = []
    temps = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.split(' ')
            t = line[0]
            s = line[1]
            taille.append(t)
            temps.append(s)
                
    return (taille, temps)

def main(): 
    if len(sys.argv) < 2:
        print("Il faut donner le nom du fichier en argument")
        exit()
    filename = sys.argv[1]
    (taille, temps) = read_data(filename)
    plt.plot(taille,temps)
    plt.title(filename)
    plt.xlabel("Taille des instances")
    plt.ylabel("Temps d'éxecution (en s)")
    plt.show()


if __name__ == '__main__':
    main()