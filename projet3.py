'''
Dervaux Florence, N° de matricule : 000396246, groupe 1

projet 3: Le démineur
'''

#constantes
widht = 9
#letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']

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

matrice = [['*','*','*','*','*','*','*','*','*'],
           ['*','*','*','*','*','*','*','*','*'],
           ['*','*','*','*','*','*','*','*','*'],
           ['*','*','*','*','*','*','*','*','*'],
           ['*','*','*','*','*','*','*','*','*'],
           ['*','*','*','*','*','*','*','*','*'],
           ['*','*','*','*','*','*','*','*','*'],
           ['*','*','*','*','*','*','*','*','*'],
           ['*','*','*','*','*','*','*','*','*']]



def showGrille(matrice):
    print('  ', end=' ')
    for i in range(1, 10, 1):
        print(i, end='   ')
    print()
    print(' ', 36*'-')   

    count = 1
    for j in matrice:
        print(count, end=' |')
        for k in j:
            print(k, end=' | ')
        print('')
        print(' ', 36 * '-')
        count += 1

def askCoord():
    print('\nEntrez les coordonnées de votre coup:')
    ok = False
    while not ok:
        try:
            ligne = checkcoord(int(input('Numéro de la ligne:')), widht) -1
            colonne = checkcoord(int(input('Numéro de la colonne:')), widht) -1
            ok = True
        except:
            print("\nVous n'avez pas entré un nombre!")

    return(colonne, ligne)

def checkcoord(coord,valMax):
    while (coord > valMax or coord < 1): 
        coord=int(input('vous avez indiqué une coordonnée incorrecte, réessayez:'))
    return coord





showGrille(matrice)
askCoord()


