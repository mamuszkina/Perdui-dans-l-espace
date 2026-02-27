import pygame

import config
from game_state import GameState
from game_state import grayscale


class portier5:
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
        self.PNJ = pygame.image.load("imgs/characters/portier.png").convert_alpha()
        self.PNJ = pygame.transform.flip(self.PNJ, True, False)
        self.PNJ = pygame.transform.scale(self.PNJ, (config.SCREEN_WIDTH//5, config.SCREEN_HEIGHT//1.1))
        self.PNJ_gray = grayscale(self.PNJ)

        self.PNJ2 = pygame.image.load("imgs/characters/portier.png").convert_alpha()
        self.PNJ2 = pygame.transform.scale(self.PNJ2, (config.SCREEN_WIDTH//5, config.SCREEN_HEIGHT//1.1))
        self.PNJ2_gray = grayscale(self.PNJ2)
        
        self.gandalf = pygame.image.load("imgs/characters/gandalf.png").convert_alpha()
        self.gandalf = pygame.transform.flip(self.gandalf, True, False)
        self.gandalf = pygame.transform.scale(self.gandalf, (config.SCREEN_WIDTH //5, config.SCREEN_HEIGHT //1.1))
        self.gandalf_gray = grayscale(self.gandalf)

        self.cut = 0
        self.max_cut = 31

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
        if self.cut == 24:
            self.game.event = None
        elif self.cut == 26:
            self.game.event = None
        elif self.cut == 28:
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
        if self.game.Gandalf5_dialogue_done == False and self.cut < 25:
            self.cut = 25
            return

        if self.game.portier5 == True and self.cut < 27:
            self.cut = 27
            return

        if self.game.enfant5_dialogue_done == True and self.cut < 29:
            self.cut = 29
            
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
        elif self.cut == 31:
            self.render_scene_31()
        
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
    def _render_dialogue_box_Gandalf(self, text):
        dialogue_rect = self.screen.blit(self.dialogPNJ, (config.SCREEN_WIDTH // 2.8, config.SCREEN_HEIGHT // 1.4))      # chiffres = position bulle de dialogue
        self.screen.blit(self.gandalf, (config.SCREEN_WIDTH // 6, config.SCREEN_HEIGHT * 0.5))

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

    def _render_dialogue_box(self, text):
        dialogue_rect = self.screen.blit(self.dialog, (config.SCREEN_WIDTH // 2.8, config.SCREEN_HEIGHT // 1.4))      # chiffres = position bulle de dialogue
        self.screen.blit(self.gandalf_gray, (config.SCREEN_WIDTH // 6, config.SCREEN_HEIGHT * 0.5))

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

    def _render_dialogue_box_portier_Gandalf(self, text):
        dialogue_rect = self.screen.blit(self.dialog, (config.SCREEN_WIDTH // 2.8, config.SCREEN_HEIGHT // 1.4))       # chiffres = position bulle de dialogue
        self.screen.blit(self.PNJ2, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        self.screen.blit(self.gandalf_gray, (config.SCREEN_WIDTH // 6, config.SCREEN_HEIGHT * 0.5))
        

        font = pygame.font.Font("fonts/elfique.ttf", 20)           #20 = taille des lettres
        color = config.BLACK

        max_width = dialogue_rect.width - 60
        max_height = dialogue_rect.height - 60

        font, wrapped = self.get_fitting_font(
            text=text,
            font_path="fonts/elfique.ttf",
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

    def _render_dialogue_box_Gandalf_portier(self, text):
        dialogue_rect = self.screen.blit(self.dialogPNJ, (config.SCREEN_WIDTH // 2.8, config.SCREEN_HEIGHT // 1.4))       # chiffres = position bulle de dialogue
        self.screen.blit(self.PNJ2_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        self.screen.blit(self.gandalf, (config.SCREEN_WIDTH // 6, config.SCREEN_HEIGHT * 0.5))
        

        font = pygame.font.Font("fonts/elfique.ttf", 20)           #20 = taille des lettres
        color = config.BLACK

        max_width = dialogue_rect.width - 60
        max_height = dialogue_rect.height - 60

        font, wrapped = self.get_fitting_font(
            text=text,
            font_path="fonts/elfique.ttf",
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

    def _render_dialogue_box_portier_Charlie(self, text):
        dialogue_rect = self.screen.blit(self.dialogPNJ, (config.SCREEN_WIDTH // 2.8, config.SCREEN_HEIGHT // 1.4))       # chiffres = position bulle de dialogue
        self.screen.blit(self.PNJ, (config.SCREEN_WIDTH // 6, config.SCREEN_HEIGHT * 0.5))
        
        font = pygame.font.Font("fonts/elfique.ttf", 20)           #20 = taille des lettres
        color = config.BLACK

        max_width = dialogue_rect.width - 60
        max_height = dialogue_rect.height - 60

        font, wrapped = self.get_fitting_font(
            text=text,
            font_path="fonts/elfique.ttf",
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
            
    def _render_dialogue_box_Answer_PNJ(self, text):
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
        y = dialogue_rect.y + 40

        for line in wrapped:
            if chars_left <= 0:
                break
            visible = line[:chars_left]
            surf = font.render(visible, True, color)
            self.screen.blit(surf, (dialogue_rect.x + 30, y))         # chiffre, y = décalage début de bulle
            chars_left -= len(line) + 1
            y += font.get_height() + 6 

    
      
            
    def render_scene_0(self):
        self._render_dialogue_box("Bon, Gandalf, si tu m'expliquais ce qui s'est passé avec cet homme ?")
        self.screen.blit(self.charlie_mécontent, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_1(self):
        self._render_dialogue_box_Gandalf("Mais rien du tout ! Je parlais tranquillement à quelqu'un d'autre, et ce malfrat est venu m'agresser, que soi-disant j'aurais fait pleurer sa fille !")
        self.screen.blit(self.charlie_mécontent_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        
    def render_scene_2(self):
        self._render_dialogue_box("Et, il dit vrai ?")
        self.screen.blit(self.charlie, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        
    def render_scene_3(self):
        self._render_dialogue_box_Gandalf("Mais j'en sais rien moi si c'est sa fille ! Puis j'ai rien fait du tout, il s'avère juste que j'ai parlé à cette enfant et que par la suite elle a pleuré. Après, est-ce que ça a un rapport, c'est une autre histoire.")
        self.screen.blit(self.charlie_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        
    def render_scene_4(self):
        self._render_dialogue_box("Mais, tu lui disais quoi à cette enfant ?")
        self.screen.blit(self.charlie_surpris, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        
    def render_scene_5(self):
        self._render_dialogue_box_Gandalf("Rien d'autre que la stricte vérité ! C'est une catastrophe, elle fait une faute à chaque phrase qu'elle prononce ! ça irrite mes oreilles délicates !")
        self.screen.blit(self.charlie_surpris_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        
    def render_scene_6(self):
        self._render_dialogue_box("Bon, bon... Je vois. Il va falloir trouver un moyen d'arranger les choses avec cet homme. Fais-lui tes excuses.")
        self.screen.blit(self.charlie, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        
    def render_scene_7(self):
        self._render_dialogue_box_Gandalf("Hors de question ! C'est lui qui devrait s'excuser, j'ai rendu service à sa fille en lui donnant une leçon gratuite !")
        self.screen.blit(self.charlie_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        
    def render_scene_8(self):
        self._render_dialogue_box("Gandalf !")
        self.screen.blit(self.charlie_mécontent, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        
    def render_scene_9(self):
        self._render_dialogue_box_Gandalf("Bon, bon... Mais c'est seulement pour rentrer dans mon labo que j'accepte !")
        self.screen.blit(self.charlie_mécontent_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        
    def render_scene_10(self):
        self._render_dialogue_box_Gandalf_portier("Je suis désolé. ça va comme ça ?")
        
    def render_scene_11(self):
        self._render_dialogue_box_portier_Gandalf("Certainement pas. C'est auprès de ma fille que tu dois t'excuser. Si elle accepte tes excuses je les accepterais aussi.")
        
    def render_scene_12(self):
        self._render_dialogue_box("Alors ?")
        self.screen.blit(self.charlie, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        
    def render_scene_13(self):
        self._render_dialogue_box_Gandalf("Il veut que j'aille m'excuser auprès de sa fille.")
        self.screen.blit(self.charlie_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        
    def render_scene_14(self):
        self._render_dialogue_box("Logique. C'est tout ?")
        self.screen.blit(self.charlie, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_15(self):
        self._render_dialogue_box_Gandalf("Il veut aussi que je donne un vrai cours de langue à sa fille en compensation.")
        self.screen.blit(self.charlie_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_16(self):
        self._render_dialogue_box("Ah ben ça va être facile pour un linguiste de l'univers comme toi !")
        self.screen.blit(self.charlie_content, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_17(self):
        self._render_dialogue_box_Gandalf("Mais non c'est pas facile ! Je les connais pas les règles de grammaire ! J'interagis avec le subsconscient des gens je te rappelle ! ça a pas de règles le subconscient ! Je sais juste si les prases sont correctes ou pas !")
        self.screen.blit(self.charlie_content_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_18(self):
        self._render_dialogue_box("Sérieusement ? Tu ennuies cette petite fille alors que tu ne peux même pas dire ce qu'elle dit de faux ? Vraiment Gandalf...")
        self.screen.blit(self.charlie_mécontent, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_19(self):
        self._render_dialogue_box("En tout cas ça va pas me changer de d'habitude. On va aller parler à des gens, lire ce qu'on peut lire, et on comprendra bien deux trois règles pour faire plaisir à son père.")
        self.screen.blit(self.charlie, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_20(self):
        self._render_dialogue_box("Il faudrait pouvoir prendre des notes de ce qu'on trouve comme règles. J'ai vu un grand panneau blanc sur la place, on pourra écrire dessus.")
        self.screen.blit(self.charlie, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_21(self):
        self._render_dialogue_box_Gandalf("Il faut aussi trouver la petite fille. Elle est partie en courant après notre... Discussion.")
        self.screen.blit(self.charlie_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_22(self):
        self._render_dialogue_box("ça, ça peut attendre. Déjà on cherche des règles de dialogue, puis on note tout sur le tableau blanc, et quand on semble être prêts on cherche l'enfant pour lui dire ce qu'on a appris.")
        self.screen.blit(self.charlie, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_23(self):
        self._render_dialogue_box("Allez, en route.")
        self.screen.blit(self.charlie, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_24(self):
        self._render_dialogue_box("")
        self.game.portier5 = True

    def render_scene_25(self):
        self._render_dialogue_box_portier_Charlie("Et bla et bla et blablabla")
        self.screen.blit(self.charlie_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_26(self):
        self._render_dialogue_box_portier_Charlie("")

    def render_scene_27(self):
        self._render_dialogue_box("On sait ce qu'on a à faire. Allons chercher des indices sur la langue.")
        self.screen.blit(self.charlie, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_28(self):
        self._render_dialogue_box("")

    def render_scene_29(self):
        self._render_dialogue_box_portier_Charlie("Ma fille est venue me voir, elle m'a dit que le monsieur avait été gentil avec elle. Elle m'a aussi raconté la leçon que vous lui avez donnée. Gandalf, vous pouvez remercier votre ami je pense.")
        self.screen.blit(self.charlie_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_30(self):
        self._render_dialogue_box_Gandalf("Il dit que sa fille est venue le voir et qu'elle va mieux. On va enfin pouvoir rentrer chez nous.")
        self.screen.blit(self.charlie_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_31(self):
        self._render_dialogue_box("ça veut dire qu'il nous laisse passer ? Oh merci ! Merci monsieur ! Allez, on file à ton labo !")
        self.screen.blit(self.charlie_content, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        self.game.portier5_2_dialogue_done = True