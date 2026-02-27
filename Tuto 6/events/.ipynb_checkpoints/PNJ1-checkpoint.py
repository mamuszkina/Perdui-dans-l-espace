import pygame

import config
from game_state import GameState

pygame.mixer.init()

class PNJ1:
    def __init__(self, screen, game, player):
        self.screen = screen
        self.game = game
        self.player = player
        self.prof_image = pygame.image.load("imgs/prof.png")
        self.dialog = pygame.image.load("imgs/dialog.png")
        self.ECLAIR_BLANC = pygame.image.load("imgs/ECLAIR_BLANC.jpg")

        self.cut = 0
        self.max_cut = 4
        self.has_teleported = False # added a teleport flag

        # Typewriter state when creating the PNJ
        self.char_delay_ms = 30                       # 1= très rapide ; 100= très lent
        self.current_char = 0
        self.last_update = 0
    
    def load(self):
        self.current_char = 0
        self.last_update = pygame.time.get_ticks()
    
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
            
        if self.cut > self.max_cut:
            self.game.event = None
            return

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.game_state = GameState.ENDED

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game.game_state = GameState.ENDED

                elif event.key == pygame.K_RETURN:
                    self.cut += 1
                    self.current_char = 0
                    self.last_update = pygame.time.get_ticks()

        now = pygame.time.get_ticks() # mise à jour du texte
        if now - self.last_update > self.char_delay_ms:
            self.current_char += 1
            self.last_update = now
    
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

    @staticmethod   # to avoid that the following function reads self automatically
    def wrap_text(text, font, max_width):
        words = text.split()
        lines = []
        current = ""

        for word in words:
            test = (current + " " + word).strip()
            if font.size(test)[0] <= max_width:
                current = test
            else:
                if current:
                    lines.append(current)
                current = word

        if current:
            lines.append(current)
        return lines

    # create a function for dialogue box
    def _render_dialogue_box(self, text):
        dialogue_rect = self.screen.blit(self.dialog, (0, 450))      # chiffres = position bulle de dialogue

        font = pygame.font.Font("fonts/PokemonGb.ttf", 20)           #20 = taille des lettres
        color = config.BLUE

        wrapped = self.wrap_text(text, font, dialogue_rect.width - 60)

        chars_left = self.current_char
        y = dialogue_rect.y + 30                                      # 30 = décalage avec le haut

        for line in wrapped:
            if chars_left <= 0:
                break
            visible = line[:chars_left]
            surf = font.render(visible, True, color)
            self.screen.blit(surf, (dialogue_rect.x + 30, y))         # chiffre, y = décalage début de bulle
            chars_left -= len(line) + 1
            y += font.get_height() + 6 

    def _render_dialogue_box_Lightning(self, text):
        dialogue_rect = self.screen.blit(self.ECLAIR_BLANC, (0, 0))      # chiffres = position bulle de dialogue

        font = pygame.font.Font("fonts/Lightning.ttf", 250)           #20 = taille des lettres
        color = config.YELLOW

        wrapped = self.wrap_text(text, font, dialogue_rect.width - 20)

        chars_left = self.current_char
        y = dialogue_rect.y + 60                                      # 30 = décalage avec le haut

        for line in wrapped:
            if chars_left <= 0:
                break
            visible = line[:chars_left]
            surf = font.render(visible, True, color)
            self.screen.blit(surf, (dialogue_rect.x + 30, y))         # chiffre, y = décalage début de bulle
            chars_left -= len(line) + 1
            y += font.get_height() + 6

    def _render_dialogue_box_Answer(self, text):
        dialogue_rect = self.screen.blit(self.dialog, (0, 450))      # chiffres = position bulle de dialogue

        font = pygame.font.Font("fonts/PokemonGbAnswer.ttf", 20)           #20 = taille des lettres
        color = config.BLACK

        wrapped = self.wrap_text(text, font, dialogue_rect.width - 20)

        chars_left = self.current_char
        y = dialogue_rect.y + 30                                      # 30 = décalage avec le haut

        for line in wrapped:
            if chars_left <= 0:
                break
            visible = line[:chars_left]
            surf = font.render(visible, True, color)
            self.screen.blit(surf, (dialogue_rect.x + 30, y))         # chiffre, y = décalage début de bulle
            chars_left -= len(line) + 1
            y += font.get_height() + 6
            
    def render_scene_0(self):
        self._render_dialogue_box("Bonjour Charlie !")

    def render_scene_1(self):
        self._render_dialogue_box("Vous venez acheter votre pain et votre éclair au chocolat, comme d’habitude ?")

    def render_scene_2(self):
        self._render_dialogue_box("Attendez, je vous prépare ça")

    def render_scene_3(self):
        self._render_dialogue_box_Lightning("KABOOM")

    def render_scene_4(self):
        self._render_dialogue_box_Answer("Mais c'est quoi ça ??!")


