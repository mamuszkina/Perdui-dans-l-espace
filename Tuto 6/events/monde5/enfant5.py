import pygame

import config
from game_state import GameState
from game_state import grayscale


class enfant5:
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
        self.panneau = pygame.image.load("imgs/monde5/dessin_enfant.png").convert_alpha()
        self.panneau = pygame.transform.scale(self.panneau, (config.SCREEN_WIDTH//1.5, config.SCREEN_HEIGHT//1.5))
        self.charlie = pygame.image.load("imgs/characters/charlie.png").convert_alpha()
        self.charlie = pygame.transform.scale(self.charlie, (config.SCREEN_WIDTH //5, config.SCREEN_HEIGHT //1.1))
        self.charlie_gray = grayscale(self.charlie)
        self.charlie_penaud = pygame.image.load("imgs/characters/C_penaud.png").convert_alpha()
        self.charlie_penaud = pygame.transform.scale(self.charlie_penaud, (config.SCREEN_WIDTH //5, config.SCREEN_HEIGHT //1.1))
        self.charlie_penaud_gray = grayscale(self.charlie_penaud)
        self.charlie_surpris = pygame.image.load("imgs/characters/C_surpris.png").convert_alpha()
        self.charlie_surpris = pygame.transform.scale(self.charlie_surpris, (config.SCREEN_WIDTH //5, config.SCREEN_HEIGHT //1.1))
        self.charlie_surpris_gray = grayscale(self.charlie_surpris)
        self.charlie_mécontent = pygame.image.load("imgs/characters/C_mécontent.png").convert_alpha()
        self.charlie_mécontent = pygame.transform.scale(self.charlie_mécontent, (config.SCREEN_WIDTH //5, config.SCREEN_HEIGHT //1.1))
        self.charlie_mécontent_gray = grayscale(self.charlie_mécontent)
        self.charlie_content = pygame.image.load("imgs/characters/C_content.png").convert_alpha()
        self.charlie_content = pygame.transform.scale(self.charlie_content, (config.SCREEN_WIDTH //5, config.SCREEN_HEIGHT //1.1))
        self.charlie_content_gray = grayscale(self.charlie_content)
        self.PNJ = pygame.image.load("imgs/characters/enfant_deux.png").convert_alpha()
        self.PNJ = pygame.transform.flip(self.PNJ, True, False)
        self.PNJ = pygame.transform.scale(self.PNJ, (config.SCREEN_WIDTH//5, config.SCREEN_HEIGHT//1.1))
        self.PNJ_gray = grayscale(self.PNJ)
        self.gandalf = pygame.image.load("imgs/characters/gandalf.png").convert_alpha()
        self.gandalf = pygame.transform.flip(self.gandalf, True, False)
        self.gandalf = pygame.transform.scale(self.gandalf, (config.SCREEN_WIDTH //5, config.SCREEN_HEIGHT //1.1))
        self.gandalf_gray = grayscale(self.gandalf)

        self.cut = 0
        self.max_cut = 41

        # Typewriter state when creating the PNJ
        self.char_delay_ms = 30                     # 1= très rapide ; 100= très lent
        self.current_char = 0
        self.last_update = 0
        # Nombre total de caractères du texte courant (après "wrap")
        self.current_dialogue_total_chars = 0

        # --- Nouveaux attributs pour le choix multiple ---
        self.choice_active = False               # True quand on affiche les choix
        self.choice_index = 0                    # index du choix sélectionné
        self.choices = ["0"]
        self.choices1 = []
        self.choices2 = ["mariage", "oncle", "testament"]
        self.choices3 = ["tête", "dinosaure", "lièvre"]
        self.choices4 = ["eau", "dent", "serpillière"]
        self.choices5 = ["sauterelle", "queue", "pot"]
        self.choices1status = ["attente"]
        self.choices2status = ["attente"]
        self.choices3status = ["attente"]
        self.choices4status = ["attente"]
        self.choices5status = ["attente"]
        self.resolved = False
        self.é = False
        self.ù = False
        self.à = False
        self.ç = False

    def load(self):
        self.current_char = 0
        self.last_update = pygame.time.get_ticks()
  
    def update(self):
        if self.cut == 1:
            self.game.event = None
        elif self.cut == 4:
            self.game.event = None
        elif self.cut == 14:
            self.cut = 12
        elif self.cut == 21:
            self.cut = 19
        elif self.cut == 28:
            self.cut = 26
        elif self.cut == 35:
            self.cut = 33
        elif self.cut == 17:
            self.cut = 10
        elif self.cut == 24:
            self.cut = 10
        elif self.cut == 31:
            self.cut = 10
        elif self.cut == 38:
            self.cut = 10
        elif self.cut == 40:
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

                # --- Mode choix actif : flèches + Entrée gèrent le menu ---
                elif self.choice_active:
                    if event.key == pygame.K_UP:
                        self.choice_index = (self.choice_index - 1) % max(1, len (self.choices))
                    elif event.key == pygame.K_DOWN:
                        self.choice_index = (self.choice_index + 1) % max(1, len (self.choices))
                    elif event.key == pygame.K_RETURN:
                        self.handle_choice()

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

        if (
            self.cut == 10
            and self.choices1status == ["attente"]
            and not self.choice_active
        ):
            self.choices = self.choices1
            if self.é == False:
                self.choices = self.choices + ["é"]
            if self.à == False:
                self.choices = self.choices + ["à"]
            if self.ù == False:
                self.choices = self.choices + ["ù"]
            if self.ç == False:
                self.choices = self.choices + ["ç"]
            self.choice_active = True
            self.choice_index = 0

        elif (
            self.cut == 12
            and self.choices2status == ["attente"]
            and not self.choice_active
        ):
            self.choices = self.choices2
            self.choice_active = True
            self.choice_index = 0

        elif (
            self.cut == 19
            and self.choices3status == ["attente"]
            and not self.choice_active
        ):
            self.choices = self.choices3
            self.choice_active = True
            self.choice_index = 0

        elif (
            self.cut == 26
            and self.choices4status == ["attente"]
            and not self.choice_active
        ):
            self.choices = self.choices4
            self.choice_active = True
            self.choice_index = 0

        elif (
            self.cut == 33
            and self.choices5status == ["attente"]
            and not self.choice_active
        ):
            self.choices = self.choices5
            self.choice_active = True
            self.choice_index = 0
                
    def render(self):

        if self.game.Gandalf5_dialogue_done == True and self.cut < 2:
            self.cut = 2
            return

        if self.game.panneau_done == True and self.cut < 5:
            self.cut = 5
            return

        if self.game.enfant5_dialogue_done == True and self.cut < 10:
            self.cut = 41
            return

        if self.é == True and self.ù == True and self.à == True and self.ç == True and self.cut in (37, 30, 23, 16) :
            self.cut = 39

        if self.choice_active:
            self.render_choice()
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
        elif self.cut == 14:
            self.render_scene_14()
        elif self.cut == 15:
            self.render_scene_15()
        elif self.cut == 16:
            self.render_scene_16()
        elif self.cut == 16:
            self.render_scene_16()
        elif self.cut == 17:
            self.render_scene_17()
        elif self.cut == 18:
            self.render_scene_18()
        elif self.cut == 19:
            self.render_scene_19()
        elif self.cut == 20:
            self.render_scene_20()
        elif self.cut == 21:
            self.render_scene_21()
        elif self.cut == 22:
            self.render_scene_22()
        elif self.cut == 23:
            self.render_scene_23()
        elif self.cut == 24:
            self.render_scene_24()
        elif self.cut == 25:
            self.render_scene_25()
        elif self.cut == 26:
            self.render_scene_26()
        elif self.cut == 27:
            self.render_scene_27()
        elif self.cut == 28:
            self.render_scene_28()
        elif self.cut == 29:
            self.render_scene_29()
        elif self.cut == 30:
            self.render_scene_30()
        elif self.cut == 31:
            self.render_scene_31()
        elif self.cut == 32:
            self.render_scene_32()
        elif self.cut == 33:
            self.render_scene_33()
        elif self.cut == 34:
            self.render_scene_34()
        elif self.cut == 35:
            self.render_scene_35()
        elif self.cut == 36:
            self.render_scene_36()
        elif self.cut == 37:
            self.render_scene_37()
        elif self.cut == 38:
            self.render_scene_38()
        elif self.cut == 39:
            self.render_scene_39()
        elif self.cut == 40:
            self.render_scene_40()
        elif self.cut == 41:
            self.render_scene_41()
        
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
    def _render_dialogue_box_PNJ(self, text):
        self.screen.blit(self.panneau, (config.SCREEN_WIDTH // 6, config.SCREEN_HEIGHT // 10))
        dialogue_rect = self.screen.blit(self.dialogPNJ, (config.SCREEN_WIDTH // 2.8, config.SCREEN_HEIGHT // 1.4))       # chiffres = position bulle de dialogue
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

    def _render_dialogue_box_PNJ_no_panneau(self, text):
        dialogue_rect = self.screen.blit(self.dialogPNJ, (config.SCREEN_WIDTH // 2.8, config.SCREEN_HEIGHT // 1.4))       # chiffres = position bulle de dialogue
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

    def _render_dialogue_box_Gandalf(self, text):
        dialogue_rect = self.screen.blit(self.dialogPNJ, (config.SCREEN_WIDTH // 2.8, config.SCREEN_HEIGHT // 1.4))      # chiffres = position bulle de dialogue
        self.screen.blit(self.charlie_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

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
        self.screen.blit(self.panneau, (config.SCREEN_WIDTH // 6, config.SCREEN_HEIGHT // 10))
        dialogue_rect = self.screen.blit(self.dialog, (config.SCREEN_WIDTH // 2.8, config.SCREEN_HEIGHT // 1.4))      # chiffres = position bulle de dialogue
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


    def _render_dialogue_box_Answer_no_panneau(self, text):
        dialogue_rect = self.screen.blit(self.dialog, (config.SCREEN_WIDTH // 2.8, config.SCREEN_HEIGHT // 1.4))      # chiffres = position bulle de dialogue
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

    def _render_dialogue_box_Answer_first(self, text):
        dialogue_rect = self.screen.blit(self.dialog, (config.SCREEN_WIDTH // 2.8, config.SCREEN_HEIGHT // 1.4))      # chiffres = position bulle de dialogue
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

    def _render_dialogue_box_Answer_Gandalf(self, text):
        dialogue_rect = self.screen.blit(self.dialog, (config.SCREEN_WIDTH // 2.8, config.SCREEN_HEIGHT // 1.4))      # chiffres = position bulle de dialogue
        self.screen.blit(self.gandalf_gray, (config.SCREEN_WIDTH // 6, config.SCREEN_HEIGHT * 0.5))

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

    # --- NOUVEAU : rendu du menu de choix ---
    def render_choice(self):
        self.screen.blit(self.panneau, (config.SCREEN_WIDTH // 6, config.SCREEN_HEIGHT // 10))
        dialogue_rect = self.screen.blit(self.dialog, (config.SCREEN_WIDTH // 2.8, config.SCREEN_HEIGHT // 1.4))
        self.screen.blit(self.charlie, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        self.screen.blit(self.gandalf_gray, (config.SCREEN_WIDTH // 6, config.SCREEN_HEIGHT * 0.5))

        if self.game.homme_finito == True :
            self.screen.blit(self.panneau, (50, 10))

        font = pygame.font.Font("fonts/PokemonGb.ttf", 20)
        color = config.BLACK

        # --- Question ---
        question = ""
        surf_q = font.render(question, True, color)
        self.screen.blit(surf_q, (dialogue_rect.x + 30, dialogue_rect.y + 20))

        # Positions de base
        y = dialogue_rect.y + 60 
        x_text = dialogue_rect.x + 50 
        x_arrow = dialogue_rect.x + 40 

        for i, choice in enumerate(self.choices):
            # --- Ajout du > uniquement sur la ligne sélectionnée ---
            if i == self.choice_index:
                display_text = choice
            else:
                display_text = choice

            surf = font.render(display_text, True, color)
            self.screen.blit(surf, (x_text, y))

            # --- Flèche rouge pour le choix sélectionné ---
            if i == self.choice_index:
                arrow_points = [
                    (x_arrow, y + 8),        # pointe
                    (x_arrow - 10, y + 2),   # haut
                    (x_arrow - 10, y + 14),  # bas
                ]
                pygame.draw.polygon(self.screen, (255, 0, 0), arrow_points)

            y += font.get_height() + 8    

    # --- NOUVEAU : logique des réponses ---
    def handle_choice(self):
        choices = self.choices[self.choice_index]

        if choices == "ù":
            self.choice_active = False
            self.cut = 11
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        elif choices == "à":
            self.choice_active = False
            self.cut = 18
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        elif choices == "ç":
            self.choice_active = False
            self.cut = 25
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        elif choices == "é":
            self.choice_active = False
            self.cut = 32
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        elif choices == "mariage":
            self.choice_active = False
            self.cut = 13
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        elif choices == "testament":
            self.choice_active = False
            self.cut = 13
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        elif choices == "oncle":
            self.choice_active = False
            self.cut = 15
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        elif choices == "dinosaure":
            self.choice_active = False
            self.cut = 20
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        elif choices == "tête":
            self.choice_active = False
            self.cut = 20
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        elif choices == "lièvre":
            self.choice_active = False
            self.cut = 22
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        elif choices == "dent":
            self.choice_active = False
            self.cut = 27
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        elif choices == "serpillière":
            self.choice_active = False
            self.cut = 27
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        elif choices == "eau":
            self.choice_active = False
            self.cut = 29
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        elif choices == "sauterelle":
            self.choice_active = False
            self.cut = 34
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        elif choices == "pot":
            self.choice_active = False
            self.cut = 34
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        elif choices == "queue":
            self.choice_active = False
            self.cut = 36
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

            
#SCENE ZERO
    def render_scene_0(self):
        self._render_dialogue_box_Answer_first("Cette enfant est en pleurs. Pauvre petite...")
        self.screen.blit(self.charlie_penaud, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_1(self):
        self._render_dialogue_box_Answer("")
        
#SCENE UN
    def render_scene_2(self):
        self._render_dialogue_box_Gandalf("C'est elle. C'est l'enfant qui est partie en pleurant.")
        self.screen.blit(self.charlie_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        
    def render_scene_3(self):
        self._render_dialogue_box_Answer_Gandalf("Au moins, on saura où elle est pour la suite. Laissons-là pour l'instant.")
        self.screen.blit(self.charlie, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        
    def render_scene_4(self):
        self._render_dialogue_box_Answer("")

#SCENE DEUX        
    def render_scene_5(self):
        self._render_dialogue_box_Answer_no_panneau("Coucou toi. Je sais que tu ne me comprend pas mais j'ai ici un panneau pour qu'on puisse voir ensemble les spécificités de ta langue.")
        self.screen.blit(self.charlie, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        
    def render_scene_6(self):
        self._render_dialogue_box_PNJ_no_panneau("Je comprend pas ce que vous dites, monsieur...")
        self.screen.blit(self.charlie_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        
    def render_scene_7(self):
        self._render_dialogue_box_Answer("Regarde. J'ai récolté tous ces mots et je les ait rangés selon s'ils ont un 'ç', un 'à', un 'é' ou un 'ù'. On peut essayer de voir leurs points communs ensemble ?")
        self.screen.blit(self.charlie, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        
    def render_scene_8(self):
        self._render_dialogue_box_PNJ("Ohh je crois que je comprend ce que tu veux... Mais je sais pas si je vais y arriver...")
        self.screen.blit(self.charlie_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        
    def render_scene_9(self):
        self._render_dialogue_box_Answer("On va voir ça catégorie par catégorie. On commence par lequel ?")
        self.screen.blit(self.charlie, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_10(self):
        self._render_dialogue_box_Answer("")

#ù        
    def render_scene_11(self):
        self._render_dialogue_box_Answer("Voyons voir... En fonction de tous les mots écrits ici, si je devais ajouter un mot, je pense que je mettrais...")
        self.screen.blit(self.charlie, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        
    def render_scene_12(self):
        self._render_dialogue_box_Answer("")
        
    def render_scene_13(self):
        self._render_dialogue_box_Answer("Mh, elle me fait non de la tête, ça doit pas être ça. Et là elle se pointe du doigt...")
        self.screen.blit(self.charlie_penaud, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_14(self):
        self._render_dialogue_box_Answer("")

    def render_scene_15(self):
        self._render_dialogue_box_Answer("Oui, c'est ça ! C'est logique en fait.  C’est un groupe qui rassemble toutes les personnes. Tous les humains quoi. Les oncles et tantes, les frères et sœurs, les hommes et les femmes...")
        self.screen.blit(self.charlie_content, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        self.ù = True

    def render_scene_16(self):
        self._render_dialogue_box_Answer("On teste un autre groupe ?")
        self.screen.blit(self.charlie, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_17(self):
        self._render_dialogue_box_Answer("")

#à
    def render_scene_18(self):
        self._render_dialogue_box_Answer("Voyons voir... En fonction de tous les mots écrits ici, si je devais ajouter un mot, je pense que je mettrais...")
        self.screen.blit(self.charlie, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        
    def render_scene_19(self):
        self._render_dialogue_box_Answer("")
        
    def render_scene_20(self):
        self._render_dialogue_box_Answer("Ah ben super, elle se moque de moi ! ça doit pas être ça. Elle se met à dessiner de touuuuuuut petits animaux...")
        self.screen.blit(self.charlie_mécontent, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_21(self):
        self._render_dialogue_box_Answer("")

    def render_scene_22(self):
        self._render_dialogue_box_Answer("ça y est j'ai compris ! C’est un groupe pour ranger les petits animaux ! Les grenouilles, les musaraignes, les hamsters... Marrant !")
        self.screen.blit(self.charlie_content, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        self.à = True

    def render_scene_23(self):
        self._render_dialogue_box_Answer("On teste un autre groupe ?")
        self.screen.blit(self.charlie, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_24(self):
        self._render_dialogue_box_Answer("")
#ç
    def render_scene_25(self):
        self._render_dialogue_box_Answer("Voyons voir... En fonction de tous les mots écrits ici, si je devais ajouter un mot, je pense que je mettrais...")
        self.screen.blit(self.charlie, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        
    def render_scene_26(self):
        self._render_dialogue_box_Answer("")
        
    def render_scene_27(self):
        self._render_dialogue_box_Answer("L'enfant me fait non de la tête. Puis là elle mime un parapluie...")
        self.screen.blit(self.charlie, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_28(self):
        self._render_dialogue_box_Answer("")

    def render_scene_29(self):
        self._render_dialogue_box_Answer("Et un groupe avec tous les liquides, un ! Je suppose que le sang, l’océan, les rivières, tout ça doit être contenu ici.")
        self.screen.blit(self.charlie_content, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        self.ç = True

    def render_scene_30(self):
        self._render_dialogue_box_Answer("On teste un autre groupe ?")
        self.screen.blit(self.charlie, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_31(self):
        self._render_dialogue_box_Answer("")
#é
    def render_scene_32(self):
        self._render_dialogue_box_Answer("Voyons voir... En fonction de tous les mots écrits ici, si je devais ajouter un mot, je pense que je mettrais...")
        self.screen.blit(self.charlie, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        
    def render_scene_33(self):
        self._render_dialogue_box_Answer("")
        
    def render_scene_34(self):
        self._render_dialogue_box_Answer("Elle pouffe de rire ! Et elle redessine les objets en exagérant leur longueur.")
        self.screen.blit(self.charlie, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_35(self):
        self._render_dialogue_box_Answer("")

    def render_scene_36(self):
        self._render_dialogue_box_Answer("Son visage s'illumine, ça doit être ça. Toutes les choses longues sont rangées dedans.  Il était vraiment pas facile celui-là. Les croccodiles, les bâtons, les cordes, c’est long tout ça !")
        self.screen.blit(self.charlie_content, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_37(self):
        self._render_dialogue_box_Answer("On teste un autre groupe ?")
        self.screen.blit(self.charlie, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        self.é = True

    def render_scene_38(self):
        self._render_dialogue_box_Answer("")

    def render_scene_39(self):
        self._render_dialogue_box_Answer("L'enfant trépigne de joie de m'avoir aidé. ça fait plaisir à voir ! J'ai plus qu'à dire à ton père que tu te sens mieux !")
        self.screen.blit(self.charlie_content, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        self.game.enfant5_dialogue_done = True 

    def render_scene_40(self):
        self._render_dialogue_box_Answer("")

    def render_scene_41(self):
        self._render_dialogue_box_Answer("C'est bien plus agréable de la savoir joyeuse !")
        self.screen.blit(self.charlie_content, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))