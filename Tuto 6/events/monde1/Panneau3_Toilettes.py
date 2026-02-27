import pygame

import config
from game_state import GameState


class Panneau3_Toilettes:
    def __init__(self, screen, game, player):
        self.screen = screen
        self.game = game
        self.player = player
        self.dialog = pygame.image.load("imgs/monde5/dessin.png").convert_alpha()
        self.dialog = pygame.transform.scale(self.dialog, (config.SCREEN_WIDTH//2, config.SCREEN_HEIGHT//2))

#NE PAS OUBLIER DE CHANGER LE NOMBRE DE MAX CUTS
        self.cut = 0
        self.max_cut = 0

        # Typewriter state when creating the PNJ
        self.char_delay_ms = 30                       # 1= très rapide ; 100= très lent
        self.current_char = 0
        self.last_update = 0
        self.current_dialogue_total_chars = 0
    
    def load(self):
        self.current_char = 0
        self.last_update = pygame.time.get_ticks()

    def update(self):
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
        if self.cut == 0:
            self.render_scene_0()

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
        dialogue_rect = self.screen.blit(self.dialog, (config.SCREEN_WIDTH // 4, config.SCREEN_HEIGHT // 4))      # chiffres = position bulle de dialogue

        color = config.BLACK

        max_width = dialogue_rect.width - dialogue_rect.width//4
        max_height = dialogue_rect.height - 60

        font, wrapped = self.get_fitting_font(
            text=text,
            font_path="fonts/panneau.ttf",
            max_width=max_width,
            max_height=max_height,
            start_size=30,
            min_size=12
        )        
        self.current_dialogue_total_chars = sum(len(line) + 1 for line in wrapped)

        chars_left = self.current_char
        y = dialogue_rect.y + 120                                      # 30 = décalage avec le haut

        for line in wrapped:
            if chars_left <= 0:
                break
            visible = line[:chars_left]
            surf = font.render(visible, True, color)
            x_offset = config.SCREEN_WIDTH // 13
            self.screen.blit(surf, (dialogue_rect.x + x_offset, y))
            chars_left -= len(line) + 1
            y += font.get_height() + 6 
    
    def render_scene_0(self):
        self._render_dialogue_box("TOILETTES PUBLIQUES POUR TOUTIS")
        self.game.unlock_pokedex_entry(1, "Panneau3")
