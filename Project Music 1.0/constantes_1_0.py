# Importation des modules de Pygame

import pygame
from pygame.locals import *

# Initialisation des modules de Pygame

pygame.init

# Mise en place des paramètres composants de la fenêtre

fenetre = pygame.display.set_mode((1280, 768))
pygame.display.set_caption("Project Music")

# Mise en place des constantes principales du programme

infinite = 1
instrument = 0
mode = 0

# Initialisation interface

mode_libre = pygame.image.load("interface/mode_1.png").convert_alpha()
mode_lecture = pygame.image.load("interface/mode_2.png").convert_alpha()
mode_partition = pygame.image.load("interface/mode_3.png").convert_alpha()
interface_instrument_p = pygame.image.load("interface/Interface_instrument_1.png").convert_alpha()
interface_instrument_o = pygame.image.load("interface/Interface_instrument_2.png").convert_alpha()
interface_instrument_c = pygame.image.load("interface/Interface_instrument_3.png").convert_alpha()
fond = pygame.image.load("interface/Fond.png").convert_alpha()
partitions = pygame.image.load("interface/emplacements.png")

# Initialisation des images composant le clavier

clavier_init = pygame.image.load("clavier/clavier_init.jpg").convert_alpha()
clavier_do = pygame.image.load("clavier/do.png").convert_alpha()
clavier_do2 = pygame.image.load("clavier/do#.png").convert_alpha()
clavier_re = pygame.image.load("clavier/re.png").convert_alpha()
clavier_re2 = pygame.image.load("clavier/re#.png").convert_alpha()
clavier_mi = pygame.image.load("clavier/mi.png").convert_alpha()
clavier_fa = pygame.image.load("clavier/fa.png").convert_alpha()
clavier_fa2 = pygame.image.load("clavier/fa#.png").convert_alpha()
clavier_sol = pygame.image.load("clavier/sol.png").convert_alpha()
clavier_sol2 = pygame.image.load("clavier/sol#.png").convert_alpha()
clavier_la = pygame.image.load("clavier/la.png").convert_alpha()
clavier_la2 = pygame.image.load("clavier/la#.png").convert_alpha()
clavier_si = pygame.image.load("clavier/si.png").convert_alpha()
clavier_do_2 = pygame.image.load("clavier/do2.png").convert_alpha()

# Initialisation des notes de piano

p_do = pygame.mixer.Sound("piano/p-do.wav")
p_do_ = pygame.mixer.Sound("piano/p-do#.wav")
p_re = pygame.mixer.Sound("piano/p-re.wav")
p_re_ = pygame.mixer.Sound("piano/p-re.wav")
p_mi = pygame.mixer.Sound("piano/p-mi.wav")
p_fa = pygame.mixer.Sound("piano/p-fa.wav")
p_fa_ = pygame.mixer.Sound("piano/p-fa#.wav")
p_sol = pygame.mixer.Sound("piano/p-sol.wav")
p_sol_ = pygame.mixer.Sound("piano/p-sol#.wav")
p_la = pygame.mixer.Sound("piano/p-la.wav")
p_la_ = pygame.mixer.Sound("piano/p-la#.wav")
p_si = pygame.mixer.Sound("piano/p-si.wav")
p_do2 = pygame.mixer.Sound("piano/p-do2.wav")

# Initialisation des notes d'orgue

o_do = pygame.mixer.Sound("orgue/o-do.wav")
o_do_ = pygame.mixer.Sound("orgue/o-do#.wav")
o_re = pygame.mixer.Sound("orgue/o-re.wav")
o_re_ = pygame.mixer.Sound("orgue/o-re#.wav")
o_mi = pygame.mixer.Sound("orgue/o-mi.wav")
o_fa = pygame.mixer.Sound("orgue/o-fa.wav")
o_fa_ = pygame.mixer.Sound("orgue/o-fa#.wav")
o_sol = pygame.mixer.Sound("orgue/o-sol.wav")
o_sol_ = pygame.mixer.Sound("orgue/o-sol#.wav")
o_la = pygame.mixer.Sound("orgue/o-la.wav")
o_la_ = pygame.mixer.Sound("orgue/o-la#.wav")
o_si = pygame.mixer.Sound("orgue/o-si.wav")
o_do2 = pygame.mixer.Sound("orgue/o-do2.wav")

# Initialisation des notes de claveçin

c_do = pygame.mixer.Sound("clavecin/c-do.wav")
c_do_ = pygame.mixer.Sound("clavecin/c-do#.wav")
c_re = pygame.mixer.Sound("clavecin/c-re.wav")
c_re_ = pygame.mixer.Sound("clavecin/c-re#.wav")
c_mi = pygame.mixer.Sound("clavecin/c-mi.wav")
c_fa = pygame.mixer.Sound("clavecin/c-fa.wav")
c_fa_ = pygame.mixer.Sound("clavecin/c-fa#.wav")
c_sol = pygame.mixer.Sound("clavecin/c-sol.wav")
c_sol_ = pygame.mixer.Sound("clavecin/c-sol#.wav")
c_la = pygame.mixer.Sound("clavecin/c-la.wav")
c_la_ = pygame.mixer.Sound("clavecin/c-la#.wav")
c_si = pygame.mixer.Sound("clavecin/c-si.wav")
c_do2 = pygame.mixer.Sound("clavecin/c-do2.wav")
