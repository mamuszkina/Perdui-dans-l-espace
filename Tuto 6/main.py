import pygame
import config
import sys
from game_state import GameState
from game import Game
from menu import Menu
from game_view.map import Map

pygame.init()

def running_in_browser() -> bool:
    # pygbag/emscripten builds usually run on platform "emscripten"
    return sys.platform == "emscripten"

if running_in_browser():
    # Web (pygbag): fixed logical resolution, scaled to the browser canvas.
    # Avoid RESIZABLE (often problematic in pygbag).
    screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT), pygame.SCALED)
else:
    # Desktop: true fullscreen at monitor resolution
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    config.SCREEN_WIDTH, config.SCREEN_HEIGHT = screen.get_size()

pygame.mixer.init()

#pygame.mixer.music.load("a_druidesa.mp3")
#pygame.mixer.music.set_volume(60)                       #Monter le son : +X 
#pygame.mixer.music.play(-1)


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