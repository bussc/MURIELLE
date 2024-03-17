import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Définition des couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)

# Définition de la taille du plateau
TAILLE_CASE = 50
NB_COLONNES = 5
NB_LIGNES = 5

# Initialisation du plateau
plateau = [[0 for _ in range(NB_COLONNES)] for _ in range(NB_LIGNES)]

# Fonction pour dessiner le plateau
def dessiner_plateau():
    for ligne in range(NB_LIGNES):
        for colonne in range(NB_COLONNES):
            couleur_case = BLANC if (ligne + colonne) % 2 == 0 else NOIR
            pygame.draw.rect(ecran, couleur_case, (colonne * TAILLE_CASE, ligne * TAILLE_CASE, TAILLE_CASE, TAILLE_CASE))

# Fonction pour dessiner les pièces
def dessiner_pieces():
    for ligne in range(NB_LIGNES):
        for colonne in range(NB_COLONNES):
            if plateau[ligne][colonne] == 1:
                pygame.draw.circle(ecran, (255, 0, 0), (colonne * TAILLE_CASE + TAILLE_CASE // 2, ligne * TAILLE_CASE + TAILLE_CASE // 2), TAILLE_CASE // 2 - 5)
            elif plateau[ligne][colonne] == 2:
                pygame.draw.circle(ecran, (0, 0, 255), (colonne * TAILLE_CASE + TAILLE_CASE // 2, ligne * TAILLE_CASE + TAILLE_CASE // 2), TAILLE_CASE // 2 - 5)

# Initialisation de la fenêtre
largeur = NB_COLONNES * TAILLE_CASE
hauteur = NB_LIGNES * TAILLE_CASE
ecran = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption('Jeu Songo')

# Boucle principale
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    dessiner_plateau()
    dessiner_pieces()

    pygame.display.flip

