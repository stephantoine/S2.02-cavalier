"""###################### Déclaration des constantes ######################"""
LIGNE = 8
COLONNE = 8
TAILLE = LIGNE*COLONNE  #taille de la grille ici 64 cases


"""#############################  Fonctions  #############################"""


"""Cette fonction à pour but de calculer les voisins d'une case, elle renvoie ceux qui 
ne sont pas en dehors de la grille et ceux par lesquels le cavalier n'est pas encore passé"""

def voisin(pos, chemin):    #on recupere la position de la case (tuple) et le chemin parcouru par le cavalier jusqu'à maintenant
    lig = pos[0]   #on recupere la ligne et la colonne dans la position
    col = pos[1]
    possibleL = True #vérifier si on ne déplace pas le cavalier en dehors de la grille ou que la case voisine n'est pas déjà dans le chemin
    possibleC = True
    possibleChem = True
    listeVoisins = [] #liste des voisins sur lesquels le cavalier peut aller depuis sa position
    listeTemp = [(lig-2, col-1), (lig-2, col+1), (lig+2, col-1), (lig+2, col+1), (lig-1, col+2), (lig+1, col+2), (lig-1, col-2), (lig+1, col-2)] #on cree une liste temporaire qui contient tous les voisins possibles
    for i in range(len(listeTemp)): #parcours de la liste temporaire
        if listeTemp[i][0] < 0 or listeTemp[i][0] > LIGNE-1: #si la ligne est en dehors de la grille
            possibleL = False
        if listeTemp[i][1] < 0 or listeTemp[i][1] > LIGNE-1: #si la colonne est en dehors de la grille
            possibleC = False
        for j in range(len(chemin)): #on parcourt le chemin
            if chemin[j] == listeTemp[i]: #si une des cases du chemin correspond à un des voisins de la case
                possibleChem = False
        if possibleL == True and possibleC == True and possibleChem == True: #si la ligne et la colonne ne sont pas en dehors de la grille et que la case n'est pas dans le chemin
            listeVoisins.append(listeTemp[i]) #on ajoute a listeVoisin le voisin
        else: #on repasse les trois bool à true pour les autres cases
            possibleL = True
            possibleC = True
            possibleChem = True
    return listeVoisins #on renvoie la liste des voisins de la case


"""Cette fonction remplit un tableau 2D avec le chemin parcouru par le cavalier, chaque case 
du tableau aura une valeur entre 1 et 64 qui correspond à l'ordre des cases parcourues"""

def remplirTableau(chemin, tableau): #on passe en parametre le tableau 2D vide et le chemin parcouru par le cavalier
    indice = 1 #variable qui va de 1 à TAILLE pour avoir l'ordre des cases parcourues
    for element in chemin: #on parcourt le chemin
        i = element[0] #on recupere la premier valeur du tuple pour la ligne
        j = element[1] #puis la deuxième valeur pour la colonne
        tableau[i][j] = indice #on affecte la valeur de l'indice à la case du tableau (exemple : la premiere position du cavalier est (3,4) alors dans le tableau en (3,4) on met la valeur 1)
        indice+=1
    return tableau #on retourne le tableau complété



"""Cette fonction sert à initialiser un dictionnaire de liste qui contient les voisins, dans ce dictionnaire les clés sont 
un nombre qui correspond à l'ordre dans lequel les cases sont parcourues et les valeurs sont une liste de ses voisins"""

def initDicoVoisins():
    dico = {} #déclaration du dictionnaire vide
    for i in range(1,TAILLE+1): #on parcourt chaque case de l'échiquier et on initialise chaque clé du dictionnaire par une liste vide
        dico[i] = []
    return dico #on renvoie le dictionnaire initialisé


"""Cette fonction va parcourir le tableau rempli et afficher
 l'ordre des déplacments du cavalier sur l'échequier"""

