import pygame

import config
from game_state import GameState
from game_state import grayscale


class portier6:
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
        self.PNJ = pygame.image.load("imgs/characters/portier.png").convert_alpha()
        self.PNJ = pygame.transform.flip(self.PNJ, True, False)
        self.PNJ = pygame.transform.scale(self.PNJ, (config.SCREEN_WIDTH//5, config.SCREEN_HEIGHT//1.1))
        self.PNJ_gray = grayscale(self.PNJ)
    

        self.cut = 0
        self.max_cut = 30

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
        self.choices1 = ["Ne plus rien poser"]
        self.choices1status = ["attente"]

        self.enfantFAUX = False
        self.voitureFAUX = False
        self.ouraganFAUX = False
        self.luneFAUX = False
        self.arbreFAUX = False
        self.orangeFAUX = False
        self.enfantVRAI = False
        self.voitureVRAI = False
        self.ouraganVRAI = False
        self.luneVRAI = False
        self.arbreVRAI = False
        self.orangeVRAI = False


    def load(self):
        self.current_char = 0
        self.last_update = pygame.time.get_ticks()

  
    def update(self):
        if self.cut == 6:
            self.game.event = None
        elif self.cut == 8:
            self.game.event = None
        elif self.cut == 28:
            self.game.event = None
        elif self.cut == 16:
            self.cut = 14
        elif self.cut == 20:
            self.cut = 18
        elif self.cut == 24:
            self.cut = 22
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
            self.cut in (14, 18, 22)
            and self.choices1status == ["attente"]
            and not self.choice_active
        ) :
            self.choices = self.choices1
            if self.enfantFAUX == False and self.enfantVRAI == False:
                self.choices = self.choices + ["L'enfant"]
            if self.voitureFAUX == False and self.voitureVRAI == False:
                self.choices = self.choices + ["La voiture"]
            if self.ouraganFAUX == False and self.ouraganVRAI == False:
                self.choices = self.choices + ["L'ouragan"]
            if self.luneFAUX == False and self.luneVRAI == False:
                self.choices = self.choices + ["La lune"]
            if self.arbreFAUX == False and self.arbreVRAI == False:
                self.choices = self.choices + ["L'arbre"]
            if self.orangeFAUX == False and self.orangeVRAI == False:
                self.choices = self.choices + ["L'orange"]
            self.choice_active = True
            self.choice_index = 0
     
    
    def render(self):
        if self.choice_active:
            self.render_choice()
            return
        
        if self.game.portier6 == True and self.cut < 7:
            self.cut = 7

        if self.game.Fig_Enfant == True and self.game.Fig_Lune == True and self.game.Fig_Voiture == True and self.game.Fig_Ouragan == True and self.game.Fig_Orange == True and self.game.Fig_Arbre == True and self.cut < 9 :
            self.cut = 9

        if self.enfantVRAI == True and self.voitureVRAI == True and self.ouraganVRAI == True and self.luneVRAI == True and self.arbreVRAI == True and self.orangeVRAI == True and self.cut == 26:
            self.cut = 29
            
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
        
        if self.cut == 14:
            if choices == "L'enfant" :
                self.choice_active = False
                self.enfantFAUX = True
                self.cut = 15
                self.current_char = 0
                self.last_update = pygame.time.get_ticks()
            if choices == "La voiture" :
                self.choice_active = False
                self.voitureVRAI = True
                self.cut = 15
                self.current_char = 0
                self.last_update = pygame.time.get_ticks()
            if choices == "L'ouragan" :
                self.choice_active = False
                self.ouraganVRAI = True
                self.cut = 15
                self.current_char = 0
                self.last_update = pygame.time.get_ticks()
            if choices == "La lune" :
                self.choice_active = False
                self.luneVRAI = True
                self.cut = 15
                self.current_char = 0
                self.last_update = pygame.time.get_ticks()
            if choices == "L'arbre" :
                self.choice_active = False
                self.arbreFAUX = True
                self.cut = 15
                self.current_char = 0
                self.last_update = pygame.time.get_ticks()
            if choices == "L'orange" :
                self.choice_active = False
                self.orangeFAUX = True
                self.cut = 15
                self.current_char = 0
                self.last_update = pygame.time.get_ticks()
            if choices == "Ne plus rien poser" :
                self.choice_active = False
                self.cut = 17
                self.current_char = 0
                self.last_update = pygame.time.get_ticks()

        if self.cut == 18:
            if choices == "L'enfant" :
                self.choice_active = False
                self.enfantVRAI = True
                self.cut = 19
                self.current_char = 0
                self.last_update = pygame.time.get_ticks()
            if choices == "La voiture" :
                self.choice_active = False
                self.voitureFAUX = True
                self.cut = 19
                self.current_char = 0
                self.last_update = pygame.time.get_ticks()
            if choices == "L'ouragan" :
                self.choice_active = False
                self.ouraganFAUX = True
                self.cut = 19
                self.current_char = 0
                self.last_update = pygame.time.get_ticks()
            if choices == "La lune" :
                self.choice_active = False
                self.luneFAUX = True
                self.cut = 19
                self.current_char = 0
                self.last_update = pygame.time.get_ticks()
            if choices == "L'arbre" :
                self.choice_active = False
                self.arbreFAUX = True
                self.cut = 19
                self.current_char = 0
                self.last_update = pygame.time.get_ticks()
            if choices == "L'orange" :
                self.choice_active = False
                self.orangeFAUX = True
                self.cut = 19
                self.current_char = 0
                self.last_update = pygame.time.get_ticks()
            if choices == "Ne plus rien poser" :
                self.choice_active = False
                self.cut = 21
                self.current_char = 0
                self.last_update = pygame.time.get_ticks()


        if self.cut == 22:
            if choices == "L'enfant" :
                self.choice_active = False
                self.enfantFAUX = True
                self.cut = 23
                self.current_char = 0
                self.last_update = pygame.time.get_ticks()
            if choices == "La voiture" :
                self.choice_active = False
                self.voitureFAUX = True
                self.cut = 23
                self.current_char = 0
                self.last_update = pygame.time.get_ticks()
            if choices == "L'ouragan" :
                self.choice_active = False
                self.ouraganFAUX = True
                self.cut = 23
                self.current_char = 0
                self.last_update = pygame.time.get_ticks()
            if choices == "La lune" :
                self.choice_active = False
                self.luneFAUX = True
                self.cut = 23
                self.current_char = 0
                self.last_update = pygame.time.get_ticks()
            if choices == "L'arbre" :
                self.choice_active = False
                self.arbreVRAI = True
                self.cut = 23
                self.current_char = 0
                self.last_update = pygame.time.get_ticks()
            if choices == "L'orange" :
                self.choice_active = False
                self.orangeVRAI = True
                self.cut = 23
                self.current_char = 0
                self.last_update = pygame.time.get_ticks()
            if choices == "Ne plus rien poser" :
                self.choice_active = False
                self.cut = 25
                self.current_char = 0
                self.last_update = pygame.time.get_ticks()
            

    def render_scene_0(self):
        self._render_dialogue_box("Kalabidou gekigo, comma trodi futiba ?")
        self.screen.blit(self.charlie_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_1(self):
        self._render_dialogue_box_Answer("Euh, bonjour... Je suppose que je peux pas rentrer comme ça ?...")
        self.screen.blit(self.charlie, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        
    def render_scene_2(self):
        self._render_dialogue_box("Chebibah figussika lompe nubabatawa... Grappiari nekko piloupilou.")
        self.screen.blit(self.charlie_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        
    def render_scene_3(self):
        self._render_dialogue_box_Answer("Il a l'air désespéré... Mais pourquoi il me montre des figurines ? C'est un mystère mystérieux...")
        self.screen.blit(self.charlie_penaud, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        
    def render_scene_4(self):
        self._render_dialogue_box("Fouloulou grappibah tromposippi galoufront !")
        self.screen.blit(self.charlie_penaud_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        
    def render_scene_5(self):
        self._render_dialogue_box_Answer("Il mime du vent et me fait 6 avec sa main... Peut-être que si je lui retrouve 6 figurines, il me laissera passer ? J'ai qu'à essayer, je vois pas trop quoi faire de plus...")
        self.screen.blit(self.charlie_penaud, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        
    def render_scene_6(self):
        self._render_dialogue_box("")
        self.game.compris6 = True
        self.game.portier6 = True
        
    def render_scene_7(self):
        self._render_dialogue_box_Answer("Je dois encore trouver des figurines, il m'en faut six.")
        self.screen.blit(self.charlie, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        
    def render_scene_8(self):
        self._render_dialogue_box("")
        
    def render_scene_9(self):
        self._render_dialogue_box("Gabilou powa bouddaaaaaaaaa !")
        self.screen.blit(self.charlie_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        
    def render_scene_10(self):
        self._render_dialogue_box_Answer("Il a l'air content ! J'ai dû bien comprendre ! Il va peut-être me laisser passer maintenant ?")
        self.screen.blit(self.charlie_content, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        
    def render_scene_11(self):
        self._render_dialogue_box("Choupichou boudi bada bada, genkilou mondoro akka !")
        self.screen.blit(self.charlie_content_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_12(self):
        self._render_dialogue_box_Answer("Il me tend trois boites maintenant, super... Il a l'air de vouloir que je range les figurines.")
        self.screen.blit(self.charlie_penaud, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_13(self):
        self._render_dialogue_box_Answer("Je pose quoi dans cette boite notée 'PIM' ?")
        self.screen.blit(self.charlie, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        #Dessin d'une boite avec écrit PIM

    def render_scene_14(self):
        self._render_dialogue_box_Answer("")

    def render_scene_15(self):
        self._render_dialogue_box_Answer("OK. Dans celle là je met autre chose ?")
        self.screen.blit(self.charlie, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_16(self):
        self._render_dialogue_box_Answer("")

    def render_scene_17(self):
        self._render_dialogue_box_Answer("ça ira. Et dans cette boite notée 'PAM', je met quoi ?")
        self.screen.blit(self.charlie, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        #dessin d'une boite avec écrit PAM

    def render_scene_18(self):
        self._render_dialogue_box_Answer("")

    def render_scene_19(self):
        self._render_dialogue_box_Answer("OK. Dans celle là je met autre chose ?")
        self.screen.blit(self.charlie, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_20(self):
        self._render_dialogue_box_Answer("")

    def render_scene_21(self):
        self._render_dialogue_box_Answer("ça ira. Et dans la dernière boite notée 'POUM', je met quoi ?")
        self.screen.blit(self.charlie, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        #dessin d'une boite avec écrit POUM

    def render_scene_22(self):
        self._render_dialogue_box_Answer("")

    def render_scene_23(self):
        self._render_dialogue_box_Answer("OK. Dans celle là je met autre chose ?")
        self.screen.blit(self.charlie, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_24(self):
        self._render_dialogue_box_Answer("")

    def render_scene_25(self):
        self._render_dialogue_box_Answer("ça m'a l'air bien. J'ai plus qu'à montrer ça au portier et... prier pour que ça lui convienne.")
        self.screen.blit(self.charlie, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_26(self):
        self._render_dialogue_box("Grabidou fouloulou pakontan ! Rabibibabidans !")
        self.screen.blit(self.charlie_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_27(self):
        self._render_dialogue_box_Answer("Mhhh il n'est définitivement pas content... J'ai dû me tromper quelque part. Je ferais mieux de retourner en ville pour voir si je ne trouve pas des indices.")
        self.screen.blit(self.charlie_mécontent, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_28(self):
        self._render_dialogue_box("")
        self.enfantFAUX = False
        self.voitureFAUX = False
        self.ouraganFAUX = False
        self.luneFAUX = False
        self.arbreFAUX = False
        self.orangeFAUX = False
        self.enfantVRAI = False
        self.voitureVRAI = False
        self.ouraganVRAI = False
        self.luneVRAI = False
        self.arbreVRAI = False
        self.orangeVRAI = False
        
    def render_scene_29(self):
        self._render_dialogue_box("Grabidou trokoul trocontan ! Faivou ahahbichon !")
        self.screen.blit(self.charlie_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_30(self):
        self._render_dialogue_box_Answer("Ahhhh ça a l'air d'aller ! Bingo ! Je vais pouvoir enfin aller voir Gandalf ! Pour la dernière fois j'en suis sûr !")
        self.screen.blit(self.charlie_content, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        self.game.portier6_2_dialogue_done = True