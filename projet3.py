'''
Dervaux Florence, N° de matricule : 000396246, groupe 1

projet 3: Le démineur
'''

#constantes
widht = 9 #taille de la grille

#grille par défaut 
grille = {}
grille[(0, 7)] = 'B'
grille[(1, 5)] = 'B'
grille[(1, 6)] = 'B'
grille[(1, 8)] = 'B'
grille[(2, 4)] = 'B'
grille[(3, 4)] = 'B'
grille[(5, 5)] = 'B'
grille[(5, 7)] = 'B'
grille[(7, 0)] = 'B'
grille[(7, 5)] = 'B'


def initGame(widht):
    '''
    Crée la matrice contenant l'état du jeu
    '''
    matrice = []
    for i in range (widht):
        rang = []
        for j in range (widht):
            rang.append("*")
        matrice.append(rang)
    return matrice

def showGrille(matrice, widht):
    '''
    Affichage de la grille de jeu
    '''
    print('   ', end=' ')
    for i in range(1, widht+1, 1):
        print(i, end='   ')
    print()
    print(' ', 36*'-')   

    count = 1
    for j in matrice:
        print(count, end=' | ')
        for k in j:
            print(k, end=' | ')
        print('')
        print(' ', 36 * '-')
        count += 1

def askCoord():
    '''
    Demande les coordonnées du prochain coup
    '''
    print('\nEntrez les coordonnées de votre coup:')
    ok = False
    while not ok:
        try:
            ligne = checkCoord(int(input('Numéro de la ligne:')), widht) -1
            colonne = checkCoord(int(input('Numéro de la colonne:')), widht) -1
            ok = True
        except:
            print("\nVous n'avez pas entré un nombre!")

    return(ligne, colonne)

def checkCoord(coord, widht):
    '''
    Vérifie si les coordonnées entrées sont dans la grille
    '''
    while (coord > widht or coord < 1): 
        coord=int(input('Vous avez indiqué une coordonnée incorrecte, réessayez:'))
    return coord

def checkLoose(coord, dicoBombe):
    '''
    Vérifie si les coordonnées entrées sont une bombe
    '''
    loose = False
    coordBombes = dicoBombe.keys()
    if coord in coordBombes:
        loose = True
    return loose

def checkWin(dicoBombe, matrice):
    '''
    Vérifie si la matrice ne contient plus des '*' aux emplacement des bombes
    '''
    win = False
    coordBombes = dicoBombe.keys()
    for liste in matrice:
        for elem in liste:
            if elem == '*' and (liste, elem) in coordBombes:
                win = True
            else = False

def bombeNear(coord, matrice, dicoBombe):
    '''
    Vérifie si il y a des bombes autour de la case sélectionnée.
    Si oui, compte les bombes et affiche le nombre correspondant
    Si non, affiche des espaces vides 
    '''
    i, j = coord[0], coord[1]

    # Liste des coordonnées des cases autour de la case choisie
    listeCoord = [(i-1, j-1), (i-1, j), (i-1, j+1),
                  (i, j-1), (i, j+1),
                  (i+1, j-1), (i+1, j), (i+1, j+1)]
    
    # Suppression des éléments sortant de la grille
    if i == 0:
        listeCoord[0], listeCoord[1], listeCoord[2] = None, None, None
    elif i == 8:
        listeCoord[5], listeCoord[6], listeCoord[7] = None, None, None
    if j == 0:
        listeCoord[0], listeCoord[3], listeCoord[5] = None, None, None
    elif j == 8:
        listeCoord[2], listeCoord[4], listeCoord[7] = None, None, None

    # Compte les bombes se trouvant autour de la case choisie
    coordBombes = dicoBombe.keys()            
    countBomb = 0
    for elem in listeCoord:
        if elem in coordBombes:
            countBomb += 1
    
    # Si il n'y a pas de bombes, remplis les cases avec un caractère vide
    # Si il y a des bombes, met le nombre dans la case choisie 
    if countBomb == 0:
        matrice[i][j] = ' '
        for elem in listeCoord:
            if elem != None:
                matrice[elem[0]][elem[1]] = ' '
    else:
        matrice[i][j] = countBomb
    return matrice





def main():
    matriceJeu = initGame(widht)
    showGrille(matriceJeu)
    coord = askCoord()
    loose = checkLoose(coord, grille)
    matriceJeu = bombeNear(coord, matriceJeu, grille)
    showGrille(matriceJeu)

if __name__ == '__main__':
    main()
