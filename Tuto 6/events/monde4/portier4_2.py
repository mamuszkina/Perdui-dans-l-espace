import pygame

import config
from game_state import GameState
from game_state import grayscale


class portier4_2:
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
        self.PNJ = pygame.image.load("imgs/characters/portier.png").convert_alpha()
        self.PNJ = pygame.transform.flip(self.PNJ, True, False)
        self.PNJ = pygame.transform.scale(self.PNJ, (config.SCREEN_WIDTH//5, config.SCREEN_HEIGHT//1.1))
        self.PNJ_gray = grayscale(self.PNJ)

        self.cut = 0
        self.max_cut = 27
        self.has_teleported = False

        # Typewriter state when creating the PNJ
        self.char_delay_ms = 30                     # 1= très rapide ; 100= très lent
        self.current_char = 0
        self.last_update = 0
        self.current_dialogue_total_chars = 0

        # --- Nouveaux attributs pour le choix multiple ---
        self.choice_active = False               # True quand on affiche les choix
        self.choice_index = 0                    # index du choix sélectionné
        self.choices = ["0"]
        self.choices1 = ["Euh, oui, oui...", "Non, moi je viens voir Gandalf"]
        self.choices1status = ["attente"]
        self.goodbye = False  

    def load(self):
        self.current_char = 0
        self.last_update = pygame.time.get_ticks()

  
    def update(self):
        if self.has_teleported:
            return
            
        if self.cut == 5:
            self.game.event = None
        elif self.cut == 7:
            self.game.event = None
        elif self.cut == 12:
            self.game.event = None
        elif self.cut == 14:
            self.game.event = None
        elif self.cut == 20:
            self.game.event = None
        elif self.cut == 22:
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
                        self.choice_index = (self.choice_index - 1) % len (self.choices)
                    elif event.key == pygame.K_DOWN:
                        self.choice_index = (self.choice_index + 1) % len (self.choices)
                    elif event.key == pygame.K_RETURN:
                        self.handle_choice()

                # --- Message d'au revoir : Entrée ferme le dialogue ---
                elif self.goodbye:
                    if event.key == pygame.K_RETURN:
                        if self.current_char < self.current_dialogue_total_chars:
                            self.current_char = self.current_dialogue_total_chars
                    # 2e ENTER : passer à la case suivante
                        else: self.game.event = None

                # --- Dialogue normal : Entrée avance les cases ---
                elif event.key == pygame.K_RETURN:
                    # 1er ENTER : finir d'afficher le texte
                    if self.current_char < self.current_dialogue_total_chars:
                        self.current_char = self.current_dialogue_total_chars
                    # 2e ENTER : passer à la case suivante
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
            self.cut == 1
            and self.choices1status == ["attente"]
            and not self.goodbye
            and not self.choice_active
        ):
            self.choices = self.choices1
            self.choice_active = True
            self.choice_index = 0
 #           self.handle_choice1
        elif self.cut == 2:
            self.cut = 4
    
    def render(self):            
        # Si on a choisi "non" -> message d'au revoir
        if self.goodbye:
            self.render_goodbye()
            return

        if self.choice_active:
            self.render_choice()
            return

        if self.game.portier4_2dialogue1_done == True and self.cut < 6:
            self.cut = 6
            return

        if self.game.lezard == True and self.game.portier4_2dialogue1_done == True and self.cut < 8:
            self.cut = 8
            return
            
        if self.game.serpent == True and self.game.portier4_2dialogue1_done == True and self.cut < 8:
            self.cut = 8
            return

        if self.game.grenouille == True and self.game.portier4_2dialogue1_done == True and self.cut < 10:
            self.cut = 10
            return

        if self.game.portier4_2dialogue2_done == True and self.game.herbe == False and self.cut < 13:
            self.cut = 13
            return

        if self.game.portier4_2dialogue2_done == True and self.game.baton == False and self.cut < 13:
            self.cut = 13
            return

        if self.game.portier4_2dialogue2_done == True and self.game.bocal == False and self.cut < 13:
            self.cut = 13
            return

        if self.game.herbe == True and self.game.portier4_2dialogue2_done == True and self.cut < 15: 
            self.cut = 15
            return

        if self.game.baton == True and self.game.portier4_2dialogue2_done == True and self.cut < 15: 
            self.cut = 15
            return

        if self.game.bocal == True and self.game.portier4_2dialogue2_done == True and self.cut < 17: 
            self.cut = 17
            return

        if self.game.portier4_2dialogue3_done == True and self.cut < 21:
            self.cut = 21
            return

        if self.game.inun == True and self.game.portier4_2dialogue3_done == True and self.cut < 27:
            self.cut = 27
            return

        if self.game.amoka == True and self.game.portier4_2dialogue3_done == True and self.cut < 23:
            self.cut = 23
            return

        if self.game.isi == True and self.game.portier4_2dialogue3_done == True and self.cut < 25:
            self.cut = 25
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

    def _render_dialogue_box_penaud(self, text):
        dialogue_rect = self.screen.blit(self.dialogPNJ, (config.SCREEN_WIDTH // 2.8, config.SCREEN_HEIGHT // 1.4))      # chiffres = position bulle de dialogue
        self.screen.blit(self.charlie_penaud_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
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
        self.screen.blit(self.charlie_penaud, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
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

    # --- NOUVEAU : message quand le joueur répond "non" ---
    def render_goodbye(self):
        self._render_dialogue_box("")

    # --- NOUVEAU : logique des réponses ---
    def handle_choice(self):
        choices = self.choices[self.choice_index]

        if choices == "Euh, oui, oui..." :
            self.choice_active = False
            self.choices1status = ["fini"]
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        elif choices == "Non, moi je viens voir Gandalf":
            self.choice_active = False
            self.cut = 3
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()
        
        
    def render_scene_0(self):
        self._render_dialogue_box("C’est vous qui êtes venu pour le poste d’assistant ?")

    def render_scene_1(self):
        self._render_dialogue_box_penaud("Bien, alors on va pouvoir commencer.")
        
    def render_scene_2(self):
        self._render_dialogue_box("")

    def render_scene_3(self):
        self._render_dialogue_box_penaud("Il vous reçevra si vous passez la première CRRRRZZZK de l’entretien. Si vous êtes prêt, on va pouvoir commencer.")

    def render_scene_4(self):
        self._render_dialogue_box_penaud("Votre but est de répondre aux besoins de sa seigneurie. On va tester votre aptitude à répondre CRRRRRR rapidement à ses besoins. Pour commencer, la CRRRRRZZZZK ISI de sa seigneurie s’est encore échappée ! Rattapez-là et CZZZZZZRRRRK rapportez-là moi.")

    def render_scene_5(self):
        self._render_dialogue_box("")
        self.game.portier4_2dialogue1_done = True

    def render_scene_6(self):
        self._render_dialogue_box("Apportez-moi la CRRRZZZZKZKZZZZ ISI de sa seigneurie.")

    def render_scene_7(self):
        self._render_dialogue_box("")

    def render_scene_8(self):
        self._render_dialogue_box("Mais non, voyons ! Regardez, cet animal est tout long, avec une allure reptilienne. La CRRRRRRKK ISI de sa seigneurie n’a pas la même forme. Revenez tenter votre chance une autre fois.")

    def render_scene_9(self):
        self._render_dialogue_box("")
        self.game.teleport_to_map("monde4_N", [22, 19])
        self.game.event = None
        self.has_teleported = True
        self.game.portier4_2dialogue1_done = False
        self.game.portier4_2dialogue2_done = False
        self.game.portier4_2dialogue3_done = False
        self.game.lezard = False
        self.game.serpent = False 
        self.game.grenouille = False
        self.game.herbe = False
        self.game.bocal = False 
        self.game.baton = False
        self.game.inun = False
        self.game.amoka = False 
        self.game.isi = False

    def render_scene_10(self):
        self._render_dialogue_box("Bien, bien... Excellent. C’est sa seigneurie qui va être contente.")

    def render_scene_11(self):
        self._render_dialogue_box("Tant qu’à faire, allez la remettre dans sa CZZZZZKKZZZZ ANON, c'est sur la table.")

    def render_scene_12(self):
        self._render_dialogue_box("")
        self.game.portier4_2dialogue2_done = True

    def render_scene_13(self):
        self._render_dialogue_box("Remettez la grenouille dans sa CZZZZZKKZZZZ ANON sur la table.")

    def render_scene_14(self):
        self._render_dialogue_box("")

    def render_scene_15(self):
        self._render_dialogue_box("Ah, ce n’est pas le bon endroit. Elle préfère les lieux anon, comme les maisons, les pots, les voitures, enfin les choses à peu près rondes avec un contenant. Revenez plus tard réessayer si vous voulez.")

    def render_scene_16(self):
        self._render_dialogue_box("")
        self.game.teleport_to_map("monde4_N", [22, 19])
        self.game.event = None
        self.has_teleported = True
        self.game.portier4_2dialogue1_done = False
        self.game.portier4_2dialogue2_done = False
        self.game.portier4_2dialogue3_done = False
        self.game.lezard = False
        self.game.serpent = False 
        self.game.grenouille = False
        self.game.herbe = False
        self.game.bocal = False 
        self.game.baton = False
        self.game.inun = False
        self.game.amoka = False 
        self.game.isi = False

    def render_scene_17(self):
        self._render_dialogue_box("Excellent. Vous faites vraiment du très bon travail.")

    def render_scene_18(self):
        self._render_dialogue_box("Dernière étape. Si vous la réussissez, alors vous pourrez aller voir Gandalf pour la suite.")

    def render_scene_19(self):
        self._render_dialogue_box("Sa seigneurie est en train de faire un gateau, mais elle a oublié de prendre la farine. Allez lui prendre dans le placard.")

    def render_scene_20(self):
        self._render_dialogue_box("")
        self.game.portier4_2dialogue3_done = True

    def render_scene_21(self):
        self._render_dialogue_box("Allez prendre de la farine dans le placard à droite.")

    def render_scene_22(self):
        self._render_dialogue_box("")

    def render_scene_23(self):
        self._render_dialogue_box("ahahah ! ça c’est la nourriture de l’animal de sa seigneurie, je doute que ça donne un beau gateau ! non, ce que sa seigneurie cherche à mettre dans son gateau, c’est quelque chose de très fin, comme de la poussière. Revenez une autre fois.")

    def render_scene_24(self):
        self._render_dialogue_box("")
        self.game.teleport_to_map("monde4_N", [22, 19])
        self.game.event = None
        self.has_teleported = True
        self.game.portier4_2dialogue1_done = False
        self.game.portier4_2dialogue2_done = False
        self.game.portier4_2dialogue3_done = False
        self.game.lezard = False
        self.game.serpent = False 
        self.game.grenouille = False
        self.game.herbe = False
        self.game.bocal = False 
        self.game.baton = False
        self.game.inun = False
        self.game.amoka = False 
        self.game.isi = False

    def render_scene_25(self):
        self._render_dialogue_box("ah non, ça ce sont les graines pour les oiseaux. Ce que sa seigneurie veut mettre dans le gateau est beaucoup plus fin, fin comme de la poussière ! Revenez essayer une autre fois si vous voulez. Bonne chance ! ")

    def render_scene_26(self):
        self._render_dialogue_box("")
        self.game.teleport_to_map("monde4_N", [22, 19])
        self.game.event = None
        self.has_teleported = True
        self.game.portier4_2dialogue1_done = False
        self.game.portier4_2dialogue2_done = False
        self.game.portier4_2dialogue3_done = False
        self.game.lezard = False
        self.game.serpent = False 
        self.game.grenouille = False
        self.game.herbe = False
        self.game.bocal = False 
        self.game.baton = False
        self.game.inun = False
        self.game.amoka = False 
        self.game.isi = False

    def render_scene_27(self):
        self._render_dialogue_box("Bravo ! Bravo bravo ! Vous êtes très efficace dites donc ! Je vous en prie, passez dans la salle suivante rencontrer Gandalf, il vous parlera des modalités de votre contrat !")
        self.game.portier4_2_cache = True