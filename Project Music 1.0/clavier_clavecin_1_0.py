# Importation des modules de Pygame

import pygame
from pygame.locals import *

# Initialisation des modules de Pygame

pygame.init()

# Importation des constantes

from constantes_1_0 import *

# Modification de la variable instrument (permet de stabiliser le programme)

instrument = 2

# Création de la fonction permettant de jouer du clavecin

def claveçin_mod():

    # Instructions permettant à la fonction d'accéder aux variables

    global infinite
    global instrument
    global mode

    # Chargement des évènements de Pygame

    for event in pygame.event.get():

        # Instructions permettant au programme de se fermer correctement

        if event.type == QUIT:
            infinite = 0

        # Instructions permettant de jouer la note adéquate et de l'afficher sur le clavier

        if event.type == KEYDOWN:
            
                if event.key == K_e:
                    c_do.play()
                    fenetre.blit(clavier_do, (569,249))
                    pygame.display.flip()
                    
                if event.key == K_4:
                    c_do_.play()
                    fenetre.blit(clavier_do2, (580,225))
                    pygame.display.flip()
                    
                if event.key == K_r:
                    c_re.play()
                    fenetre.blit(clavier_re, (591,249))
                    pygame.display.flip()
                    
                if event.key == K_5:
                    c_re_.play()
                    fenetre.blit(clavier_re2, (601,225))
                    pygame.display.flip()
                    
                if event.key == K_t:
                    c_mi.play()
                    fenetre.blit(clavier_mi, (612,249))
                    pygame.display.flip()
                    
                if event.key == K_y:
                    c_fa.play()
                    fenetre.blit(clavier_fa, (633,249))
                    pygame.display.flip()
                    
                if event.key == K_7:
                    c_fa_.play()
                    fenetre.blit(clavier_fa2, (647,249))
                    pygame.display.flip()
                    
                if event.key == K_u:
                    c_sol.play()
                    fenetre.blit(clavier_sol, (654,249))
                    pygame.display.flip()
                    
                if event.key == K_8:
                    c_sol_.play()
                    fenetre.blit(clavier_sol2, (666,249))
                    pygame.display.flip()
                    
                if event.key == K_i:
                    c_la.play()
                    fenetre.blit(clavier_la, (675,249))
                    pygame.display.flip()
                    
                if event.key == K_9:
                    c_la_.play()
                    fenetre.blit(clavier_la2, (689,249))
                    pygame.display.flip()
                    
                if event.key == K_o:
                    c_si.play()
                    fenetre.blit(clavier_si, (696,249))
                    pygame.display.flip()
                    
                if event.key == K_p:
                    c_do2.play()
                    fenetre.blit(clavier_do_2, (715,249))
                    pygame.display.flip()

        # Instructions permettant de remettre le clavier à l'état initial                    

        if event.type == KEYUP:
            fenetre.blit(clavier_init, (400,200))
            pygame.display.flip()

        if event.type == MOUSEBUTTONDOWN :

            # Changement de mode lorsque l'on clique dans les zones adéquates
                
            if event.button == 1 and 7 <= event.pos[0] <= 233 and 7 <= event.pos[1] <= 109:
                mode = 0
                
            if event.button == 1 and 240 <= event.pos[0] <= 472 and 7 <= event.pos[1] <= 109:
                mode = 1
                
            if event.button == 1 and 479 <= event.pos[0] <= 703 and 7 <= event.pos[1] <= 109:
                mode = 2
                
            # Changement d'instrument lorsque l'on clique dans les zones adéquates

            if event.button == 1 and 997 <= event.pos[0] <= 1171 and 157 <= event.pos[1] <= 262:
                instrument = 0
                
            if event.button == 1 and 997 <= event.pos[0] <= 1171 and 269 <= event.pos[1] <= 384:
                instrument = 1
                
            if event.button == 1 and 997 <= event.pos[0] <= 1171 and 391 <= event.pos[1] <= 510:
                instrument = 2

    # Exportation des variables sous forme de tableau

    return ([infinite, instrument, mode])
