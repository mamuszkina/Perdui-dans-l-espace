import pygame

import config
from game_state import GameState


class PNJ21:
    def __init__(self, screen, game, player):
        self.screen = screen
        self.game = game
        self.player = player
        self.prof_image= pygame.image.load("imgs/prof2.png")                        #Pas utile à priori
        self.dialog = pygame.image.load("imgs/dialog.png")

        self.cut = 0
        self.max_cut = 11

        # Typewriter state when creating the PNJ
        self.char_delay_ms = 30                     # 1= très rapide ; 100= très lent
        self.current_char = 0
        self.last_update = 0
        # Nombre total de caractères du texte courant (après "wrap")
        self.current_dialogue_total_chars = 0


    def load(self):
        self.current_char = 0
        self.last_update = pygame.time.get_ticks()

  
    def update(self):
        if self.cut == 5:
            self.game.event = None
        elif self.cut == 10:
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

    
    def render(self):
        if self.game.go_gandalf == False and self.game.Gandalf5_dialogue_done == False and self.cut == 1:
            self.cut = 11

        if self.game.go_gandalf == True and self.game.Gandalf5_dialogue_done == False and self.cut == 1:
            self.game.event = None

        if self.game.compris == True and self.game.Gandalf5_dialogue_done == True and self.cut == 2:
            self.cut = 4

        if self.game.PNJ20_parlé == True and self.cut < 6:
            self.cut = 6
            
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
    def _render_dialogue_box_PNJ(self, text):
        dialogue_rect = self.screen.blit(self.dialog, (0, 450))      # chiffres = position bulle de dialogue

        font = pygame.font.Font("fonts/elfique.ttf", 20)           #20 = taille des lettres
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

    def _render_dialogue_box_Gandalf(self, text):
        dialogue_rect = self.screen.blit(self.dialog, (0, 450))      # chiffres = position bulle de dialogue

        font = pygame.font.Font("fonts/PokemonGb.ttf", 20)           #20 = taille des lettres
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
            

    def render_scene_0(self):
        self._render_dialogue_box_PNJ("Chut ! Vous allez faire fuir les à-têtards.")

    def render_scene_1(self):
        self._render_dialogue_box_Gandalf("Il dit qu'on va faire fuir les à-têtards.")
        
    def render_scene_2(self):
        self._render_dialogue_box_Answer("Les à-têtards ? Tu es sûr pour le 'à' ?")
        
    def render_scene_3(self):
        self._render_dialogue_box_Gandalf("Le 'à-' ne se traduit pas dans ta langue. Mais il y a bien un 'à-' devant le mot têtard.")
        self.game.compris = True
        
    def render_scene_4(self):
        self._render_dialogue_box_Answer("Un 'à-' devant têtard. Un indice de plus. On va ajouter ça au panneau d'affichage.")
        self.game.têtard = True
        
    def render_scene_5(self):
        self._render_dialogue_box_Answer("")
        
    def render_scene_6(self):
        self._render_dialogue_box_PNJ("Oh, merci ! C’est ma ù-belle-sœur qui vous envoie ? Quelle ù-femme formidable ! J’avais super soif ! J’en ç-salive d’avance, merci !")
        
    def render_scene_7(self):
        self._render_dialogue_box_Answer("Qu'est-ce qu'il dit ?")
        
    def render_scene_8(self):
        self._render_dialogue_box_Gandalf("Il nous remercie. Et il nous demande si c'est bien sa ù-belle-soeur qui nous envoie. Il dit que c'est une ù-femme formidable. Il dit aussi qu'il en ç-salive d'avance.")
        
    def render_scene_9(self):
        self._render_dialogue_box_Answer("Donc, on a un 'ù-' devant belle-soeur et un autre 'ù-' devant femme, en plus d'un ç-devant salive. Allons noter ça avant d'oublier.")
        self.game.femme = True
        self.game.belle_soeur = True
        self.game.salive = True
        
    def render_scene_10(self):
        self._render_dialogue_box_Answer("")
        
    def render_scene_11(self):
        self._render_dialogue_box_Answer("Hein ? Evidemment, je comprend strictement rien. Super. Bon, j'ai plus qu'à aller voir Gandalf. Comme d'habitude...")
        self.game.go_gandalf = True