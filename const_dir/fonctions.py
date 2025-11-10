def voisin(pos):   #on recupere la position de la case (tuple)
    lig = pos[0]   #on recupere la ligne et la colonne dans la position de départ
    col = pos[1]
    possibleL = True #deux booleens pour verifier si on ne deplace pas le cavalier en dehors de la grille
    possibleC = True
    listeVoisin = [] #liste finale à renvoyer
    listeTemp = [[lig-2, col-1], [lig-2, col+1], [lig+2, col-1], [lig+2, col+1], [lig-1, col+2], [lig+1, col+2], [lig-1, col-2], [lig+1, col-2]] #on cree une liste temporaire qui contient tous les voisins possibles
    for i in range(len(listeTemp)): #parcours de la liste temporaire
        if listeTemp[i][0] < 0 or listeTemp[i][0] > 7: #si la ligne est en dehors de la grille
            possibleL = False #on passe son booleen à false
        if listeTemp[i][1] < 0 or listeTemp[i][1] > 7: #pareil pour la colonne
            possibleC = False
        if possibleL == True and possibleC == True: #si la ligne et la colonne ne sont pas en dehors de la grille
            listeVoisin.append(listeTemp[i]) #on ajoute a la liste finale le tuple de la case valide
        possibleL = True #on repasse les deux bool à true pour les autres cases
        possibleC = True
    return listeVoisin #on renvoie la liste finale

print(voisin([7,0]))


LIGNE = 8
COLONNE = 8
TAILLE = LIGNE * COLONNE

grille = []


def afficheGrille(LIGNE,COLONNE):
    var = 0
    while var < TAILLE :
        for i in range(COLONNE +1): 
            for j in range(LIGNE + 1):
                if j < LIGNE :
                    print("+------", end='')
                else : 
                    print("+")
            if i < COLONNE :
                for j in range(COLONNE +1):
                    if j < COLONNE :
                        if var < 9 :
                            print("|  ",var," ",end='')
                        elif var == 9 :
                            print("|  ",var," ",end='')
                        else : 
                            print("| ",var," ",end='')
                        var = var + 1
                    else : 
                        print("|")
                    
    print()


def positionActuelle(liste l):
    return l[-1]

def retirerVoisin(grille, position, voisin):
    grille[position].remove(voisin)

def backtracking(grille, case, chemin):
    # commencer le parcours (en profondeur), en marquant les cases visitées, et de
    # retourner en arrière si le chemin emprunté conduit à une impasse

    #enregistrement des cases visités
    voisins = []
    # tant que toutes les cases n'ont pas été visitées = tant que le nombre d'éléments de chemin est inférieur à la TAILLE de la grille
    while len(chemin) < TAILLE:
        # ajouter la position de cette case à la variable chemin
        chemin.append(case)
        # regarder les voisins de la case
        voisins = trouveVoisins(grille[pos])
        # si la liste voisins possède des voisins on rappelle le backtracking
        if len(voisins) > 0:
            newCase = voisins[0]
            backtracking(grille, newCase, chemin)
        # sinon on retourne en arrière
        else:
            chemin.pop()
            voisin.pop()
            case.pop()

def tourFini(nbCasesVisitées):
    tourFini = False
    if(nbCasesVisitées == TAILLE):
        tourFini = True
    return tourFini

def printRes(tourFini):
    if(tourFini == True):
        print("Le cavalier à fait un tour complet")
    else:
        print("Le cavalier n'a pas pu faire un tour complet")
