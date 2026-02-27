import pygame

import config
from game_state import GameState
from game_state import grayscale


class Gandalf5_1:
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
        
        #Eclair adapté taille écran
        self.ECLAIR_BLANC = pygame.image.load("imgs/ECLAIR_BLANC.jpg").convert_alpha()
        self.ECLAIR_BLANC = pygame.transform.scale(self.ECLAIR_BLANC, (config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
        # Son de tonnerre
        self.lightning_sound = pygame.mixer.Sound("sons/lightning.mp3")
        self.lightning_played = False
        self.lightning_sound.set_volume(0.8)   # entre 0.0 et 1.0

        self.cut = 0
        self.max_cut = 12
        self.has_teleported = False

        # Typewriter state when creating the PNJ
        self.char_delay_ms = 30                     # 1= très rapide ; 100= très lent
        self.current_char = 0
        self.last_update = 0
        self.current_dialogue_total_chars = 0

    def load(self):
        self.current_char = 0
        self.last_update = pygame.time.get_ticks()
  
    def update(self):
        if self.has_teleported:
            return

        if self.cut > self.max_cut:
            self.game.teleport_to_map("monde6", [14, 30])  # [1, 4] = entry position on map 01
            self.game.event = None
            self.has_teleported = True
            self.lightning_sound.stop()
            self.game.mondes456.set_volume(0.8)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.game_state = GameState.ENDED

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game.game_state = GameState.ENDED

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

    def render(self):      
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
        self._render_dialogue_box("Enfin chez soi ! Fiou, plus jamais je quitte mon labo ! Je suis quand même mieux ici !")
        self.screen.blit(self.charlie_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_1(self):
        self._render_dialogue_box_Answer("J’aimerais bien être enfin chez moi, moi aussi. Mais c'est mal parti. Puis j’ai clairement pas de quoi ranger les liquides, les objets longs, les petits animaux dans ma langue.") 
        self.screen.blit(self.charlie, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_2(self):
        self._render_dialogue_box_Answer("D’ailleurs, je vois pas bien la différence avec la langue d’avant et les classificateurs.")
        self.screen.blit(self.charlie_penaud, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_3(self):
        self._render_dialogue_box("C’est vrai que ça peut se ressembler. Ici il y a concordance des temps. C’est à dire que des mots s’accordent. En quelque sorte, les lettres du groupe se retrouvent sur plusieurs mots qui concernent ce groupe.")
        self.screen.blit(self.charlie_penaud_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_4(self):
        self._render_dialogue_box("Dans la phrase 'je pleure des larmes de croccodile'. Si 'ç' c’est la lettre du liquide, je dis : « Je J-pleure des J-larmes de J-croccodile ». C'est une langue à classe nominale.")
        self.screen.blit(self.charlie_penaud_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_5(self):
        self._render_dialogue_box("Dans une langue à classificateur, comme avant, on aurait simplement dit 'je pleure des larmes de ç-crocodile'.")
        self.screen.blit(self.charlie_penaud_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_6(self):
        self._render_dialogue_box_Answer("Oui, comme dans ma langue, donc... Sauf que moi on range pas les choses comme ça.")
        self.screen.blit(self.charlie, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_7(self):
        self._render_dialogue_box("Mais si tu n’as pas de système pour les liquides, les choses longues, ou autre... Alors tu as quoi ?")
        self.screen.blit(self.charlie_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_8(self):
        self._render_dialogue_box_Answer("Euh ben... Le masculin et le féminin.. Dans ma langue les mots eau, salive, larmes, corde, enfin tout ça, ça dépend juste de leur genre...")
        self.screen.blit(self.charlie, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_9(self):
        self._render_dialogue_box("Mais il fallait le dire de suite ! Alors tu es dans un système de genre grammatical ! Ça change tout, c’est pas du tout le même système de classification ! Parce que les langues à genre grammatical, il y en a 1400 ! Ça réduit nos chances !")
        self.screen.blit(self.charlie_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_10(self):
        self._render_dialogue_box_Answer("ça reste encore beaucoup...")
        self.screen.blit(self.charlie_surpris, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_11(self):
        self._render_dialogue_box("Oh, sois un peu positif ! On a quand même bien avancé ! On sait que tu es dans un système de langue ou il y a une concordance des temps, et ou on classe les choses en fonction du genre. Allez, on tente ! Zou !")
        self.screen.blit(self.charlie_surpris_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_12(self):
        if not self.lightning_played:
            self.game.mondes456.set_volume(0)          # Pause la musique de fond
            self.lightning_sound.play()         # Joue le tonnerre
            self.lightning_played = True
        self._render_dialogue_box_Lightning("KABOOM")
        self.game.tp_monde6 = True