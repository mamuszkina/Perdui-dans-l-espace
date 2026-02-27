import pygame

import config
from game_state import GameState
from time import sleep


class PNJ3:
    def __init__(self, screen, game, player):
        self.screen = screen
        self.game = game
        self.prof_image= pygame.image.load("imgs/prof2.png")                        #Pas utile à priori
        self.dialog = pygame.image.load("imgs/dialog.png")

        self.cut = 0
        self.max_cut = 6

    def load(self):
        pass

    def render(self):
        if self.cut == 0:
            self.render_scene_0()
        elif self.cut == 1:
            self.render_scene_1()
        elif self.cut == 2:
            self.render_scene_2()
        elif self.cut == 3:
            self.render_scene_3()
        elif self.cut == 4:
            self.render_scene_4()
        elif self.cut == 5:
            self.render_scene_5()
        elif self.cut == 6:
            self.render_scene_6()

    def render_scene_0(self):
        self.screen.blit(self.dialog, (0, 300))
        font = pygame.font.Font('fonts/PokemonGb.ttf', 20)
        img = font.render("...", True, config.BLUE)
        self.screen.blit(img, (40, 330))
        pass

    def render_scene_1(self):
        self.screen.blit(self.dialog, (0, 300))
        font = pygame.font.Font('fonts/PokemonGbAnswer.ttf', 20)
        img = font.render("[Partir] = (o)", True, config.BLUE)
        self.screen.blit(img, (40, 370))
        img = font.render("[Rester] = (n)", True, config.BLUE)
        self.screen.blit(img, (40, 420))
        pass

    def render_scene_2(self):
        self.screen.blit(self.dialog, (0, 300))
        font = pygame.font.Font('fonts/PokemonGb.ttf', 20)
        img = font.render("", True, config.BLUE)
        self.screen.blit(img, (40, 400))
        pass

    def render_scene_3(self):
        self.screen.blit(self.dialog, (0, 300))
        font = pygame.font.Font('fonts/PokemonGb.ttf', 20)
        img = font.render("...", True, config.BLUE)
        self.screen.blit(img, (40, 400))
        pass

    def render_scene_4(self):
        self.screen.blit(self.dialog, (0, 300))
        font = pygame.font.Font('fonts/PokemonGbAnswer.ttf', 20)
        img = font.render("[Partir] = (o)", True, config.BLUE)
        self.screen.blit(img, (40, 370))
        img = font.render("[Rester] = (n)", True, config.BLUE)
        self.screen.blit(img, (40, 420))
        pass

    def render_scene_5(self):
        self.screen.blit(self.dialog, (0, 300))
        font = pygame.font.Font('fonts/PokemonGb.ttf', 20)
        img = font.render("", True, config.BLUE)
        self.screen.blit(img, (40, 400))
        pass

    def render_scene_6(self):
        self.screen.blit(self.dialog, (0, 300))
        font = pygame.font.Font('fonts/PokemonGb.ttf', 20)
        img = font.render("...Bonjour...", True, config.BLUE)
        self.screen.blit(img, (40, 400))
        pass

    def update(self):
        if self.cut > self.max_cut:
            self.game.event = None
        elif self.cut == 2:                             #intégrer un choix multiple 
            self.game.event = None
        elif self.cut == 5:
            self.game.event = None

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.game_state = GameState.ENDED
            #     handle key events
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game.game_state = GameState.ENDED
                elif event.key == pygame.K_o:
                    self.cut = self.cut + 1
                elif event.key == pygame.K_n:
                    self.cut = self.cut + 2
                if event.key == pygame.K_RETURN:
                    self.cut = self.cut + 1
