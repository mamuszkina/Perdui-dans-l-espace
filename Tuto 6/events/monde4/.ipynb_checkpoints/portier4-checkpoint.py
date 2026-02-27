import pygame

import config
from game_state import GameState


class PNJ8:
    def __init__(self, screen, game, player):
        self.screen = screen
        self.game = game
        self.player = player
        self.prof_image= pygame.image.load("imgs/prof2.png")                        #Pas utile à priori
        self.dialog = pygame.image.load("imgs/dialog.png")

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
        self.choices1 = ["C'est PNJ7 qui m'envoie", "Bonjour, vous n'auriez pas une clef par hasard ?"]
        self.choices1status = ["attente"]
        self.choices2 = ["LE LAISSER PASSER A38 !!!", "Pitié, aidez-moi..."]
        self.choices2status = ["attente"]
        self.goodbye = False                     # True après "n'hésite pas à revenir"

    def load(self):
        self.current_char = 0
        self.last_update = pygame.time.get_ticks()

        # On réinitialise aussi les états de choix à chaque lancement de PNJ1
        self.choices1status = ["attente"]
        self.choices2status = ["attente"]
        self.choice_active = False
        self.choice_index = 0
        self.goodbye = False
  
    def update(self):
        if self.cut == 1:
            self.game.event = None
        elif self.cut == 8:
            self.game.event = None
        elif self.cut == 10:
            self.game.event = None
        elif self.cut == 18:
            self.game.event = None
        elif self.cut == 21:
            self.game.event = None
        elif self.cut == 23:
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
            self.cut == 2
            and self.choices1status == ["attente"]
            and not self.goodbye
            and not self.choice_active
        ):
            self.choices = self.choices1
            self.choice_active = True
            self.choice_index = 0

        if (
            self.cut == 11
            and self.choices1status == ["attente"]
            and not self.goodbye
            and not self.choice_active
        ):
            self.choices = self.choices1
            self.choice_active = True
            self.choice_index = 0
    
    def render(self):
        if self.goodbye:
            self.render_goodbye()
            return

        if self.game.PNJ8_dialogue_done == False and self.game.PNJ7_dialogue_done == True and self.cut < 2:
            self.cut = 2
            return

        if self.game.PNJ8_dialogue_done == True and self.game.PNJ9_dialogue_done == False and self.cut < 9:
            self.cut = 9
            return

        if self.game.PNJ9_dialogue_done == True and self.game.Maison_papier_dialogue_done == False and self.cut < 11:
            self.cut = 11
            return

        if self.game.Maison_papier_dialogue_done == True and self.game.PNJ10_dialogue_done == False and self.cut < 19:
            self.cut = 19
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

    # create a function for dialogue box
    def _render_dialogue_box(self, text):
        dialogue_rect = self.screen.blit(self.dialog, (0, 450))      # chiffres = position bulle de dialogue

        font = pygame.font.Font("fonts/PokemonGb.ttf", 20)           #20 = taille des lettres
        color = config.BLUE

        wrapped = self.wrap_text(text, font, dialogue_rect.width - 60)

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

    def _render_dialogue_box_Answer(self, text):
        dialogue_rect = self.screen.blit(self.dialog, (0, 450))      # chiffres = position bulle de dialogue

        font = pygame.font.Font("fonts/PokemonGbAnswer.ttf", 20)           #20 = taille des lettres
        color = config.BLACK

        wrapped = self.wrap_text(text, font, dialogue_rect.width - 20)

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

    # --- NOUVEAU : logique des réponses ---
    def handle_choice(self):
        choices = self.choices[self.choice_index]

        if choices == "C'est PNJ7 qui m'envoie":
            self.choice_active = False
            self.choices1status = ["fini"]
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        elif choices == "Bonjour, vous n'auriez pas une clef par hasard ?":
            self.choice_active = False
            self.goodbye = True
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        elif choices == "LE LAISSER PASSER A38 !!!":
            self.choice_active = False
            self.goodbye = True
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        elif choices == "Pitié, aidez-moi...":
            self.choice_active = False
            self.choices2status = ["fini"]
            self.current_char = 0
            self.last_update = pygame.time.get_ticks(), 

    def render_goodbye(self):
        self._render_dialogue_box("Pourquoi je vous donnerais mes clefs ? Désolae mais c'est non.")

