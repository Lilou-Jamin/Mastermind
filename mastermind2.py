import secrets
import pygame
import mm2

# En cas de partie gagnée
def win(fenetre, tentative):
    font = pygame.font.SysFont("monospace", 25) 
    txt = font.render(f"Bravo l'ordinateur a gagné en {tentative} tentative(s) !",1, mm2.Rouge)
    fenetre.blit(txt,[20,700])
    pygame.display.update()
    # On retourne False pour mettre fin au jeu
    return False


# Fonction de calcul du résultat
def calcul_res(secret, proposition):
    blanc = 0
    noir = 0
    p2 = proposition.copy()
    for i in range(5):
        # On regarde si un élément de secret à l'index i est égal à un élément de proposition au même index i
        if secret[i] == proposition[i]:
            # Si oui on ajout un pion blanc
            # Nous retirons l'élement de la liste p2 pour ne plus le prendre en compte les pions mal placés
                blanc = blanc+1
                p2.remove(proposition[i])
    for i in range(5):
        # Nous regardons si un élement de secret à l'index i est contenu dans la liste p2
        if secret[i] in p2:
            # Si oui alors on ajoute un pion noir
            noir = noir + 1
            # Retrait de cet élement de la liste p2 pour éviter de le comptabiliser plusieurs fois
            p2.remove(secret[i])
    res = [blanc,noir]
    return res


def start():
    pygame.init()
    fenetre = pygame.display.set_mode([800,800])
    fenetre.fill(mm2.Blanc)

    # Affichage d'un texte
    myfont = pygame.font.SysFont("monospace", 25)
    lab = myfont.render("MasterMind - Pierre Lilou Chérine",1, mm2.Noir)
    fenetre.blit(lab,[100,750])
    pygame.display.update()
    mm2.replayButton(fenetre)
    mm2.gameMode(fenetre)
    # Importation de fonctions contenues dans le fichier mm2 pour afficher le plateau et le choix des couleurs
    mm2.afficherPlateau(fenetre)
    mm2.afficherChoixCouleur(fenetre)

    secret = mm2.construireProposition(fenetre,0.5)
    res = mm2.getGameMode(fenetre, secret)
    manche = True
    if res[1] == True:
        win(fenetre,res[0])
    mm2.getChoixCouleur()

    enterpressed = False
    while not enterpressed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
              
if __name__ == "__main__":
    start()


