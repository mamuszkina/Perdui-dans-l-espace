import pygame

import config
from game_state import GameState

import webbrowser


class bibliothèque:
    def __init__(self, screen, game, player):
        self.screen = screen
        self.game = game
        self.player = player
        self.dialog = pygame.image.load("imgs/dialog2.png").convert_alpha()
        self.dialog = pygame.transform.scale(self.dialog, (config.SCREEN_WIDTH//3.5, config.SCREEN_HEIGHT//4.5))

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
        self.choices1 = ["A grammar of sabane, A Nambikwaran Language", "Mes premiers classificateurs, mon livre illustré", "Serpents AMOKA et lézards AMOKA de nos régions", "Partir"]
        self.choices1status = ["attente"]
        self.choices2 = ["Reposer le livre", "Tourner la page"]
        self.choices2status = ["attente"]
        self.choices3 = ["La grenouille", "La graine d'avocat", "L'araignée", "Le serpent"]
        self.choices3status = ["attente"]
        self.goodbye = False                     # True après "n'hésite pas à revenir"
#        self.internet = False

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
            self.cut == 1
            and self.choices1status == ["attente"]
            and not self.goodbye
            and not self.choice_active
        ):
            self.choices = self.choices1
            self.choice_active = True
            self.choice_index = 0

        if (
            self.cut == 3
            and self.choices1status == ["attente"]
            and not self.goodbye
            and not self.choice_active
        ):
            self.choices = self.choices1
            self.choice_active = True
            self.choice_index = 0
            
        if (
            self.cut == 6
            and self.choices2status == ["attente"]
            and not self.goodbye
            and not self.choice_active
        ):
            self.choices = self.choices2
            self.choice_active = True
            self.choice_index = 0
            
        if (
            self.cut == 9
            and self.choices3status == ["attente"]
            and not self.goodbye
            and not self.choice_active
        ):
            self.choices = self.choices3
            self.choice_active = True
            self.choice_index = 0
            
        if (
            self.cut == 11
            and self.choices3status == ["attente"]
            and not self.goodbye
            and not self.choice_active
        ):
            self.choices = self.choices3
            self.choice_active = True
            self.choice_index = 0
            
        if (
            self.cut == 14
            and self.choices1status == ["attente"]
            and not self.goodbye
            and not self.choice_active
        ):
            self.choices = self.choices1
            self.choice_active = True
            self.choice_index = 0
            
        if (
            self.cut == 18
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
        dialogue_rect = self.screen.blit(self.dialog, (config.SCREEN_WIDTH // 2.8, config.SCREEN_HEIGHT // 1.4))

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
        dialogue_rect = self.screen.blit(self.dialog, (config.SCREEN_WIDTH // 2.8, config.SCREEN_HEIGHT // 1.4))

        font = pygame.font.Font("fonts/PokemonGb.ttf", 20)
        color = config.BLACK

        # --- Question ---
        question = ""
        surf_q = font.render(question, True, color)
        self.screen.blit(surf_q, (dialogue_rect.x + 30, dialogue_rect.y + 20))

        # Positions de base
        y = dialogue_rect.y + 60
        x_text = dialogue_rect.x + 30
        x_arrow = dialogue_rect.x + 20

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

        
        if choices == "A grammar of sabane, A Nambikwaran Language":
            self.choice_active = False
            self.cut = 2
            webbrowser.open("https://130.60.24.118/gramfinder/p/south_america/dearaujo_sabane2004v2_o.pdf")
            pass
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        elif choices == "Mes premiers classificateurs, mon livre illustré":
            self.choice_active = False
            self.cut = 4
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        elif choices == "Reposer le livre":
            self.choice_active = False
            self.choices = self.choices1
            self.choice_active = True
            self.choice_index = 0
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()
            

        elif choices == "Tourner la page":
            self.choice_active = False
            self.cut = 7
            self.current_char = 0
            self.last_update = pygame.time.get_ticks() 
            
        elif choices == "La grenouille":
            self.choice_active = False
            self.cut = 10
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()
            
        elif choices == "La graine d'avocat":
            self.choice_active = False
            self.cut = 10
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()
            
        elif choices == "L'araignée":
            self.choice_active = False
            self.cut = 10
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()
            
        elif choices == "Le serpent":
            self.choice_active = False
            self.cut = 12
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()
            
        elif choices == "Serpents AMOKA et lézards AMOKA de nos régions":
            self.choice_active = False
            self.cut = 15
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()
            
        elif choices == "Partir":
            self.choice_active = False
            self.goodbye = True
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

    def render_goodbye(self):
        self._render_dialogue_box("Je lirai peut-être plus tard.")


        
        
        
    def render_scene_0(self):
        self._render_dialogue_box("Il y a plein de livres dans cette bibliothèque... Lequel je peux lire ?")

    def render_scene_1(self):
        self._render_dialogue_box("")
        
#LIVRE A RALLONGE
    def render_scene_2(self):
        self._render_dialogue_box("Cest un livre de plus de mille pages sur toutes les règles de la langue. C’est sûr qu’avec ça je comprendrais tout, mais je serais mort de vieillesse avant d’avoir fini de le lire")
#        webbrowser.open("https://130.60.24.118/gramfinder/p/south_america/dearaujo_sabane2004v2_o.pdf")

    def render_scene_3(self):
        self._render_dialogue_box ("")

    def render_scene_4(self):
        self._render_dialogue_box("Les classificateurs peuvent indiquer la forme d’un mot. Par exemple, le classificateur IAWA désigne les objets qui ont une forme de barque.")
        self.game.unlock_pokedex_entry(4, "bibliothèque.0")

    def render_scene_5(self):
        self._render_dialogue_box("Les barques, les cuillers, les pelures de fruits, tous ces objets ont cette forme particulière aux barques. On dit donc une barque IAWA, une pelure de fruit IAWA, une cuillère IAWA.")

    def render_scene_6(self):
        self._render_dialogue_box("")

    def render_scene_7(self):
        self._render_dialogue_box("Pour savoir quels sont les classificateurs à utiliser, il suffit de comprendre la forme de l’objet.")
        self.game.unlock_pokedex_entry(4, "bibliothèque.1")

    def render_scene_8(self):
        self._render_dialogue_box("Essaie avec ces objets ! D’après toi, quel est l’intrus parmi une une grenouille, une araignée, une graine d’avocat et un serpent ?")
#CREER UN DIALOGUE TEXT AVEC UNE GRENOUILLE, UNE ARAIGNEE UN AVOCAT ET UN SERPENT QUI S'AFFICHENT A L'ECRAN

    def render_scene_9(self):
        self._render_dialogue_box("")

    def render_scene_10(self):
        self._render_dialogue_box("Regade bien la forme de cet objet. Il est rond, comme les autres. Lequel n'est pas rond ?")

#SCENE TROIS
    def render_scene_11(self):
        self._render_dialogue_box("")

    def render_scene_12(self):
        self._render_dialogue_box("Bingo ! Le serpent a beau être un animal comme la grenouille et l’araignée, il n’est pas rond ! Il sera défini par un autre classificateur. Le classificateur des objets ronds est ISI. On dit « une grenouille ISI », « une araignée ISI », « une graine d’avocat ISI »")
        self.game.unlock_pokedex_entry(4, "bibliothèque.2")

    def render_scene_13(self):
        self._render_dialogue_box("Le livre s'arrête ici.")

    def render_scene_14(self):
        self._render_dialogue_box("")

    def render_scene_15(self):
        self._render_dialogue_box("C’est un livre qui parle des animaux qu’on peut trouver dans la forêt. Il y a toujours écrit AMOKA après les mots serpents et lézards. ")

    def render_scene_16(self):
        self._render_dialogue_box("Les serpents AMOKA et les lézards AMOKA sont nombreux dans la région. Ces animaux sont long et flexibles, tout comme les larves AMOKA, les mille pattes AMOKA dont ils se nourrissent.")
        self.game.unlock_pokedex_entry(4, "bibliothèque.3")

    def render_scene_17(self):
        self._render_dialogue_box("Le livre s'arrête ici.")

    def render_scene_18(self):
        self._render_dialogue_box("")