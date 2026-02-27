import pygame

import config
from game_state import GameState
from game_state import grayscale

class PNJ11:
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
        self.PNJ = pygame.image.load("imgs/characters/trois.png").convert_alpha()
        self.PNJ = pygame.transform.flip(self.PNJ, True, False)
        self.PNJ = pygame.transform.scale(self.PNJ, (config.SCREEN_WIDTH//5, config.SCREEN_HEIGHT//1.1))
        self.PNJ_gray = grayscale(self.PNJ)

        self.cut = 0
        self.max_cut = 17

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
        self.choices1 = ["Acteur", "Acteurice", "Actrice", "Acteurë"]
        self.choices2 = ["agriculteurice", "agriculteuri", "agricultrice"]
        self.choices1status = ["attente"]
        self.choices2status = ["attente"]
#        self.resolved = False
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
        elif self.cut == 16:
            self.game.event = None
        elif self.cut == 8:
            self.cut = 10
        elif self.cut == 13:
            self.cut = 15
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
            self.cut == 7
            and self.choices1status == ["attente"]
            and not self.goodbye
            and not self.choice_active
        ):
            self.choices = self.choices1
            self.choice_active = True
            self.choice_index = 0
 #           self.handle_choice1
        elif (
            self.cut == 12
            and self.choices2status == ["attente"]
            and not self.goodbye
            and not self.choice_active
        ):
            self.choices = self.choices2
            self.choice_active = True
            self.choice_index = 0
    
    def render(self):
        # Si on a choisi "non" -> message d'au revoir
        if self.goodbye:
            self.render_goodbye()
            return

        if self.game.portier3_1_dialogue_done == True and self.cut < 2:
            self.cut = 2
            return 

        if self.game.PNJ11_dialogue_done == True and self.cut < 17:
            self.cut = 17
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
        self._render_dialogue_box("au revoir")

    # --- NOUVEAU : logique des réponses ---
    def handle_choice(self):
        choices = self.choices[self.choice_index]

        if choices == "Acteur":
            self.choice_active = False
            self.choices1status = ["fini"]
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        elif choices == "Acteurice":
            self.choice_active = False
            self.cut = 9
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        elif choices == "Actrice":
            self.choice_active = False
            self.choices1status = ["fini"]
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        elif choices == "Acteurë":
            self.choice_active = False
            self.choices1status = ["fini"]
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()
          
        elif choices == "agriculteurice":
            self.choice_active = False
            self.cut = 14
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()
            
        elif choices == "agriculteuri":
            self.choice_active = False
            self.choices2status = ["fini"]
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()
            
        elif choices == "agricultrice":
            self.choice_active = False
            self.choices2status = ["fini"]
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()
       
#SCENE ZERO
    def render_scene_0(self):
        self._render_dialogue_box("Oui, je peux vous aider ?")

    def render_scene_1(self):
        self._render_dialogue_box_Answer("")
    
#SCENE UN
    def render_scene_2(self):
        self._render_dialogue_box_Answer("Euh salut...")

    def render_scene_3(self):
        self._render_dialogue_box("Bonjour ! On se connait ?")

    def render_scene_4(self):
        self._render_dialogue_box_Answer("Non... Je viens d’arriver en ville pour un... séjour forcé.")
        
    def render_scene_5(self):
        self._render_dialogue_box("Oh tu vas voir tu vas adorer cet endroit ! Moi c'est Alix. Je gagne ma vie en tournant dans des films.")
        
    def render_scene_6(self):
        self._render_dialogue_box_Answer("Oh donc tu es...")
        
    def render_scene_7(self):
        self._render_dialogue_box("Euh, oui, enfin je suis acteurice quoi. Mais c’est pas grave je t’ai comprisse.")
        
    def render_scene_8(self):
        self._render_dialogue_box("")
        
    def render_scene_9(self):
        self._render_dialogue_box("Oui, c’est ça. Je tourne dans des super films, tu m'as sans doute vu dans lea seigneurë des anneaux.")
        
    def render_scene_10(self):
        self._render_dialogue_box("J’ai failli faire un autre métier. Comme toute ma famille est portée sur l’agriculture, j’étais à deux doigts de reprendre le champs de carottes.")
        
    def render_scene_11(self):
        self._render_dialogue_box_Answer("Ah oui, pour devenir...")
        
    def render_scene_12(self):
        self._render_dialogue_box("Agriculteurice, mais tu as l'idée oui.")
        
    def render_scene_13(self):
        self._render_dialogue_box("")
        
    def render_scene_14(self):
        self._render_dialogue_box("Exactement. Je suis bien contende d’y avoir échappéë. Un talent comme le mien, dans des carottes ! Non mais quel gâchis ça auait été !")
        
    def render_scene_15(self):
        self._render_dialogue_box("En tout cas, profite de ton séjour !")
        self.game.unlock_pokedex_entry(3, "PNJ11")
        self.game.unlock_pokedex_entry(3, "PNJ11.1")
        self.game.unlock_pokedex_entry(3, "PNJ11.2")
        
    def render_scene_16(self):
        self._render_dialogue_box("")
        self.game.PNJ11_dialogue_done = True
       
 #SCENES SUIVANTES      
    def render_scene_17(self):
        self._render_dialogue_box("Profite de ton séjour !")