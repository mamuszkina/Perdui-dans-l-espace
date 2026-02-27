import pygame

import config
from game_state import GameState
from game_state import grayscale



class PNJ3:
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
        self.charlie_surpris = pygame.image.load("imgs/characters/C_surpris.png").convert_alpha()
        self.charlie_surpris = pygame.transform.scale(self.charlie_surpris, (config.SCREEN_WIDTH //5, config.SCREEN_HEIGHT //1.1))
        self.charlie_gray = grayscale(self.charlie)
        self.PNJ = pygame.image.load("imgs/characters/enfant_un.png").convert_alpha()
        self.PNJ = pygame.transform.flip(self.PNJ, True, False)
        self.PNJ = pygame.transform.scale(self.PNJ, (config.SCREEN_WIDTH//5, config.SCREEN_HEIGHT//1.1))
        self.PNJ_gray = grayscale(self.PNJ)

        self.cut = 0
        self.max_cut = 4

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
        self.choices1 = ["Rester", "Partir"]
        self.choices2 = ["Insister", "Ne pas insister"]
        self.choices1status = ["attente"]
        self.choices2status = ["attente"]
        self.goodbye = False                     # True après "n'hésite pas à revenir"

    def load(self):
        self.current_char = 0
        self.last_update = pygame.time.get_ticks()
  
    def update(self):
        if self.cut == 3:
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
                        self.choice_index = (self.choice_index - 1) % 2
                    elif event.key == pygame.K_DOWN:
                        self.choice_index = (self.choice_index + 1) % 2
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

        # --- Déclenchement de la question à choix multiple ---
        # On pose la question sur la case 2 (cut == 2), UNE SEULE fois,
        # tant que le joueur n'a pas répondu "oui".

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
        elif (
            self.cut == 2
            and self.choices2status == ["attente"]
            and not self.goodbye
            and not self.choice_active
        ):
            self.choices = self.choices2
            self.choice_active = True
            self.choice_index = 0
    
    def render(self):
        # Si on a choisi "non" -> message d'au revoir
        if self.goodbye:
            self.render_goodbye()
            return

        if self.game.PNJ3_dialogue_done == True and self.cut == 0:
            self.cut = 4

        # Si le menu de choix est actif, on l'affiche par-dessus le reste
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
        dialogue_rect = self.screen.blit(self.dialogPNJ, (config.SCREEN_WIDTH // 2.8, config.SCREEN_HEIGHT // 1.4))       # chiffres = position bulle de dialogue
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

    # --- NOUVEAU : message quand le joueur répond "non" ---
    def render_goodbye(self):
        self._render_dialogue_box("... Au revoir ...")

    # --- NOUVEAU : logique des réponses ---
    def handle_choice(self):
        choices = self.choices[self.choice_index]

        if choices == "Rester":
            # On désactive le menu, on marque la question comme répondue
            # et on laisse cut à 2 : la prochaine fois, render_scene_2
            # ("Attendez, je vous prépare ça.") sera affichée.
            self.choice_active = False
            self.choices1status = ["fini"]
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        elif choices == "Partir":
            # On affiche "N'hésite pas à revenir." puis on attend Entrée
            # pour fermer l'événement.
            self.choice_active = False
            self.goodbye = True
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        elif choices == "Insister":
            # On désactive le menu, on marque la question comme répondue
            # et on laisse cut à 2 : la prochaine fois, render_scene_2
            # ("Attendez, je vous prépare ça.") sera affichée.
            self.choice_active = False
            self.choices2status = ["fini"]
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        elif choices == "Ne pas insister":
            # On affiche "N'hésite pas à revenir." puis on attend Entrée
            # pour fermer l'événement.
            self.choice_active = False
            self.goodbye = True
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()
    
    def render_scene_0(self):
        self._render_dialogue_box(".........................................")

    def render_scene_1(self):
        self._render_dialogue_box("...........................................")

    def render_scene_2(self):
        self._render_dialogue_box("...Bonjour... J'aime pas trop parler aux gens en vrai...")
        self.game.PNJ3_dialogue_done = True

    def render_scene_3(self):
        self._render_dialogue_box("")

    def render_scene_4(self):
        self._render_dialogue_box("Non, sérieusement, j'ai pas envie de parler...")