import pygame

import config
from game_state import GameState
from game_state import grayscale


class Gandalf3:
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
        self.PNJ = pygame.image.load("imgs/characters/gandalf.png").convert_alpha()
        self.PNJ = pygame.transform.flip(self.PNJ, True, False)
        self.PNJ = pygame.transform.scale(self.PNJ, (config.SCREEN_WIDTH//5, config.SCREEN_HEIGHT//1.1))
        self.PNJ_gray = grayscale(self.PNJ)
        
        #Eclair adapté taille écran
        self.ECLAIR_BLANC = pygame.image.load("imgs/ECLAIR_BLANC.jpg").convert_alpha()
        self.ECLAIR_BLANC = pygame.transform.scale(self.ECLAIR_BLANC, (config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
        # Son de tonnerre
        self.lightning_sound = pygame.mixer.Sound("sons/lightning.mp3")
        self.lightning_played = False
        self.lightning_sound.set_volume(0.8)   # entre 0.0 et 1.0
        #son drama
        self.drama_sound = pygame.mixer.Sound("sons/drama.mp3")
        self.drama_played = False
        self.drama_sound.set_volume(0.2)   # entre 0.0 et 1.0

        self.cut = 0
        self.max_cut = 71
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
        self.choices1 = ["Qui êtes-vous ?", "C'était quoi ces univers ?", "C'est quoi cet éclair et ce KABOOM ?"]
        self.choices2 = ["ça t'arrive de parler normalement ?", "Sérieusement, c'est CA ton disque de sauvegarde ?", "Euh... 4 ?"]
        self.choices1status = ["attente"]
        self.choices2status = ["attente"]

    def load(self):
        self.current_char = 0
        self.last_update = pygame.time.get_ticks()
  
    def update(self):
        if self.has_teleported:
            return
        if self.cut > self.max_cut:
            self.game.teleport_to_map("monde4", [10, 20])  # [1, 4] = entry position on map 01
            self.game.event = None
            self.has_teleported = True
            self.lightning_sound.stop()
            self.game.mondes123.set_volume(0.8)

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
            self.cut == 4
            and self.choices1status == ["attente"]
            and not self.choice_active
        ):
            self.choices = self.choices1
            self.choice_active = True
            self.choice_index = 0
        elif (
            self.cut == 12
            and self.choices1status == ["attente"]
            and not self.choice_active
        ):
            self.choices = self.choices1
            self.choice_active = True
            self.choice_index = 0
        elif (
            self.cut == 26
            and self.choices1status == ["attente"]
            and not self.choice_active
        ):
            self.choices = self.choices1
            self.choice_active = True
            self.choice_index = 0
        elif (
            self.cut == 36
            and self.choices1status == ["attente"]
            and not self.choice_active
        ):
            self.choices = self.choices1
            self.choice_active = True
            self.choice_index = 0
        elif (
            self.cut == 66
            and self.choices2status == ["attente"]
            and not self.choice_active
        ):
            self.choices = self.choices2
            self.choice_active = True
            self.choice_index = 0

            
    def render(self):
        if self.game.Gandalf3_QuiEtesVous_dialogue_done == True and self.game.Gandalf3_KABOOM_dialogue_done == True and self.game.Gandalf3_UniversAvant_dialogue_done == True and self.cut < 37:
            self.cut = 37
            return

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
        elif self.cut == 50:
            self.render_scene_50()
        elif self.cut == 51:
            self.render_scene_51()
        elif self.cut == 52:
            self.render_scene_52()
        elif self.cut == 53:
            self.render_scene_53()
        elif self.cut == 54:
            self.render_scene_54()
        elif self.cut == 55:
            self.render_scene_55()
        elif self.cut == 56:
            self.render_scene_56()
        elif self.cut == 57:
            self.render_scene_57()
        elif self.cut == 58:
            self.render_scene_58()
        elif self.cut == 59:
            self.render_scene_59()
        elif self.cut == 60:
            self.render_scene_60()
        elif self.cut == 61:
            self.render_scene_61()
        elif self.cut == 62:
            self.render_scene_62()
        elif self.cut == 63:
            self.render_scene_63()
        elif self.cut == 64:
            self.render_scene_64()
        elif self.cut == 65:
            self.render_scene_65()
        elif self.cut == 66:
            self.render_scene_66()
        elif self.cut == 67:
            self.render_scene_67()
        elif self.cut == 68:
            self.render_scene_68()
        elif self.cut == 69:
            self.render_scene_69()
        elif self.cut == 70:
            self.render_scene_70()
        elif self.cut == 71:
            self.render_scene_71()
 

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

    def handle_choice(self):
        choices = self.choices[self.choice_index]
        
        if choices == "Qui êtes-vous ?":
            self.choice_active = False
            self.cut = 5
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        elif choices == "C'était quoi ces univers ?":
            self.choice_active = False
            self.cut = 13
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        elif choices == "C'est quoi cet éclair et ce KABOOM ?":
            self.choice_active = False
            self.cut = 27
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        elif choices == "ça t'arrive de parler normalement ?":
            self.choice_active = False
            self.choices2status = ["fini"]
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        elif choices == "Sérieusement, c'est CA ton disque de sauvegarde ?":
            self.choice_active = False
            self.choices2status = ["fini"]
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        elif choices == "Euh... 4 ?":
            self.choice_active = False
            self.choices2status = ["fini"]
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()
    
    def render_scene_0(self):
        self._render_dialogue_box("Encore toi ? Non mais c'est pas vrai, tu te fiches de moi ! Pourquoi tu es encore là !")
        self.screen.blit(self.charlie_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_1(self):
        self._render_dialogue_box_Answer("Moi je crois que c'est plutôt vous qui vous fichez de moi ! Vous deviez me ramener chez moi ! Vous m'avez dit d'oublier cette histoire complètement loufoque ! Alors non seulement je suis pas chez moi, mais en plus je peux absolument pas oublier que j'ai atterri dans un univers parralèle,")
        self.screen.blit(self.charlie_mécontent, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_2(self):
        self._render_dialogue_box_Answer("UN UNIVERS PARALLELE !!!")
        self.screen.blit(self.charlie_mécontent, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_3(self):
        self._render_dialogue_box("Calme-toi, calme-toi. Cette fois, on va être obligé de se poser de toute façon. Trois erreurs à la suite, c'est pas normal. J'ai un souci quelque part, je vais devoir reprendre ça correctement. ça nous laisse le temps de parler. Qu'est-ce que tu veux savoir ?")
        self.screen.blit(self.charlie_mécontent_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_4(self):
        self._render_dialogue_box("")

    def render_scene_5(self):
        self._render_dialogue_box("Je suis Gandalf le Grand, linguiste des univers. Je suis chargé de répertorier et d'étudier les langues de tous les univers connus et inconnus. Je créé de grandes bases de données en répertoriant les sons utilisés, les façons de former des phrases, les manières de classer des mots, etc.")
        self.screen.blit(self.charlie_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_6(self):
        self._render_dialogue_box("Je constate les points communs et les différences entre les langues. De cette façon je peux répondre à plein de questions, comment on catégorise des langues, est-ce que la façon dont on parle façonne la façon dont on pense, est-ce qu'il y a des choses communes à toutes les langues, bref plein de choses.")
        self.screen.blit(self.charlie_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_7(self):
        self._render_dialogue_box_Answer("Donc tu es un peu le gardien des langues ?")
        self.screen.blit(self.charlie, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_8(self):
        self._render_dialogue_box("Oui et non. Je ne garde rien, j'observe. Quand je peux je répertorie des langues en danger, qui sont vouées à disparaître, pour qu'il  y ait toujours des données sur ces langues. Mais je n'agis pas sur le changement des langues, sur leur diffusion ou leur disparition.")
        self.screen.blit(self.charlie_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_9(self):
        self._render_dialogue_box("Mais même s'il y a plein de choses à savoir, personnellement il y a deux sujets qui me tiennent à coeur. La catégorisation des langues (c'est-à-dire comment dans une langue on va regrouper les mots) et l'impact du genre sur la société.")
        self.screen.blit(self.charlie_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_10(self):
        self._render_dialogue_box("Enfin bref. La linguistique des univers c'est passionnant, je pourrais en parler des heures. Mais on va peut-être s'arrêter là.")
        self.screen.blit(self.charlie_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_11(self):
        self._render_dialogue_box("Tu as d'autres questions ?")
        self.screen.blit(self.charlie_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        self.game.Gandalf3_QuiEtesVous_dialogue_done = True

    def render_scene_12(self):
        self._render_dialogue_box("")

    def render_scene_13(self):
        self._render_dialogue_box("Cette fois tu étais dans l'univers qu'on appelle comunément Borde. Il s'agit du même principe que les deux autres univers où tu as été transporté : la langue n'a pas de genre. Les mots ne gardent pas de trace du genre de la personne.")
        self.screen.blit(self.charlie_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_14(self):
        self._render_dialogue_box("Dans ta langue, si je dis 'un chauffeur', tu vois directement un homme non ? Dans l'univers de Borde, on dit eune chaufeureuse. Et on ne sait pas le genre de cette personne.")
        self.screen.blit(self.charlie_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_15(self):
        self._render_dialogue_box_Answer("Mais attend, tu veux dire qu'il n'y a pas d'hommes ou de femmes dans ce monde ?")
        self.screen.blit(self.charlie_surpris, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_16(self):
        self._render_dialogue_box("Si, il y en a. Ce n'est simplement pas la première information qu'on reçoit d'une personne, rien qu'en parlant d'elle.")
        self.screen.blit(self.charlie_surpris_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_17(self):
        self._render_dialogue_box_Answer("Dans mon univers on dit 'chauffeur' ou 'chauffeuse', c'est bien plus facile. J'ai pas envie de dénaturer ma langue ou d'invisibiliser le genre des personnes.")
        self.screen.blit(self.charlie_mécontent, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_18(self):
        self._render_dialogue_box("C'est le destin de toutes les langues d'être 'dénaturées'. Les langues changent en fonction de leur utilisation, c'est ce qui fait qu'une langue est en vie. Dans certains univers, des institutions ont décrété il y a longtemps que 'le genre masculin est le plus pur'. C'est à cause de ça que le masculin générique est utilisé. ça n'a rien de naturel.")
        self.screen.blit(self.charlie_mécontent_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_19(self):
        self._render_dialogue_box("D'ailleurs, quand tu parles d'invisibilisation, le masculin générique (donc la règle qui dit que le masculin l'emporte sur le féminin) participe beaucoup à l'invisibilisation des femmes dans une société.")
        self.screen.blit(self.charlie_mécontent_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_20(self):
        self._render_dialogue_box_Answer("Je ne suis pas d'accord avec toi... C'est une règle qu'on apprend très tôt à l'école, donc on a conscience que quand on parle au masculin, il peut y avoir des femmes dans un groupe.")
        self.screen.blit(self.charlie, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_21(self):
        self._render_dialogue_box("Détrompe-toi. Il y a des études qui montrent que dans les univers où le masculin générique est utilisé, des femmes vont moins postuler à des offres d'emploi écrites au masculin. D'autres encore montrent que si on parle à des gens d'un groupe de chanteurs (avec du masculin générique), les gens seront surpris de voir des chanteuses.")
        self.screen.blit(self.charlie_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_22(self):
        self._render_dialogue_box_Answer("Mouais, enfin, utile ou pas, j'ai pas envie que des chercheurs des univers me dictent comment parler...")
        self.screen.blit(self.charlie_mécontent, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_23(self):
        self._render_dialogue_box("ça tombe bien, ce n'est pas mon but. Moi, je me contente d'observer et de constater, parfois de chercher des solutions. J'observe qu'il y a du masculin générique, je constate que ce masculin générique participe à un biais genré dans la société, parfois je solutionne de nouvelles façons de parler pour dégenrer.")
        self.screen.blit(self.charlie_mécontent_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_24(self):
        self._render_dialogue_box("Libre aux gens d'utiliser ou pas les solutions proposées. Je ne suis pas là pour imposer. Mais trève de bavardages sur les langues.")
        self.screen.blit(self.charlie_mécontent_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_25(self):
        self._render_dialogue_box("Tu as d'autres questions ?")
        self.screen.blit(self.charlie_mécontent_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        self.game.Gandalf3_UniversAvant_dialogue_done = True

    def render_scene_26(self):
        self._render_dialogue_box("")

    def render_scene_27(self):
        self._render_dialogue_box("ça, mon cher, ce sont les planètes qui font du billard. Enfin pas toutes seules hein, elle sont pas mal aidées par des sur-humains, ou des super-héros, enfin selon comment tu les appelles.")
        self.screen.blit(self.charlie_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_28(self):
        self._render_dialogue_box_Answer("Attend QUOI ?")
        self.screen.blit(self.charlie_surpris, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_29(self):
        self._render_dialogue_box("Oui, en gros c'est des gens qui se crééent des embrouilles pour rien, gnégnégné c'est moi le plus fort, gnagnagna je vais casser ta planète,... là je crois que cette fois-ci c'est un certain San-gotham qui se prend la tête avec un Réfree-zérateur, une histoire de planète à détruire je crois.")
        self.screen.blit(self.charlie_surpris_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_30(self):
        self._render_dialogue_box("Sauf que du coup, bah pour se battre, évidemment ils n'ont rien trouvé de mieux que de se balancer des planètes sur la tronche ! Et donc de les déplacer et reconfigurer tout le temps les conditions socio-climatiques des planètes ! Et qui c'est qui doit tout remettre en place par derrière ?! Bah c'est bibi !")
        self.screen.blit(self.charlie_surpris_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_31(self):
        self._render_dialogue_box_Answer("Attend vous êtes en train de me dire que si je me retrouve loin de chez moi, c'est parce que des super-héros se battent avec des planètes ?!")
        self.screen.blit(self.charlie_surpris, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_32(self):
        self._render_dialogue_box("Se battent, se chamaillent, jouent aux quilles, ça dépend. Le souci c'est que déplacer une planète peut avoir des conséquences déstastreuses pour les habitants. Si une planète bouge plus près du Soleil, plus loin d'un trou noir, si elle entre en collision avec une autre, enfin jte dis pas la galère...")
        self.screen.blit(self.charlie_surpris_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_33(self):
        self._render_dialogue_box("Et quand les planètes sont lancées trop fort, on peut avoir des... des bugs si tu veux. Des choses, ou des gens (comme toi) qui ont été propulsées plus loin, et qui se retrouvent sur une autre planète.")
        self.screen.blit(self.charlie_surpris_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_34(self):
        self._render_dialogue_box("Moi normalement (comme si j'avais que ça à faire !) je remet la planète à sa place, puis je lance un appel à tous les gens qui se seraient égarés, et zou, je les ramène chez eux. Mais cette fois, j'y arrive pas...")
        self.screen.blit(self.charlie_surpris_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_35(self):
        self._render_dialogue_box("Tu as d'autres questions ?")
        self.screen.blit(self.charlie_surpris_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        self.game.Gandalf3_KABOOM_dialogue_done = True

    def render_scene_36(self):
        self._render_dialogue_box("")

    def render_scene_37(self):
        self._render_dialogue_box("Je comprend pas pourquoi j'arrive pas à te ramener chez toi, mes calculs doivent être faux... Ta planète est bien située à (33 673 ± 42stat ± 71sys) al (1 312 ± 13stat ± 22sys) pc[ de distance du centre galactique ?")
        self.screen.blit(self.charlie_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_38(self):
        self._render_dialogue_box_Answer("Euh vous attendez pas VRAIMENT une réponse pas vrai ? Moi la seule chose que je sais c'est que j'allais tranquillement acheter mon pain, puis j'ai vu un immense éclair (dans le magasin, oui oui !) et...")
        self.screen.blit(self.charlie_surpris, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_39(self):
        self._render_dialogue_box("Attend tu as vu un quoi ?! Un éclair ??")
        self.screen.blit(self.charlie_surpris_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_40(self):
        self._render_dialogue_box_Answer("Oui ! Et puis j'ai entendu un grand KABOOM et...")
        self.screen.blit(self.charlie, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_41(self):
        self._render_dialogue_box("Attend attend attend... attend... Ils n'auraient quand même pas...")
        self.screen.blit(self.charlie_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_42(self):
        self._render_dialogue_box("..........................................................")
        self.screen.blit(self.charlie_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_43(self):
        self._render_dialogue_box("...................................................")
        self.screen.blit(self.charlie_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_44(self):
        self._render_dialogue_box("Je le savais ! Quels mufles ! ça devait bien arriver un jour ! Ils ont déchiré l'espace-temps !")
        self.screen.blit(self.charlie_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        if not self.drama_played:
            self.game.mondes123.set_volume(0)          # Pause la musique de fond
            self.drama_sound.play()         # Joue le tonnerre
            self.drama_played = True
        
    def render_scene_45(self):
        self._render_dialogue_box_Answer("Ils ont déchiré l'espace-quoi ?!")
        self.screen.blit(self.charlie_surpris, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_46(self):
        self._render_dialogue_box("Tu n'as pas bougé, tu es toujours sur ta planète d'origine ! Et ta planète d'origine n'a pas changé de galaxie, mais d'univers ! L'espace-temps a été entièrement brouillé après qu'ils aient lancé trop fort leurs satanées planètes-boules-de-pétanque !")
        self.screen.blit(self.charlie_surpris_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_47(self):
        self._render_dialogue_box_Answer("Mais-mais tu sais régler ça pas vrai ?! Je veux pas être coincé dans un autre espace-temps moi !")
        self.screen.blit(self.charlie_surpris, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_48(self):
        self._render_dialogue_box("Ah ben ça, c'est plus difficile que prévu... Je vais être obligé de réinstaller tout les systèmes galactiques et universaux... En espérant que la mise à jour n'entraine pas trop de soucis...")
        self.screen.blit(self.charlie_surpris_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_49(self):
        self._render_dialogue_box("............ ça y est. Je lance la mise à jour. C'est le moment de prier, jeune Charlie.")
        self.screen.blit(self.charlie_surpris_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_50(self):
        if self.drama_played:
            self.drama_sound.stop()
            self.drama_played = False
        if not self.lightning_played:
            self.lightning_sound.play()         # Joue le tonnerre
            self.lightning_played = True
        self._render_dialogue_box_Lightning("KABOOM")

    def render_scene_51(self):
        if self.lightning_played:
            self.lightning_sound.stop()
            self.game.mondes123.set_volume(0.8)
            self.lightning_played = False
        self._render_dialogue_box(".................................. C'est bon ! ça a marché ! Tout est remis en place !")
        self.screen.blit(self.charlie_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_52(self):
        self._render_dialogue_box_Answer("Ahhhhh c'est une excellente nouvelle ! Je vais enfin pouvoir rentrer chez moi !")
        self.screen.blit(self.charlie_content, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_53(self):
        self._render_dialogue_box("Oui ! Je suis bien sur la Terre, dans le bon espace-temps ! Tu habites où ?")
        self.screen.blit(self.charlie_content_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_54(self):
        self._render_dialogue_box_Answer("A paris.")
        self.screen.blit(self.charlie_content, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_55(self):
        self._render_dialogue_box(".................................")
        self.screen.blit(self.charlie_content_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_56(self):
        self._render_dialogue_box(".....................................")
        self.screen.blit(self.charlie_content_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_57(self):
        self._render_dialogue_box(".......................................")
        self.screen.blit(self.charlie_content_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_58(self):
        self._render_dialogue_box_Answer("J'aime pas ce silence.")
        self.screen.blit(self.charlie_mécontent, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_59(self):
        self._render_dialogue_box("Tu vas rire. La mise a jour a supprimé tout mon système de sauvegarde. ")
        self.screen.blit(self.charlie_mécontent_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_60(self):
        self._render_dialogue_box_Answer("Et concrètement ça veut dire quoi ?")
        self.screen.blit(self.charlie, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_61(self):
        self._render_dialogue_box("Ben que je sais pas où est Paris. Mais c’est pas grave c’est pas grave. Ça va juste prendre plus de temps mais je vais te ramener manuellement chez toi, avec le jeu de données de mon disque de sauvegarde externe.")
        self.screen.blit(self.charlie_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_62(self):
        self._render_dialogue_box_Answer("Et, elle date d’il y a longtemps ta dernière sauvegarde ?")
        self.screen.blit(self.charlie, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_63(self):
        self._render_dialogue_box("Pas trop longtemps, enfin, disons qu’elle date d’un temps raisonnable. Je devrais pouvoir te ramener chez toi avec une légère marge d’erreur d’une centaine de kilomètres si tu réponds à quelques questions.")
        self.screen.blit(self.charlie_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_64(self):
        self._render_dialogue_box_Answer("J'ai peur de tes questions.")
        self.screen.blit(self.charlie, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_65(self):
        self._render_dialogue_box("Donc. C'est quoi le mode de dissémination de ta langue ?")
        self.screen.blit(self.charlie_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_66(self):
        self._render_dialogue_box("Bon, bon... quelles sont les caractéristiques de ta classification nominale ?")
        self.screen.blit(self.charlie_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_67(self):
        self._render_dialogue_box_Answer("Mais euh si je te dis que je parle français, tu peux pas me ramener à partir de ça ?")
        self.screen.blit(self.charlie_surpris, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_68(self):
        self._render_dialogue_box("Ah non, les noms des langues j’ai jamais écrit. Ça serait peut-être une bonne idée de l’ajouter plus tard, tiens.")
        self.screen.blit(self.charlie_surpris_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_69(self):
        self._render_dialogue_box_Answer("Mais du coup tu ne sais pas où me ramener sur terre !")
        self.screen.blit(self.charlie_surpris, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_70(self):
        self._render_dialogue_box("Bon. Ben on va tenter un truc au hasard. Si c’est pas le bon endroit, je vais m’incarner vers chez toi, au cas où. Tu n’auras qu’à me contacter et on réessaiera. Allez, bonne chance !")
        self.screen.blit(self.charlie_surpris_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_71(self):
        if not self.lightning_played:
            self.game.mondes123.set_volume(0)          # Pause la musique de fond
            self.lightning_sound.play()         # Joue le tonnerre
            self.lightning_played = True
        self._render_dialogue_box_Lightning("KABOOM")
        self.game.tp_monde4 = True