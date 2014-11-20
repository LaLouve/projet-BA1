'''
Florence Dervaux
n° matricule: 000396246

INFO-F101 Programmation

Projet n°1: Le bonneteau
'''
#Import
from random import randint

print('\n~~~ Bienvenue dans le jeu \"Le bonneteau\" ~~~')

# Initialisation des variables
numOfGoblet = 3  # nombre de gobelets
winnings = 0  # comptabilise la somme gagnée ou perdue
playerBet = 1  # initialisation pour entrer dans la boucle while

# Vérification de l'entrée utilisateur pour l'argent de départ
moneyOK = False
while not moneyOK:
    try:
        playerMoney = float(input('\n\nVeuillez indiquer la quantité d\'argent'
                                  ' que vous possédez: '))  # argent du joueur
        moneyOK = True
    except:
        print('\nVous n\'avez pas entré une quantité d\'argent correcte.')


# boucle principale
while 0 < playerBet < playerMoney and playerMoney > 0:
    # Quitte le jeu si le joueur entre une mise négative ou
    # si il n'a plus d'argent

    print('\n\n~~~~~~~~~~~~~~~~~~')

    # Vérifiaction de l'entrée utilisateur pour la mise
    betOk = False
    while not betOk:
        try:
            playerBet = float(input('Veuillez indiquer votre mise (ou -1 pour'
                                    ' quitter le jeu): '))  # mise du joueur
            if playerBet <=  playerMoney:
                betOk = True
            else:
                print ('\nVous avez entré une somme d\'argent suppérieure à celle'
                        ' que vous possédez')
        except:
            print('\nVous n\'avez pas entré une quantité d\'argent correcte.')

    if playerBet > 0:
        print('\nLes goblets sont numérotés dans l\'ordre de 1 à', numOfGoblet)

        # Vérifiaction du numéro de gobelet entré par l'utilisateur
        choiceOk = False
        while not choiceOk:
            try:
                choicePlayer = int(input('Veuillez indiquer le goblet sous lequel'
                                         ' vous pensez que le jeton se trouve: '))
                if 1 <= choicePlayer <= numOfGoblet:
                    choiceOk = True
                else:
                    print(
                        '\nVous n\'avez pas entré un nombre compris entre 1 et',
                        numOfGoblet,
                        '.')
            except:
                print('\nVous n\'avez pas entré un numéro de gobelet correct.')

        jeton = randint(1, numOfGoblet)  # choix du goblets gagnant

        # cas gagnant
        if choicePlayer == jeton:
            playerMoney += 2 * playerBet
            winnings += 2 * playerBet
            print('Gagné !')
            print('Vous avez gagné', 2 * playerBet, '€!')

        # cas perdant
        else:
            playerMoney -= playerBet
            winnings -= playerBet
            print('Perdu !')
            print('Vous avez perdu', playerBet, '€!')
        print('Vous avez', playerMoney, '€ dans votre poche.')


# Fin du jeu et affichage des résultats
print('\n\n~~~ Fin du jeu ~~~')
print('Vous avez', playerMoney, '€ dans votre poche.')

# cas gagnant
if winnings >= 0:
    print('Vous avez gagné', winnings, '€.')
# cas perdant
else:
    winnings = str(winnings)[1:]  # permet de retirer le - de la somme perdue
    print('vous avez perdu', winnings, '€.')