#SCENE ZERO 
    def render_scene_0(self):
        self._render_dialogue_box("Quoi ? Un éclair blanc ? Un Kaboom ? Désolae, je n’ai rien vu de tout ça.")

    def render_scene_1(self):
        self._render_dialogue_box("")
        
#SCENE UN
    def render_scene_2(self):
        self._render_dialogue_box("Ah oui, la clef ! Normalement c’est mu cousaine qui doit garder la porte du labo. Mais comme al est malade, iel a refilé la clef à saon filx, PNJX.")

    def render_scene_3(self):
        self._render_dialogue_box_Answer ("Ah alors c’est PNJX qui l’a ?")

    def render_scene_4(self):
        self._render_dialogue_box("Non, non, iel avait peur de la perdre, alors al me l’a refilée.")

    def render_scene_5(self):
        self._render_dialogue_box_Answer("Ah donc c’est vous qui l’avez !")

    def render_scene_6(self):
        self._render_dialogue_box("Mais noon ! PNJ9 est passae me la récupérer il y a quelques jours. Al m’a harcelae pour que je lui passe ! Al ne me l’a pas encore rendue, al doit encore l’avoir. ")

    def render_scene_7(self):
        self._render_dialogue_box_Answer("C'est pas facile, votre histoire...")

    def render_scene_8(self):
        self._render_dialogue_box("")
        self.game.PNJ8_dialogue_done = True

#SCENE DEUX
    def render_scene_9(self):
        self._render_dialogue_box("PNJ9 doit trainer chez al avec ce froid. Al habite au Sud de la ville. Allez lui demander.")

    def render_scene_10(self):
        self._render_dialogue_box("")

#SCENE TROIS
    def render_scene_11(self):
        self._render_dialogue_box("Mais bien sûr, avec plaisir ! Vous cherchez quoi ?")

    def render_scene_12(self):
        self._render_dialogue_box_Answer("La maison de PNJ11.")

    def render_scene_13(self):
        self._render_dialogue_box("Oh mais al n'est pas chez al, al est partae en tournée !")

    def render_scene_14(self):
        self._render_dialogue_box_Answer("Je sais, oui...")

    def render_scene_15(self):
        self._render_dialogue_box("C'est Un grandae Acteur vous savez... Al est passionae de son métier, et si vous aviez vu comme al joue bien les Heros Grecs !")

    def render_scene_16(self):
        self._render_dialogue_box_Answer("Oui, oui... Et sa maison ?")

    def render_scene_17(self):
        self._render_dialogue_box("Ah oui oui sa maison ! C'est celle juste à côté.")

    def render_scene_18(self):
        self._render_dialogue_box("")

#SCENE QUATRE
    def render_scene_19(self):
        self._render_dialogue_box("Ah, on dirait l'écriture de PNJ10 ça ! Vous avez trouvé ce mot chez PNJ11 ? C'est Un Grand Acteur vous savez.")
        
    def render_scene_20(self):
        self._render_dialogue_box_Answer("Oui, on me l'avez déjà dit...")

    def render_scene_21(self):
        self._render_dialogue_box("")

#SCENE CINQ
    def render_scene_22(self):
        self._render_dialogue_box_Answer("Je ferais mieux d'aller voir PNJ7. Ce félon !")

    def render_scene_23(self):
        self._render_dialogue_box_Answer("")

#SCENE SIX
    def render_scene_24(self):
        self._render_dialogue_box("Si vous avez le temps, vous devriez aller voir XXXXXX. Une très belle pièce de théâtre, très réussie !")