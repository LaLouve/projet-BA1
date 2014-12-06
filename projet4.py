'''
Dervaux Florence, N° de matricule : 000396246, groupe 4

Projet 4: Introdiction à la sténographie

The cake is a lie!
'''
from sys import argv


def info_image(nom_image):
    '''
    Récupère l'header de l'image contenant les informations de celle-ci
    telle que sa taille et la valeur maximale d'un pixel
    '''
    image = open(nom_image)
    identifier = (image.readline()).strip()

    if identifier != 'P2':
        print('Le fichier n\'est pas un fichier PGM!')
        width, height, valMax = None, None, None
    else:
        size = (image.readline()).split()
        width = int(size[0])
        height = int(size[1])
        valMax = int((image.readline()).strip())

    image.close()
    return (identifier, width, height, valMax)


def charger_image(nom_image):
    '''
    lit le fichier image et renvoie la matrice des pixels
    '''
    identifier, width, height, valMax = info_image(nom_image)

    pixelMatrix = []

    if identifier == 'P2':
        sizeX = int(width)
        sizeY = int(height)

        image = open(nom_image)
        imageBrut = image.read().split()[1:]

        for y in range(sizeY):
            lineOffset = sizeX * y
            line = []
            for x in range(sizeX):
                line.append(int(imageBrut[lineOffset + x + 3]))
            pixelMatrix.append(line)
        image.close()

    return pixelMatrix


def writePGM(nom_image, pgm, info):
    '''
    Permet d'écrire les infos dans un fichier pgm
    '''
    fichier = open(nom_image, "w")
    body = "\n".join([" ".join([str(y) for y in x]) for x in pgm])

    fichier.write(
        "P2\n{0} {1}\n{2}\n{3}\n".format(
            info[1],
            info[2],
            info[3],
            body))
    fichier.close()


def encodageMethode(source, code):
    '''
    crée le corps du fichier a encoder
    '''
    infoSource = info_image(source)
    bodySource = charger_image(source)

    infoCode = info_image(code)
    bodyCode = charger_image(code)

    for i in range(infoSource[2]):
        for j in range(infoSource[1]):
            parite = bodySource[i][j] % 2
            if parite == 0 and bodyCode[i][
                    j] != 0 and bodySource[i][j] == infoSource[3]:
                bodySource[i][j] -= 2
            bodySource[i][j] += bodyCode[i][j] - parite

    return bodySource


def decodageMethode(crypt):
    '''
    crée le corps du fichier décrypté
    '''
    infoCrypt = info_image(crypt)
    bodyCrypt = charger_image(crypt)

    for i in range(infoCrypt[2]):
        for j in range(infoCrypt[1]):
            bodyCrypt[i][j] %= 2
    return bodyCrypt


def encodage(source, code, res):
    '''
    permet l'encodage d'une image "code" dans une image "source"
    le résultat est inscrit dans une troisième image "res"
    '''
    infoSource = None
    infoCode = None

    try:
        infoSource = info_image(source)
    except IOError as e:
        print("Impossible d'ouvrir {0}".format(source))

    try:
        infoCode = info_image(code)
        if infoCode[3] != 1:
            print("Le fichier {0} n'est pas au bon format !".format(code))
            infoCode = None

        if infoCode[0] != 'P2':
            print("Le fichier {0} n'est pas au bon format !".format(code))
            infoCode = None

    except IOError as e:
        print("Impossible d'ouvrir {0}".format(code))

    if not(infoSource is None or infoCode is None):
        writePGM(res, encodageMethode(source, code), infoSource)


def decodage(crypt, claire):
    '''
    Permet le décodage d'une image cryptée, "crypt"
    le résultat est inscrit dans une nouvelle image "claire"
    '''
    infoCrypt = None
    try:
        infoCrypt = info_image(crypt)
        infoCrypt = (infoCrypt[0], infoCrypt[1], infoCrypt[2], 1)

        if infoCrypt[0] != 'P2':
            print("Le fichier {0} n'est pas au bon format !".format(crypt))
            infoCrypt = None

    except IOError as e:
        print("Impossible d'ouvrir {0}".format(crypt))

    if not(infoCrypt is None):
        writePGM(claire, decodageMethode(crypt), infoCrypt)


if __name__ == '__main__':
    print("\nProjet sténographie:\n", 18 * '~')
    if len(argv) == 5 and argv[1] == "codage":
        text = "Fichier source: {}\nFichier code: {}\nFichier destination: {}".format(
            argv[2],
            argv[3],
            argv[4])
        print(text)
        encodage(argv[2], argv[3], argv[4])
        print("Codage: Travail terminé !")

    elif len(argv) == 4 and argv[1] == "decodage":
        text = "Fichier source: {}\nFichier destination: {}".format(
            argv[2],
            argv[3])
        print(text)
        decodage(argv[2], argv[3])
        print("Décodage: Travail terminé !")

    elif argv[1] not in ["codage", "decodage"]:
        print("Operation non comprise.")
    else:
        print("nombre de paramètre non conforme.")
