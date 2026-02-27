import pygame

import config
from game_state import GameState
from game_state import grayscale


class PNJ10:
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
     
        self.PNJ = pygame.image.load("imgs/characters/enfant_un.png").convert_alpha()
        self.PNJ = pygame.transform.flip(self.PNJ, True, False)
        self.PNJ = pygame.transform.scale(self.PNJ, (config.SCREEN_WIDTH//5, config.SCREEN_HEIGHT//1.1))
        self.PNJ_gray = grayscale(self.PNJ)

        self.cut = 0
        self.max_cut = 24

        # Typewriter state when creating the PNJ
        self.char_delay_ms = 30                     # 1= très rapide ; 100= très lent
        self.current_char = 0
        self.last_update = 0
        self.current_dialogue_total_chars = 0

        # --- Nouveaux attributs pour le choix multiple ---
        self.choice_active = False               # True quand on affiche les choix
        self.choice_index = 0                    # index du choix sélectionné
        self.choices = ["0"]
        self.choices1 = ["T'aurais pas des clefs à me passer ?", "C'est toi Cordelia ?"]
        self.choices1status = ["attente"]
        self.choices2 = ["C'est ici la maison de Priss ?", "T'as vraiment aucune clef à me passer ?"]
        self.choices2status = ["attente"]
        self.choices3 = ["T'es vraiment CERTAIN que t'as pas de clef ?" , "C'est ton écriture ?"]
        self.choices3status = ["attente"]
        self.goodbye = False                     # True après "n'hésite pas à revenir"

    def load(self):
        self.current_char = 0
        self.last_update = pygame.time.get_ticks()
  
    def update(self):
        if self.cut == 1:
            self.game.event = None
        elif self.cut == 3:
            self.game.event = None
        elif self.cut == 6:
            self.game.event = None
        elif self.cut == 14:
            self.game.event = None
        elif self.cut == 21:
            self.game.event = None
        elif self.cut == 24:
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

        # --- Déclenchement de la question à choix multiple ---
        # On pose la question sur la case 2 (cut == 2), UNE SEULE fois,
        # tant que le joueur n'a pas répondu "oui".

        if (
            self.cut == 4
            and self.choices1status == ["attente"]
            and not self.goodbye
            and not self.choice_active
        ):
            self.choices = self.choices1
            self.choice_active = True
            self.choice_index = 0

        elif (
            self.cut == 7
            and self.choices2status == ["attente"]
            and not self.goodbye
            and not self.choice_active
        ):
            self.choices = self.choices2
            self.choice_active = True
            self.choice_index = 0

        elif (
            self.cut == 15
            and self.choices3status == ["attente"]
            and not self.goodbye
            and not self.choice_active
        ):
            self.choices = self.choices3
            self.choice_active = True
            self.choice_index = 0
    
    def render(self):
        if self.goodbye:
            self.render_goodbye()
            return

        if self.game.PNJ8_dialogue_done == False and self.game.PNJ7_dialogue_done == True and self.cut < 2:
            self.cut = 2
            return

        if self.game.PNJ8_dialogue_done == True and self.game.PNJ9_dialogue_done == False and self.cut < 4:
            self.cut = 4
            return

        if self.game.PNJ9_dialogue_done == True and self.game.Maison_papier_dialogue_done == False and self.cut < 7:
            self.cut = 7
            return

        if self.game.Maison_papier_dialogue_done == True and self.game.PNJ10_dialogue_done == False and self.cut < 15:
            self.cut = 15
            return

        if self.game.PNJ10_dialogue_done == True and self.game.PNJ7_2_dialogue_done == False and self.cut < 22:
            self.cut = 22
            return

        if self.game.PNJ7_2_dialogue_done == True and self.cut < 24:
            self.cut = 24
            return

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

    # --- NOUVEAU : logique des réponses ---
    def handle_choice(self):
        choices = self.choices[self.choice_index]

        if choices == "T'aurais pas des clefs à me passer ?":
            self.choice_active = False
            self.goodbye = True
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        elif choices == "C'est toi Cordelia ?":
            self.choice_active = False
            self.choices1status = ["fini"]
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        elif choices == "T'as vraiment aucune clef à me passer ?":
            self.choice_active = False
            self.goodbye = True
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        elif choices == "C'est ici la maison de Priss ?":
            self.choice_active = False
            self.choices2status = ["fini"]
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        elif choices == "C'est ton écriture ?":
            self.choice_active = False
            self.choices3status = ["fini"]
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        elif choices == "T'es vraiment CERTAIN que t'as pas de clef ?":
            self.choice_active = False
            self.choices3status = ["fini"]
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

    def render_goodbye(self):
        self._render_dialogue_box("Une clef ? Mh, si le lieu est fermé, et que tu n'as pas la clef, c'est peut-être qu'il y a une bonne raison, non ?")
        self.screen.blit(self.charlie_penaud_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

#SCENE ZERO
    def render_scene_0(self):
        self._render_dialogue_box("Gandalf de la Scène Errès ? Connais pas. Peut-être an nouval.")
        self.screen.blit(self.charlie_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        self.game.unlock_pokedex_entry(2, "PNJ10.0")

    def render_scene_1(self):
        self._render_dialogue_box("")
        
#SCENE UN
    def render_scene_2(self):
        self._render_dialogue_box("Une clef ? ça ne me dit rien non...")
        self.screen.blit(self.charlie_penaud_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_3(self):
        self._render_dialogue_box("")

#SCENE DEUX
    def render_scene_4(self):
        self._render_dialogue_box("Cordelia ? Non, moi c'est Anatol.")
        self.screen.blit(self.charlie_penaud_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_5(self):
        self._render_dialogue_box("Où se trouve Cordelia ? J'en sais rien moi, je lu surveille pas !")
        self.screen.blit(self.charlie_penaud_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        self.game.unlock_pokedex_entry(2, "PNJ10.1")

    def render_scene_6(self):
        self._render_dialogue_box("")

#SCENE TROIS
    def render_scene_7(self):
        self._render_dialogue_box("Ah non, ici c'est la maison de mes parents. Pourquoi tu cherches la maison de mu tancle ?")
        self.screen.blit(self.charlie_penaud_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        self.game.unlock_pokedex_entry(2, "PNJ10.2")

    def render_scene_8(self):
        self._render_dialogue_box_Answer("J'ai besoin des clefs du labo.")
        self.screen.blit(self.charlie, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
    
    def render_scene_9(self):
        self._render_dialogue_box_Answer("Avec les clef du labo je peux ouvrir les portes de la Scène Errès parce que peut-être que dedans il y a une personne qui pourra m'aider à rentrer chez moi.")
        self.screen.blit(self.charlie, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_10(self):
        self._render_dialogue_box("Pourquoi tu rentres pas directement chez toi ?")
        self.screen.blit(self.charlie_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_11(self):
        self._render_dialogue_box_Answer("C'est que je sais même pas où c'est chez moi. C'est dans un autre espace-temps, ou je sais pas quoi...")
        self.screen.blit(self.charlie_penaud, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_12(self):
        self._render_dialogue_box("Un autre espace-temps... Mais bien sûr ! Dis donc, c'est pas parce que j'ai huit ans et demi qu'il faut me raconter des salades ! Si tu veux pas me dire pourquoi tu cherches la maison de mu tancle, t'as qu'à juste pas me le dire !")
        self.screen.blit(self.charlie_penaud_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_13(self):
        self._render_dialogue_box_Answer("Mais je .....Oh et puis zut !")
        self.screen.blit(self.charlie_mécontent, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_14(self):
        self._render_dialogue_box("")
    
#SCENE QUATRE
    def render_scene_15(self):
        self._render_dialogue_box("Hé mais c'est mon papier !")
        self.screen.blit(self.charlie_penaud_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_16(self):
        self._render_dialogue_box_Answer("Donc c'est toi qui a laissé ce mot ?")
        self.screen.blit(self.charlie_surpris, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_17(self):
        self._render_dialogue_box("Oui oui c’est moi ! Camille et moi, on voulait aller prendre du carton dans le labo pour faire un château !")
        self.screen.blit(self.charlie_surpris_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_18(self):
        self._render_dialogue_box_Answer("Ah super, alors tu vas pouvoir me passer cette fichue clef !")
        self.screen.blit(self.charlie, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_19(self):
        self._render_dialogue_box("Ben je voudrais bien, mais c’est que je l’ai pas moi ! à la fin Camille a dit qu’al allait tout ranger, donc al a gardé les cartons et la clef. Vous devriez aller lu voir.")
        self.screen.blit(self.charlie_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_20(self):
        self._render_dialogue_box_Answer("Quoi ? Mais c'est la première personne à qui j'ai demandé ! Il va m'entendre ce fieffé filou !")
        self.screen.blit(self.charlie_mécontent, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_21(self):
        self._render_dialogue_box_Answer("")
        self.game.PNJ10_dialogue_done = True

#SCENE CINQ
    def render_scene_22(self):
        self._render_dialogue_box_Answer("Je ferais mieux d'aller voir Camille. Ce félon !")
        self.screen.blit(self.charlie_mécontent, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_23(self):
        self._render_dialogue_box_Answer("")

#SCENE SIX
    def render_scene_24(self):
        self._render_dialogue_box("ça y est ? T'as trouvé ta clef ?")