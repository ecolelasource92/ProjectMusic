import pygame
from pygame.locals import *

pygame.init

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

# Initialisation des notes de musique

do = pygame.mixer.Sound("piano/1-do(c1).wav")
do_ = pygame.mixer.Sound("piano/2-do#(c1s).wav")
re = pygame.mixer.Sound("piano/3-re(d1).wav")
re_ = pygame.mixer.Sound("piano/4-re#(d1s).wav")
mi = pygame.mixer.Sound("piano/5-mi(e1).wav")
fa = pygame.mixer.Sound("piano/6-fa(f1).wav")
fa_ = pygame.mixer.Sound("piano/7-fa#(f1s).wav")
sol = pygame.mixer.Sound("piano/8-sol(g1).wav")
sol_ = pygame.mixer.Sound("piano/9-sol#(g1s).wav")
la = pygame.mixer.Sound("piano/10-la(a1).wav")
la_ = pygame.mixer.Sound("piano/11-la#(a1s).wav")
si = pygame.mixer.Sound("piano/12-si(b1).wav")
do2 = pygame.mixer.Sound("piano/13-do2(c2).wav")
