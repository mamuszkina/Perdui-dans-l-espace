import pygame

import config
from game_state import GameState
from game_state import grayscale


class Gandalf5:
    def __init__(self, screen, game, player, npc_ref=None):
        self.screen = screen
        self.game = game
        self.player = player
        #Dialogue adapté taille écran
        self.dialog = pygame.image.load("imgs/dialog.png").convert_alpha()
        self.dialog = pygame.transform.scale(self.dialog, (config.SCREEN_WIDTH//3.5, config.SCREEN_HEIGHT//4.5))
        self.dialogPNJ = pygame.transform.flip(self.dialog, True, False).convert_alpha()
        self.dialogPNJ = pygame.transform.scale(self.dialogPNJ, (config.SCREEN_WIDTH//3.5, config.SCREEN_HEIGHT//4.5))
        self.dialog_off = pygame.image.load("imgs/dialog2.png").convert_alpha()
        self.dialog_off = pygame.transform.scale(self.dialog_off, (config.SCREEN_WIDTH//3.5, config.SCREEN_HEIGHT//4.5))

        #Perso adaptés taille écran
        self.charlie = pygame.image.load("imgs/characters/charlie.png").convert_alpha()
        self.charlie = pygame.transform.scale(self.charlie, (config.SCREEN_WIDTH //5, config.SCREEN_HEIGHT //1.1))
        self.charlie_gray = grayscale(self.charlie)
        self.charlie_penaud = pygame.image.load("imgs/characters/C_penaud.png").convert_alpha()
        self.charlie_penaud = pygame.transform.scale(self.charlie_penaud, (config.SCREEN_WIDTH //5, config.SCREEN_HEIGHT //1.1))
        self.charlie_penaud_gray = grayscale(self.charlie_penaud)
        self.charlie_surpris = pygame.image.load("imgs/characters/C_surpris.png").convert_alpha()
        self.charlie_surpris = pygame.transform.scale(self.charlie_surpris, (config.SCREEN_WIDTH //5, config.SCREEN_HEIGHT //1.1))
        self.charlie_surpris_gray = grayscale(self.charlie_surpris)
        self.charlie_mécontent = pygame.image.load("imgs/characters/C_mécontent.png").convert_alpha()
        self.charlie_mécontent = pygame.transform.scale(self.charlie_mécontent, (config.SCREEN_WIDTH //5, config.SCREEN_HEIGHT //1.1))
        self.charlie_mécontent_gray = grayscale(self.charlie_mécontent)
        self.charlie_content = pygame.image.load("imgs/characters/C_content.png").convert_alpha()
        self.charlie_content = pygame.transform.scale(self.charlie_content, (config.SCREEN_WIDTH //5, config.SCREEN_HEIGHT //1.1))
        self.charlie_content_gray = grayscale(self.charlie_content)
        self.PNJ = pygame.image.load("imgs/characters/gandalf.png").convert_alpha()
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
        self.choices1 = ["Il a pas forcément tord...", "Oh non, mon pauvre..."]
        self.choices1status = ["attente"]

    def load(self):
        self.current_char = 0
        self.last_update = pygame.time.get_ticks()

        # On réinitialise aussi les états de choix à chaque lancement de PNJ1
        self.choices1status = ["attente"]
        self.choice_active = False
        self.choice_index = 0
  
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
                        self.choice_index = (self.choice_index - 1) % len (self.choices)
                    elif event.key == pygame.K_DOWN:
                        self.choice_index = (self.choice_index + 1) % len (self.choices)
                    elif event.key == pygame.K_RETURN:
                        self.handle_choice()

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
            self.cut == 4
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
        dialogue_rect = self.screen.blit(self.dialogPNJ, (config.SCREEN_WIDTH // 2.8, config.SCREEN_HEIGHT // 1.4))      # chiffres = position bulle de dialogue
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
        y = dialogue_rect.y + 40                                      # 30 = décalage avec le haut

        for line in wrapped:
            if chars_left <= 0:
                break
            visible = line[:chars_left]
            surf = font.render(visible, True, color)
            self.screen.blit(surf, (dialogue_rect.x + 30, y))         # chiffre, y = décalage début de bulle
            chars_left -= len(line) + 1
            y += font.get_height() + 6 

    def _render_dialogue_box_off(self, text):
        dialogue_rect = self.screen.blit(self.dialog_off, (config.SCREEN_WIDTH // 2.8, config.SCREEN_HEIGHT // 1.4))      # chiffres = position bulle de dialogue
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
        y = dialogue_rect.y + 40                                      # 30 = décalage avec le haut

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
        y = dialogue_rect.y + 40                                      # 30 = décalage avec le haut

        for line in wrapped:
            if chars_left <= 0:
                break
            visible = line[:chars_left]
            surf = font.render(visible, True, color)
            self.screen.blit(surf, (dialogue_rect.x + 30, y))         # chiffre, y = décalage début de bulle
            chars_left -= len(line) + 1
            y += font.get_height() + 6 

    # --- NOUVEAU : rendu du menu de choix ---
    def get_fitting_font_for_choices(self, choices, font_path, max_width, max_height,
                                    start_size=20, min_size=12,
                                    line_spacing=6, choice_spacing=8):
        """Trouve une taille de police qui permet d'afficher *tous* les choix dans la bulle.
        - wrap chaque choix sur plusieurs lignes si besoin
        - vérifie que la hauteur totale (toutes les lignes + espacements) rentre dans max_height
        Retourne (font, wrapped_choices) où wrapped_choices = [ [ligne1, ligne2, ...], ... ].
        """
        for size in range(start_size, min_size - 1, -1):
            font = pygame.font.Font(font_path, size)
            wrapped_choices = [self.wrap_text(c, font, max_width) for c in choices]

            total_lines = sum(len(lines) for lines in wrapped_choices)
            if total_lines == 0:
                return font, wrapped_choices

            total_height = total_lines * (font.get_height() + line_spacing)
            total_height += max(0, len(choices) - 1) * choice_spacing

            if total_height <= max_height:
                return font, wrapped_choices

        font = pygame.font.Font(font_path, min_size)
        wrapped_choices = [self.wrap_text(c, font, max_width) for c in choices]
        return font, wrapped_choices

    # --- NOUVEAU : rendu du menu de choix ---
    def render_choice(self):
        dialogue_rect = self.screen.blit(
            self.dialog,
            (config.SCREEN_WIDTH // 2.8, config.SCREEN_HEIGHT // 1.4)
        )
        self.screen.blit(self.charlie_penaud, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        self.screen.blit(self.PNJ_gray, (config.SCREEN_WIDTH // 6, config.SCREEN_HEIGHT * 0.5))

        color = config.BLACK

        # --- Question (optionnelle) ---
        question = ""
        max_width = dialogue_rect.width - 100   # marges gauche/droite
        x_text = dialogue_rect.x + 50
        x_arrow = dialogue_rect.x + 40

        y = dialogue_rect.y + 35

        # 1) Question avec fitting font (si tu en mets une)
        if question:
            q_font, q_lines = self.get_fitting_font(
                text=question,
                font_path="fonts/PokemonGb.ttf",
                max_width=max_width,
                max_height=dialogue_rect.height // 3,
                start_size=20,
                min_size=12
            )
            for line in q_lines:
                surf_q = q_font.render(line, True, color)
                self.screen.blit(surf_q, (dialogue_rect.x + 30, y))
                y += q_font.get_height() + 6
            y += 8
        else:
            y = dialogue_rect.y + 60

        # 2) Fitting font pour tous les choix
        available_height = (dialogue_rect.y + dialogue_rect.height - 30) - y
        font, wrapped_choices = self.get_fitting_font_for_choices(
            choices=self.choices,
            font_path="fonts/PokemonGb.ttf",
            max_width=max_width,
            max_height=available_height,
            start_size=20,
            min_size=12,
            line_spacing=6,
            choice_spacing=10
        )

        line_spacing = 6
        choice_spacing = 10

        # 3) Render multi-lignes
        for i, lines in enumerate(wrapped_choices):
            if not lines:
                lines = [""]

            for j, line in enumerate(lines):
                surf = font.render(line, True, color)
                self.screen.blit(surf, (x_text, y))

                if i == self.choice_index and j == 0:
                    arrow_points = [
                        (x_arrow, y + font.get_height() // 2),
                        (x_arrow - 10, y + 2),
                        (x_arrow - 10, y + font.get_height() - 2),
                    ]
                    pygame.draw.polygon(self.screen, (255, 0, 0), arrow_points)

                y += font.get_height() + line_spacing

            y += choice_spacing   

    # --- NOUVEAU : logique des réponses ---
    def handle_choice(self):
        choices = self.choices[self.choice_index]

        if choices == "Il a pas forcément tord...":
            self.choice_active = False
            self.choices1status = ["fini"]
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        elif choices == "Oh non, mon pauvre...":
            self.choice_active = False
            self.choices1status = ["fini"]
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()


    def render_scene_0(self):
        self._render_dialogue_box_Answer("Gandalf ?! Qu’est-ce que tu fais là ?")
        self.screen.blit(self.charlie_surpris, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_1(self):
        self._render_dialogue_box("Oh, Charlie ! Une chose horrible m’est arrivée ! Quand j’ai été téléporté avec toi dans cette ville, j’ai aterri non pas dans mon labo, mais ici, en plein milieu de la ville !")
        self.screen.blit(self.charlie_surpris_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        
    def render_scene_2(self):
        self._render_dialogue_box_Answer("Mais tu ne peux pas demander au portier de te laisser accéder à ton labo ?")
        self.screen.blit(self.charlie_surpris, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        
    def render_scene_3(self):
        self._render_dialogue_box("J’ai bien essayé, mais cet uluberlu refuse de me laisser entrer ! Il m’a carrément dit d’aller 'apprendre la politesse avant de demander à rentrer chez les gens'!")
        self.screen.blit(self.charlie_surpris_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        
    def render_scene_4(self):
        self._render_dialogue_box("Tu ne peux pas imaginer ce que je ressens, coincé hors de chez moi, sans possibilité de rentrer...")
        self.screen.blit(self.charlie_surpris_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        
    def render_scene_5(self):
        self._render_dialogue_box_Answer("Euh, je crois que si, je peux l’imaginer...")
        self.screen.blit(self.charlie, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        
    def render_scene_6(self):
        self._render_dialogue_box("Et me voilà coincé là, alors que mon labo est à deux pas !")
        self.screen.blit(self.charlie_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        
    def render_scene_7(self):
        self._render_dialogue_box_Answer("Mais tu peux pas nous téléporter autre part ? De toute façon c’est pas chez moi ici, je comprend strictement rien.")
        self.screen.blit(self.charlie, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        
    def render_scene_8(self):
        self._render_dialogue_box("Ben non, tête de noeud ! Je peux pas téléporter les gens comme ca dans la ville, je risque de commettre des dégâts irréparables ! Je dois faire ça dans mon vaisseau, hors de l’espace-temps !")
        self.screen.blit(self.charlie_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        
    def render_scene_9(self):
        self._render_dialogue_box_Answer("Ton vaisseau est hors de l’espace-temps ??!")
        self.screen.blit(self.charlie_surpris, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        
    def render_scene_10(self):
        self._render_dialogue_box("En plus on a besoin de plus d’indices sur ta langue maternelle, tu peux pas te contenter de venir ici et de dire « Eh gnégnégné, c’est pas chez moi là » !")
        self.screen.blit(self.charlie_surpris_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        
    def render_scene_11(self):
        self._render_dialogue_box("Il y a 7 000 langues dans le monde, fiacre de laitue ! En supprimant les langues à classificateurs, il en reste 5110, moins celle là, on est à 5109, à ce rythme on y arrivera jamais !")
        self.screen.blit(self.charlie_surpris_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        
    def render_scene_12(self):
        self._render_dialogue_box_Answer("Hé ben, le portier avait pas tort en te disant d’aller apprendre la politesse...")
        self.screen.blit(self.charlie_penaud, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        
    def render_scene_13(self):
        self._render_dialogue_box_Answer("Mais c’est pas faux. Je dois pouvoir te dire ce qui est pareil et ce qui est différent entre cette langue et la mienne pour qu’on rentre vite.")
        self.screen.blit(self.charlie, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        
    def render_scene_14(self):
        self._render_dialogue_box("C’est ça, fais. Mais ça règle pas le problème, ce portier refuse de me laisser passer !")
        self.screen.blit(self.charlie_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_15(self):
        self._render_dialogue_box_Answer("Si tu m’aides, je t’aide. Accompagne moi pour être mon traducteur, et je me débrouille avec le portier !")
        self.screen.blit(self.charlie, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_16(self):
        self._render_dialogue_box("Fffff moi, un garant du temps et de l’espace de tous les univers connus et inconnus, aux pouvoir sans limites, je vais faire la traduction pour un humain... Trop content... Vraiment trop content.")
        self.screen.blit(self.charlie_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_17(self):
        self._render_dialogue_box_off("Gandalf rejoint ton équipe !")
        self.screen.blit(self.charlie_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        self.game.Gandalf5_dialogue_done = True
        # Après ce dialogue, Gandalf5 rejoint l'équipe et suit le joueur (uniquement monde5/monde5_N hors rooms)
        self.game.gandalf5_following = True
        # Position de départ du follower = dernière position du joueur si dispo
        player = self.game.player
        # On privilégie la dernière position du joueur si elle existe,
        # mais on force toujours une case LIBRE et différente de la case du joueur.
        preferred = []
        if hasattr(player, "last_position"):
            preferred.append(player.last_position[:])

        spawn = self.game._find_free_adjacent_tile_for_gandalf5(preferred_positions=preferred)
        if spawn is None:
            # Fallback (cas extrême) : au pire, on tentera de le placer via sync() juste après.
            spawn = player.last_position[:] if hasattr(player, "last_position") else player.position[:]

        self.game.gandalf5_follower_spawn = [spawn[0], spawn[1]]

        # Refresh immédiat
        self.game.sync_gandalf5_follower_on_current_map()