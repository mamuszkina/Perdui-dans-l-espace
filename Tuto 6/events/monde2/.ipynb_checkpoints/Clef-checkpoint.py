import pygame

import config
from game_state import GameState


class PNJ10:
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
        self.current_dialogue_total_chars = 0

        # --- Nouveaux attributs pour le choix multiple ---
        self.choice_active = False               # True quand on affiche les choix
        self.choice_index = 0                    # index du choix sélectionné
        self.choices = ["0"]
        self.choices1 = ["Euh, j'ai pas compris...", "OK, mais..."]
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
        if self.has_teleported:
            return
        if self.cut > self.max_cut:
            self.game.teleport_to_map("monde2", [8, 29])  # [1, 4] = entry position on map 01
            self.game.event = None
            # specify has teleported already
            self.has_teleported = True
            
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
            self.cut == 24
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

        if choices == "Euh, j'ai pas compris...":
            self.choice_active = False
            self.choices1status = ["fini"]
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        elif choices == "OK, mais...":
            self.choice_active = False
            self.choices1status = ["fini"]
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

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
    
    def render_scene_0(self):
        self._render_dialogue_box_Answer("Excusez-moi… C’est vous Gandalf ?")

    def render_scene_1(self):
        self._render_dialogue_box("(Grogne dans sa barbe) Si je remet ça là..")

    def render_scene_2(self):
        self._render_dialogue_box("Ben Elio et Léo ! Desquellis tu veux que je parles pardi !")

    def render_scene_3(self):
        self._render_dialogue_box_Answer ("Pardon...")

    def render_scene_4(self):
        self._render_dialogue_box("Et que je remet ça ici… ça va me prendre des milliers d’années si je fais ça manuellement !")

    def render_scene_5(self):
        self._render_dialogue_box_Answer("...")

    def render_scene_6(self):
        self._render_dialogue_box_Answer("Gandalf !")

    def render_scene_7(self):
        self._render_dialogue_box_Answer("Gandalf !")

    def render_scene_8(self):
        self._render_dialogue_box("Hein ? Quoi ? Oui ! Qu'est-ce que vous voulez !")

    def render_scene_9(self):
        self._render_dialogue_box("Oh attendez… Vous n’êtes pas de la même aura que les habitants d’ici, vous... Un problème de plus, génial...")

    def render_scene_10(self):
        self._render_dialogue_box_Answer("Euh attendez, vous pouvez m’expliquer ?!")

    def render_scene_11(self):
        self._render_dialogue_box_Answer("C’est quoi cette histoire d’aura ? C’était quoi cet éclair blanc et ce son ? Et pourquoi tout le monde met un i à la fin des mots ? Et surtout, pourquoi personne ne voit le problème ! Me dites pas que je suis le seul à m’en rendre compte, quoi !")

    def render_scene_12(self):
        self._render_dialogue_box("Ah oui, oui, je vois… Vous ne venez clairement pas d’ici...")

    def render_scene_13(self):
        self._render_dialogue_box_Answer("Ben si justement je viens d’ici ! J’allais tranquillement acheter mon pain, comme tous les matins, et...")

    def render_scene_14(self):
        self._render_dialogue_box("Non mais oui, je sais, mais vous ne devez pas venir d’ici, je veux dire, dans cet espace temps.")

    def render_scene_15(self):
        self._render_dialogue_box_Answer("De QUOI ?!")

    def render_scene_16(self):
        self._render_dialogue_box("Oui, enfin ne vous inquiétez pas hein, vous êtes pas loin de chez vous, c’est presque le même endroit, mais ici, on utilise la terminaison en i.")

    def render_scene_17(self):
        self._render_dialogue_box_Answer("Mais que-que-quoi ?")

    def render_scene_18(self):
        self._render_dialogue_box("Oui, c’est que dans cet univers, la langue a été dégenrée pour  les humains de manière à ce que le genre prenne moins de place. Donc à chaque fois que quand on parle, on utilise un marqueur de genre, ben pouf ! On utilise plutot le mot féminin, puis on met un « i » final.")

    def render_scene_19(self):
        self._render_dialogue_box("Ou un « is » au pluriel aussi.")

    def render_scene_20(self):
        self._render_dialogue_box("Joueusi, amicali, conseilleiri, paysanni, ou paysannis au pluriel... Enfin, vous voyez, c’est pas compliqué. D’ailleurs, dans cet univers on parle comme ça naturellement, mais dans d’autres univers des chercheurs -ou des chercheuris- ont proposé cette « solution en i.")

    def render_scene_21(self):
        self._render_dialogue_box("C’est passionnant, n’est-ce pas, tous ces essais...")

    def render_scene_22(self):
        self._render_dialogue_box_Answer("Euh passionnant oui, mais vous, vous parlez normalement pourtant ! Enfin je veux dire, vous parlez comme moi !")

    def render_scene_23(self):
        self._render_dialogue_box("Ah mais moi c’est pas pareil, je ne viens pas d’ici. Je viens de nulle part. Ou de partout, si vous préférez. Je parle en interagissant directement avec votre subconscient. Comme ça je parle toutes les langues, et tout le monde me comprend. C’est plus pratique, dans mon métier.")

    def render_scene_24(self):
        self._render_dialogue_box_Answer("Mais je comprend pas ce que je fais ici !")

    def render_scene_25(self):
        self._render_dialogue_box("Ah, ben ça, c’est une autre histoire. Moi aussi j’aimerais comprendre. Mais ça c’est mon boulot. Vous, vous rentrez chez vous. Et tâchez d’oublier toute cette histoire ! Allez, salut !")

    def render_scene_26(self):
        self._render_dialogue_box_Answer("Attendez, non !")

    def render_scene_27(self):
        self._render_dialogue_box_Lightning("KABOOM")

