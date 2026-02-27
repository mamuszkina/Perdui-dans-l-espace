import pygame

import config
from game_state import GameState
from game_state import grayscale


class PNJ12:
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
        self.PNJ = pygame.image.load("imgs/characters/enfant_un.png").convert_alpha()
        self.PNJ = pygame.transform.flip(self.PNJ, True, False)
        self.PNJ = pygame.transform.scale(self.PNJ, (config.SCREEN_WIDTH//5, config.SCREEN_HEIGHT//1.1))
        self.PNJ_gray = grayscale(self.PNJ)

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
        self.choices1 = ["copaines", "copains", "copinis"]
        self.choices2 = ["voisanes", "voisinx", "voisaines"]
        self.choices3 = ["eune fantassine", "eune fantassinë", "eune fantassaine"]
        self.choices1status = ["attente"]
        self.choices2status = ["attente"]
        self.choices3status = ["attente"]
#        self.resolved = False
        self.goodbye = False                     # True après "n'hésite pas à revenir"

    def load(self):
        self.current_char = 0
        self.last_update = pygame.time.get_ticks()

        # On réinitialise aussi les états de choix à chaque lancement de PNJ1
        self.choices1status = ["attente"]
        self.choices2status = ["attente"]
        self.choices3status = ["attente"]
        self.choice_active = False
        self.choice_index = 0
        self.goodbye = False
  
    def update(self):
        if self.cut == 1:
            self.game.event = None
        elif self.cut == 9:
            self.cut = 8
        elif self.cut == 13:
            self.cut = 12
        elif self.cut == 15:
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

        # --- Déclenchement de la question à choix multiple ---
        # On pose la question sur la case 2 (cut == 2), UNE SEULE fois,
        # tant que le joueur n'a pas répondu "oui".

        if (
            self.cut == 5
            and self.choices1status == ["attente"]
            and not self.goodbye
            and not self.choice_active
        ):
            self.choices = self.choices1
            self.choice_active = True
            self.choice_index = 0
 #           self.handle_choice1
        elif (
            self.cut == 8
            and self.choices2status == ["attente"]
            and not self.goodbye
            and not self.choice_active
        ):
            self.choices = self.choices2
            self.choice_active = True
            self.choice_index = 0
        elif (
            self.cut == 12
            and self.choices3status == ["attente"]
            and not self.goodbye
            and not self.choice_active
        ):
            self.choices = self.choices3
            self.choice_active = True
            self.choice_index = 0
        elif self.cut == 9:
            self.cut == 8
        elif self.cut == 13:
            self.cut == 12
    
    def render(self):
        # Si on a choisi "non" -> message d'au revoir
        if self.goodbye:
            self.render_goodbye()
            return

        if self.game.portier3_2_dialogue_done == True and self.game.PNJ12_dialogue_done == False and self.cut < 2:
            self.cut = 2
            return

        if self.game.PNJ12_dialogue_done == True and self.cut < 16:
            self.cut = 16
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
        self.screen.blit(self.charlie_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
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
        self.screen.blit(self.charlie, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
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
    def render_choice(self):
        dialogue_rect = self.screen.blit(self.dialog, (config.SCREEN_WIDTH // 2.8, config.SCREEN_HEIGHT // 1.4))      # chiffres = position bulle de dialogue
        self.screen.blit(self.charlie, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        self.screen.blit(self.PNJ_gray, (config.SCREEN_WIDTH // 6, config.SCREEN_HEIGHT * 0.5))

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

    # --- NOUVEAU : message quand le joueur répond "non" ---
    def render_goodbye(self):
        self._render_dialogue_box("... Au revoir ...")

    # --- NOUVEAU : logique des réponses ---
    def handle_choice(self):
        choices = self.choices[self.choice_index]

        if choices == "copaines":
            self.choice_active = False
            self.cut = 6
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        elif choices == "copains":
            self.choice_active = False
            self.choices1status = ["fini"]
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        elif choices == "copinis":
            self.choice_active = False
            self.choices1status = ["fini"]
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        elif choices == "voisaines":
            self.choice_active = False
            self.cut = 10
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()
            
        elif choices == "voisinx":
            self.choice_active = False
            self.choices2status = ["fini"]
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()
            
        elif choices == "voisanes":
            self.choice_active = False
            self.choices2status = ["fini"]
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()
            
        elif choices == "eune fantassaine":
            self.choice_active = False
            self.cut = 14
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()
            
        elif choices == "eune fantassine":
            self.choice_active = False
            self.choices3status = ["fini"]
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()
            
        elif choices == "eune fantassinë":
            self.choice_active = False
            self.choices3status = ["fini"]
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()
       
            
#SCENE ZERO, UN ET DEUX
    def render_scene_0(self):
        self._render_dialogue_box_Answer("Cet enfant joue tranquillement. Il n'a pas l'air très disposé à me parler pour l'instant.")

    def render_scene_1(self):
        self._render_dialogue_box_Answer("")
        
#SCENE TROIS
    def render_scene_2(self):
        self._render_dialogue_box_Answer("Salut gamaine ! Tu joues à quoi ?")
        
    def render_scene_3(self):
        self._render_dialogue_box("Ben tu vois, ellui, c’est lea sorcièle qui essaie d’empêcher un balrog de tuer toute son équipe. ")
        
    def render_scene_4(self):
        self._render_dialogue_box_Answer("Tiens, marrant ! Et tu joues pas avec tes...")
        
    def render_scene_5(self):
        self._render_dialogue_box("Hein ? Ah mes copaines tu veux dire ?")
        
    def render_scene_6(self):
        self._render_dialogue_box("Ben là je suis bien toude seulë. Mais enfin pour l’instant y a pas grand monde pour jouer avec moi, c’est les vacances.")
        
    def render_scene_7(self):
        self._render_dialogue_box_Answer("Tu veux dire que tout le monde est parti parmi tes...")
        
    def render_scene_8(self):
        self._render_dialogue_box("Mes quoi ?")
        
    def render_scene_9(self):
        self._render_dialogue_box("")
        self.choices2status = ["attente"]
        
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
        self._render_dialogue_box("Maiiiis y a pas de fantassaine dans la scène ! Mh... Mais ça pourrait être rigolo d’en ajouter eune... T’as raison il m’en faut eune ! Je vais aller chercher ça ! Merci pour l’idée !")
        self.game.unlock_pokedex_entry(3, "PNJ12.0")
        self.game.unlock_pokedex_entry(3, "PNJ12.2")

    def render_scene_15(self):
        self._render_dialogue_box("")
        self.game.PNJ12_dialogue_done = True

#SCENES SUIVANTES
    def render_scene_16(self):
        self._render_dialogue_box("Enfants du condor ! Et du Rohan ! Mes adelphes ! Un jour peut venir, ou le courage des humains faillira, où nous abandonnerons nos amiës, et briserons tout lien. Mais ce jour n'est pas arrivé !")
        self.game.unlock_pokedex_entry(3, "PNJ12.1")