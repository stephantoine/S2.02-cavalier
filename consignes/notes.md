# A faire 

- grille de 8*8 cases 

- programme principal pour tout regrouper

- recuperer le nombre de cases 

- verifier que toutes les cases de la grille sont parcourues avec une variable 

- constante position de départ

# Liste des fonctions

- fonction voisin qui donne les huit possibilités: 

1. (l-2, c-1)
2. (l-2, c+1)
3. (c+2, l-1) 
4. (c+2, l+1) 
5. (l+2, c+1) 
6. (l+2, c-1) 
7. (c-2, l+1) 
8. (c-2, l-1)

- une fonction backtracking récursif

- une fonction pour afficher la grille 

- une fonction qui donne la pos du cavalier

- une fonction possible qui vérifie que la case existe

- fonction qui retire le voisin sur lequel on a été depuis la case precedente 

l'échiquier va être un tableau (m * n) de dictionnaires : une clé va être associée à la position de la case et les valeurs de cette clé vont être une liste de positions des voisins disponibles
