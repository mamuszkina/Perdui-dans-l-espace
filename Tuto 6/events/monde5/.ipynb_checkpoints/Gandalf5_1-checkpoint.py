import pygame

import config
from game_state import GameState


class Gandalf4:
    def __init__(self, screen, game, player):
        self.screen = screen
        self.game = game
        self.player = player
        self.prof_image= pygame.image.load("imgs/prof.png")                        #Pas utile à priori
        self.dialog = pygame.image.load("imgs/dialog.png")
        self.dialog2 = pygame.image.load("imgs/dialog2.png")
        self.ECLAIR_BLANC = pygame.image.load("imgs/ECLAIR_BLANC.jpg")
        self.lightning_sound = pygame.mixer.Sound("lightning.mp3")
        self.lightning_played = False
        self.lightning_sound.set_volume(0.8)   # entre 0.0 et 1.0

        self.cut = 0
        self.max_cut = 30
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
        self.choices1 = ["J'ai été pris à l'entretien !", "Je suis toujours pas chez moi !"]
        self.choices1status = ["attente"]

    def load(self):
        self.current_char = 0
        self.last_update = pygame.time.get_ticks()

        self.choices1status = ["attente"]
        self.choices2status = ["attente"]
        self.choice_active = False
        self.choice_index = 0
  
    def update(self):
        if self.has_teleported:
            return

        if self.cut == 4:
            self.cut = 6
        elif self.cut > self.max_cut:
            self.game.teleport_to_map("monde5", [14, 33])  # [1, 4] = entry position on map 01
            self.game.event = None
            # specify has teleported already
            self.has_teleported = True
            
