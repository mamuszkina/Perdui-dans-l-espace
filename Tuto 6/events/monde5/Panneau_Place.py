import pygame

import config
from game_state import GameState
from game_state import grayscale


class Panneau_Place:
    def __init__(self, screen, game, player):
        self.screen = screen
        self.game = game
        self.player = player
        #Dialogue adapté taille écran
        self.dialog = pygame.image.load("imgs/dialog.png").convert_alpha()
        self.dialog = pygame.transform.scale(self.dialog, (config.SCREEN_WIDTH//3.5, config.SCREEN_HEIGHT//4.5))
        self.dialogPNJ = pygame.transform.flip(self.dialog, True, False).convert_alpha()
        self.dialogPNJ = pygame.transform.scale(self.dialogPNJ, (config.SCREEN_WIDTH//3.5, config.SCREEN_HEIGHT//4.5))

        self.panneau = pygame.image.load("imgs/monde5/dessin_panneau.png").convert_alpha()
        self.panneau = pygame.transform.scale(self.panneau, (config.SCREEN_WIDTH//1.5, config.SCREEN_HEIGHT//1.5))

        #Perso adaptés taille écran
        self.charlie = pygame.image.load("imgs/characters/charlie.png").convert_alpha()
        self.charlie = pygame.transform.scale(self.charlie, (config.SCREEN_WIDTH //5, config.SCREEN_HEIGHT //1.1))
        self.charlie_gray = grayscale(self.charlie)
        self.PNJ = pygame.image.load("imgs/characters/gandalf.png").convert_alpha()
        self.PNJ = pygame.transform.flip(self.PNJ, True, False)
        self.PNJ = pygame.transform.scale(self.PNJ, (config.SCREEN_WIDTH//5, config.SCREEN_HEIGHT//1.1))
        self.PNJ_gray = grayscale(self.PNJ)
        
        self.homme = pygame.image.load("imgs/monde5/homme.png").convert_alpha()
        self.homme = pygame.transform.scale(self.homme, (config.SCREEN_WIDTH//23, config.SCREEN_HEIGHT//14))
        self.femme = pygame.image.load("imgs/monde5/femme.png").convert_alpha()
        self.femme = pygame.transform.scale(self.femme, (config.SCREEN_WIDTH//19, config.SCREEN_HEIGHT//12.5))
        self.boue = pygame.image.load("imgs/monde5/boue.png").convert_alpha()
        self.boue = pygame.transform.scale(self.boue, (config.SCREEN_WIDTH//12, config.SCREEN_HEIGHT//16))
        self.croccodile = pygame.image.load("imgs/monde5/crocodile.png").convert_alpha()
        self.croccodile = pygame.transform.scale(self.croccodile, (config.SCREEN_WIDTH//10, config.SCREEN_HEIGHT//15))
        self.beau_frere = pygame.image.load("imgs/monde5/beau-frère.png").convert_alpha()
        self.beau_frere = pygame.transform.scale(self.beau_frere, (config.SCREEN_WIDTH//20, config.SCREEN_HEIGHT//13.5))
        self.belle_soeur = pygame.image.load("imgs/monde5/belle-soeur.png").convert_alpha()
        self.belle_soeur = pygame.transform.scale(self.belle_soeur, (config.SCREEN_WIDTH//18, config.SCREEN_HEIGHT//14))
        self.tetard = pygame.image.load("imgs/monde5/têtard.png").convert_alpha()
        self.tetard = pygame.transform.scale(self.tetard, (config.SCREEN_WIDTH//13, config.SCREEN_HEIGHT//15))
        self.lait = pygame.image.load("imgs/monde5/lait.png").convert_alpha()
        self.lait = pygame.transform.scale(self.lait, (config.SCREEN_WIDTH//17, config.SCREEN_HEIGHT//12))
        self.pigeon = pygame.image.load("imgs/monde5/pigeon.png").convert_alpha()
        self.pigeon = pygame.transform.scale(self.pigeon, (config.SCREEN_WIDTH//12.6, config.SCREEN_HEIGHT//12))
        self.chauve_souris = pygame.image.load("imgs/monde5/chauve-souris.png").convert_alpha()
        self.chauve_souris = pygame.transform.scale(self.chauve_souris, (config.SCREEN_WIDTH//13, config.SCREEN_HEIGHT//14))
        self.rat = pygame.image.load("imgs/monde5/rat.png").convert_alpha()
        self.rat = pygame.transform.scale(self.rat, (config.SCREEN_WIDTH//12.6, config.SCREEN_HEIGHT//12))
        self.mari = pygame.image.load("imgs/monde5/mari.png").convert_alpha()
        self.mari = pygame.transform.scale(self.mari, (config.SCREEN_WIDTH//18, config.SCREEN_HEIGHT//13))
        self.larmes = pygame.image.load("imgs/monde5/larmes.png").convert_alpha()
        self.larmes = pygame.transform.scale(self.larmes, (config.SCREEN_WIDTH//10, config.SCREEN_HEIGHT//13))
        self.salive = pygame.image.load("imgs/monde5/salive.png").convert_alpha()
        self.salive = pygame.transform.scale(self.salive, (config.SCREEN_WIDTH//15, config.SCREEN_HEIGHT//12))
        self.corde = pygame.image.load("imgs/monde5/corde.png").convert_alpha()
        self.corde = pygame.transform.scale(self.corde, (config.SCREEN_WIDTH//11, config.SCREEN_HEIGHT//15))
        self.serpent = pygame.image.load("imgs/monde5/serpent.png").convert_alpha()
        self.serpent = pygame.transform.scale(self.serpent, (config.SCREEN_WIDTH//15, config.SCREEN_HEIGHT//15))
        self.langue = pygame.image.load("imgs/monde5/langue.png").convert_alpha()
        self.langue = pygame.transform.scale(self.langue, (config.SCREEN_WIDTH//14, config.SCREEN_HEIGHT//14))

        self.cut = 0
        self.max_cut = 106

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
        self.choices1 = ["Partir"]
        self.choices2 = ["ù", "à", "ç", "é"]
        self.choices1status = ["attente"]
        self.choices2status = ["attente"]
        self.goodbye = False                     # True après "n'hésite pas à revenir"

    def load(self):
        self.current_char = 0
        self.last_update = pygame.time.get_ticks()
  
    def update(self):
        if self.cut == 1:
            self.game.event = None
        elif self.cut == 7:
            self.cut = 3
        elif self.cut == 13:
            self.cut = 3
        elif self.cut == 19:
            self.cut = 3
        elif self.cut == 25:
            self.cut = 3
        elif self.cut == 31:
            self.cut = 3
        elif self.cut == 37:
            self.cut = 3
        elif self.cut == 43:
            self.cut = 3
        elif self.cut == 49:
            self.cut = 3
        elif self.cut == 55:
            self.cut = 3
        elif self.cut == 61:
            self.cut = 3
        elif self.cut == 67:
            self.cut = 3
        elif self.cut == 73:
            self.cut = 3
        elif self.cut == 79:
            self.cut = 3
        elif self.cut == 85:
            self.cut = 3
        elif self.cut == 91:
            self.cut = 3
        elif self.cut == 97:
            self.cut = 3
        elif self.cut == 103:
            self.cut = 3
        elif self.cut == 9:
            self.cut = 5
        elif self.cut == 15:
            self.cut = 11
        elif self.cut == 21:
            self.cut = 17
        elif self.cut == 27:
            self.cut = 23
        elif self.cut == 33:
            self.cut = 29
        elif self.cut == 39:
            self.cut = 35
        elif self.cut == 45:
            self.cut = 41
        elif self.cut == 51:
            self.cut = 47
        elif self.cut == 57:
            self.cut = 53
        elif self.cut == 63:
            self.cut = 59
        elif self.cut == 69:
            self.cut = 6
        elif self.cut == 75:
            self.cut = 71
        elif self.cut == 81:
            self.cut = 77
        elif self.cut == 87:
            self.cut = 83
        elif self.cut == 93:
            self.cut = 89
        elif self.cut == 99:
            self.cut = 95
        elif self.cut == 105:
            self.cut = 101
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
            self.choices = self.choices1
            if self.game.homme == True and self.game.homme_finito == False :
                self.choices = self.choices + ["homme"]
            if self.game.boue == True and self.game.boue_finito == False :
                self.choices = self.choices + ["boue"]
            if self.game.croccodile == True and self.game.croccodile_finito == False :
                self.choices = self.choices + ["crocodile"]
            if self.game.beau_frère == True and self.game.beau_frère_finito == False :
                self.choices = self.choices + ["beau-frère"]
            if self.game.belle_soeur == True and self.game.belle_soeur_finito == False :
                self.choices = self.choices + ["belle-soeur"]
            if self.game.têtard == True and self.game.têtard_finito == False :
                self.choices = self.choices + ["têtard"]
            if self.game.lait == True and self.game.lait_finito == False :
                self.choices = self.choices + ["lait"]
            if self.game.pigeon == True and self.game.pigeon_finito == False :
                self.choices = self.choices + ["pigeon"]
            if self.game.chauve_souris == True and self.game.chauve_souris_finito == False :
                self.choices = self.choices + ["chauve-souris"]
            if self.game.rat == True and self.game.rat_finito == False :
                self.choices = self.choices + ["rat"]
            if self.game.mari == True and self.game.mari_finito == False :
                self.choices = self.choices + ["mari"]
            if self.game.larmes == True and self.game.larmes_finito == False :
                self.choices = self.choices + ["larmes"]
            if self.game.salive == True and self.game.salive_finito == False :
                self.choices = self.choices + ["salive"]
            if self.game.corde == True and self.game.corde_finito == False :
                self.choices = self.choices + ["corde"]
            if self.game.serpent == True and self.game.serpent_finito == False :
                self.choices = self.choices + ["serpent"]
            if self.game.langue == True and self.game.langue_finito == False :
                self.choices = self.choices + ["langue"]
            if self.game.femme == True and self.game.femme_finito == False :
                self.choices = self.choices + ["femme"]
            self.choice_active = True
            self.choice_index = 0
        
        elif (
            self.cut in(5, 11, 17, 23, 29, 35, 41, 47, 53, 59, 65, 71, 77, 83, 89, 95, 101)
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
            
        # --- le panneau est TOUJOURS visible pendant l'event ---
        self.screen.blit(self.panneau, (config.SCREEN_WIDTH // 6, config.SCREEN_HEIGHT // 10))

        if self.game.portier5 == True and self.cut <2:
            self.cut = 2
            return

        if self.game.homme_finito == True :
            self.screen.blit(self.homme, (config.SCREEN_WIDTH // 2, config.SCREEN_HEIGHT // 2.3))

        if self.game.boue_finito == True :
            self.screen.blit(self.boue, (config.SCREEN_WIDTH // 2.5, config.SCREEN_HEIGHT // 3.35))

        if self.game.croccodile_finito == True :
            self.screen.blit(self.croccodile, (config.SCREEN_WIDTH // 1.75 ,config.SCREEN_HEIGHT // 3.35)) 

        if self.game.beau_frère_finito == True :
            self.screen.blit(self.beau_frere, (config.SCREEN_WIDTH // 1.8, config.SCREEN_HEIGHT // 2.1))

        if self.game.belle_soeur_finito == True :
            self.screen.blit(self.belle_soeur, (config.SCREEN_WIDTH //1.6, config.SCREEN_HEIGHT //2.1))

        if self.game.têtard_finito == True :
            self.screen.blit(self.tetard, (config.SCREEN_WIDTH // 2.5, config.SCREEN_HEIGHT // 2.13))

        if self.game.lait_finito == True :
            self.screen.blit(self.lait, (config.SCREEN_WIDTH // 4.2, config.SCREEN_HEIGHT // 3.7))

        if self.game.pigeon_finito == True :
            self.screen.blit(self.pigeon, (config.SCREEN_WIDTH // 3.1, config.SCREEN_HEIGHT // 2.08))

        if self.game.chauve_souris_finito == True :
            self.screen.blit(self.chauve_souris, (config.SCREEN_WIDTH // 3.1, config.SCREEN_HEIGHT // 2.7))

        if self.game.rat_finito == True :
            self.screen.blit(self.rat, (config.SCREEN_WIDTH // 3.8, config.SCREEN_HEIGHT // 2.3))

        if self.game.mari_finito == True :
            self.screen.blit(self.mari, (config.SCREEN_WIDTH //1.45, config.SCREEN_HEIGHT //2.4))

        if self.game.larmes_finito == True :
            self.screen.blit(self.larmes, (config.SCREEN_WIDTH //3.1, config.SCREEN_HEIGHT //5))

        if self.game.salive_finito == True :
            self.screen.blit(self.salive, (config.SCREEN_WIDTH // 3.1, config.SCREEN_HEIGHT // 3.6))

        if self.game.corde_finito == True :
            self.screen.blit(self.corde, (config.SCREEN_WIDTH // 2, config.SCREEN_HEIGHT // 3.8))

        if self.game.serpent_finito == True :
            self.screen.blit(self.serpent, (config.SCREEN_WIDTH //1.45, config.SCREEN_HEIGHT //3.35))

        if self.game.langue_finito == True :
            self.screen.blit(self.langue, (config.SCREEN_WIDTH // 1.6 ,config.SCREEN_HEIGHT // 4.4))

        if self.game.femme_finito == True :
            self.screen.blit(self.femme, (config.SCREEN_WIDTH // 1.8, config.SCREEN_HEIGHT // 2.6))

        if self.game.femme_finito == True and self.game.langue_finito == True and self.game.serpent_finito == True and self.game.corde_finito == True and self.game.salive_finito == True and self.game.larmes_finito == True and self.game.mari_finito == True and self.game.rat_finito == True and self.game.chauve_souris_finito == True and self.game.pigeon_finito == True and self.game.lait_finito == True and self.game.belle_soeur_finito == True and self.game.beau_frère_finito == True and self.game.croccodile_finito == True and self.game.boue_finito == True and self.game.homme_finito == True and self.cut < 106 :
            self.cut = 106


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
        elif self.cut == 32:
            self.render_scene_32()
        elif self.cut == 33:
            self.render_scene_33()
        elif self.cut == 34:
            self.render_scene_34()
        elif self.cut == 35:
            self.render_scene_35()
        elif self.cut == 36:
            self.render_scene_36()
        elif self.cut == 37:
            self.render_scene_37()
        elif self.cut == 38:
            self.render_scene_38()
        elif self.cut == 39:
            self.render_scene_39()
        elif self.cut == 40:
            self.render_scene_40()
        elif self.cut == 41:
            self.render_scene_41()
        elif self.cut == 42:
            self.render_scene_42()
        elif self.cut == 43:
            self.render_scene_43()
        elif self.cut == 44:
            self.render_scene_44()
        elif self.cut == 45:
            self.render_scene_45()
        elif self.cut == 46:
            self.render_scene_46()
        elif self.cut == 47:
            self.render_scene_47()
        elif self.cut == 48:
            self.render_scene_48()
        elif self.cut == 49:
            self.render_scene_49()
        elif self.cut == 50:
            self.render_scene_50()
        elif self.cut == 51:
            self.render_scene_51()
        elif self.cut == 52:
            self.render_scene_52()
        elif self.cut == 53:
            self.render_scene_53()
        elif self.cut == 54:
            self.render_scene_54()
        elif self.cut == 55:
            self.render_scene_55()
        elif self.cut == 56:
            self.render_scene_56()
        elif self.cut == 57:
            self.render_scene_57()
        elif self.cut == 58:
            self.render_scene_58()
        elif self.cut == 59:
            self.render_scene_59()
        elif self.cut == 60:
            self.render_scene_60()
        elif self.cut == 61:
            self.render_scene_61()
        elif self.cut == 62:
            self.render_scene_62()
        elif self.cut == 63:
            self.render_scene_63()
        elif self.cut == 64:
            self.render_scene_64()
        elif self.cut == 65:
            self.render_scene_65()
        elif self.cut == 66:
            self.render_scene_66()
        elif self.cut == 67:
            self.render_scene_67()
        elif self.cut == 68:
            self.render_scene_68()
        elif self.cut == 69:
            self.render_scene_69()
        elif self.cut == 70:
            self.render_scene_70()
        elif self.cut == 71:
            self.render_scene_71()
        elif self.cut == 72:
            self.render_scene_72()
        elif self.cut == 73:
            self.render_scene_73()
        elif self.cut == 74:
            self.render_scene_74()
        elif self.cut == 75:
            self.render_scene_75()
        elif self.cut == 76:
            self.render_scene_76()
        elif self.cut == 77:
            self.render_scene_77()
        elif self.cut == 78:
            self.render_scene_78()
        elif self.cut == 79:
            self.render_scene_79()
        elif self.cut == 80:
            self.render_scene_80()
        elif self.cut == 81:
            self.render_scene_81()
        elif self.cut == 82:
            self.render_scene_82()
        elif self.cut == 83:
            self.render_scene_83()
        elif self.cut == 84:
            self.render_scene_84()
        elif self.cut == 85:
            self.render_scene_85()
        elif self.cut == 86:
            self.render_scene_86()
        elif self.cut == 87:
            self.render_scene_87()
        elif self.cut == 88:
            self.render_scene_88()
        elif self.cut == 89:
            self.render_scene_89()
        elif self.cut == 90:
            self.render_scene_90()
        elif self.cut == 91:
            self.render_scene_91()
        elif self.cut == 92:
            self.render_scene_92()
        elif self.cut == 93:
            self.render_scene_93()
        elif self.cut == 94:
            self.render_scene_94()
        elif self.cut == 95:
            self.render_scene_95()
        elif self.cut == 96:
            self.render_scene_96()
        elif self.cut == 97:
            self.render_scene_97()
        elif self.cut == 98:
            self.render_scene_98()
        elif self.cut == 99:
            self.render_scene_99()
        elif self.cut == 100:
            self.render_scene_100()
        elif self.cut == 101:
            self.render_scene_101()
        elif self.cut == 102:
            self.render_scene_102()
        elif self.cut == 103:
            self.render_scene_103()
        elif self.cut == 104:
            self.render_scene_104()
        elif self.cut == 105:
            self.render_scene_105()
        elif self.cut == 106:
            self.render_scene_106()
        
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
    def _render_dialogue_box_Charlie_Seul(self, text):
        dialogue_rect = self.screen.blit(self.dialog, (config.SCREEN_WIDTH // 2.8, config.SCREEN_HEIGHT // 1.4))      # chiffres = position bulle de dialogue
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

    def _render_dialogue_box_Gandalf(self, text):
        dialogue_rect = self.screen.blit(self.dialogPNJ, (config.SCREEN_WIDTH // 2.8, config.SCREEN_HEIGHT // 1.4))      # chiffres = position bulle de dialogue
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
        self.screen.blit(self.charlie, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
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

    # --- NOUVEAU : message quand le joueur répond "non" ---
    def render_goodbye(self):
        self._render_dialogue_box_Answer("Je continuerais plus tard.")

    # --- NOUVEAU : logique des réponses ---
    def handle_choice(self):
        choices = self.choices[self.choice_index]

        if choices == "homme":
            self.choice_active = False
            self.cut = 4
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        elif choices == "boue":
            self.choice_active = False
            self.cut = 10
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        elif choices == "crocodile":
            self.choice_active = False
            self.cut = 16
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()
            
        elif choices == "beau-frère":
            self.choice_active = False
            self.cut = 22
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        elif choices == "belle-soeur":
            self.choice_active = False
            self.cut = 28
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        elif choices == "têtard":
            self.choice_active = False
            self.cut = 34
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        elif choices == "lait":
            self.choice_active = False
            self.cut = 40
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()
            
        elif choices == "pigeon":
            self.choice_active = False
            self.cut = 46
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        elif choices == "chauve-souris":
            self.choice_active = False
            self.cut = 52
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        elif choices == "rat":
            self.choice_active = False
            self.cut = 58
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        elif choices == "mari":
            self.choice_active = False
            self.cut = 64
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()
            
        elif choices == "larmes":
            self.choice_active = False
            self.cut = 70
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        elif choices == "salive":
            self.choice_active = False
            self.cut = 76
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        elif choices == "corde":
            self.choice_active = False
            self.cut = 82
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        elif choices == "serpent":
            self.choice_active = False
            self.cut = 88
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()
            
        elif choices == "langue":
            self.choice_active = False
            self.cut = 94
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        elif choices == "femme":
            self.choice_active = False
            self.cut = 100
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

        elif self.cut == 11 and choices == "ç":
            self.choice_active = False
            self.cut = 12
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        elif self.cut == 11 and choices != "ç":
            self.choice_active = False
            self.cut = 14
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        elif self.cut == 17 and choices == "é":
            self.choice_active = False
            self.cut = 18
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        elif self.cut == 17 and choices != "é":
            self.choice_active = False
            self.cut = 20
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        elif self.cut == 23 and choices == "ù":
            self.choice_active = False
            self.cut = 24
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        elif self.cut == 23 and choices != "ù":
            self.choice_active = False
            self.cut = 26
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        elif self.cut == 29 and choices == "ù":
            self.choice_active = False
            self.cut = 30
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        elif self.cut == 29 and choices != "ù":
            self.choice_active = False
            self.cut = 32
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        elif self.cut == 35 and choices == "à":
            self.choice_active = False
            self.cut = 36
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        elif self.cut == 35 and choices != "à":
            self.choice_active = False
            self.cut = 38
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        elif self.cut == 41 and choices == "ç":
            self.choice_active = False
            self.cut = 42
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        elif self.cut == 41 and choices != "ç":
            self.choice_active = False
            self.cut = 44
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        elif self.cut == 47 and choices == "à":
            self.choice_active = False
            self.cut = 48
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        elif self.cut == 47 and choices != "à":
            self.choice_active = False
            self.cut = 50
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        elif self.cut == 53 and choices == "à":
            self.choice_active = False
            self.cut = 54
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        elif self.cut == 53 and choices != "à":
            self.choice_active = False
            self.cut = 56
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        elif self.cut == 59 and choices == "à":
            self.choice_active = False
            self.cut = 60
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        elif self.cut == 59 and choices != "à":
            self.choice_active = False
            self.cut = 62
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        elif self.cut == 65 and choices == "ù":
            self.choice_active = False
            self.cut = 66
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        elif self.cut == 65 and choices != "ù":
            self.choice_active = False
            self.cut = 68
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        elif self.cut == 71 and choices == "ç":
            self.choice_active = False
            self.cut = 72
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        elif self.cut == 71 and choices != "ç":
            self.choice_active = False
            self.cut = 74
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        elif self.cut == 77 and choices == "ç":
            self.choice_active = False
            self.cut = 78
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        elif self.cut == 77 and choices != "ç":
            self.choice_active = False
            self.cut = 80
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        elif self.cut == 83 and choices == "é":
            self.choice_active = False
            self.cut = 84
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        elif self.cut == 83 and choices != "é":
            self.choice_active = False
            self.cut = 86
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        elif self.cut == 89 and choices == "é":
            self.choice_active = False
            self.cut = 90
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        elif self.cut == 89 and choices != "é":
            self.choice_active = False
            self.cut = 92
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        elif self.cut == 95 and choices == "é":
            self.choice_active = False
            self.cut = 96
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        elif self.cut == 95 and choices != "é":
            self.choice_active = False
            self.cut = 98
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        elif self.cut == 101 and choices == "ù":
            self.choice_active = False
            self.cut = 102
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        elif self.cut == 101 and choices != "ù":
            self.choice_active = False
            self.cut = 104
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

       
            
#SCENE ZERO
    def render_scene_0(self):
        self._render_dialogue_box_Charlie_Seul("C'est un panneau vide. Il y a des feutres à côté pour dessiner dessus.")  

    def render_scene_1(self):
        self._render_dialogue_box_Answer("")
        
#SCENE UN
    def render_scene_2(self):
        self._render_dialogue_box_Answer("Que dessiner dessus ?")
        
    def render_scene_3(self):
        self._render_dialogue_box_Answer("")

#HOMME        
    def render_scene_4(self):
        self._render_dialogue_box_Answer("Et je range le mot 'homme' dans quelle colonne ?")
        
    def render_scene_5(self):
        self._render_dialogue_box_Answer("")
        
    def render_scene_6(self):
        self._render_dialogue_box_Answer("ça me parait bien ici. Est-ce que j'ai d'autres mots à dessiner ? Voyons...")
        self.game.homme_finito = True
        
    def render_scene_7(self):
        self._render_dialogue_box_Answer("")
        
    def render_scene_8(self):
        self._render_dialogue_box_Gandalf("Tu es sûr Charlie ? Si je me souviens bien, on avait entendu 'Jeune ù-homme, essuyez vos chaussures pleines de ç-boue quand vous rentrez chez les gens !'")
        
    def render_scene_9(self):
        self._render_dialogue_box_Answer("")

#BOUE
    def render_scene_10(self):
        self._render_dialogue_box_Answer("Et je range le mot 'boue' dans quelle colonne ?")
        
    def render_scene_11(self):
        self._render_dialogue_box_Answer("")
        
    def render_scene_12(self):
        self._render_dialogue_box_Answer("ça me parait bien ici. Est-ce que j'ai d'autres mots à dessiner ? Voyons...")
        self.game.boue_finito = True
        
    def render_scene_13(self):
        self._render_dialogue_box_Answer("")
        
    def render_scene_14(self):
        self._render_dialogue_box_Gandalf("Tu es sûr Charlie ? Si je me souviens bien, on avait entendu 'Jeune ù-homme, essuyez vos chaussures pleines de ç-boue quand vous rentrez chez les gens !'")
        
    def render_scene_15(self):
        self._render_dialogue_box_Answer("")

#CROCCODILE
    def render_scene_16(self):
        self._render_dialogue_box_Answer("Et je range le mot 'crocodile' dans quelle colonne ?")
        
    def render_scene_17(self):
        self._render_dialogue_box_Answer("")
        
    def render_scene_18(self):
        self._render_dialogue_box_Answer("ça me parait bien ici. Est-ce que j'ai d'autres mots à dessiner ? Voyons...")
        self.game.croccodile_finito = True
        
    def render_scene_19(self):
        self._render_dialogue_box_Answer("")
        
    def render_scene_20(self):
        self._render_dialogue_box_Gandalf("Tu es sûr Charlie ? Si je me souviens bien, on avait lu 'Expression du jour : verser des ç-larmes de é-crocodile.'")
        
    def render_scene_21(self):
        self._render_dialogue_box_Answer("")

#BEAU-FRERE
    def render_scene_22(self):
        self._render_dialogue_box_Answer("Et je range le mot 'beau-frère' dans quelle colonne ?")
        
    def render_scene_23(self):
        self._render_dialogue_box_Answer("")
        
    def render_scene_24(self):
        self._render_dialogue_box_Answer("ça me parait bien ici. Est-ce que j'ai d'autres mots à dessiner ? Voyons...")
        self.game.beau_frère_finito = True
        
    def render_scene_25(self):
        self._render_dialogue_box_Answer("")
        
    def render_scene_26(self):
        self._render_dialogue_box_Gandalf("Tu es sûr Charlie ? Si je me souviens bien, on avait entendu 'Vous pouvez apporter cette bouteille de ç-lait à mon ù-beau-frère ?'")
        
    def render_scene_27(self):
        self._render_dialogue_box_Answer("")

#BELLE-SOEUR
    def render_scene_28(self):
        self._render_dialogue_box_Answer("Et je range le mot 'belle-soeur' dans quelle colonne ?")
        
    def render_scene_29(self):
        self._render_dialogue_box_Answer("")
        
    def render_scene_30(self):
        self._render_dialogue_box_Answer("ça me parait bien ici. Est-ce que j'ai d'autres mots à dessiner ? Voyons...")
        self.game.belle_soeur_finito = True
        
    def render_scene_31(self):
        self._render_dialogue_box_Answer("")
        
    def render_scene_32(self):
        self._render_dialogue_box_Gandalf("Tu es sûr Charlie ? Si je me souviens bien, on avait entendu 'C’est ma ù-belle-soeur qui vous envoie ? Quelle ù-femme formidable ! J’avais super soif ! J’en ç-salive d’avance, merci !'.")
        
    def render_scene_33(self):
        self._render_dialogue_box_Answer("")

#TETARD
    def render_scene_34(self):
        self._render_dialogue_box_Answer("Et je range le mot 'têtard' dans quelle colonne ?")
        
    def render_scene_35(self):
        self._render_dialogue_box_Answer("")
        
    def render_scene_36(self):
        self._render_dialogue_box_Answer("ça me parait bien ici. Est-ce que j'ai d'autres mots à dessiner ? Voyons...")
        self.game.têtard_finito = True
        
    def render_scene_37(self):
        self._render_dialogue_box_Answer("")
        
    def render_scene_38(self):
        self._render_dialogue_box_Gandalf("Tu es sûr Charlie ? Si je me souviens bien, on avait entendu 'Vous allez faire fuir les à-têtards.'")
        
    def render_scene_39(self):
        self._render_dialogue_box_Answer("")

#LAIT
    def render_scene_40(self):
        self._render_dialogue_box_Answer("Et je range le mot 'lait' dans quelle colonne ?")
        
    def render_scene_41(self):
        self._render_dialogue_box_Answer("")
        
    def render_scene_42(self):
        self._render_dialogue_box_Answer("ça me parait bien ici. Est-ce que j'ai d'autres mots à dessiner ? Voyons...")
        self.game.lait_finito = True
        
    def render_scene_43(self):
        self._render_dialogue_box_Answer("")
        
    def render_scene_44(self):
        self._render_dialogue_box_Gandalf("Tu es sûr Charlie ? Si je me souviens bien, on avait entendu 'Vous pouvez apporter cette bouteille de ç-lait à mon ù-beau-frère ?'")
        
    def render_scene_45(self):
        self._render_dialogue_box_Answer("")

#PIGEON
    def render_scene_46(self):
        self._render_dialogue_box_Answer("Et je range le mot 'pigeon' dans quelle colonne ?")
        
    def render_scene_47(self):
        self._render_dialogue_box_Answer("")
        
    def render_scene_48(self):
        self._render_dialogue_box_Answer("ça me parait bien ici. Est-ce que j'ai d'autres mots à dessiner ? Voyons...")
        self.game.pigeon_finito = True
        
    def render_scene_49(self):
        self._render_dialogue_box_Answer("")
        
    def render_scene_50(self):
        self._render_dialogue_box_Gandalf("Tu es sûr Charlie ? Si je me souviens bien, on avait entendu 'Quand le è-serpent tire la è-langue, le à-pigeon s'enfuit.'")
        
    def render_scene_51(self):
        self._render_dialogue_box_Answer("")

#CHAUVE-SOURIS
    def render_scene_52(self):
        self._render_dialogue_box_Answer("Et je range le mot 'chauve-souris' dans quelle colonne ?")
        
    def render_scene_53(self):
        self._render_dialogue_box_Answer("")
        
    def render_scene_54(self):
        self._render_dialogue_box_Answer("ça me parait bien ici. Est-ce que j'ai d'autres mots à dessiner ? Voyons...")
        self.game.chauve_souris_finito = True
        
    def render_scene_55(self):
        self._render_dialogue_box_Answer("")
        
    def render_scene_56(self):
        self._render_dialogue_box_Gandalf("Tu es sûr Charlie ? Si je me souviens bien, on avait entendu 'Est-ce que c’est vrai que les à-chauve-souris c’est des à-rats qui ont volé les ailes aux à-pigeons'")
        
    def render_scene_57(self):
        self._render_dialogue_box_Answer("")

#RAT
    def render_scene_58(self):
        self._render_dialogue_box_Answer("Et je range le mot 'rat' dans quelle colonne ?")
        
    def render_scene_59(self):
        self._render_dialogue_box_Answer("")
        
    def render_scene_60(self):
        self._render_dialogue_box_Answer("ça me parait bien ici. Est-ce que j'ai d'autres mots à dessiner ? Voyons...")
        self.game.rat_finito = True
        
    def render_scene_61(self):
        self._render_dialogue_box_Answer("")
        
    def render_scene_62(self):
        self._render_dialogue_box_Gandalf("Tu es sûr Charlie ? Si je me souviens bien, on avait entendu 'Est-ce que c’est vrai que les à-chauve-souris c’est des à-rats qui ont volé les ailes aux à-pigeons'")
        
    def render_scene_63(self):
        self._render_dialogue_box_Answer("")

#MARI
    def render_scene_64(self):
        self._render_dialogue_box_Answer("Et je range le mot 'mari' dans quelle colonne ?")
        
    def render_scene_65(self):
        self._render_dialogue_box_Answer("")
        
    def render_scene_66(self):
        self._render_dialogue_box_Answer("ça me parait bien ici. Est-ce que j'ai d'autres mots à dessiner ? Voyons...")
        self.game.mari_finito = True
        
    def render_scene_67(self):
        self._render_dialogue_box_Answer("")
        
    def render_scene_68(self):
        self._render_dialogue_box_Gandalf("Tu es sûr Charlie ? Si je me souviens bien, on avait entendu 'Je suis sûre que c’est mon ù-mari qui lui raconte des bêtises...'")
        
    def render_scene_69(self):
        self._render_dialogue_box_Answer("")

#LARMES
    def render_scene_70(self):
        self._render_dialogue_box_Answer("Et je range le mot 'larmes' dans quelle colonne ?")
        
    def render_scene_71(self):
        self._render_dialogue_box_Answer("")
        
    def render_scene_72(self):
        self._render_dialogue_box_Answer("ça me parait bien ici. Est-ce que j'ai d'autres mots à dessiner ? Voyons...")
        self.game.larmes_finito = True
        
    def render_scene_73(self):
        self._render_dialogue_box_Answer("")
        
    def render_scene_74(self):
        self._render_dialogue_box_Gandalf("Tu es sûr Charlie ? Si je me souviens bien, on avait lu 'Expression du jour : verser des ç-larmes de é-crocodile.'.")
        
    def render_scene_75(self):
        self._render_dialogue_box_Answer("")

#SALIVE
    def render_scene_76(self):
        self._render_dialogue_box_Answer("Et je range le mot 'salive' dans quelle colonne ?")
        
    def render_scene_77(self):
        self._render_dialogue_box_Answer("")
        
    def render_scene_78(self):
        self._render_dialogue_box_Answer("ça me parait bien ici. Est-ce que j'ai d'autres mots à dessiner ? Voyons...")
        self.game.salive_finito = True
        
    def render_scene_79(self):
        self._render_dialogue_box_Answer("")
        
    def render_scene_80(self):
        self._render_dialogue_box_Gandalf("Tu es sûr Charlie ? Si je me souviens bien, on avait entendu 'C’est ma ù-belle-sœur qui vous envoie ? Quelle ù-femme formidable ! J’avais super soif ! J’en ç-salive d’avance, merci !'")
        
    def render_scene_81(self):
        self._render_dialogue_box_Answer("")

#CORDE
    def render_scene_82(self):
        self._render_dialogue_box_Answer("Et je range le mot 'corde' dans quelle colonne ?")
        
    def render_scene_83(self):
        self._render_dialogue_box_Answer("")
        
    def render_scene_84(self):
        self._render_dialogue_box_Answer("ça me parait bien ici. Est-ce que j'ai d'autres mots à dessiner ? Voyons...")
        self.game.corde_finito = True
        
    def render_scene_85(self):
        self._render_dialogue_box_Answer("")
        
    def render_scene_86(self):
        self._render_dialogue_box_Gandalf("Tu es sûr Charlie ? Si je me souviens bien, on avait lu 'urgent cherche é-corde pour concert.'")
        
    def render_scene_87(self):
        self._render_dialogue_box_Answer("")

#SERPENT
    def render_scene_88(self):
        self._render_dialogue_box_Answer("Et je range le mot 'serpent' dans quelle colonne ?")
        
    def render_scene_89(self):
        self._render_dialogue_box_Answer("")
        
    def render_scene_90(self):
        self._render_dialogue_box_Answer("ça me parait bien ici. Est-ce que j'ai d'autres mots à dessiner ? Voyons...")
        self.game.serpent_finito = True
        
    def render_scene_91(self):
        self._render_dialogue_box_Answer("")
        
    def render_scene_92(self):
        self._render_dialogue_box_Gandalf("Tu es sûr Charlie ? Si je me souviens bien, on avait entendu 'Quand le è-serpent tire la è-langue, le à-pigeon s'enfuit.'")
        
    def render_scene_93(self):
        self._render_dialogue_box_Answer("")

#LANGUE
    def render_scene_94(self):
        self._render_dialogue_box_Answer("Et je range le mot 'langue' dans quelle colonne ?")
        
    def render_scene_95(self):
        self._render_dialogue_box_Answer("")
        
    def render_scene_96(self):
        self._render_dialogue_box_Answer("ça me parait bien ici. Est-ce que j'ai d'autres mots à dessiner ? Voyons...")
        self.game.langue_finito = True
        
    def render_scene_97(self):
        self._render_dialogue_box_Answer("")
        
    def render_scene_98(self):
        self._render_dialogue_box_Gandalf("Tu es sûr Charlie ? Si je me souviens bien, on avait entendu 'Quand le è-serpent tire la è-langue, le à-pigeon s'enfuit.'")
        
    def render_scene_99(self):
        self._render_dialogue_box_Answer("")

#FEMME
    def render_scene_100(self):
        self._render_dialogue_box_Answer("Et je range le mot 'femme' dans quelle colonne ?")
        
    def render_scene_101(self):
        self._render_dialogue_box_Answer("")
        
    def render_scene_102(self):
        self._render_dialogue_box_Answer("ça me parait bien ici. Est-ce que j'ai d'autres mots à dessiner ? Voyons...")
        self.game.femme_finito = True
        
    def render_scene_103(self):
        self._render_dialogue_box_Answer("")
        
    def render_scene_104(self):
        self._render_dialogue_box_Gandalf("Tu es sûr Charlie ? Si je me souviens bien, on avait entendu 'C’est ma ù-belle-sœur qui vous envoie ? Quelle ù-femme formidable ! J’avais super soif ! J’en ç-salive d’avance, merci !'")
        
    def render_scene_105(self):
        self._render_dialogue_box_Answer("")

#FIN
    def render_scene_106(self):
        self._render_dialogue_box_Answer("Je pense qu'on a assez d'indices. On va pouvoir aller voir l'enfant du portier pour comprendre ensemble les règles de rassemblement dans cette langue.")
        self.game.panneau_done = True

#Note pour plus tard : quand on a décrété qu'on a assez de mots pour le panneau : self.game.panneau_done = True. Gandalf arrête de nous suivre et on amène avec nous le panneau jusqu'à la petite fille.