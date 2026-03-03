import pygame

import config
from game_state import GameState


class Fantome_du_lac:
    def __init__(self, screen, game, player):
        self.screen = screen
        self.game = game
        self.player = player

        self.dialog = pygame.image.load("imgs/dialog2.png").convert_alpha()
        self.dialog = pygame.transform.scale(self.dialog, (config.SCREEN_WIDTH//3.5, config.SCREEN_HEIGHT//4.5))
        self.dialogCharlie = pygame.image.load("imgs/dialog.png").convert_alpha()
        self.dialogCharlie = pygame.transform.scale(self.dialog, (config.SCREEN_WIDTH//3.5, config.SCREEN_HEIGHT//4.5))
        
        self.digicode = pygame.image.load("imgs/digicode.png").convert_alpha()
        self.digicode = pygame.transform.scale(self.digicode, (config.SCREEN_WIDTH//2.8, config.SCREEN_HEIGHT//1.3)) 

        self.charlie = pygame.image.load("imgs/characters/charlie.png").convert_alpha()
        self.charlie = pygame.transform.scale(self.charlie, (config.SCREEN_WIDTH //5, config.SCREEN_HEIGHT //1.1))
        self.charlie_content = pygame.image.load("imgs/characters/C_mécontent.png").convert_alpha()
        self.charlie_content = pygame.transform.scale(self.charlie_content, (config.SCREEN_WIDTH //5, config.SCREEN_HEIGHT //1.1))
        
        self.touchesdigicode = pygame.image.load("imgs/digicode2.png").convert_alpha()
        self.touchesdigicode = pygame.transform.scale(self.touchesdigicode, (config.SCREEN_WIDTH//3.2, config.SCREEN_HEIGHT//2.5)) 
        
        self.enigme = pygame.image.load("imgs/enigme.png").convert_alpha()
        self.enigme = pygame.transform.scale(self.enigme, (config.SCREEN_WIDTH//3, config.SCREEN_HEIGHT//4))
        
        # Son de digicode
        self.digicodeFAUX = pygame.mixer.Sound("sons/digicodefaux.ogg")
        self.digicodeVRAI = pygame.mixer.Sound("sons/digicodevrai.ogg")
        self.digicodeFAUX_played = False
        self.digicodeVRAI_played = False
        self.digicodeFAUX.set_volume(0.8)
        self.digicodeVRAI.set_volume(0.8)


        self.cut = 0
        self.max_cut = 12

        # Typewriter state when creating the PNJ
        self.char_delay_ms = 30                     # 1= très rapide ; 100= très lent
        self.current_char = 0
        self.last_update = 0
        self.current_dialogue_total_chars = 0

        # --- Nouveaux attributs pour le choix multiple ---
        self.choice_active = False               # True quand on affiche les choix
        self.choice_index = 0                    # index du choix sélectionné
        self.choice_cols = 4                     # nombre de colonnes
        self.choices = ["0"]
        self.choices1 = ["montae", "xe", "séx", "sae", "monté", "ssi", "sée", "montéi", "sse", "un", "une", "an"]
        self.goodbye = False                     # True après "n'hésite pas à revenir"

    def load(self):
        self.current_char = 0
        self.last_update = pygame.time.get_ticks()
  
    def update(self):
        if self.cut == 1:
            self.game.event = None
        elif self.cut > self.max_cut:
            if hasattr(self.game, "Fantome_du_lac_dialogue_done"):          #hasattr = si il a un attribut (une variable) qui s'appelle "fantomedulac"
                self.game.Fantome_du_lac_dialogue_done = True
                self.game.mondes123.set_volume(0.8)
                self.game.event = None

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.game_state = GameState.ENDED

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game.game_state = GameState.ENDED

                # --- Mode choix actif : flèches + Entrée gèrent le menu ---
                elif self.choice_active:
                    n = len(self.choices)
                    cols = max(1, int(getattr(self, "choice_cols", 3)))

                    if event.key == pygame.K_LEFT:
                        self.choice_index = max(0, self.choice_index - 1)
                    elif event.key == pygame.K_RIGHT:
                        self.choice_index = min(n - 1, self.choice_index + 1)
                    elif event.key == pygame.K_UP:
                        self.choice_index = max(0, self.choice_index - cols)
                    elif event.key == pygame.K_DOWN:
                        self.choice_index = min(n - 1, self.choice_index + cols)
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
            self.cut == 4
            and not self.goodbye
            and not self.choice_active
        ):
            self.choices = self.choices1
            self.choice_active = True
            self.choice_index = 0
        elif (
            self.cut == 5
            and not self.goodbye
            and not self.choice_active
        ):
            self.choices = self.choices1
            self.choice_active = True
            self.choice_index = 0
        elif (
            self.cut == 6
            and not self.goodbye
            and not self.choice_active
        ):
            self.choices = self.choices1
            self.choice_active = True
            self.choice_index = 0
        elif (
            self.cut == 7
            and not self.goodbye
            and not self.choice_active
        ):
            self.choices = self.choices1
            self.choice_active = True
            self.choice_index = 0
        elif (
            self.cut == 8
            and not self.goodbye
            and not self.choice_active
        ):
            self.choices = self.choices1
            self.choice_active = True
            self.choice_index = 0
        elif (
            self.cut == 9
            and not self.goodbye
            and not self.choice_active
        ):
            
            self.choices = self.choices1
            self.choice_active = True
            self.choice_index = 0

        elif (
            self.cut == 10
            and not self.goodbye
            and not self.choice_active
        ):
            
            self.choices = self.choices1
            self.choice_active = True
            self.choice_index = 0
    
    def render(self):
        if self.game.Clef == True and self.cut <2:
            self.cut = 2
            return

        # Si on a choisi "non" -> message d'au revoir
        if self.goodbye:
            self.render_goodbye()
            return

         # --- Si un menu de choix est actif, on n'affiche QUE le menu ---
        if self.choice_active:
            # on affiche la scène (texte) puis on superpose le menu
            # (donc PAS de return)
            pass
            
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

        if self.choice_active:
            self.render_choice()

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


    def _render_dialogue_box_content(self, text):
        dialogue_rect = self.screen.blit(self.dialogCharlie, (config.SCREEN_WIDTH // 2.8, config.SCREEN_HEIGHT // 1.4))      # chiffres = position bulle de dialogue
        self.screen.blit(self.charlie_content, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

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
        dialogue_rect = self.screen.blit(self.dialogCharlie, (config.SCREEN_WIDTH // 2.8, config.SCREEN_HEIGHT // 1.4))      # chiffres = position bulle de dialogue
        self.screen.blit(self.charlie, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

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

    def _render_dialogue_box_Digicode(self, text):
        self.screen.blit(self.digicode, (config.SCREEN_WIDTH // 3.8, config.SCREEN_HEIGHT //16))      # chiffres = position bulle de dialogue
        dialogue_rect = self.screen.blit(self.dialog, (config.SCREEN_WIDTH // 2.8, config.SCREEN_HEIGHT // 1.4))      # chiffres = position bulle de dialogue
        
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
        y = dialogue_rect.y + 40                                      # 30 = décalage avec le haut

        for line in wrapped:
            if chars_left <= 0:
                break
            visible = line[:chars_left]
            surf = font.render(visible, True, color)
            self.screen.blit(surf, (dialogue_rect.x + 30, y))         # chiffre, y = décalage début de bulle
            chars_left -= len(line) + 1
            y += font.get_height() + 6 

    def _render_dialogue_box_Enigme(self, text):
        dialogue_rect = self.screen.blit(self.enigme, (config.SCREEN_WIDTH // 3.5, config.SCREEN_HEIGHT // 9))  

        font = pygame.font.Font("fonts/digicode.ttf", 60)           #20 = taille des lettres
        color = config.WHITE

        max_width = dialogue_rect.width - 60
        max_height = dialogue_rect.height - 60

        font, wrapped = self.get_fitting_font(
            text=text,
            font_path="fonts/digicode.ttf",
            max_width=max_width,
            max_height=max_height,
            start_size=60,
            min_size=12
        )

        self.current_dialogue_total_chars = sum(len(line) + 1 for line in wrapped)

        chars_left = self.current_char
        y = dialogue_rect.y + 5                                      # 30 = décalage avec le haut

        for line in wrapped:
            if chars_left <= 0:
                break
            visible = line[:chars_left]
            surf = font.render(visible, True, color)
            self.screen.blit(surf, (dialogue_rect.x + 15, y))         # chiffre, y = décalage début de bulle
            chars_left -= len(line) + 1
            y += font.get_height() + 6 

    def _render_dialogue_box_Entrée(self, text):
        digicode = self.screen.blit(self.digicode, (config.SCREEN_WIDTH // 3.8, config.SCREEN_HEIGHT //16)) 

        font = pygame.font.Font("fonts/PokemonGb.ttf", 20)           #20 = taille des lettres
        color = config.BLACK

        wrapped = self.wrap_text(text, font, digicode.width - 20)

        self.current_dialogue_total_chars = sum(len(line) + 1 for line in wrapped)

        chars_left = self.current_char
        y = digicode.y + 30                                      # 30 = décalage avec le haut

        for line in wrapped:
            if chars_left <= 0:
                break
            visible = line[:chars_left]
            surf = font.render(visible, True, color)
            self.screen.blit(surf, (digicode.x + 30, y))         # chiffre, y = décalage début de bulle
            chars_left -= len(line) + 1
            y += font.get_height() + 6 

    
    def draw_red_arrow(self, surface, x, y, h):
        """
        Dessine un triangle rouge pointant vers la droite.
        (x, y) = coin haut-gauche
        h = hauteur du triangle
        """
        points = [
            (x, y),               # haut gauche
            (x, y + h),           # bas gauche
            (x + h, y + h // 2),  # pointe
        ]
        pygame.draw.polygon(surface, (220, 0, 0), points)

    # --- NOUVEAU : rendu du menu de choix ---
    def render_choice(self):
        if not getattr(self, "choices", None):
            return

        # 1) dessine la bulle de dialogue de base (comme tes scènes)
        dialogue_rect = self.screen.blit(self.touchesdigicode, (config.SCREEN_WIDTH // 3.4, config.SCREEN_HEIGHT // 2.6))  

        # 2) zone intérieure utilisable (marges)
        pad_x = 10
        pad_y = 40
        inner_x = dialogue_rect.x + pad_x
        inner_y = dialogue_rect.y + pad_y
        inner_w = dialogue_rect.width + 2 * pad_x  #largeur des choix colonne
        inner_h = dialogue_rect.height - 2 * pad_y

        # 3) police + métriques
        font = pygame.font.Font("fonts/digicode.ttf", 27)
        color_text = config.BLACK
        line_h = font.get_height() + 110  #modifier espacement haut-bas

        n = len(self.choices)
        if n == 0:
            return

        # 4) colonnes/rows : on ajuste pour que ça tienne en hauteur
        cols = max(1, int(getattr(self, "choice_cols", 3)))
        max_rows = max(1, inner_h // line_h + 30)

        # si ça ne tient pas, on augmente le nb de colonnes (dans la limite raisonnable)
        rows = (n + cols - 1) // cols
        while rows > max_rows and cols < n:
            cols += 2
            rows = (n + cols - 1) // cols

        # largeur d'une colonne
        col_w = inner_w // cols

        sel = self.choice_index

        # 5) rendu des choix dans la bulle
        for i, choice in enumerate(self.choices):
            r = i // cols
            c = i % cols

            x = inner_x + c * col_w
            y = inner_y + r * line_h - 35 

            # zone de la "cellule"
            cell_rect = pygame.Rect(x, y, col_w, line_h)

            # highlight sélection (cadre discret)
            if i == sel:
                pygame.draw.rect(self.screen, config.BLACK, cell_rect, width=2, border_radius=6)

            text_x = cell_rect.x + 30   # laisse la place pour la flèche
            text_y = cell_rect.y + 30

            txt_surf = font.render(str(choice), True, color_text)
            self.screen.blit(txt_surf, (text_x, text_y))
    
  
    # --- NOUVEAU : logique des réponses ---
    def handle_choice(self):
        choices = self.choices[self.choice_index]

        if choices == "un" :
            self.choice_active = False
            self.goodbye = True
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        elif choices == "ssi" :
            self.choice_active = False
            self.goodbye = True
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        elif choices == "séx" :
            self.choice_active = False
            self.goodbye = True
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        elif choices == "sée" :
            self.choice_active = False
            self.goodbye = True
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        elif choices == "montéi" :
            self.choice_active = False
            self.goodbye = True
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        elif choices == "monté" :
            self.choice_active = False
            self.goodbye = True
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()
   
        elif self.cut == 4:
            if choices == "an" : 
                self.choice_active = False
                self.cut = 5
                self.current_char = 0
                self.last_update = pygame.time.get_ticks()
            else : 
                self.choice_active = False
                self.goodbye = True
                self.current_char = 0
                self.last_update = pygame.time.get_ticks()

        elif self.cut == 5:
            if choices == "sse" : 
                self.choice_active = False
                self.cut = 6
                self.current_char = 0
                self.last_update = pygame.time.get_ticks()
            else : 
                self.choice_active = False
                self.goodbye = True
                self.current_char = 0
                self.last_update = pygame.time.get_ticks()

        elif self.cut == 6:
            if choices == "xe" : 
                self.choice_active = False
                self.cut = 7
                self.current_char = 0
                self.last_update = pygame.time.get_ticks()
            else : 
                self.choice_active = False
                self.goodbye = True
                self.current_char = 0
                self.last_update = pygame.time.get_ticks()

        elif self.cut == 7:
            if choices == "sae" : 
                self.choice_active = False
                self.cut = 8
                self.current_char = 0
                self.last_update = pygame.time.get_ticks()
            else : 
                self.choice_active = False
                self.goodbye = True
                self.current_char = 0
                self.last_update = pygame.time.get_ticks()

        elif self.cut == 8:
            if choices == "montae" : 
                self.choice_active = False
                self.cut = 9
                self.current_char = 0
                self.last_update = pygame.time.get_ticks()
            else : 
                self.choice_active = False
                self.goodbye = True
                self.current_char = 0
                self.last_update = pygame.time.get_ticks()

        elif self.cut == 9:
            if choices == "une" : 
                self.choice_active = False
                self.cut = 10
                self.current_char = 0
                self.last_update = pygame.time.get_ticks()
            else : 
                self.choice_active = False
                self.goodbye = True
                self.current_char = 0
                self.last_update = pygame.time.get_ticks()

        elif self.cut == 10:
            if choices == "une" : 
                self.choice_active = False
                self.cut = 11
                self.current_char = 0
                self.last_update = pygame.time.get_ticks()
            else : 
                self.choice_active = False
                self.goodbye = True
                self.current_char = 0
                self.last_update = pygame.time.get_ticks()



    def render_goodbye(self):
        self.screen.blit(self.digicode, (config.SCREEN_WIDTH // 3.8, config.SCREEN_HEIGHT //16))
        if not self.digicodeFAUX_played:
            self.digicodeFAUX.play()         # Joue le tonnerre
            self.digicodeFAUX_played = True
        self._render_dialogue_box_Answer("Bon, c'est pas ça... Y a plus qu'à recommencer...")
        
    def render_scene_0(self):
        self._render_dialogue_box_Answer("C'est fermé à clef.")

    def render_scene_1(self):
        self._render_dialogue_box_Answer("")

    def render_scene_2(self):
        self._render_dialogue_box_Answer("La clef tourne dans la serrure avec un clic particulièrement satisfaisant.")

    def render_scene_3(self):
        self._render_dialogue_box_Digicode("Mais un digicode empêche encore l'accès à l'intérieur du bâtiment. C'est pas vrai !")
        self._render_dialogue_box_Enigme("__  Rus__, rou__, ru___,  ______  sur  ___  brosse,  ___  rose à la main")

    def render_scene_4(self):
        self._render_dialogue_box_Entrée("")
        self._render_dialogue_box_Enigme("__  Rus__, rou__, ru___,  ______  sur  ___  brosse,  ___  rose à la main")

    def render_scene_5(self):
        self._render_dialogue_box_Entrée("")
        self._render_dialogue_box_Enigme("An Rus__, rou__, ru___,  ______  sur  ___  brosse,  ___  rose à la main")

    def render_scene_6(self):
        self._render_dialogue_box_Entrée("")
        self._render_dialogue_box_Enigme("An Russe, rou__, ru___,  ______  sur  ___  brosse,  ___  rose à la main")

    def render_scene_7(self):
        self._render_dialogue_box_Entrée("")
        self._render_dialogue_box_Enigme("An Russe, rouxe, rus__,  ______  sur  ___  brosse,  ___  rose à la main")

    def render_scene_8(self):
        self._render_dialogue_box_Entrée("")
        self._render_dialogue_box_Enigme("An Russe, rouxe, rusae,  ______  sur  ___  brosse,  ___  rose à la main")

    def render_scene_9(self):
        self._render_dialogue_box_Entrée("")
        self._render_dialogue_box_Enigme("An Russe, rouxe, rusae, montae sur  ___  brosse,  ___  rose à la main")

    def render_scene_10(self):
        self._render_dialogue_box_Entrée("")
        self._render_dialogue_box_Enigme("An Russe, rouxe, rusae, montae sur une rosse,  ___  rose à la main")

    def render_scene_11(self):
        if not self.digicodeVRAI_played:
            self.digicodeVRAI.play()         # Joue le tonnerre
            self.digicodeVRAI_played = True
        self._render_dialogue_box_Digicode("La porte s'ouvre ! Enfin ! Quel satisfaction !")
        self._render_dialogue_box_Enigme("An russe, rouxe, rusae, montae sur une rosse, une rose à la main")

    def render_scene_12(self):
        if self.digicodeVRAI_played:
            self.digicodeVRAI.stop()
            self.digicodeVRAI_played = False
        self._render_dialogue_box_content("Gandalf, t'as intérêt à pas te planter cette fois !")