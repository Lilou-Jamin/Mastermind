# Importation du module pygame
import pygame
import random
import math
import mastermind2

# Définition des variables globales
Noir = (0,0,0)
Blanc = (255,255,255)
Gris = (128,128,128)
Bleu = (0,0,255)
Rouge = (255,0,0)
Vert = (0,255,0)
Orange = (225,127,0)
Rose = (255,0,127)
Jaune = (255,255,0)
Marron = (160,60,0)

nbCases = 5
TabCouleur = [Noir, Blanc, Gris, Bleu, Rouge, Vert, Orange, Rose, Jaune]

def afficherSecret(laFenetre:pygame.Surface,leSecret:list)->None:
    for i in range(len(leSecret)):
        pygame.draw.circle(laFenetre,leSecret[i],[320+40*i,20],15)
        pygame.draw.circle(laFenetre,Noir,[320+40*i, 20],15,1)
    pygame.display.update()

def afficherCombinaison(laFenetre:pygame.Surface,laCombinaison:list,numLigne:int)->None:
    for i in range(nbCases):
        pygame.draw.circle(laFenetre,Marron,[320+40*i,40+40*(numLigne-1)],15)
    for i in range(len(laCombinaison)):
        pygame.draw.circle(laFenetre,laCombinaison[i],[320+40*i,40+40* (numLigne-1)],15)
        pygame.draw.circle(laFenetre,Noir,[320+40*i, 40+40* (numLigne-1)],15,1)
    pygame.display.update()

def afficherPlateau(f:pygame.Surface)->None:
    pygame.draw.rect(f,Marron,[300,0,200,40])
    for i in range(5):
        pygame.draw.rect(f,Noir,[300+40*i,0,40,40],1)
    pygame.draw.rect(f,Marron,[300,60,200,40*15])
    pygame.draw.rect(f,Marron,[520,60,40,40*15])
    for l in range(15):
        for i in range(nbCases):
            pygame.draw.rect(f,Noir,[300+40*i,60+40*l,40,40],1)
        pygame.draw.rect(f,Noir,[520,60+40*l,40,40],1)

    text1 = "Nb noir = Nb mal placé"
    text2 = "Nb blanc = Nb bien placé"
    text3 = "Choix pion"
    text4 = "Retirer dernier pion"
    myfont = pygame.font.SysFont("monospace", 15)
    label1 = myfont.render(text1, 1, Noir)
    label2 = myfont.render(text2, 1, Noir)
    label3 = myfont.render(text3, 1, Noir)
    label4 = myfont.render(text4, 1, Noir)
    f.blit(label3, (100, 200))
    f.blit(label4, (100, 430))
    f.blit(label1, (570, 200))
    f.blit(label2, (570, 220))
    pygame.display.update()

# Création des boutons sur le côté droit
def replayButton(f):
    pygame.draw.circle(f,TabCouleur[4],[750,20],15)
    myfont = pygame.font.SysFont("monospace", 15)
    lab = myfont.render("Rejouer",1, Noir)
    f.blit(lab,[720,35])
    pygame.display.update()

def gameMode(f):
    pygame.draw.circle(f,TabCouleur[5],[750,100],15)
    myfont = pygame.font.SysFont("monospace", 15)
    lab = myfont.render("Naïve",1, Noir)
    f.blit(lab,[730,115])

    pygame.draw.circle(f, TabCouleur[5], [750, 150], 15)
    myfont = pygame.font.SysFont("monospace", 15)
    lab = myfont.render("Intelligente", 1, Noir)
    f.blit(lab, [690, 170])
    pygame.display.update()

def getGameMode(f,code)->None:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                positionSouris = pygame.mouse.get_pos()
                if distance(positionSouris, [750,100])<15:
                    return methodeNaive(f,code)
                elif distance(positionSouris, [750,150])<15:
                    return methodeIntelligente(f, code)



def afficherChoixCouleur(f:pygame.Surface)->None:
    for i in range(len(TabCouleur)):
        pygame.draw.circle(f,TabCouleur[i],[75,80+40*i],15)
        pygame.draw.circle(f,Noir,[75,80+40*i],15,1)
    pygame.draw.circle(f,Marron,[75,80+40*9],15)
    pygame.draw.circle(f,Noir,[75,80+40*9],15,1)
    pygame.display.update()

def distance(a:list,b:list)->float:
    return math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)