def afficheGrille(LIGNE, COLONNE, tableau): #on passe en paramètre les constantes de ligne et de colonne et la tableau
    var = 0 #variable qui va servir au bon affichage de l'échiquier et à créer un échiquier à la bonne taille
    while var < TAILLE :
        for i in range(COLONNE +1): #on parcourt chaque case du tableau
            for j in range(LIGNE + 1):
                if j < LIGNE : #si on arrive pas au bout de la ligne on délimite le haut de la case
                    print("+------", end='')
                else : #sinon on marque la fin de la ligne
                    print("+")
            if i < COLONNE : #si on arrive pas à la fin de la colonne
                for j in range(COLONNE +1): #on parcourt chaque colonne
                    if j < COLONNE : #si on n'est pas à la dernière colonne
                        # affichage spécifique en fonction du nombre de chiffres de la case du tableau
                        if tableau[i][j] <= 9 : #si la valeur du tableau est inférieur ou égale à 9 on met 2 espaces
                            print("|  ",tableau[i][j]," ",end='')
                        else : #sinon elle est supérieur et on enlève un espace
                            print("| ",tableau[i][j]," ",end='')
                        var+=1
                    else : #si on arrive à la fin de la ligne
                        print("|")


"""Cette fonction récursive fait parcourir la grille au chevalier, si elle tombe dans une 
impasse elle revient en arrière et teste d'autres possibilités tant que l'échiquier n'est pas parcourut en entier"""

def backtracking(pos, chemin, dicoListe): #on prend en parametre la position de depart, le chemin qui va être complété et le dictionnaire de liste
    if(len(chemin)==TAILLE):  #condition d'arrêt si la longueur du chemin est egale à la taille alors le cavalier à parcouru toute la grille
        return chemin #on renvoie le chemin
    else:
        chemin.append(pos) #on ajoute au chemin la position actuelle du cavalier
        if (dicoListe[len(chemin)] == []): #si la liste des voisins de la case actuelle est vide (ex: len(chemin) = 3 on cherche dans dicoListe les voisins de la 3eme case)
            VoisinsCaseActuelle = voisin(pos, chemin) #on initialise sa liste de voisins avec la fonction voisin
            dicoListe[len(chemin)] = VoisinsCaseActuelle #on ajoute sa liste des voisins dans le dictionnaire
        else:
            VoisCaseActuelle = dicoListe[len(chemin)] #si la liste des voisins à déjà été créée, on la récupère grâce à dicoListe
        if (VoisinsCaseActuelle == []): #si la liste des voisins de la case actuelle est vide (on est dans une impasse)
            chemin.pop() #on enleve du chemin la case actuelle
            listeAvant = dicoListe[len(chemin)]  #on recupere la liste de voisins de la case précédente
            while (listeAvant == []): #tant que les listes des cases précédentes sont vides on revient en arrière
                chemin.pop() #on enlève une nouvelle fois la case actuelle du chemin
                listeAvant = dicoListe[len(chemin)] #on prend la liste de la case d'encore avant
            suivant = listeAvant.pop() #si elle a des voisins on prend le dernier de ses voisins et on le conserve dans une variable
        else: #sinon c'est que la case du début avait des voisins
            suivant = VoisinsCaseActuelle.pop() #dans ce cas on conserve le dernier de ses voisins dans une variable
        dicoListe[len(chemin)] = VoisinsCaseActuelle #on met à jour la liste de ses voisins dans le disctionnaire
        return backtracking(suivant, chemin, dicoListe) #on rappelle la fonction cette fois ci avec la case suivante dont la position est dans la variable suivant, avec le chemin et le dictionnaire


"""###########################  Programme principal  ###########################"""

tab = [] #on créé un tableau vide qui va représenter l'échiquier
for i in range(LIGNE): #on initialise le tableau, par un tableau 2d qui va contenir que des listes de 0
    tab.append([0] * COLONNE)
caseDepart = (3,4) #case de départ du cavalier
chemin = [] # on créé la liste du chemin parcourut par le cavalier
listePiles = initDicoVoisins() #on crée et initialise le dictionnaire qui va sauvegarder les listes de voisins des cases
cheminParcouru = backtracking(caseDepart, chemin, listePiles) #on appelle le backtracking, qui va donc permettre au cavalier de parcourir l'échiquier, et on conserve le chemin dans la variable cheminParcouru
remplirTableau(cheminParcouru, tab) #on remplit le tableau 2D avec le chemin parcouru par le cavalier
afficheGrille(LIGNE, COLONNE, tab) #on affiche le tableau



"""le probleme c'est que notre programme atteint la limite de recursivité de python, 
pour le regler il faudrait passer des parties de la méthode récursive en itérative"""