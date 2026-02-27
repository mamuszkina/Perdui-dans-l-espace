import pygame

import config
from game_state import GameState


class PNJ24_1:
    def __init__(self, screen, game, player):
        self.screen = screen
        self.game = game
        self.player = player
        self.prof_image= pygame.image.load("imgs/prof2.png")                        #Pas utile à priori
        self.dialog = pygame.image.load("imgs/dialog.png")

        self.cut = 0
        self.max_cut = 7

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
        if self.cut == 6:
            self.game.event = None
        if self.cut > self.max_cut:
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
        #Si on 
        if self.game.go_gandalf == False and self.game.Gandalf5_dialogue_done == False and self.cut == 1:
            self.cut = 7

        if self.game.go_gandalf == True and self.game.Gandalf5_dialogue_done == False and self.cut == 1:
            self.game.event = None

        if self.game.compris == True and self.game.Gandalf5_dialogue_done == True and self.cut == 3:
            self.cut = 5
            
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


    def render_scene_0(self):
        self._render_dialogue_box_PNJ("Jeune ù-homme, essuyez vos chaussures pleines de ç-boue quand vous rentrez chez les gens !")

    def render_scene_1(self):
        self._render_dialogue_box_Answer("Qu'est-ce qu'il dit ?")
        
    def render_scene_2(self):
        self._render_dialogue_box_Gandalf("Il t'a dit qu'un jeune ù-homme comme toi doit essuyer ses chaussures pleines de ç-boue quand tu rentre chez les gens.")
        
    def render_scene_3(self):
        self._render_dialogue_box_Answer("De la ç-boue ? Un jeune ù-homme ? Tu traduis bien là ?")
        
    def render_scene_4(self):
        self._render_dialogue_box_Gandalf("Le ç- et le ù- ne se traduisent pas dans ta langue. Mais il y a bien un ç- devant le mot boue et un ù- devant homme.")
        self.game.compris = True
        
    def render_scene_5(self):
        self._render_dialogue_box_Answer("D'accord. Alors on note que le mot 'boue' porte un 'ç' et on verra plus tard ce que ça veut dire. Allons écrire ça sur le panneau d'affichage.")
        self.game.boue = True
        self.game.homme = True

    def render_scene_6(self):
        self._render_dialogue_box_Answer("")

    def render_scene_7(self):
        self._render_dialogue_box_Answer("Hein ? Evidemment, je comprend strictement rien. Super. Bon, j'ai plus qu'à aller voir Gandalf. Comme d'habitude...")
        self.game.go_gandalf = True