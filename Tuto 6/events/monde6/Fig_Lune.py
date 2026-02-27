import pygame

import config
from game_state import GameState


class Fig_Lune:
    def __init__(self, screen, game, player):
        self.screen = screen
        self.game = game
        self.player = player
        self.dialog = pygame.image.load("imgs/dialog2.png").convert_alpha()
        self.dialog = pygame.transform.scale(self.dialog, (config.SCREEN_WIDTH//3.5, config.SCREEN_HEIGHT//4.5))
        self.figurine = pygame.image.load("imgs/monde6/lune.png").convert_alpha()
        self.figurine = pygame.transform.scale(self.figurine, (config.SCREEN_WIDTH//6, config.SCREEN_HEIGHT//5))

        self.cut = 0
        self.max_cut = 4

        # Typewriter state when creating the PNJ
        self.char_delay_ms = 30                     # 1= très rapide ; 100= très lent
        self.current_char = 0
        self.last_update = 0
        # Nombre total de caractères du texte courant (après "wrap")
        self.current_dialogue_total_chars = 0


    def load(self):
        self.current_char = 0
        self.last_update = pygame.time.get_ticks()

  
    def update(self):
        if self.cut == 1:
            self.game.event = None
        elif self.cut == 3:
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

                # --- Dialogue normal : Entrée avance les cases ---
                elif event.key == pygame.K_RETURN:
                    if self.current_char < self.current_dialogue_total_chars:
                        self.current_char = self.current_dialogue_total_chars
                    else:
                        self.cut += 1
                        self.current_char = 0
                        self.last_update = pygame.time.get_ticks()

        # Mise à jour du texte "machine à écrire"
        now = pygame.time.get_ticks()
        if now - self.last_update > self.char_delay_ms:
            self.current_char += 1
            self.last_update = now

    
    def render(self):
        if self.game.portier6 == True and self.game.Fig_Lune == False and self.cut <2:
            self.cut = 2

        if self.game.Fig_Lune == True and self.cut == 0:
            self.cut = 4
            
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
        self._render_dialogue_box("C'est une figurine de lune. Quelqu'un a dû la faire tomber.")
        self.screen.blit(self.figurine, (config.SCREEN_WIDTH//4, config.SCREEN_HEIGHT//2))

    def render_scene_1(self):
        self._render_dialogue_box("")
        
    def render_scene_2(self):
        self._render_dialogue_box("ça doit être une des six figurines du portier. Je ferais mieux de la ramasser.")
        self.screen.blit(self.figurine, (config.SCREEN_WIDTH//4, config.SCREEN_HEIGHT//2))
        self.game.Fig_Lune = True

    def render_scene_3(self):
        self._render_dialogue_box("")

    def render_scene_4(self):
        self._render_dialogue_box("C'est ici que j'ai trouvé la figurine de la lune.")
        
