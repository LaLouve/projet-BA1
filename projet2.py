'''
Dervaux Florence, N° de matricule : 000396246, groupe 4

Projet 2: "Save private data" or "jHeaven strikes back"

Edward Snowden is hiding in Russia
'''

import sys


def substitution(subKey, message):
    '''
    substitution des caractères du message
    key représente le décallage
    pour le décryptage, utiliser -subKey
    '''
    substitutionMessage = ''
    for l in message:
        lTmp = l
        if ord('a') <= ord(l) <= ord('z'):
            lTmp = (ord(l) - ord('a') + subKey) % 26
            lTmp = chr(lTmp + ord('a'))

        elif ord('A') <= ord(l) <= ord('Z'):
            lTmp = (ord(l) - ord('A') + subKey) % 26
            lTmp = chr(lTmp + ord('A'))

        elif ord('0') <= ord(l) <= ord('9'):
            lTmp = (ord(l) - ord('0') + subKey) % 10
            lTmp = chr(lTmp + ord('0'))

        substitutionMessage += lTmp
    return substitutionMessage


def permutation(permKey, message):
    '''
    permutation des caractères du message
    permKey représente la taille d'un block
    analyser algébriquement pour ne pas utiliser de sous-listes
    et pouvoir utiliser la même fonction pour décrypter en utilisant
    (len(message)//permKey) comme permKey
    '''
    permutationMessage = ''
    for i in range(permKey):
        for j in range(0, len(message), permKey):
            permutationMessage += message[i + j]
    return permutationMessage


def padding(permKey, message):
    '''
    padding du message
    peut être utilisée pour le cryptage et le décryptage
    pour le décryptage, on cherche le '@' et on supprime tous les
    caractères suivants
    '''
    if permKey > 0:
        paddingMessage = message + '@#' + '#' * \
            (- ((len(message) + 2) % -permKey))
    else:
        paddingMessage = message[:message.rfind('@')]
    return paddingMessage


def encrypt(permKey, subKey, message):
    '''
    cryptage = padding puis substitution et permutation
    '''
    paddingMessage = padding(permKey, message)
    substitutionMessage = substitution(subKey, paddingMessage)
    encryptMessage = permutation(permKey, substitutionMessage)
    return encryptMessage


def decrypt(permKey, subKey, message):
    '''
    décryptage = permutation puis substitution et padding
    '''
    permutationMessage = permutation(len(message) // permKey, message)
    substitutionMessage = substitution(-subKey, permutationMessage)
    decryptMessage = padding(-permKey, substitutionMessage)
    return decryptMessage


def main(action, subKey, permKey, message):
    '''
    vérifie les paramètres et affiche les résultats
    '''
    if (permKey <= 0 or subKey < 0 or action not in ['e', 'd']):
        print('Wrong parameters!')
    elif action == 'd' and len(message) % permKey != 0:
        print('\nMessage length must be a multiple of the permutation key')
    else:
        print("\nMessage: {}\nSubstitution Key: {}\nPermutation Key: {}"
              .format(message, subKey, permKey))
        if action == 'e':
            print('Encrypted message:', encrypt(permKey, subKey, message))
        else:
            print('Decrypted message:', decrypt(permKey, subKey, message))


if __name__ == '__main__':
    '''
    récupère, vérife et formate les paramètres
    appel de la focntion principale, main
    '''
    if len(sys.argv) < 5:
        print('\nNot enough parameters')
    else:
        action = sys.argv[1][0].lower()

        if sys.argv[2].isdigit():
            subKey = int(sys.argv[2])
        else:
            subKey = -1  # wrong parameters dans le main

        if sys.argv[3].isdigit():
            permKey = int(sys.argv[3])
        else:
            permKey = -1  # wrong parameters dans le main

        message = ' '.join(sys.argv[4:])

        main(action, subKey, permKey, message)
