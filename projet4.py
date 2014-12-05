'''
Dervaux Florence, N° de matricule : 000396246, groupe 4

Projet 4: Introdiction à la sténographie
'''

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
        width = size[0]
        height = size[1]
        valMax = (image.readline()).strip()

    image.close()
    return (identifier, width, height, valMax)

def charger_image(nom_image):
    identifier, width, height, valMax = info_image(nom_image)
    sizeX = int(width)
    sizeY = int(height)

    image = open(nom_image)
    imageBrut = image.read().split()[1:]

    pixelMatrix = []
    for y in range(sizeY):
        lineOffset = sizeX*y
        line = []
        for x in range(sizeX):
           line.append(int(imageBrut[lineOffset + x + 3 ]))
        pixelMatrix.append(line)
    
    return pixelMatrix








def main(): 
    print(charger_image('math.pgm'))


if __name__ == "__main__":
    main()