#        if self.cut == 50:
#            if self.lightning_played:
#                self.lightning_sound.stop()
#                pygame.mixer.music.unpause()
#                self.lightning_played = False
#            return

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
            self.cut == 1
            and self.choices1status == ["attente"]
            and not self.choice_active
        ):
            self.choices = self.choices1
            self.choice_active = True
            self.choice_index = 0

            
    def render(self):
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
        dialogue_rect = self.screen.blit(self.dialog2, (0, 450))      # chiffres = position bulle de dialogue

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

    def render_choice(self):
        dialogue_rect = self.screen.blit(self.dialog, (0, 450))
        font = pygame.font.Font("fonts/PokemonGbAnswer.ttf", 20)
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

        if choices == "J'ai été pris à l'entretien !":
            self.choice_active = False
            self.cut = 2
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        elif choices == "Je suis toujours pas chez moi !":
            self.choice_active = False
            self.cut = 5
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

    
    def render_scene_0(self):
        self._render_dialogue_box_Answer("Gandalf !")

    def render_scene_1(self):
        self._render_dialogue_box_Answer("") 

    def render_scene_2(self):
        self._render_dialogue_box("Euh super, mais qu'est-ce que tu veux que ça me fasse ?")

    def render_scene_3(self):
        self._render_dialogue_box_Answer("ça te fait que pour une fois que j'arrive à décrocher un job, je peux même pas l'accepter parce que je suis toujours pas chez moi !")

    def render_scene_4(self):
        self._render_dialogue_box("")

    def render_scene_5(self):
        self._render_dialogue_box("Comment ça ? Mais enfin au pire c'est pas si grave si tu n'es pas chez toi non ? J'ai pas tout résolu vec ton poisson-traduction ?")

    def render_scene_6(self):
        self._render_dialogue_box_Answer("Ah ben parlons-en de ton poisson-traduction ! Non seulement c'est dégueulasse, mais en plus il est cassé !")

    def render_scene_7(self):
        self._render_dialogue_box("Cassé ? Tu m'as cassé mon poisson-traduction ? Mais enfin qu'est-ce que tu as fait avec ?!")

    def render_scene_8(self):
        self._render_dialogue_box_Answer("Rien, mais une fois  arrivé dans la maison, il s’est mis à faire des CRRRRRZZ et des CKKKKK immondes ! Pour une fois que j'en avais vraiment besoin, évidemment c'est à ce moment qu'il a flanché !")

    def render_scene_9(self):
        self._render_dialogue_box("Je vois. C’est parce que sa seigneurie a une grenouille chez elle. C’est bien connu, les poisson-traduction ont peur des grenouilles, alors ils se mettent à crier et ne font plus bien leur travail de traduction.")

    def render_scene_10(self):
        self._render_dialogue_box_Answer("Mmmouais. ça me semble plutôt être une facilité scénaristique ça.")

    def render_scene_11(self):
        self._render_dialogue_box("Oui bon, passons. Toujours pas chez toi donc ?")

    def render_scene_12(self):
        self._render_dialogue_box_Answer("Oula non ! C’est trop bizarre, ici quand les gens parlent, ils rajoutent un petit mot pour décrire la forme d’un objet. Rond, granuleux... Mais qui fait ça !?")

    def render_scene_13(self):
        self._render_dialogue_box("Environ 35% des langues de la Terre, mon ami..")

    def render_scene_14(self):
        self._render_dialogue_box("C’est très pratique ! Si à un moment tu perd le fil de la discussion, que tu rates un mot ou quoi, il te suffit de connaitre ces petits mots, ces classificateurs, pour voir à peu près de quoi on parle.")

    def render_scene_15(self):
        self._render_dialogue_box_Answer("Oui, j’ai pu voir pendant le test. On m’a demandé de la farine, j’ai pu prendre l’étiquette de ce mot – de ce classificateur – qui est le même pour parler de poussière.")

    def render_scene_16(self):
        self._render_dialogue_box("Ce qu’il y a de vraiment drôle, c’est que toutes les langues n’ont pas du tout les mêmes classificateurs. Les classificateurs peuvent décrire des objets longs et fins, des choses rondes, des personnes, des lieux.")

    def render_scene_17(self):
        self._render_dialogue_box("Il y a des langues qui ont plus de 100 classificateurs !")

    def render_scene_18(self):
        self._render_dialogue_box_Answer("Ouah ! Heureusement il n’y en avait pas autant ici, j'aurais été sacrément dans la mouise. J’en ai compté 4, mais il y en a peut-être plus.")

    def render_scene_19(self):
        self._render_dialogue_box("Après une petite mise à jour de mon disque de données, dans cette langue (le Sabanê), il y a 7 classificateurs.")

    def render_scene_20(self):
        self._render_dialogue_box_Answer("Mais donc, les langues qui ont beaucoup de classificateurs, ce sont des langues qui doivent être très difficiles à apprendre ! Je suis bien content qu’il n’y ait pas ce système dans ma langue.")

    def render_scene_21(self):
        self._render_dialogue_box("Détrompe-toi, ce sont des langues qui ont un énorme avantage, elles n’ont pas de système de concordance.")

    def render_scene_22(self):
        self._render_dialogue_box_Answer("De système de quoi ?")

    def render_scene_23(self):
        self._render_dialogue_box("Concordance. C'est à dire que la forme d'un mot ne change pas selon le nombre ou autre. 'Un cheval' par exemple, restera 'un cheval' peut importe qu'il y en ait un, deux ou mille. Ce n'est pas le cas dans toutes les langues.")

    def render_scene_24(self):
        self._render_dialogue_box_Answer("Alors dans ce cas, de la concordance il y en a dans ma langue.")

    def render_scene_25(self):
        self._render_dialogue_box("Ah ben dis-moi ça ! Donc tu ne fais clairement pas partie d’une langue à classificateur.")

    def render_scene_26(self):
        self._render_dialogue_box_Answer(" Pour sûr ! Moi y a tout un tas de règle, d’accords, de concordance, de je ne sais pas quoi étouétou...")

    def render_scene_27(self):
        self._render_dialogue_box("C’est un excellent indice pour la suite ! ça enlève bien des langues du monde ! Je vais pouvoir t’amener dans une langue qui n’est pas une langue à classificateur. Je configure mon disque de données.")

    def render_scene_28(self):
        self._render_dialogue_box("................................")

    def render_scene_29(self):
        self._render_dialogue_box("ça ne nous laisse lus que XXX essais de langue. On va y arriver ! Je vais t'envoyer..... Ici, tiens ! Allez, bon courage !")

    def render_scene_30(self):
        self._render_dialogue_box_Lightning("KABOOM")