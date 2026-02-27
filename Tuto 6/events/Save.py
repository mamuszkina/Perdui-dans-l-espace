import pygame

import config
from game_state import GameState


class Save:
    def __init__(self, screen, game, player):
        self.screen = screen
        self.game = game
        self.player = player

        self.dialog = pygame.image.load("imgs/dialog2.png").convert_alpha()
        self.dialog = pygame.transform.scale(self.dialog, (config.SCREEN_WIDTH//3.5, config.SCREEN_HEIGHT//4.5))

        self.cut = 0
        self.max_cut = 24

        # Typewriter state when creating the PNJ
        self.char_delay_ms = 30                       # 1= très rapide ; 100= très lent
        self.current_char = 0
        self.last_update = 0
        self.current_dialogue_total_chars = 0

        # --- Nouveaux attributs pour le choix multiple ---
        self.choice_active = False               # True quand on affiche les choix
        self.choice_index = 0                    # index du choix sélectionné
        self.choices = ["0"]
        self.choices1 = ["Oui", "Non"]

        # --- Saisie de texte (mot secret) ---
        # À la fin du dialogue, Save0 ouvre une zone de saisie.
        # Si le joueur tape "badaboum" puis Entrée, on le téléporte au monde1
        # aux mêmes coordonnées.
        self.input_active = False
        self.secret_word1 = "chocolat"            #!! que des minuscules !
        self.secret_word2 = "noyau"
        self.secret_word3 = "xanders"
        self.secret_word4 = "soquette"
        self.secret_word5 = "rififi"
        self.secret_word6 = "unicorn"

        self.has_teleported = False

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

                # --- Mode saisie actif : on capte les lettres ---
                elif self.input_active:
                    # Entrée : valider
                    if event.key == pygame.K_RETURN:
                        if self.input_text.strip().lower() == self.secret_word1:
                            self.input_active = False
                            self.cut = 9
                        elif self.input_text.strip().lower() == self.secret_word2:
                            self.input_active = False
                            self.cut = 11
                        elif self.input_text.strip().lower() == self.secret_word3:
                            self.input_active = False
                            self.cut = 13
                        elif self.input_text.strip().lower() == self.secret_word4:
                            self.input_active = False
                            self.cut = 15
                        elif self.input_text.strip().lower() == self.secret_word5:
                            self.input_active = False
                            self.cut = 17
                        elif self.input_text.strip().lower() == self.secret_word6:
                            self.input_active = False
                            self.cut = 19
                        else:
                            self.input_active = False
                            self.cut = 21
                    # Retour arrière
                    elif event.key == pygame.K_BACKSPACE:
                        self.input_text = self.input_text[:-1]
                    else:
                        # Ajout de caractères imprimables
                        if event.unicode and event.unicode.isprintable():
                            # limite simple pour éviter les débordements
                            if len(self.input_text) < 24:
                                self.input_text += event.unicode

                # --- Mode choix actif : flèches + Entrée gèrent le menu ---
                elif self.choice_active:
                    if event.key == pygame.K_UP:
                        self.choice_index = (self.choice_index - 1) % 2
                    elif event.key == pygame.K_DOWN:
                        self.choice_index = (self.choice_index + 1) % 2
                    elif event.key == pygame.K_RETURN:
                        self.handle_choice()

                # --- Dialogue normal : Entrée avance les cases ---
                elif event.key == pygame.K_RETURN:
                    if self.current_char < self.current_dialogue_total_chars:
                        self.current_char = self.current_dialogue_total_chars
                    else:
                        # Si on est sur la dernière case de dialogue,
                        # on ouvre la zone de saisie au lieu de fermer.
                        if self.cut == 8 :
                            self.input_active = True
                            self.input_text = ""
                            self.input_feedback = ""
                        else:
                            self.cut += 1
                            self.current_char = 0
                            self.last_update = pygame.time.get_ticks()

        now = pygame.time.get_ticks() # mise à jour du texte
        if now - self.last_update > self.char_delay_ms:
            self.current_char += 1
            self.last_update = now    



        if (
            self.cut in (10, 12, 14, 16, 18, 20, 23)
            and not self.choice_active
        ):
            self.choices = self.choices1
            self.choice_active = True
            self.choice_index = 0
    
    def render(self):
        # Zone de saisie (après la fin du dialogue)
        if self.input_active:
            self.render_input()
            return

        # Si le menu de choix est actif, on l'affiche par-dessus le reste
        if self.choice_active:
            self.render_choice()
            return

        if self.game.tp_monde1 == False and self.game.tp_monde1 == False and self.game.tp_monde2 == False and self.game.tp_monde3 == False and self.game.tp_monde4 == False and self.game.tp_monde5 == False and self.game.tp_monde6 == False and self.cut == 2 :
            self.cut = 8

        if self.game.tp_monde1 == True and self.game.tp_monde2 == False :
            if self.cut == 1 :
                self.cut = 2
            elif self.cut == 3 :
                self.cut = 8

        if self.game.tp_monde2 == True and self.game.tp_monde3 == False :
            if self.cut == 1 :
                self.cut = 2
            elif self.cut == 4 :
                self.cut = 8

        if self.game.tp_monde3 == True and self.game.tp_monde4 == False :
            if self.cut == 1 :
                self.cut = 2
            elif self.cut == 5 :
                self.cut = 8

        if self.game.tp_monde4 == True and self.game.tp_monde5 == False :
            if self.cut == 1 :
                self.cut = 2
            elif self.cut == 6 :
                self.cut = 8

        if self.game.tp_monde5 == True and self.game.tp_monde6 == False :
            if self.cut == 1 :
                self.cut = 2
            elif self.cut == 7 :
                self.cut = 8

        if self.game.tp_monde5 == True and self.game.tp_monde6 == True :
            if self.cut == 1 :
                self.cut = 2

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

    # --- NOUVEAU : rendu du menu de choix ---
    def render_choice(self):
        dialogue_rect = self.screen.blit(self.dialog, (config.SCREEN_WIDTH // 2.8, config.SCREEN_HEIGHT // 1.4))

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


    # --- NOUVEAU : rendu de la zone de saisie ---
    def render_input(self):
        dialogue_rect = self.screen.blit(self.dialog, (config.SCREEN_WIDTH // 2.8, config.SCREEN_HEIGHT // 1.4))

        font = pygame.font.Font("fonts/PokemonGb.ttf", 20)
        color = config.BLACK

        prompt = "Quel est le mot de passe ?"
        surf_prompt = font.render(prompt, True, color)
        self.screen.blit(surf_prompt, (dialogue_rect.x + 30, dialogue_rect.y + 20))

        # Champ de saisie (affichage)
        # Curseur clignotant simple
        cursor = "|" if (pygame.time.get_ticks() // 400) % 2 == 0 else ""
        display = (self.input_text + cursor)[:24]
        surf_in = font.render(display, True, color)
        self.screen.blit(surf_in, (dialogue_rect.x + 30, dialogue_rect.y + 60))

        if self.input_feedback:
            surf_fb = font.render(self.input_feedback, True, color)
            self.screen.blit(surf_fb, (dialogue_rect.x + 30, dialogue_rect.y + 95))

    # --- NOUVEAU : logique des réponses ---
    def handle_choice(self):
        choices = self.choices[self.choice_index]

        if self.cut == 10:
            if choices == "Oui":
                self.choice_active = False
                from game_view.map import Map
                world = Map(self.screen)
                world.load("monde1", self.player)
                room = Map(self.screen)
                room.load_room("monde1", "02", self.player)
                self.game.tp_monde1 = True

                self.game.maps = [world, room]
                self.game.map = room
                self.game.event = None
                return
            elif choices == "Non":
                self.choice_active = False
                self.current_char = 0
                self.cut = 16
                self.last_update = pygame.time.get_ticks()

        if self.cut == 12:
            if choices == "Oui":
                self.choice_active = False
                from game_view.map import Map
                world = Map(self.screen)
                world.load("monde2", self.player)
                room = Map(self.screen)
                room.load_room("monde2", "01", self.player)
                self.game.tp_monde1 = True
                self.game.tp_monde2 = True

                self.game.maps = [world, room]
                self.game.map = room
                self.game.event = None
                return
            elif choices == "Non":
                self.choice_active = False
                self.current_char = 0
                self.cut = 16
                self.last_update = pygame.time.get_ticks()

        if self.cut == 14:
            if choices == "Oui":
                self.choice_active = False
                from game_view.map import Map
                world = Map(self.screen)
                world.load("monde3", self.player)
                room = Map(self.screen)
                room.load_room("monde3", "01", self.player)
                self.game.tp_monde1 = True
                self.game.tp_monde2 = True
                self.game.tp_monde3 = True

                self.game.maps = [world, room]
                self.game.map = room
                self.game.event = None
                return
            elif choices == "Non":
                self.choice_active = False
                self.current_char = 0
                self.cut = 16
                self.last_update = pygame.time.get_ticks()

        if self.cut == 16:             #<non ! dehors avec poisson
            if choices == "Oui":
                self.choice_active = False
                from game_view.map import Map
                self.game.teleport_to_map("monde4", [10, 20])
                self.has_teleported = True
                self.game.tp_monde1 = True
                self.game.tp_monde2 = True
                self.game.tp_monde3 = True
                self.game.tp_monde4 = True
                self.game.event = None
                return
            elif choices == "Non":
                self.choice_active = False
                self.current_char = 0
                self.cut = 16
                self.last_update = pygame.time.get_ticks()

        if self.cut == 18:
            if choices == "Oui":
                self.choice_active = False
                from game_view.map import Map
                world = Map(self.screen)
                world.load("monde5", self.player)
                room = Map(self.screen)
                room.load_room("monde5", "02", self.player)
                self.game.tp_monde1 = True
                self.game.tp_monde2 = True
                self.game.tp_monde3 = True
                self.game.tp_monde4 = True
                self.game.tp_monde5 = True

                self.game.maps = [world, room]
                self.game.map = room
                self.game.event = None
                return
            elif choices == "Non":
                self.choice_active = False
                self.current_char = 0
                self.cut = 16
                self.last_update = pygame.time.get_ticks()

        if self.cut == 20:
            if choices == "Oui":
                self.choice_active = False
                from game_view.map import Map
                world = Map(self.screen)
                world.load("monde6", self.player)
                room = Map(self.screen)
                room.load_room("monde6", "02", self.player)
                self.game.tp_monde1 = True
                self.game.tp_monde2 = True
                self.game.tp_monde3 = True
                self.game.tp_monde4 = True
                self.game.tp_monde5 = True
                self.game.tp_monde6 = True

                self.game.maps = [world, room]
                self.game.map = room
                self.game.event = None
                return
            elif choices == "Non":
                self.choice_active = False
                self.current_char = 0
                self.cut = 16
                self.last_update = pygame.time.get_ticks()        

        elif self.cut == 23:
            if choices == "Oui":
                self.choice_active = False
                self.current_char = 0
                self.cut = 0
                self.last_update = pygame.time.get_ticks()
            elif choices == "Non":
                self.choice_active = False
                self.current_char = 0
                self.cut = 24
                self.last_update = pygame.time.get_ticks()
                
    
    def render_scene_0(self):
        self._render_dialogue_box("Mise à jour des mots de passes connus...")

    def render_scene_1(self):
        self._render_dialogue_box("Aucun mot de passe pour cet endroit.")

    def render_scene_2(self):
        self._render_dialogue_box("Le mot de passe du premier monde est 'chocolat'")

    def render_scene_3(self):
        self._render_dialogue_box("Le mot de passe du deuxième monde est 'noyau'")

    def render_scene_4(self):
        self._render_dialogue_box("Le mot de passe du troisième monde est 'xanders'")

    def render_scene_5(self):
        self._render_dialogue_box("Le mot de passe du quatrième monde est 'soquette'")

    def render_scene_6(self):
        self._render_dialogue_box("Le mot de passe du cinquième monde est 'rififi'")

    def render_scene_7(self):
        self._render_dialogue_box("Le mot de passe du sixième monde est 'unicorn'")

    def render_scene_8(self):        
        self._render_dialogue_box("Mot de passe requis pour la téléportation")

    def render_scene_9(self):
        self._render_dialogue_box("Voulez-vous être téléporté au monde 1 ?")

    def render_scene_10(self):
        self._render_dialogue_box("")

    def render_scene_11(self):
        self._render_dialogue_box("Voulez-vous être téléporté au monde 2 ?")

    def render_scene_12(self):
        self._render_dialogue_box("")

    def render_scene_13(self):
        self._render_dialogue_box("Voulez-vous être téléporté au monde 3 ?")

    def render_scene_14(self):
        self._render_dialogue_box("")

    def render_scene_15(self):
        self._render_dialogue_box("Voulez-vous être téléporté au monde 4 ?")

    def render_scene_16(self):
        self._render_dialogue_box("")

    def render_scene_17(self):
        self._render_dialogue_box("Voulez-vous être téléporté au monde 5 ?")

    def render_scene_18(self):
        self._render_dialogue_box("")

    def render_scene_19(self):
        self._render_dialogue_box("Voulez-vous être téléporté au monde 6 ?")

    def render_scene_20(self):
        self._render_dialogue_box("")

    def render_scene_21(self):
        self._render_dialogue_box("Mot de passe incorrect")

    def render_scene_22(self):
        self._render_dialogue_box("Réessayer ?")

    def render_scene_23(self):
        self._render_dialogue_box("")

    def render_scene_24(self):
        self._render_dialogue_box("L'ordinateur va s'éteindre.")
