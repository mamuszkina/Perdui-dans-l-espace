import pygame

import config
from game_state import GameState


class Panneau_Place:
    def __init__(self, screen, game, player):
        self.screen = screen
        self.game = game
        self.player = player
        self.prof_image= pygame.image.load("imgs/prof2.png")                        #Pas utile à priori
        self.dialog = pygame.image.load("imgs/dialog.png")
        self.panneau = pygame.image.load("imgs/monde5/dessin.png")
        self.homme = pygame.image.load("imgs/monde5/homme.png")

        self.cut = 0
        self.max_cut = 16

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
        self.choices1 = ["homme", "Partir"]
        self.choices2 = ["ù", "à", "ç", "é"]
#        self.choices3 = ["eune fantassine", "eune fantassinë", "eune fantassaine"]
        self.choices1status = ["attente"]
        self.choices2status = ["attente"]
#        self.choices3status = ["attente"]
#        self.resolved = False
        self.goodbye = False                     # True après "n'hésite pas à revenir"

    def load(self):
        self.current_char = 0
        self.last_update = pygame.time.get_ticks()

        # On réinitialise aussi les états de choix à chaque lancement de PNJ1
#        self.choices1status = ["attente"]
#        self.choices2status = ["attente"]
#        self.choices3status = ["attente"]
#        self.choice_active = False
#        self.choice_index = 0
#        self.goodbye = False
  
    def update(self):
        print(self.game.homme_finito)
        if self.cut == 1:
            self.game.event = None
        elif self.cut == 7:
            self.cut = 3
        elif self.cut == 9:
            self.cut = 5
#        elif self.cut == 15:
#            self.game.event = None
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
                        self.choice_index = (self.choice_index - 1) % max(1, len (self.choices))
                    elif event.key == pygame.K_DOWN:
                        self.choice_index = (self.choice_index + 1) % max(1, len (self.choices))
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

        if (
            self.cut == 3
            and self.choices1status == ["attente"]
            and not self.goodbye
            and not self.choice_active
        ):
            if getattr(self.game, "homme", False):
                self.choices = self.choices1
            else:
                self.choices = ["homme"]
            self.choice_active = True
            self.choice_index = 0
        elif (
            self.cut == 5
            and self.choices2status == ["attente"]
            and not self.goodbye
            and not self.choice_active
        ):
            self.choices = self.choices2
            self.choice_active = True
            self.choice_index = 0
#ajouter femme, belle_soeur, beau_frère, etc si on voit que ça marche
    
    def render(self):
        # Si on a choisi "non" -> message d'au revoir
        if self.goodbye:
            self.render_goodbye()
            return

        if self.game.Gandalf5_dialogue_done == False and self.cut < 0:
            self.cut = 0
            return

        if self.game.homme == True and self.cut <2:
            self.cut = 2
            return

        if self.game.homme_finito == True :
            self.screen.blit(self.panneau, (50, 10))

#        if self.game.PNJ12_dialogue_done == True and self.cut < 16:
#            self.cut = 16
#            return

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
        panneau = self.screen.blit(self.panneau, (50, 10))

        if self.game.homme_finito == True :
            self.screen.blit(self.panneau, (50, 10))

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
        panneau = self.screen.blit(self.panneau, (50, 10))

        if self.game.homme_finito == True :
            self.screen.blit(self.panneau, (50, 10))

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

    # --- NOUVEAU : message quand le joueur répond "non" ---
    def render_goodbye(self):
        self._render_dialogue_box("Je continuerais plus tard.")

    # --- NOUVEAU : logique des réponses ---
    def handle_choice(self):
        choices = self.choices[self.choice_index]

        if choices == "homme":
            self.choice_active = False
            self.cut = 4
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        elif choices == "Partir":
            self.choice_active = False
            self.goodbye = True
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        elif self.cut == 5 and choices == "ù":
            self.choice_active = False
            self.cut = 6
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        elif self.cut == 5 and choices != "ù":
            self.choice_active = False
            self.cut = 8
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

       
            
#SCENE ZERO
    def render_scene_0(self):
        self._render_dialogue_box_Answer("C'est un panneau vide. Il y a des feutres à côté pour dessiner dessus.")
        self.game.homme = True

    def render_scene_1(self):
        self._render_dialogue_box_Answer("")
        
#SCENE UN
    def render_scene_2(self):
        self._render_dialogue_box_Answer("Que dessiner dessus ?")
        
    def render_scene_3(self):
        self._render_dialogue_box("")

#HOMME        
    def render_scene_4(self):
        self._render_dialogue_box_Answer("Et je range le mot 'homme' dans quelle colonne ?")
        
    def render_scene_5(self):
        self._render_dialogue_box("")
        
    def render_scene_6(self):
        self._render_dialogue_box("ça me parait bien ici. Est-ce que j'ai d'autres mots à dessiner ? Voyons...")
        self.game.homme_finito = True
        
    def render_scene_7(self):
        self._render_dialogue_box_Answer("")
        
    def render_scene_8(self):
        self._render_dialogue_box_Gandalf("Tu es sûr Charlie ? Si je me souviens bien, on avait entendu 'XXXXX'.")
        
    def render_scene_9(self):
        self._render_dialogue_box("")

#MOT SUIVANT
    def render_scene_10(self):
        self._render_dialogue_box("Oui, mais moi j’aime bien être seulë des fois, et puis, en partant iels m’ont prêté leurs jouets donc c’est chouette !")
        
    def render_scene_11(self):
        self._render_dialogue_box_Answer("Tu sais ce qu’il manquerait dans ton équipe ? ")
        
    def render_scene_12(self):
        self._render_dialogue_box_Answer("Eune quoi ?")
        
    def render_scene_13(self):
        self._render_dialogue_box("")
        self.choices3status = ["attente"]
        
    def render_scene_14(self):
        self._render_dialogue_box("Maiiiis y a pas de fantassaine dans la scène ! Mh… Mais ça pourrait être rigolo d’en ajouter eune… T’as raison il m’en faut eune ! Je vais aller chercher ça ! Merci pour l’idée !")

    def render_scene_15(self):
        self._render_dialogue_box("")
        self.game.PNJ12_dialogue_done = True

#SCENES SUIVANTES
    def render_scene_16(self):
        self._render_dialogue_box("FILS du condor ! Et du Rohan ! Mes FRERES ! Un jour peut venir, ou le courage des HOMMES faillira, où nous abandonnerons nos AMIS, et briserons tout lien. Mais ce jour n'est pas arrivé !")