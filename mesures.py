from A import *
from B import *
from C import *
from D import *
from time import *
import sys


def main():
    with open("res_tache_B", 'w') as f:
        print("---------    DEBUT TACHE A   --------\n")
        for i in liste_instances:
            i = "Instances_genome/" + i
            (x,y) = lire_mots(i)
            start = time()
            dist_naif(x,y)
            end = time()
            res = round(end-start, 1)
            f.write("{} {}\n".format(len(x), res))
            print("Taille : {} Temps : {}".format(len(x),res))
            if res > 60:
                exit()

    print("\n\n")
    
    with open("res_tache_B", 'w') as f:
        print("---------    DEBUT TACHE B   --------\n")
        for i in liste_instances:
            i = "Instances_genome/" + i
            (x,y) = lire_mots(i)
            if len(x) >10000:
                break
            start = time()
            prog_dyn(x,y)
            end = time()
            res = round(end-start, 1)
            f.write("{} {}\n".format(len(x), res))
            print("Taille : {} Temps : {}".format(len(x),res))
            
    print("\n\n")

    with open("res_tache_C", 'w') as f:
        print("---------    DEBUT TACHE C   --------\n")
        for i in liste_instances:
            i = "Instances_genome/" + i
            (x,y) = lire_mots(i)
            start = time()
            dist_2(x,y)
            end = time()
            res = round(end-start, 1)
            f.write("{} {}\n".format(len(x), res))
            print("Taille : {} Temps : {}".format(len(x),res))
            if res > 600:
                exit()

    print("\n\n")
    with open("res_tache_D", 'w') as f:
        print("---------    DEBUT TACHE D   --------\n")
        for i in liste_instances:
            i = "Instances_genome/" + i
            (x,y) = lire_mots(i)
            start = time()
            sol_2(x,y)
            end = time()
            res = round(end-start, 1)
            f.write("{} {}\n".format(len(x), res))
            print("Taille : {} Temps : {}".format(len(x),res))
            if res > 600:
                exit()




liste_instances = ["Inst_0000010_44.adn",
"Inst_0000010_7.adn",
"Inst_0000010_8.adn",
"Inst_0000012_13.adn",
"Inst_0000012_32.adn",
"Inst_0000012_56.adn",
"Inst_0000013_45.adn",
"Inst_0000013_56.adn",
"Inst_0000013_89.adn",
"Inst_0000014_23.adn",
"Inst_0000014_7.adn",
"Inst_0000014_83.adn",
"Inst_0000015_2.adn",
"Inst_0000015_4.adn",
"Inst_0000015_76.adn",
"Inst_0000020_17.adn",
"Inst_0000020_32.adn",
"Inst_0000020_8.adn",
"Inst_0000050_3.adn",
"Inst_0000050_77.adn",
"Inst_0000050_9.adn",
"Inst_0000100_3.adn",
"Inst_0000100_44.adn",
"Inst_0000100_7.adn",
"Inst_0000500_3.adn",
"Inst_0000500_88.adn",
"Inst_0000500_8.adn",
"Inst_0001000_23.adn",
"Inst_0001000_2.adn",
"Inst_0001000_7.adn",
"Inst_0002000_3.adn",
"Inst_0002000_44.adn",
"Inst_0002000_8.adn",
"Inst_0003000_10.adn",
"Inst_0003000_1.adn",
"Inst_0003000_25.adn",
"Inst_0003000_45.adn",
"Inst_0005000_32.adn",
"Inst_0005000_33.adn",
"Inst_0005000_4.adn",
"Inst_0008000_32.adn",
"Inst_0008000_54.adn",
"Inst_0008000_98.adn",
"Inst_0010000_50.adn",
"Inst_0010000_7.adn",
"Inst_0010000_8.adn",
"Inst_0015000_20.adn",
"Inst_0015000_30.adn",
"Inst_0015000_3.adn",
"Inst_0020000_5.adn",
"Inst_0020000_64.adn",
"Inst_0020000_77.adn",
"Inst_0050000_63.adn",
"Inst_0050000_6.adn",
"Inst_0050000_88.adn",
"Inst_0100000_11.adn",
"Inst_0100000_3.adn",
"Inst_0100000_76.adn"]
if __name__ == "__main__":
    main()
