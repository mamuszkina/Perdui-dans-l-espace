import pygame

import config
from game_state import GameState
from game_state import grayscale


class panneau18:
    def __init__(self, screen, game, player):
        self.screen = screen
        self.game = game
        self.player = player
        #Dialogue adapté taille écran
        self.dialog = pygame.image.load("imgs/dialog.png").convert_alpha()
        self.dialog = pygame.transform.scale(self.dialog, (config.SCREEN_WIDTH//3.5, config.SCREEN_HEIGHT//4.5))
        self.dialogPNJ = pygame.transform.flip(self.dialog, True, False).convert_alpha()
        self.dialogPNJ = pygame.transform.scale(self.dialogPNJ, (config.SCREEN_WIDTH//3.5, config.SCREEN_HEIGHT//4.5))

        self.dialogPanneau = pygame.image.load("imgs/monde5/dessin.png").convert_alpha()
        self.dialogPanneau = pygame.transform.scale(self.dialogPanneau, (config.SCREEN_WIDTH//2, config.SCREEN_HEIGHT//2))

        #Perso adaptés taille écran
        self.charlie = pygame.image.load("imgs/characters/charlie.png").convert_alpha()
        self.charlie = pygame.transform.scale(self.charlie, (config.SCREEN_WIDTH //5, config.SCREEN_HEIGHT //1.1))
        self.charlie_gray = grayscale(self.charlie)
        self.PNJ = pygame.image.load("imgs/characters/gandalf.png").convert_alpha()
        self.PNJ = pygame.transform.flip(self.PNJ, True, False)
        self.PNJ = pygame.transform.scale(self.PNJ, (config.SCREEN_WIDTH//5, config.SCREEN_HEIGHT//1.1))
        self.PNJ_gray = grayscale(self.PNJ)

        self.cut = 0
        self.max_cut = 7

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
        if self.cut == 6:
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
        if self.game.compris == True and self.cut == 3:
            self.cut = 5

        if self.game.go_gandalf == True and self.game.Gandalf5_dialogue_done == False and self.cut == 1:
            self.game.event = None

        if self.game.Gandalf5_dialogue_done == False and self.cut == 1:
            self.cut = 7
            
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
    def _render_dialogue_box_Gandalf(self, text):
        dialogue_rect = self.screen.blit(self.dialogPNJ, (config.SCREEN_WIDTH // 2.8, config.SCREEN_HEIGHT // 1.4))      # chiffres = position bulle de dialogue
        self.screen.blit(self.charlie_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        self.screen.blit(self.PNJ, (config.SCREEN_WIDTH // 6, config.SCREEN_HEIGHT * 0.5))

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
        y = dialogue_rect.y + 40                                      # 30 = décalage avec le haut

        for line in wrapped:
            if chars_left <= 0:
                break
            visible = line[:chars_left]
            surf = font.render(visible, True, color)
            self.screen.blit(surf, (dialogue_rect.x + 30, y))         # chiffre, y = décalage début de bulle
            chars_left -= len(line) + 1
            y += font.get_height() + 6 
            
    def _render_dialogue_box_Answer(self, text):
        dialogue_rect = self.screen.blit(self.dialog, (config.SCREEN_WIDTH // 2.8, config.SCREEN_HEIGHT // 1.4))      # chiffres = position bulle de dialogue
        self.screen.blit(self.charlie, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        self.screen.blit(self.PNJ_gray, (config.SCREEN_WIDTH // 6, config.SCREEN_HEIGHT * 0.5))

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
        y = dialogue_rect.y + 40

        for line in wrapped:
            if chars_left <= 0:
                break
            visible = line[:chars_left]
            surf = font.render(visible, True, color)
            self.screen.blit(surf, (dialogue_rect.x + 30, y))         # chiffre, y = décalage début de bulle
            chars_left -= len(line) + 1
            y += font.get_height() + 6  

    def _render_dialogue_box_Answer_no_Gandalf(self, text):
        dialogue_rect = self.screen.blit(self.dialog, (config.SCREEN_WIDTH // 2.8, config.SCREEN_HEIGHT // 1.4))      # chiffres = position bulle de dialogue
        self.screen.blit(self.charlie, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

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
        y = dialogue_rect.y + 40

        for line in wrapped:
            if chars_left <= 0:
                break
            visible = line[:chars_left]
            surf = font.render(visible, True, color)
            self.screen.blit(surf, (dialogue_rect.x + 30, y))         # chiffre, y = décalage début de bulle
            chars_left -= len(line) + 1
            y += font.get_height() + 6  

    def _render_dialogue_box_panneau(self, text):
        dialogue_rect = self.screen.blit(self.dialogPanneau, (config.SCREEN_WIDTH // 4, config.SCREEN_HEIGHT // 4))      # chiffres = position bulle de dialogue

        color = config.BLACK

        max_width = dialogue_rect.width - dialogue_rect.width//4
        max_height = dialogue_rect.height - dialogue_rect.height//2

        font, wrapped = self.get_fitting_font(
            text=text,
            font_path="fonts/elfique.ttf",
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

    def _render_dialogue_box_static(self, text):
        dialogue_rect = self.screen.blit(
            self.dialogPanneau,
            (config.SCREEN_WIDTH // 4, config.SCREEN_HEIGHT // 4)
        )

        color = config.BLACK

        max_width = dialogue_rect.width - dialogue_rect.width // 4
        max_height = dialogue_rect.height - dialogue_rect.height // 2

        font, wrapped = self.get_fitting_font(
            text=text,
            font_path="fonts/elfique.ttf",
            max_width=max_width,
            max_height=max_height,
            start_size=30,
            min_size=12
        )

        y = dialogue_rect.y + 120

        for line in wrapped:
            surf = font.render(line, True, color)
            x_offset = config.SCREEN_WIDTH // 13
            self.screen.blit(surf, (dialogue_rect.x + x_offset, y))
            y += font.get_height() + 6
            
            
    def render_scene_0(self):
        self._render_dialogue_box_panneau("Expression du jour : verser des ç-larmes de é-crocodile.")

    def render_scene_1(self):
        self._render_dialogue_box_static("Expression du jour : verser des ç-larmes de é-crocodile.")
        self._render_dialogue_box_Answer("Gandalf ? Tu peux traduire ?")
        
    def render_scene_2(self):
        self._render_dialogue_box_static("Expression du jour : verser des ç-larmes de é-crocodile.")
        self._render_dialogue_box_Gandalf("Mhhh ça dit à peu près 'Expression du jour : verser des ç-larmes de é-crocodile.'")
        
    def render_scene_3(self):
        self._render_dialogue_box_static("Expression du jour : verser des ç-larmes de é-crocodile.")
        self._render_dialogue_box_Answer("é-crocodyle ? ç-larme ? Tu es sûr de toi ?")
        
    def render_scene_4(self):
        self._render_dialogue_box_static("Expression du jour : verser des ç-larmes de é-crocodile.")
        self._render_dialogue_box_Gandalf("Oui. Le é- et le ç- ne se traduisent pas dans ta langue, mais je n'ai pas fait d'erreurs.")
        self.game.compris = True
        
    def render_scene_5(self):
        self._render_dialogue_box_static("Expression du jour : verser des ç-larmes de é-crocodile.")
        self._render_dialogue_box_Answer("On va pouvoir ajouter cette information au panneau d'affichage.")
        self.game.croccodile = True
        self.game.larmes = True

    def render_scene_6(self):
        self._render_dialogue_box_Answer("")

    def render_scene_7(self):
        self._render_dialogue_box_static("Expression du jour : verser des ç-larmes de é-crocodile.")
        self._render_dialogue_box_Answer_no_Gandalf("Evidemment, je comprend strictement rien. Super. Bon, j'ai plus qu'à aller voir Gandalf. Comme d'habitude...")
        self.game.go_gandalf = True