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
        self.max_cut = 13

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
        elif self.cut == 7:
            self.render_scene_7()
        elif self.cut == 8:
            self.render_scene_8()
        elif self.cut == 9:
            self.render_scene_9()
        elif self.cut == 10:
            self.render_scene_10()
        elif self.cut == 11:
            self.render_scene_11()
        elif self.cut == 12:
            self.render_scene_12()
        elif self.cut == 13:
            self.render_scene_13()

    def render_scene_0(self):
        self.screen.blit(self.dialog, (0, 300))
        font = pygame.font.Font('fonts/PokemonGb.ttf', 20)
        img = font.render("...", True, config.BLUE)
        self.screen.blit(img, (40, 330))
        pass

    def render_scene_1(self):
        self.screen.blit(self.dialog, (0, 300))
        font = pygame.font.Font('fonts/PokemonGbAnswer.ttf', 20)
        img = font.render("[Monsieur ?] = (o)", True, config.BLUE)
        self.screen.blit(img, (40, 370))
        img = font.render("[Hé, dites, vous avez vu ça ?] = (n)", True, config.BLUE)
        self.screen.blit(img, (40, 420))
        pass

    def render_scene_2(self):
        self.screen.blit(self.dialog, (0, 300))
        font = pygame.font.Font('fonts/PokemonGb.ttf', 20)
        img = font.render("...", True, config.BLUE)
        self.screen.blit(img, (40, 400))
        pass

    def render_scene_3(self):
        self.screen.blit(self.dialog, (0, 300))
        font = pygame.font.Font('fonts/PokemonGb.ttf', 20)
        img = font.render("Oui...", True, config.BLUE)
        self.screen.blit(img, (40, 400))
        pass

    def render_scene_4(self):
        self.screen.blit(self.dialog, (0, 300))
        font = pygame.font.Font('fonts/PokemonGbAnswer.ttf', 20)
        img = font.render("[Ne pas insister] = (n)", True, config.BLUE)
        self.screen.blit(img, (40, 370))
        img = font.render("[Insister] = (o)", True, config.BLUE)
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
        img = font.render("...Je ne comprend pas ce que vous voulez...", True, config.BLUE)
        self.screen.blit(img, (40, 400))
        pass

    def render_scene_7(self):
        self.screen.blit(self.dialog, (0, 300))
        font = pygame.font.Font('fonts/PokemonGbAnswer.ttf', 20)
        img = font.render("Vous n’avez pas vu cet éclair blanc ? Et ce boom énorme qui a fendu le ciel ?", True, config.BLUE)
        self.screen.blit(img, (40, 400))
        pass

    def render_scene_8(self):
        self.screen.blit(self.dialog, (0, 300))
        font = pygame.font.Font('fonts/PokemonGb.ttf', 20)
        img = font.render("Rien du tout… Mais j’étais dans la lune… Peut-être que quelqu’uni d’autre a vu quelque chose...", True, config.BLUE)
        self.screen.blit(img, (40, 400))
        pass

    def render_scene_9(self):
        self.screen.blit(self.dialog, (0, 300))
        font = pygame.font.Font('fonts/PokemonGbAnswer.ttf', 20)
        img = font.render("[Hein ? Euh, oui oui, je vais aller voir...] = (n)", True, config.BLUE)
        self.screen.blit(img, (40, 370))
        img = font.render("[De quoi ?] = (o)", True, config.BLUE)
        self.screen.blit(img, (40, 420))
        pass

    def render_scene_10(self):
        self.screen.blit(self.dialog, (0, 300))
        font = pygame.font.Font('fonts/PokemonGb.ttf', 20)
        img = font.render("", True, config.BLUE)
        self.screen.blit(img, (40, 400))
        pass

    def render_scene_11(self):
        self.screen.blit(self.dialog, (0, 300))
        font = pygame.font.Font('fonts/PokemonGbAnswer.ttf', 20)
        img = font.render("Je disais que si ça se trouve, li humaini là-bas a vu quelque chose…", True, config.BLUE)
        self.screen.blit(img, (40, 400))
        pass

    def render_scene_12(self):
        self.screen.blit(self.dialog, (0, 300))
        font = pygame.font.Font('fonts/PokemonGbAnswer.ttf', 20)
        img = font.render("Hein, euh, oui, oui, merci...", True, config.BLUE)
        self.screen.blit(img, (40, 400))
        pass

    def render_scene_13(self):
        self.screen.blit(self.dialog, (0, 300))
        font = pygame.font.Font('fonts/PokemonGbAnswer.ttf', 20)
        img = font.render("Il parle super bizarrement ce monsieur, mais qu’est-ce qu’il se passe ici…", True, config.BLUE)
        self.screen.blit(img, (40, 400))
        pass
    
    def update(self):
        if self.cut > self.max_cut:
            self.game.event = None
        elif self.cut == 5:
            self.game.event = None
        elif self.cut == 10:
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
