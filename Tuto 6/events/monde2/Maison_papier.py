import pygame

import config
from game_state import GameState


class Maison_papier:
    def __init__(self, screen, game, player):
        self.screen = screen
        self.game = game
        self.player = player

        self.dialog = pygame.image.load("imgs/dialog2.png").convert_alpha()
        self.dialog = pygame.transform.scale(self.dialog, (config.SCREEN_WIDTH//3.5, config.SCREEN_HEIGHT//4.5))
        self.paper = pygame.image.load("imgs/paper.png").convert_alpha()
        self.paper = pygame.transform.scale(self.paper, (config.SCREEN_WIDTH//2, config.SCREEN_HEIGHT//3))

#NE PAS OUBLIER DE CHANGER LE NOMBRE DE MAX CUTS
        self.cut = 0
        self.max_cut = 6

        # Typewriter state when creating the PNJ
        self.char_delay_ms = 30                       # 1= très rapide ; 100= très lent
        self.current_char = 0
        self.last_update = 0
        self.current_dialogue_total_chars = 0
    
    def load(self):
        self.current_char = 0
        self.last_update = pygame.time.get_ticks()

    def update(self):
        if self.cut == 1:
            self.game.event = None
        elif self.cut == 5:
            self.game.event = None
        elif self.cut > self.max_cut:
            self.game.event = None
            return

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.game_state = GameState.ENDED

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game.game_state = GameState.ENDED

                elif event.key == pygame.K_RETURN:
                    # 1er ENTER : finir d'afficher le texte
                    if self.current_char < self.current_dialogue_total_chars:
                        self.current_char = self.current_dialogue_total_chars
                    # 2e ENTER : passer à la case suivante
                    else:
                        self.cut += 1
                        self.current_char = 0
                        self.last_update = pygame.time.get_ticks()

        now = pygame.time.get_ticks() # mise à jour du texte
        if now - self.last_update > self.char_delay_ms:
            self.current_char += 1
            self.last_update = now

    def render(self):

        if  self.game.PNJ9_dialogue_done == True and self.game.Maison_papier_dialogue_done == False and self.cut < 2:
            self.cut = 2
            return

        if self.game.Maison_papier_dialogue_done == True and self.cut < 6:
            self.cut = 6
            return

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

    # fonction pour la taille de caractère
    def get_fitting_font(self, text, font_path, max_width, max_height,
                     start_size=20, min_size=12, line_spacing=6):

        for size in range(start_size, min_size - 1, -1):
            font = pygame.font.Font(font_path, size)
            wrapped = self.wrap_text(text, font, max_width)

            total_height = len(wrapped) * (font.get_height() + line_spacing)

            if total_height <= max_height:
                return font, wrapped

        # fallback : taille minimale
        font = pygame.font.Font(font_path, min_size)
        wrapped = self.wrap_text(text, font, max_width)
        return font, wrapped

    # create a function for dialogue box
    def _render_dialogue_box(self, text):
        dialogue_rect = self.screen.blit(self.dialog, (config.SCREEN_WIDTH // 2.8, config.SCREEN_HEIGHT // 1.4))

        font = pygame.font.Font("fonts/PokemonGb.ttf", 20)           #20 = taille des lettres
        color = config.BLACK

        max_width = dialogue_rect.width - 60
        max_height = dialogue_rect.height - 60

        font, wrapped = self.get_fitting_font(
            text=text,
            font_path="fonts/PokemonGb.ttf",
            max_width=max_width,
            max_height=max_height,
            start_size=20,
            min_size=12
        )
        self.current_dialogue_total_chars = sum(len(line) + 1 for line in wrapped)

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
        self._render_dialogue_box ("Il y a vraiment plein de choses sur cette table. Des stylos, des pommes croquées, des bouts de bois,...")

    def render_scene_1(self):
        self._render_dialogue_box ("")

    def render_scene_2(self):
        self._render_dialogue_box ("Cordelia n'avait pas menti, c'est un sacré bordel. Il n'y a pas de clef ici mais un mot :")

    def render_scene_3(self):
        self.screen.blit(self.paper, (config.SCREEN_WIDTH//4, config.SCREEN_HEIGHT//3))
        font = pygame.font.Font('fonts/enfant.ttf', 40)
        img1 = font.render("Coucou voisan ! Comme tu etais", True, config.BLACK,)
        img2 = font.render("pas la je suis venux te prandre", True, config.BLACK)
        img3 = font.render("la clef du labo, si jamais tu", True, config.BLACK)
        img4 = font.render("en as besoin viens la récupéré !", True, config.BLACK)
        img5 = font.render("Bisous !", True, config.BLACK)
        self.screen.blit(img1, (config.SCREEN_WIDTH//3.8, config.SCREEN_HEIGHT//2.8))
        self.screen.blit(img2, (config.SCREEN_WIDTH//3.4, config.SCREEN_HEIGHT//2.4))
        self.screen.blit(img3, (config.SCREEN_WIDTH//3.25, config.SCREEN_HEIGHT//2.1))
        self.screen.blit(img4, (config.SCREEN_WIDTH//3, config.SCREEN_HEIGHT//2))
        self.screen.blit(img5, (config.SCREEN_WIDTH//2.7, config.SCREEN_HEIGHT//1.8))
        self.game.unlock_pokedex_entry(2, "Maison_papier")

    def render_scene_4(self):
        self._render_dialogue_box("Evidemment, la personne qui a mis ce mot n'a pas pensé à signer...")

    def render_scene_5(self):
        self._render_dialogue_box("")
        self.game.Maison_papier_dialogue_done = True

    def render_scene_6(self):
        self._render_dialogue_box("Il n'y a plus rien d'intéressant sur cette table.")
