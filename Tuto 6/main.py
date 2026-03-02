import pygame
import config
import sys
from game_state import GameState
from game import Game
from menu import Menu
from game_view.map import Map

pygame.init()
pygame.mixer.init()

#pygame.mixer.music.load("a_druidesa.mp3")
#pygame.mixer.music.set_volume(60)                       #Monter le son : +X 
#pygame.mixer.music.play(-1)

if sys.platform == "emscripten":
    # Web build (pygbag)
    screen = pygame.display.set_mode(
        (config.SCREEN_WIDTH, config.SCREEN_HEIGHT),
        pygame.SCALED | pygame.RESIZABLE
    )
else:
    # Desktop: keep your preferred fullscreen behavior
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
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