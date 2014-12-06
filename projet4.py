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
    return (identifier, int(width), int(height), int(valMax))

def charger_image(nom_image):
    identifier, width, height, valMax = info_image(nom_image)
    
    pixelMatrix = []

    if identifier == 'P2':
        sizeX = int(width)
        sizeY = int(height)

        image = open(nom_image)
        imageBrut = image.read().split()[1:]

        for y in range(sizeY):
            lineOffset = sizeX*y
            line = []
            for x in range(sizeX):
               line.append(int(imageBrut[lineOffset + x + 3 ]))
            pixelMatrix.append(line)
        image.close()
    
    return pixelMatrix

def encodageMethode(source, code):
    infoSource = info_image(source)
    bodySource = charger_image(source)

    infoCode = info_image(code)
    bodyCode = charger_image(code)


    for i in range(infoSource[2]):
        for j in range(infoSource[1]):
            parite = bodySource[i][j] % 2
            if parite == 0 and bodyCode[i][j] != 0 and bodySource[i][j] == infoSource[3]:
                bodySource[i][j] -= 2
            bodySource[i][j] += bodyCode[i][j] - parite

    return bodySource

def writePGM(nom_image, pgm, info):
    fichier = open(nom_image,"w")
    body = "\n".join([" ".join([str(y) for y in x]) for x in pgm])


    fichier.write("P2\n{0} {1}\n{2}\n{3}\n".format(info[1], info[2], info[3],body))
    fichier.close()

def encodage(source, code, res):
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
    except IOError as e:
        print("Impossible d'ouvrir {0}".format(code))

    if not(infoSource is None or infoCode is None): 
        writePGM(res, encodageMethode(source, code), infoSource)



if __name__=='__main__':
  if len(argv) == 5 and argv[1] == "codage":
     encodeProcedure(argv[2], argv[3], argv[4]) 
  elif len(argv) == 4 and argv[1] == "decodage":
     decodeProcedure(argv[2], argv[3])
  elif argv[1] not in ["codage", "decodage"]:
     print("Operation non comprise.") 
  else:
     print("nombre de paramètre non conforme.")