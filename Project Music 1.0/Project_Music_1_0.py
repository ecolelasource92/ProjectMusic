# Importation des modules de Pygame

import pygame
from pygame.locals import *

# Initialisation des modules de Pygame

pygame.init()

# Importation des constantes du programme

from constantes_1_0 import *

# Importation des fonctions composant les claviers des instruments

from clavier_piano_1_0 import *
from clavier_orgue_1_0 import *
from clavier_clavecin_1_0 import *

# Mise en place du fond et du clavier 

fenetre.blit(fond, (0,0))
fenetre.blit(clavier_init, (400,200))

pygame.display.flip()


"""

[Boucle infinie]

"""

while infinite: 

# Instructions effectuées selon l'instrument choisi

    if instrument == 0:

        # Execution de la fonction instrumentale

        piano_mod()

        # Exportation des variables de la fonction
        
        infinite_instrument_mode = piano_mod()

        # Affichage de l'instrument en cours d'utilisation
        
        fenetre.blit(interface_instrument_p, (990,150))
        pygame.display.flip()
        

    if instrument == 1:

        # Execution de la fonction instrumentale

        orgue_mod()

        # Exportation des variables de la fonction
        
        infinite_instrument_mode = orgue_mod()

        # Affichage de l'instrument en cours d'utilisation
        
        fenetre.blit(interface_instrument_o, (990,150))
        pygame.display.flip()

    if instrument == 2:

        # Execution de la fonction instrumentale

        claveçin_mod()

        # Exportation des variables de la fonction
        
        infinite_instrument_mode = claveçin_mod()

        # Affichage de l'instrument en cours d'utilisation
        
        fenetre.blit(interface_instrument_c, (990,150))       
        pygame.display.flip()

    # Conversion des variables importées sous forme de tableau en variables utilisables

    infinite = infinite_instrument_mode[0]
    instrument = infinite_instrument_mode[1]
    mode = infinite_instrument_mode[2]

# Instructions effectuées selon l'instrument choisi

    if mode == 0:

        # Affichage du mode en cours d'utilisation
        
        fenetre.blit(mode_libre, (0,0))
        pygame.display.flip

    if mode == 1:

        # Affichage du mode en cours d'utilisation

        fenetre.blit(mode_lecture, (0,0))
        pygame.display.flip

    if mode == 2:

        # Affichage du mode en cours d'utilisation

        fenetre.blit(mode_partition, (0,0))
        pygame.display.flip
    
# Instruction permettant au programme de se fermer correctement
            
pygame.quit()
