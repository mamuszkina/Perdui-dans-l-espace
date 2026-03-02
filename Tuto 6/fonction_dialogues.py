import pygame
import config
from game_state import GameState
from game import Game
from menu import Menu
from game_view.map import Map

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load("a_druidesa.mp3")
pygame.mixer.music.set_volume(60)                       #Monter le son : +X 
pygame.mixer.music.play(-1)

FLAGS = pygame.SCALED | pygame.RESIZABLE
screen = pygame.display.set_mode(
    (config.SCREEN_WIDTH, config.SCREEN_HEIGHT),
    FLAGS
)

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