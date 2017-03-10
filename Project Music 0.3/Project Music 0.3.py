# Importation des modules de Pygame
import pygame
from pygame.locals import *

# Initialisation des modules de Pygame

pygame.init()

# Création de la fenêtre

fenetre = pygame.display.set_mode((1300, 675))
pygame.display.set_caption("Project Music")

# Importation des constantes (images, notes...)

from constantes_0_3 import *

# Mise en place du clavier sur l'écran (forme initiale)

fenetre.blit(clavier_init, (400,200))
pygame.display.flip()


# Initalisation de la valeur permetant de lancer la boucle infinie

infinite = 1

# Boucle infinie

while infinite:

    # Chargement des évènements de Pygame
    
    for event in pygame.event.get():

        # Instructions permettant au programme de se fermer
        # correctement si l'on appuie sur la croix
        
        if event.type == QUIT:
            infinite = 0

        # Si l'on appuie sur une touche,
        # joue la note et met en place l'image du clavier adéquate
            
        if event.type == KEYDOWN:
            if event.key == K_e:
                do.play()
                fenetre.blit(clavier_do, (569,249))
                pygame.display.flip()
            if event.key == K_4:
                do_.play()
                fenetre.blit(clavier_do2, (580,225))
                pygame.display.flip()
            if event.key == K_r:
                re.play()
                fenetre.blit(clavier_re, (591,249))
                pygame.display.flip()
            if event.key == K_5:
                re_.play()
                fenetre.blit(clavier_re2, (601,225))
                pygame.display.flip()
            if event.key == K_t:
                mi.play()
                fenetre.blit(clavier_mi, (612,249))
                pygame.display.flip()
            if event.key == K_y:
                fa.play()
                fenetre.blit(clavier_fa, (633,249))
                pygame.display.flip()
            if event.key == K_7:
                fa_.play()
                fenetre.blit(clavier_fa2, (647,249))
                pygame.display.flip()
            if event.key == K_u:
                sol.play()
                fenetre.blit(clavier_sol, (654,249))
                pygame.display.flip()
            if event.key == K_8:
                sol_.play()
                fenetre.blit(clavier_sol2, (666,249))
                pygame.display.flip()
            if event.key == K_i:
                la.play()
                fenetre.blit(clavier_la, (675,249))
                pygame.display.flip()
            if event.key == K_9:
                la_.play()
                fenetre.blit(clavier_la2, (689,249))
                pygame.display.flip()
            if event.key == K_o:
                si.play()
                fenetre.blit(clavier_si, (696,249))
                pygame.display.flip()
            if event.key == K_p:
                do2.play()
                fenetre.blit(clavier_do_2, (715,249))
                pygame.display.flip()

        # Lorsque l'on n'appuie sur aucune touche, remet l'image
        # du clavier à son état initial
                
        if event.type == KEYUP:
            fenetre.blit(clavier_init, (400,200))
            pygame.display.flip()

# Instruction permettant au programme de se fermer correctement
            
pygame.quit()
