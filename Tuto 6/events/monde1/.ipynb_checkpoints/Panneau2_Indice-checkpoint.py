import pygame

import config
from game_state import GameState
from time import sleep


class Panneau4:
    def __init__(self, screen, game, player):
        self.screen = screen
        self.game = game
        self.prof_image= pygame.image.load("imgs/panneau.png")                        #Pas utile à priori
        self.dialog = pygame.image.load("imgs/dialog.png")

        self.cut = 0
        self.max_cut = 0

    def load(self):
        pass

    def render(self):
        if self.cut == 0:
            self.render_scene_0()

    def render_scene_0(self):
        self.screen.blit(self.dialog, (0, 300))
        font = pygame.font.Font('fonts/PokemonGb.ttf', 20)
        img = font.render("OFFRE A POURVOIR :", True, config.BLUE)
        self.screen.blit(img, (40, 350))
        img = font.render("CHEFFI DE SALON DE COIFFURE RECRUTE UNI COIFFEURI", True, config.BLUE)
        self.screen.blit(img, (40, 370))
        pass

    
    def update(self):
        if self.cut > self.max_cut:
            self.game.event = None

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.game_state = GameState.ENDED
            #     handle key events
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game.game_state = GameState.ENDED
                if event.key == pygame.K_RETURN:
                    self.cut = self.cut + 1
