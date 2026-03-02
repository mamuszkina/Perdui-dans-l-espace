import pygame
import config
from game_state import GameState
from game import Game
from menu import Menu
from game_view.map import Map

pygame.init()
pygame.mixer.init()

#pygame.mixer.music.load("a_druidesa.mp3")
#pygame.mixer.music.set_volume(60)                       #Monter le son : +X 
#pygame.mixer.music.play(-1)

#pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT)) si pas fullscreen
#CHANGER LA TAILLE DE L'ECRAN POUR UN FULLSIZE, remplacer par : screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
# IMPORTANT: si FULLSCREEN synchroniser la config avec la vraie taille de l'écran
config.SCREEN_WIDTH, config.SCREEN_HEIGHT = screen.get_size()

pygame.display.set_caption("Perdu dans l'espace")

clock = pygame.time.Clock()

game = Game(screen)

menu = Menu(screen, game)
menu.set_up()

while game.game_state != GameState.ENDED:
    clock.tick(40)

    if game.game_state == GameState.NONE:
        menu.update()

    if game.game_state == GameState.RUNNING:
        game.update()

    pygame.display.flip()