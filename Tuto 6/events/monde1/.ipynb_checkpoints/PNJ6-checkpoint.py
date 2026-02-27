import pygame

import config
from game_state import GameState


class PNJ1:
    def __init__(self, screen, game, player):
        self.screen = screen
        self.game = game
        self.prof_image = pygame.image.load("imgs/prof.png")
        self.dialog = pygame.image.load("imgs/dialog.png")
        self.ECLAIR_BLANC = pygame.image.load("imgs/ECLAIR_BLANC.png")

        self.cut = 0
        self.max_cut = 4
        self.has_teleported = False # added a teleport flag

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
            self.screen.blit(self.ECLAIR_BLANC, (0, 0))
        elif self.cut == 4:
            self.render_scene_4()

    def render_scene_0(self):
        self.screen.blit(self.dialog, (0, 300))
        font = pygame.font.Font('fonts/PokemonGb.ttf', 20)
        img = font.render("Bonjour Charlie !", True, config.BLUE)
        self.screen.blit(img, (40, 400))
        pass

    def render_scene_1(self):
        self.screen.blit(self.dialog, (0, 300))
        font = pygame.font.Font('fonts/PokemonGb.ttf', 20)
        img = font.render("Vous venez acheter votre pain", True, config.BLUE)
        self.screen.blit(img, (40, 330))                                        #position du txt (peut faire un cght ligne)
        img = font.render("et votre éclair au chocolat, comme d’habitude ?", True, config.BLUE)
        self.screen.blit(img, (40, 370))
        pass

    def render_scene_2(self):
        self.screen.blit(self.dialog, (0, 300))
        font = pygame.font.Font('fonts/PokemonGb.ttf', 20)
        img = font.render("Attendez, je vous prépare ça", True, config.BLUE)
        self.screen.blit(img, (40, 400))
        pass

    def render_scene_4(self):
        self.screen.blit(self.ECLAIR_BLANC, (0, 0))
        font = pygame.font.Font('fonts/PokemonGb.ttf', 20)
        img = font.render("Mais c'est quo ça ??!", True, config.BLUE)
        self.screen.blit(img, (40, 400))
        pass

    def update(self):
        # If we've already teleported once, do nothing
        if self.has_teleported:
            return
        if self.cut > self.max_cut:
            # The last dialog screen (render_event_4) has just been shown,
            # and the player pressed ENTER one more time.
            # -> Teleport them to overworld map "01" at a specific location if needed. If no position, it uses the default of the map set in CONFIG
            self.game.teleport_to_map("monde1", [8, 29])  # [1, 4] = entry position on map 01
            self.game.event = None
            # specify has teleported already
            self.has_teleported = True
            return

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.game_state = GameState.ENDED
            #     handle key events
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game.game_state = GameState.ENDED
                if event.key == pygame.K_RETURN:
                    self.cut = self.cut + 1


