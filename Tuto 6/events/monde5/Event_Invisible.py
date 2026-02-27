import pygame

import config
from game_state import GameState
from game_state import grayscale


class Event_Invisible:
    def __init__(self, screen, game, player):
        self.screen = screen
        self.game = game
        self.player = player
        #Dialogue adapté taille écran
        self.dialog = pygame.image.load("imgs/dialog.png").convert_alpha()
        self.dialog = pygame.transform.scale(self.dialog, (config.SCREEN_WIDTH//3.5, config.SCREEN_HEIGHT//4.5))
        self.dialogPNJ = pygame.transform.flip(self.dialog, True, False).convert_alpha()
        self.dialogPNJ = pygame.transform.scale(self.dialogPNJ, (config.SCREEN_WIDTH//3.5, config.SCREEN_HEIGHT//4.5))

        #Perso adaptés taille écran
        self.charlie = pygame.image.load("imgs/characters/charlie.png").convert_alpha()
        self.charlie = pygame.transform.scale(self.charlie, (config.SCREEN_WIDTH //5, config.SCREEN_HEIGHT //1.1))
        self.charlie_gray = grayscale(self.charlie)
        self.charlie_surpris = pygame.image.load("imgs/characters/C_surpris.png").convert_alpha()
        self.charlie_surpris = pygame.transform.scale(self.charlie_surpris, (config.SCREEN_WIDTH //5, config.SCREEN_HEIGHT //1.1))
        self.charlie_surpris_gray = grayscale(self.charlie_surpris)
        self.PNJ = pygame.image.load("imgs/characters/portier.png").convert_alpha()
        self.PNJ = pygame.transform.flip(self.PNJ, True, False)
        self.PNJ = pygame.transform.scale(self.PNJ, (config.SCREEN_WIDTH//5, config.SCREEN_HEIGHT//1.1))
        self.PNJ_gray = grayscale(self.PNJ)
        self.gandalf = pygame.image.load("imgs/characters/gandalf.png").convert_alpha()
        self.gandalf = pygame.transform.scale(self.gandalf, (config.SCREEN_WIDTH //5, config.SCREEN_HEIGHT //1.1))
        self.gandalf_gray = grayscale(self.gandalf)

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
        if self.cut > self.max_cut:
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

        if self.game.Event_Invisible_done == True :
            return
        
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
    def _render_dialogue_box_portier(self, text):
        dialogue_rect = self.screen.blit(self.dialogPNJ, (config.SCREEN_WIDTH // 2.8, config.SCREEN_HEIGHT // 1.4))       # chiffres = position bulle de dialogue
        self.screen.blit(self.gandalf_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        self.screen.blit(self.PNJ, (config.SCREEN_WIDTH // 6, config.SCREEN_HEIGHT * 0.5))
        

        font = pygame.font.Font("fonts/elfique.ttf", 20)           #20 = taille des lettres
        color = config.BLACK

        max_width = dialogue_rect.width - 60
        max_height = dialogue_rect.height - 60

        font, wrapped = self.get_fitting_font(
            text=text,
            font_path="fonts/elfique.ttf",
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

    def _render_dialogue_box_gandalf(self, text):
        dialogue_rect = self.screen.blit(self.dialog, (config.SCREEN_WIDTH // 2.8, config.SCREEN_HEIGHT // 1.4))      # chiffres = position bulle de dialogue
        self.screen.blit(self.gandalf, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        self.screen.blit(self.PNJ_gray, (config.SCREEN_WIDTH // 6, config.SCREEN_HEIGHT * 0.5))

        font = pygame.font.Font("fonts/elfique.ttf", 20)           #20 = taille des lettres
        color = config.BLACK

        max_width = dialogue_rect.width - 60
        max_height = dialogue_rect.height - 60

        font, wrapped = self.get_fitting_font(
            text=text,
            font_path="fonts/elfique.ttf",
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
            
    def _render_dialogue_box_Answer(self, text):
        dialogue_rect = self.screen.blit(self.dialog, (config.SCREEN_WIDTH // 2.8, config.SCREEN_HEIGHT // 1.4))      # chiffres = position bulle de dialogue

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
            
    def render_scene_0(self):
        self._render_dialogue_box_gandalf("Mais mais je te zut en fait !!")

    def render_scene_1(self):
        self._render_dialogue_box_Answer("Mais... Mais c'est Gandalf !")
        self.screen.blit(self.charlie_surpris, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_2(self):
        self._render_dialogue_box_portier("Moi aussi tiens ! Même que j'écris ce que je veux comme tu captes rien !")
        
    def render_scene_3(self):
        self._render_dialogue_box_Answer("Il a l'air de se prendre la tête avec l'homme à côté de la porte...")
        self.screen.blit(self.charlie, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        
    def render_scene_4(self):
        self._render_dialogue_box_gandalf("Mais laisse-moi passer !")
        
    def render_scene_5(self):
        self._render_dialogue_box_portier("Même pas en rêve ! Vas t'excuser auprès de ma fille !")
        
    def render_scene_6(self):
        self._render_dialogue_box_gandalf("C'est mort. J'ai pas à m'excuser, elle a qu'à apprendre à parler lol.")
        
    def render_scene_7(self):
        self._render_dialogue_box_Answer("ça a l'air de se tasser un peu. Je ferais mieux d'aller demander à Gandalf ce qu'il se passe.")
        self.screen.blit(self.charlie, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        self.game.Event_Invisible_done = True