import pygame

import config
from game_state import GameState
from game_state import grayscale


class Gandalf6:
    def __init__(self, screen, game, player):
        self.screen = screen
        self.game = game
        self.player = player

        #Dialogue adapté taille écran
        self.dialog = pygame.image.load("imgs/dialog.png").convert_alpha()
        self.dialog = pygame.transform.scale(self.dialog, (config.SCREEN_WIDTH//3.5, config.SCREEN_HEIGHT//4.5))
        self.dialogPNJ = pygame.transform.flip(self.dialog, True, False).convert_alpha()
        self.dialogPNJ = pygame.transform.scale(self.dialogPNJ, (config.SCREEN_WIDTH//3.5, config.SCREEN_HEIGHT//4.5))

        self.boite_allemand = pygame.image.load("imgs/monde6/boitesallemand.png").convert_alpha()
        self.boite_allemand = pygame.transform.scale(self.boite_allemand, (config.SCREEN_WIDTH //5, config.SCREEN_HEIGHT //4))
        self.boite_français = pygame.image.load("imgs/monde6/boitesfrançais.png").convert_alpha()
        self.boite_français = pygame.transform.scale(self.boite_français, (config.SCREEN_WIDTH //5, config.SCREEN_HEIGHT //4))

        #Perso adaptés taille écran
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
        self.PNJ = pygame.image.load("imgs/characters/gandalf.png").convert_alpha()
        self.PNJ = pygame.transform.flip(self.PNJ, True, False)
        self.PNJ = pygame.transform.scale(self.PNJ, (config.SCREEN_WIDTH//5, config.SCREEN_HEIGHT//1.1))
        self.PNJ_gray = grayscale(self.PNJ)
        
        #Eclair adapté taille écran
        self.ECLAIR_BLANC = pygame.image.load("imgs/ECLAIR_BLANC.jpg").convert_alpha()
        self.ECLAIR_BLANC = pygame.transform.scale(self.ECLAIR_BLANC, (config.SCREEN_WIDTH, config.SCREEN_HEIGHT))

        self.fin = pygame.image.load("imgs/fin.png").convert_alpha()
        self.fin = pygame.transform.scale(self.fin, (config.SCREEN_WIDTH, config.SCREEN_HEIGHT))

        
        # Son de tonnerre
        self.lightning_sound = pygame.mixer.Sound("sons/lightning.ogg")
        self.lightning_played = False
        self.lightning_sound.set_volume(0.8)   # entre 0.0 et 1.0

        self.Gouragan = False
        self.Gvoiture = False
        self.Genfant = False
        self.Gorange = False
        self.Garbre = False
        self.Glune = False

        self.cut = 0
        self.max_cut = 49

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
        self.choices1 = ["Ouragan", "Voiture", "Enfant", "Orange", "Arbre", "Lune"]
        self.choices2 = ["Genre grammatical", "Classificateur", "Classe nominale"]
        self.choices3 = ["0","1","2","3","4"]
        self.choices1status = ["attente"]
        self.choices2status = ["attente"]
        self.choices3status = ["attente"]


    def load(self):         
        self.current_char = 0
        self.last_update = pygame.time.get_ticks()

  
    def update(self):  
        if self.cut == 18:
            self.cut = 16
        elif self.cut == 20:
            self.cut = 16
        elif self.cut == 24:
            self.cut = 22
        elif self.cut == 26:
            self.cut = 22
        elif self.cut == 34:
            self.cut = 32
        elif self.cut == 36:
            self.cut = 32
        elif self.cut == 41:
            self.cut = 39
        elif self.cut == 43:
            self.cut = 39
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
                        self.choice_index = (self.choice_index - 1) % len (self.choices)
                    elif event.key == pygame.K_DOWN:
                        self.choice_index = (self.choice_index + 1) % len (self.choices)
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
            self.cut == 16
            and self.choices1status == ["attente"]
            and not self.choice_active
        ):
            self.choices = self.choices1
            self.choice_active = True
            self.choice_index = 0

        elif (
            self.cut == 22
            and self.choices1status == ["attente"]
            and not self.choice_active
        ):
            self.choices = self.choices1
            self.choice_active = True
            self.choice_index = 0

        elif (
            self.cut == 32
            and self.choices2status == ["attente"]
            and not self.choice_active
        ):
            self.choices = self.choices2
            self.choice_active = True
            self.choice_index = 0

        elif (
            self.cut == 39
            and self.choices3status == ["attente"]
            and not self.choice_active
        ):
            self.choices = self.choices3
            self.choice_active = True
            self.choice_index = 0

    
    def render(self):
        if self.choice_active:
            self.render_choice()
            return
       
        if self.Gouragan == True and self.Genfant == True and self.Garbre == True and self.cut <21:
            self.cut = 21

        if self.Gvoiture == True and self.Gorange == True and self.Glune == True and self.cut <27 :
            self.cut = 27
            
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
        elif self.cut == 42:
            self.render_scene_42()
        elif self.cut == 43:
            self.render_scene_43()
        elif self.cut == 44:
            self.render_scene_44()
        elif self.cut == 45:
            self.render_scene_45()
        elif self.cut == 46:
            self.render_scene_46()
        elif self.cut == 47:
            self.render_scene_47()
        elif self.cut == 48:
            self.render_scene_48()
        elif self.cut == 49:
            self.render_scene_49()
        
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
            
    def _render_dialogue_box_Answer(self, text):
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

    def _render_dialogue_box(self, text):
        dialogue_rect = self.screen.blit(self.dialogPNJ, (config.SCREEN_WIDTH // 2.8, config.SCREEN_HEIGHT // 1.4))       # chiffres = position bulle de dialogue
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
        y = dialogue_rect.y + 40

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
        self.current_dialogue_total_chars = sum(len(line) + 1 for line in wrapped)

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

    def _render_dialogue_box_fin(self, text):
        dialogue_rect = self.screen.blit(self.fin, (0,0))       # chiffres = position bulle de dialogue
        

        font = pygame.font.Font("fonts/PokemonGb.ttf", 50)           #20 = taille des lettres
        color = config.WHITE

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

    def get_fitting_font_for_choices(self, choices, font_path, max_width, max_height,
                                    start_size=20, min_size=12,
                                    line_spacing=6, choice_spacing=8):
        """Trouve une taille de police qui permet d'afficher *tous* les choix dans la bulle.
        - wrap chaque choix sur plusieurs lignes si besoin
        - vérifie que la hauteur totale (toutes les lignes + espacements) rentre dans max_height
        Retourne (font, wrapped_choices) où wrapped_choices = [ [ligne1, ligne2, ...], ... ].
        """
        for size in range(start_size, min_size - 1, -1):
            font = pygame.font.Font(font_path, size)
            wrapped_choices = [self.wrap_text(c, font, max_width) for c in choices]

            total_lines = sum(len(lines) for lines in wrapped_choices)
            if total_lines == 0:
                return font, wrapped_choices

            total_height = total_lines * (font.get_height() + line_spacing)
            total_height += max(0, len(choices) - 1) * choice_spacing

            if total_height <= max_height:
                return font, wrapped_choices

        font = pygame.font.Font(font_path, min_size)
        wrapped_choices = [self.wrap_text(c, font, max_width) for c in choices]
        return font, wrapped_choices

    # --- NOUVEAU : rendu du menu de choix ---
    def render_choice(self):
        dialogue_rect = self.screen.blit(
            self.dialog,
            (config.SCREEN_WIDTH // 2.8, config.SCREEN_HEIGHT // 1.4)
        )
        self.screen.blit(self.charlie, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        self.screen.blit(self.PNJ_gray, (config.SCREEN_WIDTH // 6, config.SCREEN_HEIGHT * 0.5))

        if 14 < self.cut < 27 : 
            self.screen.blit(self.boite_allemand, (config.SCREEN_WIDTH // 3, config.SCREEN_HEIGHT // 3))

        color = config.BLACK

        # --- Question (optionnelle) ---
        question = ""
        max_width = dialogue_rect.width - 100   # marges gauche/droite
        x_text = dialogue_rect.x + 50
        x_arrow = dialogue_rect.x + 40

        y = dialogue_rect.y + 35

        # 1) Question avec fitting font (si tu en mets une)
        if question:
            q_font, q_lines = self.get_fitting_font(
                text=question,
                font_path="fonts/PokemonGb.ttf",
                max_width=max_width,
                max_height=dialogue_rect.height // 3,
                start_size=20,
                min_size=12
            )
            for line in q_lines:
                surf_q = q_font.render(line, True, color)
                self.screen.blit(surf_q, (dialogue_rect.x + 30, y))
                y += q_font.get_height() + 6
            y += 8
        else:
            y = dialogue_rect.y + 60

        # 2) Fitting font pour tous les choix
        available_height = (dialogue_rect.y + dialogue_rect.height - 30) - y
        font, wrapped_choices = self.get_fitting_font_for_choices(
            choices=self.choices,
            font_path="fonts/PokemonGb.ttf",
            max_width=max_width,
            max_height=available_height,
            start_size=20,
            min_size=12,
            line_spacing=6,
            choice_spacing=10
        )

        line_spacing = 6
        choice_spacing = 10

        # 3) Render multi-lignes
        for i, lines in enumerate(wrapped_choices):
            if not lines:
                lines = [""]

            for j, line in enumerate(lines):
                surf = font.render(line, True, color)
                self.screen.blit(surf, (x_text, y))

                if i == self.choice_index and j == 0:
                    arrow_points = [
                        (x_arrow, y + font.get_height() // 2),
                        (x_arrow - 10, y + 2),
                        (x_arrow - 10, y + font.get_height() - 2),
                    ]
                    pygame.draw.polygon(self.screen, (255, 0, 0), arrow_points)

                y += font.get_height() + line_spacing

            y += choice_spacing    

    def handle_choice(self):
        choices = self.choices[self.choice_index]

        if self.cut == 16 :
            if choices == "Enfant":
                self.choice_active = False
                self.cut = 17
                self.Genfant = True
                self.current_char = 0
                self.last_update = pygame.time.get_ticks()
            if choices == "Arbre":
                self.choice_active = False
                self.Garbre = True
                self.cut = 17
                self.current_char = 0
                self.last_update = pygame.time.get_ticks()
            if choices == "Ouragan":
                self.choice_active = False
                self.Gouragan = True
                self.cut = 17
                self.current_char = 0
                self.last_update = pygame.time.get_ticks()
            if choices == "Voiture":
                self.choice_active = False
                self.cut = 19
                self.current_char = 0
                self.last_update = pygame.time.get_ticks()
            if choices == "Orange":
                self.choice_active = False
                self.cut = 19
                self.current_char = 0
                self.last_update = pygame.time.get_ticks()
            if choices == "Lune":
                self.choice_active = False
                self.cut = 19
                self.current_char = 0
                self.last_update = pygame.time.get_ticks()

        if self.cut == 22 :
            if choices == "Enfant":
                self.choice_active = False
                self.cut = 25
                self.current_char = 0
                self.last_update = pygame.time.get_ticks()
            elif choices == "Arbre":
                self.choice_active = False
                self.cut = 25
                self.current_char = 0
                self.last_update = pygame.time.get_ticks()
            elif choices == "Ouragan":
                self.choice_active = False
                self.cut = 25
                self.current_char = 0
                self.last_update = pygame.time.get_ticks()
            elif choices == "Voiture":
                self.choice_active = False
                self.Gvoiture = True
                self.cut = 23
                self.current_char = 0
                self.last_update = pygame.time.get_ticks()
            elif choices == "Orange":
                self.choice_active = False
                self.cut = 23
                self.Gorange = True
                self.current_char = 0
                self.last_update = pygame.time.get_ticks()
            elif choices == "Lune":
                self.choice_active = False
                self.Glune = True
                self.cut = 23
                self.current_char = 0
                self.last_update = pygame.time.get_ticks()
        
        if choices == "Genre grammatical":
            self.choice_active = False
            self.cut = 37
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        if choices == "Classificateur":
            self.choice_active = False
            self.cut = 33
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        if choices == "Classe nominale":
            self.choice_active = False
            self.cut = 35
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        if choices == "0":
            self.choice_active = False
            self.cut = 40
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        if choices == "1":
            self.choice_active = False
            self.cut = 40
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        if choices == "2":
            self.choice_active = False
            self.cut = 44
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        if choices == "3":
            self.choice_active = False
            self.cut = 42
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        if choices == "4":
            self.choice_active = False
            self.cut = 42
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

            

    def render_scene_0(self):
        self._render_dialogue_box_Answer("Gandalf ! T'as encore tout raté !")
        self.screen.blit(self.charlie_mécontent, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_1(self):
        self._render_dialogue_box("Oh, Charlie. Je dirais bien que ça fait plaisir de te revoir, mais...")
        self.screen.blit(self.charlie_mécontent_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        
    def render_scene_2(self):
        self._render_dialogue_box_Answer("Je veux rentrer chez moi ! On y est toujours pas, j'en ai marre là !")
        self.screen.blit(self.charlie_mécontent, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        
    def render_scene_3(self):
        self._render_dialogue_box("C'est peut-être pas chez toi, mais on est bien dans un pays qui marque le genre grammatical, donc on se rapproche, non ?")
        self.screen.blit(self.charlie_mécontent_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        
    def render_scene_4(self):
        self._render_dialogue_box_Answer("Mais c'est pas du genre grammatical ça, c'est du pim pam poum !")
        self.screen.blit(self.charlie_mécontent, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        
    def render_scene_5(self):
        self._render_dialogue_box("Certes mais tu habites bien dans une langue qui possède un masculin, un féminin et un neutre ?")
        self.screen.blit(self.charlie_mécontent_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        
    def render_scene_6(self):
        self._render_dialogue_box_Answer("Un neutre ? Quelle drôle d'idée ! En Français on parle en masculin et féminin, ça suffit amplement.")
        self.screen.blit(self.charlie_surpris, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        
    def render_scene_7(self):
        self._render_dialogue_box("Ah mais oui c'est vrai ! Même dans des langues au même mode de classification grammaticale, le nombre de classes peut changer ! Ce qui veut dire qu'un même morphème peut appartenir à deux catégories différentes !")
        self.screen.blit(self.charlie_surpris_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        
    def render_scene_8(self):
        self._render_dialogue_box_Answer("Mh, tu peux la refaire en français, s'il te plait ?")
        self.screen.blit(self.charlie_surpris, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        
    def render_scene_9(self):
        self._render_dialogue_box("Tiens, j'ai là des figurines que mon portier m'a offert car il les possède en double. Il les range par genre grammatical.")
        self.screen.blit(self.charlie_surpris_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        
    def render_scene_10(self):
        self._render_dialogue_box_Answer("Alors c'était ça ??!")
        self.screen.blit(self.charlie_surpris, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        
    def render_scene_11(self):
        self._render_dialogue_box("Oui, regarde.")
        self.screen.blit(self.charlie_surpris_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_12(self):
        self.screen.blit(self.boite_allemand, (config.SCREEN_WIDTH // 3, config.SCREEN_HEIGHT // 3))
        self._render_dialogue_box("Tu vois dans la boite des 'PIM' ? Ce sont les mots masculins. On dit 'un ouragan', 'un voiture', 'un lune'. Et la boite des 'PAM', ce sont les mots féminins. 'Une arbre', 'une orange'. Et 'POUM', c'est neutre. 'Enfant'.")
        self.screen.blit(self.charlie_surpris_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        
    def render_scene_13(self):
        self.screen.blit(self.boite_allemand, (config.SCREEN_WIDTH // 3, config.SCREEN_HEIGHT // 3))
        self._render_dialogue_box_Answer("Je comprend mieux... En français il n'y a que deux genres. Masculin et féminin. Et même là les mots n'ont pas le même genre.")
        self.screen.blit(self.charlie, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        
    def render_scene_14(self):
        self.screen.blit(self.boite_allemand, (config.SCREEN_WIDTH // 3, config.SCREEN_HEIGHT // 3))
        self._render_dialogue_box("Tu me montrerais comment tu les ranges dans ta langue ?")
        self.screen.blit(self.charlie_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        
    def render_scene_15(self):
        self.screen.blit(self.boite_allemand, (config.SCREEN_WIDTH // 3, config.SCREEN_HEIGHT // 3))
        self._render_dialogue_box_Answer("Bien sûr. Dans la boite du masculin il y a : ")
        self.screen.blit(self.charlie, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_16(self):
        self.screen.blit(self.boite_allemand, (config.SCREEN_WIDTH // 3, config.SCREEN_HEIGHT // 3))
        self._render_dialogue_box_Answer("")
        
    def render_scene_17(self):
        self.screen.blit(self.boite_allemand, (config.SCREEN_WIDTH // 3, config.SCREEN_HEIGHT // 3))
        self._render_dialogue_box_Answer("et aussi :")
        self.screen.blit(self.charlie, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        
    def render_scene_18(self):
        self.screen.blit(self.boite_allemand, (config.SCREEN_WIDTH // 3, config.SCREEN_HEIGHT // 3))
        self._render_dialogue_box("")
        
    def render_scene_19(self):
        self.screen.blit(self.boite_allemand, (config.SCREEN_WIDTH // 3, config.SCREEN_HEIGHT // 3))
        self._render_dialogue_box_Answer("Euh, je veux dire :")
        self.screen.blit(self.charlie, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        
    def render_scene_20(self):
        self.screen.blit(self.boite_allemand, (config.SCREEN_WIDTH // 3, config.SCREEN_HEIGHT // 3))
        self._render_dialogue_box("")
        
    def render_scene_21(self):
        self.screen.blit(self.boite_allemand, (config.SCREEN_WIDTH // 3, config.SCREEN_HEIGHT // 3))
        self._render_dialogue_box_Answer("Et dans la boite du féminin, il y a :")
        self.screen.blit(self.charlie, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_22(self):
        self.screen.blit(self.boite_allemand, (config.SCREEN_WIDTH // 3, config.SCREEN_HEIGHT // 3))
        self._render_dialogue_box_Answer("")
        
    def render_scene_23(self):
        self.screen.blit(self.boite_allemand, (config.SCREEN_WIDTH // 3, config.SCREEN_HEIGHT // 3))
        self._render_dialogue_box_Answer("et aussi :")
        self.screen.blit(self.charlie, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        
    def render_scene_24(self):
        self.screen.blit(self.boite_allemand, (config.SCREEN_WIDTH // 3, config.SCREEN_HEIGHT // 3))
        self._render_dialogue_box("")
        
    def render_scene_25(self):
        self.screen.blit(self.boite_allemand, (config.SCREEN_WIDTH // 3, config.SCREEN_HEIGHT // 3))
        self._render_dialogue_box_Answer("Euh, je veux dire :")
        self.screen.blit(self.charlie, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        
    def render_scene_26(self):
        self.screen.blit(self.boite_allemand, (config.SCREEN_WIDTH // 3, config.SCREEN_HEIGHT // 3))
        self._render_dialogue_box("")
        
    def render_scene_27(self):
        self.screen.blit(self.boite_allemand, (config.SCREEN_WIDTH // 3, config.SCREEN_HEIGHT // 3))
        self.screen.blit(self.boite_français, (config.SCREEN_WIDTH // 1.8, config.SCREEN_HEIGHT // 3))
        self._render_dialogue_box_Answer("Et voilà.")
        self.screen.blit(self.charlie, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_28(self):
        self._render_dialogue_box("Avec ces nouvelles données, je devrais pouvoir te ramener chez toi en regardant dans quelle région du monde on classe ces éléments de cette manière.")
        self.screen.blit(self.charlie_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        
    def render_scene_29(self):
        self._render_dialogue_box(".............................................................")
        self.screen.blit(self.charlie_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        
    def render_scene_30(self):
        self._render_dialogue_box("Bon, résumons ce qu’on sait. Fais-le avec moi, comme ça si je me trompe, tu ne pourras pas m’accuser.")
        self.screen.blit(self.charlie_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        
    def render_scene_31(self):
        self._render_dialogue_box("En premier, je rentre quel système de classification ?")
        self.screen.blit(self.charlie_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        
    def render_scene_32(self):
        self._render_dialogue_box("")
        
    def render_scene_33(self):
        self._render_dialogue_box("Tu es sûr ? Tu ranges selon la forme des mots ? Long, liquide ?")
        self.screen.blit(self.charlie_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_34(self):
        self._render_dialogue_box_Answer("")
        
    def render_scene_35(self):
        self._render_dialogue_box("Tu es sûr ? Tu ranges en fonction de petit, grand, animal ?")
        self.screen.blit(self.charlie_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        
    def render_scene_36(self):
        self._render_dialogue_box("")
        
    def render_scene_37(self):
        self._render_dialogue_box("ça, c'est bon. Ta langue catégorise en fonction du genre.")
        self.screen.blit(self.charlie_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        
    def render_scene_38(self):
        self._render_dialogue_box("Ensuite. Il existe combien de genres différents dans ta langue ?")
        self.screen.blit(self.charlie_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        
    def render_scene_39(self):
        self._render_dialogue_box("")

    def render_scene_40(self):
        self._render_dialogue_box_Answer("Si peu ? Tu es sûr ?")
        self.screen.blit(self.charlie_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_41(self):
        self._render_dialogue_box("")
        
    def render_scene_42(self):
        self._render_dialogue_box("Tant que ça ? Pas de doutes ?")
        self.screen.blit(self.charlie_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        
    def render_scene_43(self):
        self._render_dialogue_box_Answer("")
        
    def render_scene_44(self):
        self._render_dialogue_box("Masculin et féminin. C'est noté.")
        self.screen.blit(self.charlie_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        
    def render_scene_45(self):
        self._render_dialogue_box("Ohhhhh incroyable... Il y a plus de 1050 langue qui n'ont que deux genres différents ! ça en fait des possibilités ! Si ça se trouve, tu ne rentreras jamais chez toi, ahahahah !")
        self.screen.blit(self.charlie_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_46(self):
        self._render_dialogue_box_Answer("Oui, ahah, très drôle... Mais si cette fois ça pouvait marcher, ça serait cool...")
        self.screen.blit(self.charlie_penaud, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        
    def render_scene_47(self):
        if not self.lightning_played:
            self.game.mondes456.set_volume(0)          # Pause la musique de fond
            self.lightning_sound.play()         # Joue le tonnerre
            self.lightning_played = True
        self._render_dialogue_box_Lightning("KABOOM")

    def render_scene_48(self):
        self._render_dialogue_box_fin ("Aussi étonnant que cela puisse paraître, Charlie a fini par rentrer chez lui. Il a filé dans son appart, a pris une bonne douche, dormi 15 heures d'affilée. Quand il a parlé de cette histoire à son entourage, personne n'a voulu le croire. Mais il a fini par avoir son éclair au chocolat et ses croissants. Tout est bien qui finit bien pour lui.")

    def render_scene_49(self):
        self.game.fin_de_jeu = True
        
        
        