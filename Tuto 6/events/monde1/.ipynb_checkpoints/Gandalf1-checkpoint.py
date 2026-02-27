import pygame

import config
from game_state import GameState


class PNJ4:
    def __init__(self, screen, game, player):
        self.screen = screen
        self.game = game
        self.player = player
        self.prof_image= pygame.image.load("imgs/prof2.png")                        #Pas utile à priori
        self.dialog = pygame.image.load("imgs/dialog.png")

        self.cut = 0
        self.max_cut = 6

        # Typewriter state when creating the PNJ
        self.char_delay_ms = 30                     # 1= très rapide ; 100= très lent
        self.current_char = 0
        self.last_update = 0

        # --- Nouveaux attributs pour le choix multiple ---
        self.choice_active = False               # True quand on affiche les choix
        self.choice_index = 0                    # index du choix sélectionné
        self.choices = ["0"]
        self.choices1 = ["Mes quoi ?", "Tu as vu l'éclair blanc et ce KABOOM ?"]
        self.choices1status = ["attente"]
        self.goodbye = False                     # True après "n'hésite pas à revenir"

    def load(self):
        self.current_char = 0
        self.last_update = pygame.time.get_ticks()

        # On réinitialise aussi les états de choix à chaque lancement de PNJ1
        self.choices1status = ["attente"]
        self.choice_active = False
        self.choice_index = 0
        self.goodbye = False
  
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
                        # On termine simplement l'événement
                        self.game.event = None

                # --- Dialogue normal : Entrée avance les cases ---
                elif event.key == pygame.K_RETURN:
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
            self.cut == 2
            and self.choices1status == ["attente"]
            and not self.goodbye
            and not self.choice_active
        ):
            self.choices = self.choices1
            self.choice_active = True
            self.choice_index = 0
    
    def render(self):
        # Si on a choisi "non" -> message d'au revoir
        if self.goodbye:
            self.render_goodbye()
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

    # create a function for dialogue box
    def _render_dialogue_box(self, text):
        dialogue_rect = self.screen.blit(self.dialog, (0, 450))      # chiffres = position bulle de dialogue

        font = pygame.font.Font("fonts/PokemonGb.ttf", 20)           #20 = taille des lettres
        color = config.BLUE

        wrapped = self.wrap_text(text, font, dialogue_rect.width - 60)

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

    def _render_dialogue_box_Answer(self, text):
        dialogue_rect = self.screen.blit(self.dialog, (0, 450))      # chiffres = position bulle de dialogue

        font = pygame.font.Font("fonts/PokemonGbAnswer.ttf", 20)           #20 = taille des lettres
        color = config.BLACK

        wrapped = self.wrap_text(text, font, dialogue_rect.width - 20)

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
        dialogue_rect = self.screen.blit(self.dialog, (0, 450))

        font = pygame.font.Font("fonts/PokemonGbAnswer.ttf", 20)
        color = config.BLACK

        # --- Question ---
        question = "Que faire ?"
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

    # --- NOUVEAU : message quand le joueur répond "non" ---
    def render_goodbye(self):
        self._render_dialogue_box("... Au revoir ...")

    # --- NOUVEAU : logique des réponses ---
    def handle_choice(self):
        choices = self.choices[self.choice_index]

        if choices == "Mes quoi ?":
            # On désactive le menu, on marque la question comme répondue
            # et on laisse cut à 2 : la prochaine fois, render_scene_2
            # ("Attendez, je vous prépare ça.") sera affichée.
            self.choice_active = False
            self.choices1status = ["fini"]
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        elif choices == "Tu as vu l'éclair blanc et ce KABOOM ?":
            # On affiche "N'hésite pas à revenir." puis on attend Entrée
            # pour fermer l'événement.
            self.choice_active = False
            self.cut = 4
            self.goodbye = False
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()
    
    def render_scene_0(self):
        self._render_dialogue_box("Charlie ! Ça fait toujours plaisir quand tu viens prendre le temps de papoter !")

    def render_scene_1(self):
        self._render_dialogue_box("Comment vont tes nièci ? Ça fait longtemps qu’on les a pas vuis !")

    def render_scene_2(self):
        self._render_dialogue_box("Ben Elio et Léo ! Desquellis tu veux que je parles pardi !")

    def render_scene_3(self):
        self.cut = 5

    def render_scene_4(self):
        self._render_dialogue_box("De quoi ? Non, j’ai rien vu. Pourtant j’ai pas bougé d’ici. T’es sûri que t’es pas tombéi sur la tête ?")

    def render_scene_5(self):
        self._render_dialogue_box_Answer("Mais je comprend pas ce que tu racontes ! Parles Français, FRAN-ÇAIS !")

    def render_scene_6(self):
        self._render_dialogue_box("Hé, j’y suis pour rien si tu as des hallucinations, moi ! Vas te poser un peu à l’ombre, tu as dû te prendre une insolation...")