def getChoixCouleur()->None:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("C'est terminé !")
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP:
                positionSouris = pygame.mouse.get_pos()
                if distance(positionSouris, [75,80+40*9])<15:
                    return None
                if distance(positionSouris, [750,20])<15:
                    return mastermind2.start()
                for i in range(len(TabCouleur)) :
                    if distance(positionSouris, [75,80+40*i])<15:
                        return TabCouleur[i]

def construireProposition(f:pygame.Surface,ligne:int)->list:
    proposition = []
    while len(proposition)<5:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        couleur = getChoixCouleur()
        if couleur==None:
            if len(proposition)>0:
                del proposition[-1]
        else:
            proposition.append(couleur)
        afficherCombinaison(f,proposition,ligne)
        pygame.display.update()
    return proposition

def afficherResultat(f:pygame.Surface,res,ligne):
    x = 520
    y = 20+40*(ligne-1)
    centres = [(x+6,y+6),(x+6,y+34),(x+20,y+20),(x+34,y+6),(x+34,y+34)]
    i = 0
    while i<res[0]:
        pygame.draw.circle(f,Blanc,centres[i],4)
        i = i + 1
    j = 0
    while j<res[1]:
        pygame.draw.circle(f,Noir,centres[i],4)
        i = i + 1
        j = j + 1
    pygame.display.update()

def reloadPlateau(f,secret):
    afficherPlateau(f)
    afficherSecret(f,secret)

def dejaplace(inc,liste):
    for i in range(len(liste)):
        if inc == liste[i][1]:
            return True
    return False

# Fonction de la méthode naïve
def methodeNaive(f, codeUtilisateur):
    nbessai = 0
    trouve = False
    fait = []
    claim = 0
    while not(trouve):
        possibilites = []
        for i in range(5):
            possibilites.append(random.choice(TabCouleur))
        if not(possibilites in fait):
            nbessai += 1
            fait.append(possibilites)
            if claim > 14 :
                reloadPlateau(f,codeUtilisateur)
                claim = 0
            afficherCombinaison(f, possibilites, claim+2)
            claim +=1
            if codeUtilisateur == possibilites:
                trouve = True
    return(nbessai,trouve)

# Fonction de la méthode intelligente
def methodeIntelligente(f,secret):
    c = []
    couleur0 = []
    trouve = False
    i = 0
    claim = 0
    nbessai = 1
    # Recherche des 5 couleurs
    while not(trouve):
        possibilites = [TabCouleur[i]]*5
        afficherCombinaison(f,possibilites, claim +2)
        res = mastermind2.calcul_res(secret,possibilites)
        afficherResultat(f,res,claim + 2)
        if res[0] == 5 :
            return(nbessai, True)
        for _ in range(res[0]):
            c.append(TabCouleur[i])
        if res[0] == 0 and len(couleur0) < 1 :
            couleur0.append(TabCouleur[i])
        if len(c) >= 5 and len(couleur0) > 0:
            trouve = True
        i = i+1
        nbessai = nbessai + 1
        claim = claim + 1


    # Recherche de l'emplacement de chaque couleur
    trouve = False
    all = []
    while not(trouve):
        for color in c :
            inc = 0
            emp = False
            while not(emp):
                possibilites = []
                # Création des possiblités pour trouver l'emplacement d'une couleur
                for k in range(0,5):
                    if not(dejaplace(k,all)):
                        if k == inc :
                            poss = inc
                            possibilites.append(color)
                    if not(k == inc):
                        possibilites.append(couleur0[0])
                if len(possibilites) == 5 :
                    afficherCombinaison(f, possibilites, claim + 2)
                    res = mastermind2.calcul_res(secret, possibilites)
                    afficherResultat(f, res, claim + 2)
                    if mastermind2.calcul_res(secret,possibilites)[0] == 1 and not([color, poss] in all) :
                        all.append([color, poss])
                        emp = True
                    nbessai = nbessai + 1
                    claim = claim + 1
                inc = inc + 1
                if claim > 14:
                    reloadPlateau(f, secret)
                    claim = 0

            if len(all) == 5:
                trouve = True
    # Mise en place de la possibilité finale / On commence par trier avec les couleurs dans l'ordre
    reponse = []
    for _ in range(len(all)):
        for i in range(len(all)-1):
            if all[i][1] > all[i+1][1]:
                temp = all[i+1]
                all[i+1] = all[i]
                all[i] = temp

    # On crée une liste avec le code couleur final
    for i in range(len(all)):
        reponse.append(all[i][0])
    nbessai = nbessai + 1
    afficherCombinaison(f,reponse,claim+1)
    res = mastermind2.calcul_res(secret, reponse)
    afficherResultat(f, res, claim + 1)
    return(nbessai, True)