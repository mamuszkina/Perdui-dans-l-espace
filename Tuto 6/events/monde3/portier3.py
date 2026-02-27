import pygame

import config
from game_state import GameState
from game_state import grayscale

class portier3:
    def __init__(self, screen, game, player):
        self.screen = screen
        self.game = game   
        self.player = player

        #Combat
        self.fondcombat = pygame.image.load("imgs/battle/fondcombat.png").convert_alpha()
        self.fondcombat = pygame.transform.scale(self.fondcombat, (config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
        self.monster_pad = pygame.image.load("imgs/battle/monster_pad.png").convert_alpha()
        self.monster_pad = pygame.transform.scale(self.monster_pad, (config.SCREEN_WIDTH//4, config.SCREEN_HEIGHT//8))
        self.name_card = pygame.image.load("imgs/battle/name_card.png").convert_alpha()
        self.name_card = pygame.transform.scale(self.name_card, (config.SCREEN_WIDTH//2.5, config.SCREEN_HEIGHT//5))
        self.hp_bar = pygame.image.load("imgs/battle/hp_bar.png").convert_alpha()
        self.hp_bar = pygame.transform.scale(self.hp_bar, (config.SCREEN_WIDTH//3.5, config.SCREEN_HEIGHT//40))
        self.menu = pygame.image.load("imgs/battle/menu.png").convert_alpha()
        self.menu = pygame.transform.scale(self.menu, (config.SCREEN_WIDTH//1.1, config.SCREEN_HEIGHT//3.9))
        self.menu2 = pygame.image.load("imgs/battle/menu2.png").convert_alpha()
        self.menu2 = pygame.transform.scale(self.menu2, (config.SCREEN_WIDTH//1.4, config.SCREEN_HEIGHT//6))
        self.portier3 = pygame.image.load("imgs/battle/prof3.png").convert_alpha()
        self.portier3 = pygame.transform.scale(self.portier3, (config.SCREEN_WIDTH//8, config.SCREEN_HEIGHT//6))
        self.Charlie = pygame.image.load("imgs/battle/player.png").convert_alpha()
        self.Charlie = pygame.transform.scale(self.Charlie, (config.SCREEN_WIDTH//7, config.SCREEN_HEIGHT//6))
        
        #Dialogue adapté taille écran
        self.dialog = pygame.image.load("imgs/dialog.png").convert_alpha()
        self.dialog = pygame.transform.scale(self.dialog, (config.SCREEN_WIDTH//3.5, config.SCREEN_HEIGHT//4.5)) 
        self.dialogPNJ = pygame.transform.flip(self.dialog, True, False).convert_alpha()
        self.dialogPNJ = pygame.transform.scale(self.dialogPNJ, (config.SCREEN_WIDTH//3.5, config.SCREEN_HEIGHT//4.5))

        #Perso adaptés taille écran
        self.charlie = pygame.image.load("imgs/characters/charlie.png").convert_alpha()
        self.charlie = pygame.transform.scale(self.charlie, (config.SCREEN_WIDTH //5, config.SCREEN_HEIGHT //1.1))
        self.charlie_gray = grayscale(self.charlie)
        self.PNJ = pygame.image.load("imgs/characters/portier.png").convert_alpha()
        self.PNJ = pygame.transform.flip(self.PNJ, True, False)
        self.PNJ = pygame.transform.scale(self.PNJ, (config.SCREEN_WIDTH//5, config.SCREEN_HEIGHT//1.1))
        self.PNJ_gray = grayscale(self.PNJ)
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
        #son combat pokémon
        self.pokemon_sound = pygame.mixer.Sound("sons/pokemonfight.mp3")
        self.pokemon_played = False
        self.pokemon_sound.set_volume(0.3)   # entre 0.0 et 1.0

        self.active_phrase_text = None
        self.cut = 0
        self.max_cut = 84

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
        self.choices1 = ["Gandalf", "Un grand monsieur un peu étrange"]
        self.choices2 = ["C'est comme ça que je parle depuis toujours", "Maintenant que tu le dis..."]
        self.choices3 = ["Oh non, pitié", "Pourquoi pas"]
        self.choices4 = ["Tu peux répéter ?", "Compris"]
        self.choices5 = ["Redis, pour voir ?", "Compris !"]
        self.choices6 = ["Pas de fautes dans la phrase", "1 mot avec des fautes", "2 mots avec des fautes", "3 mots avec des fautes"]
        self.choices7 = ["Risposte", "Fuir"]
        self.choices1status = ["attente"]
        self.choices2status = ["attente"]
        self.choices3status = ["attente"]
        self.choices4status = ["attente"]
        self.choices5status = ["attente"]
        self.choices6status = ["attente"]
        self.choices7status = ["attente"]
#        self.resolved = False
        self.goodbye = False                     # True après "n'hésite pas à revenir"

        #Pour le combat
        self.health = 4
        self.base_health = 4
        self.player_health = 4
        self.player_base_health = 4

    
    def load(self):
        self.current_char = 0
        self.last_update = pygame.time.get_ticks()

        #Pour le combat
        self.health = 4
        self.base_health = 4
        self.player_health = 4
        self.player_base_health = 4


    def battle_portier3(self):
        fond = self.screen.blit(self.fondcombat, (0, 0)) 
        font = pygame.font.Font("fonts/PokemonGb.ttf", 25)
#        dialogue_rect = self.screen.blit(self.menu,(config.SCREEN_WIDTH // 6, config.SCREEN_HEIGHT // 1.5))

        #Charlie
        self.screen.blit(self.monster_pad, (config.SCREEN_WIDTH // 7, config.SCREEN_HEIGHT // 1.5))
        self.screen.blit(self.name_card, (config.SCREEN_WIDTH // 2.5, config.SCREEN_HEIGHT // 1.9))
        self.screen.blit(self.hp_bar, (config.SCREEN_WIDTH // 2.4, config.SCREEN_HEIGHT // 1.6))
        self.screen.blit(self.Charlie, (config.SCREEN_WIDTH // 5.2, config.SCREEN_HEIGHT // 1.7))
        self.screen.blit(font.render("CHARLIE", True, config.BLACK), (config.SCREEN_WIDTH // 2.4, config.SCREEN_HEIGHT // 1.8))

        #Portier3
        self.screen.blit(self.monster_pad, (config.SCREEN_WIDTH // 1.5, config.SCREEN_HEIGHT // 6))
        self.screen.blit(self.name_card, (config.SCREEN_WIDTH // 5, config.SCREEN_HEIGHT // 9))
        self.screen.blit(self.hp_bar, (config.SCREEN_WIDTH // 4.5, config.SCREEN_HEIGHT // 4.5))
        self.screen.blit(self.portier3, (config.SCREEN_WIDTH//1.4, config.SCREEN_HEIGHT//12))
        self.screen.blit(font.render("GARDIEN DE LA PORTE", True, config.BLACK), (config.SCREEN_WIDTH // 4.5, config.SCREEN_HEIGHT // 7))

        monster_percent = self.health / self.base_health
        monster_color = self.determine_health_color(monster_percent)
        pygame.draw.rect(self.screen, monster_color, pygame.Rect(config.SCREEN_WIDTH // 3.72, config.SCREEN_HEIGHT // 4.43, config.SCREEN_WIDTH//4.3 * monster_percent, config.SCREEN_HEIGHT // 48))

        player_monster_percent = self.player_health / self.player_base_health
        player_monster_color = self.determine_health_color(player_monster_percent)
        pygame.draw.rect(self.screen, player_monster_color, pygame.Rect(config.SCREEN_WIDTH // 2.16, config.SCREEN_HEIGHT // 1.595, config.SCREEN_WIDTH//4.3 * player_monster_percent, config.SCREEN_HEIGHT // 48))
  
    def determine_health_color(self, monster_percent):
        if monster_percent < .25:
            return config.RED
        if monster_percent < .7:
            return config.YELLOW
        return config.GREEN

        
    def update(self):
        if self.cut == 16: 
            self.game.event = None
        elif self.cut == 18: 
            self.game.event = None
        elif self.cut == 29: 
            self.game.event = None
        elif self.cut == 31: 
            self.game.event = None
        elif self.cut == 38: 
            self.game.event = None
        elif self.cut == 40: 
            self.game.event = None
        elif self.cut == 81: 
            self.game.event = None
        elif self.cut == 83: 
            self.game.event = None
        elif self.cut == 51:
            self.cut = 53
        elif self.cut == 56:
            self.cut = 58
        elif self.cut == 61:
            self.cut = 63
        elif self.cut == 66:
            self.cut = 68
        elif self.cut == 71:
            self.cut = 73
        elif self.cut == 76:
            self.cut = 78
        elif self.cut > self.max_cut:
            self.game.event = None
            return

        if self.health == 0 and self.cut < 80:
            self.cut = 80
        elif self.player_health == 0 and self.cut < 82:
            self.cut = 82                                 

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
            self.cut == 3
            and self.choices1status == ["attente"]
            and not self.goodbye
            and not self.choice_active
        ):
            self.choices = self.choices1
            self.choice_active = True
            self.choice_index = 0
 #           self.handle_choice1
        elif (
            self.cut == 10
            and self.choices2status == ["attente"]
            and not self.goodbye
            and not self.choice_active
        ):
            self.choices = self.choices2
            self.choice_active = True
            self.choice_index = 0
        elif (
            self.cut == 11
            and self.choices3status == ["attente"]
            and not self.goodbye
            and not self.choice_active
        ):
            self.choices = self.choices3
            self.choice_active = True
            self.choice_index = 0
        elif (
            self.cut == 15
            and self.choices4status == ["attente"]
            and not self.goodbye
            and not self.choice_active
        ):
            self.choices = self.choices4
            self.choice_active = True
            self.choice_index = 0
        elif (
            self.cut == 37
            and self.choices5status == ["attente"]
            and not self.goodbye
            and not self.choice_active
        ):
            self.choices = self.choices5
            self.choice_active = True
            self.choice_index = 0
        elif (
            self.cut == 49                                    
            and self.choices7status == ["attente"]
            and not self.goodbye
            and not self.choice_active
        ):
            self.active_phrase_text = "Ce soir, le rôle d'Ali sera joué par eune grante ténébreusse, sinistri et moche !"
            self.choices = self.choices7
            self.choice_active = True
            self.choice_index = 0
        elif (
            self.cut == 54                                    
            and self.choices7status == ["attente"]
            and not self.goodbye
            and not self.choice_active
        ):
            self.active_phrase_text = "Siouplé, c'est pas exactement lu progénituro que j'ai commandéë ! J'ai dis eune grante gaillardi aux biceps en béton armé. Et là ce que j'ai, c'est rien qu'une crevette qui parle!"
            self.choices = self.choices7
            self.choice_active = True
            self.choice_index = 0
        elif (
            self.cut == 59                                    
            and self.choices7status == ["attente"]
            and not self.goodbye
            and not self.choice_active
        ):
            self.active_phrase_text = "C’est la cata ! Comment tu dois être mal. Tu viens de perdre la totale ! Tan père, touttos ceulles de tan village, tan meilleurë amix..."
            self.choices = self.choices7
            self.choice_active = True
            self.choice_index = 0

        elif (
            self.cut == 64                                    
            and self.choices7status == ["attente"]
            and not self.goodbye
            and not self.choice_active
        ):
            self.active_phrase_text = "Comme eune humaime, sois plus violende que lea cours du torrent"
            self.choices = self.choices7
            self.choice_active = True
            self.choice_index = 0
        elif (
            self.cut == 69                                    
            and self.choices7status == ["attente"]
            and not self.goodbye
            and not self.choice_active
        ):
            self.active_phrase_text = "C'est Izma lea conseillèle de l'Empereuri. Iel est la preuve que li dinosaures ont vécu sur Terre"
            self.choices = self.choices7
            self.choice_active = True
            self.choice_index = 0

        elif (
            self.cut == 74                                    
            and self.choices7status == ["attente"]
            and not self.goodbye
            and not self.choice_active
        ):
            self.active_phrase_text = "Bon, d'accord. On en appellera eune Nemo, mais les autres, j'aimerais qu'on les appelle Marin Junior"
            self.choices = self.choices7
            self.choice_active = True
            self.choice_index = 0
        elif (
            self.cut == 79                                    
            and self.choices7status == ["attente"]
            and not self.goodbye
            and not self.choice_active
        ):
            self.active_phrase_text = "Tiens, tiens, tiens, des visiteurzes... Transgresseurx ! Espiomes ! Pas des espiomes !"
            self.choices = self.choices7
            self.choice_active = True
            self.choice_index = 0
    
    def render(self):
        # Si on a choisi "non" -> message d'au revoir
        if self.goodbye:
            self.render_goodbye()
            return

        # --- Affichage du menu de choix PAR-DESSUS le dialogue ---
        if self.choice_active:
            self.render_choice()
            return

        if self.game.portier3_1_dialogue_done == True and self.game.PNJ11_dialogue_done == False and self.cut < 17:
            self.cut = 17
            return

        if self.game.PNJ11_dialogue_done == True and self.game.portier3_2_dialogue_done == False and self.cut < 19:
            self.cut = 19
            return

        if self.game.portier3_2_dialogue_done == True and self.game.PNJ12_dialogue_done == False and self.cut < 30:
            self.cut = 30
            return

        if self.game.PNJ12_dialogue_done == True and self.game.portier3_3_dialogue_done == False and self.cut < 32:
            self.cut = 32
            return

        if self.game.portier3_3_dialogue_done == True and self.game.PNJ13_dialogue_done == False and self.cut < 39:
            self.cut = 39
            return

        if self.game.PNJ13_dialogue_done == True and self.game.portier3_4_dialogue_done == False and self.cut < 41:
            self.cut = 41
            return
        
        if self.game.portier3_4_dialogue_done == True and self.cut == 0 :
            self.cut = 84
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

    
    def _render_dialogue_box_Battle(self, text):
        dialogue_rect = self.screen.blit(self.menu, (config.SCREEN_WIDTH // 20, config.SCREEN_HEIGHT // 1.35))      # chiffres = position bulle de dialogue

        font = pygame.font.Font("fonts/PokemonGb.ttf", 30)           #20 = taille des lettres
        color = config.WHITE

        max_width = dialogue_rect.width - 100
        max_height = dialogue_rect.height - 60

        font, wrapped = self.get_fitting_font(
            text=text,
            font_path="fonts/PokemonGb.ttf",
            max_width=max_width,
            max_height=max_height,
            start_size=30,
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
            self.screen.blit(surf, (dialogue_rect.x + 85, y))         # chiffre, y = décalage début de bulle
            chars_left -= len(line) + 1
            y += font.get_height() + 6 

    
    def _render_dialogue_box_Battle_Phrase(self, text):
         # Boîte centrée (superposée au combat + au menu de choix)
        rect = self.menu.get_rect(center=(config.SCREEN_WIDTH//1.7, config.SCREEN_HEIGHT//2.2))
        dialogue_rect = self.screen.blit(self.menu2, rect.topleft)

        color = config.WHITE

        max_width = dialogue_rect.width - dialogue_rect.width // 4
        max_height = dialogue_rect.height - dialogue_rect.height // 2

        font, wrapped = self.get_fitting_font(
            text=text,
            font_path="fonts/PokemonGb.ttf",
            max_width=max_width,
            max_height= max_height,
            start_size=30,
            min_size=12
        )

        y = dialogue_rect.y + 30

        for line in wrapped:
            surf = font.render(line, True, color)
            x_offset = config.SCREEN_WIDTH // 13
            self.screen.blit(surf, (dialogue_rect.x + x_offset, y))
            y += font.get_height() + 6

            
    # --- NOUVEAU : rendu du menu de choix ---
    def render_choice(self):
        if (44 <= self.cut <= 79):
            self.battle_portier3()
            
            if self.active_phrase_text:
                self._render_dialogue_box_Battle_Phrase(self.active_phrase_text)

            dialogue_rect = self.screen.blit(self.menu, (config.SCREEN_WIDTH // 20, config.SCREEN_HEIGHT // 1.35))
            color = config.WHITE
        else :
            dialogue_rect = self.screen.blit(self.dialog, (config.SCREEN_WIDTH // 2.8, config.SCREEN_HEIGHT // 1.4))      # chiffres = position bulle de dialogue
            self.screen.blit(self.charlie_penaud, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
            self.screen.blit(self.PNJ_gray, (config.SCREEN_WIDTH // 6, config.SCREEN_HEIGHT * 0.5))
            color = config.BLACK
            
        font = pygame.font.Font("fonts/PokemonGb.ttf", 20)
        
        
        # --- Question ---
        question = ""
        surf_q = font.render(question, True, color)
        self.screen.blit(surf_q, (dialogue_rect.x + 30, dialogue_rect.y + 20))

        # Positions de base
        y = dialogue_rect.y + 60 
        x_text = dialogue_rect.x + 70 
        x_arrow = dialogue_rect.x + 60

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
        self._render_dialogue_box("Tu ne veux pas essayer ? Tant pis. Reviens tenter quand tu veux !")
        self.screen.blit(self.charlie_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    # --- NOUVEAU : logique des réponses ---
    def handle_choice(self):
        choices = self.choices[self.choice_index]

        # On quitte l'affichage \"phrase au centre\" dès que le joueur valide un choix
        self.active_phrase_text = None

        if choices == "Gandalf":
            self.choice_active = False
            self.choices1status = ["fini"]
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        elif choices == "Un grand monsieur un peu étrange":
            self.choice_active = False
            self.choices1status = ["fini"]
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        elif choices == "C'est comme ça que je parle depuis toujours":
            self.choice_active = False
            self.choices2status = ["fini"]
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        elif choices == "Maintenant que tu le dis...":
            self.choice_active = False
            self.choices2status = ["fini"]
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()
            
        elif choices == "Oh non, pitié":
            self.choice_active = False
            self.choices3status = ["fini"]
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()
            
        elif choices == "Pourquoi pas":
            self.choice_active = False
            self.cut = 13
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()
            
        elif choices == "Tu peux répéter ?":
            self.choice_active = False
            self.cut = 14
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()
            
        elif choices == "Compris":
            self.choice_active = False
            self.choices4status = ["fini"]
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        elif choices == "Compris !":
            self.choice_active = False
            self.choices5status = ["fini"]
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        elif choices == "Redis, pour voir ?":
            self.choice_active = False
            self.cut = 36
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()
        
        elif self.cut == 49 and choices == "1 mot avec des fautes" :  
            self.health -= 1
            self.choice_active = False 
            self.cut = 52
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()
            
        elif self.cut == 49 and (choices == "Pas de fautes dans la phrase" or choices == "2 mots avec des fautes" or choices == "3 mots avec des fautes"):
            self.player_health -= 1
            self.choice_active = False 
            self.cut = 50
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()
            
        elif self.cut == 54 and choices == "3 mots avec des fautes":     
            self.health -= 1
            self.choice_active = False 
            self.cut = 57
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()
            
        elif self.cut == 54 and (choices == "Pas de fautes dans la phrase" or choices == "1 mot avec des fautes" or choices == "2 mots avec des fautes"):    
            self.player_health -= 1
            self.choice_active = False 
            self.cut = 55
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()
            
        elif self.cut == 59 and choices == "3 mots avec des fautes":     
            self.health -= 1
            self.choice_active = False 
            self.cut = 62
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()
            
        elif self.cut == 59 and (choices == "Pas de fautes dans la phrase" or choices == "1 mot avec des fautes" or choices == "2 mots avec des fautes"):     
            self.player_health -= 1
            self.choice_active = False 
            self.cut = 60
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()
                
        elif self.cut == 64 and choices == "1 mot avec des fautes":    
            self.health -= 1
            self.choice_active = False 
            self.cut = 67
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()
                
        elif self.cut == 64 and (choices == "Pas de fautes dans la phrase" or choices == "2 mots avec des fautes" or choices == "3 mots avec des fautes"):     #and self.cut != question 6
            self.player_health -= 1
            self.choice_active = False 
            self.cut = 65
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()
            
        elif self.cut == 69 and choices == "2 mots avec des fautes":     #and self.cut != question 6
            self.health -= 1
            self.choice_active = False 
            self.cut = 72
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()
            
        elif self.cut == 69 and (choices == "Pas de fautes dans la phrase" or choices == "1 mot avec des fautes" or choices == "3 mots avec des fautes"):     #and self.cut != question 6
            self.player_health -= 1
            self.choice_active = False 
            self.cut = 70
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()

        elif self.cut == 74 and choices == "Pas de fautes dans la phrase":
            self.health -= 1
            self.choice_active = False 
            self.cut = 77
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()
            
        elif self.cut == 74 and (choices == "1 mot avec des fautes" or choices == "2 mots avec des fautes" or choices == "3 mots avec des fautes"):     
            self.player_health -= 1
            self.choice_active = False 
            self.cut = 75
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()
            
        elif self.cut == 79 and choices == "1 mot avec des fautes" :     
            self.health -= 1
            self.choice_active = False 
            self.cut = 82
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()
            
        elif self.cut == 79 and (choices == "Pas de fautes dans la phrase" or choices == "2 mots avec des fautes" or choices == "3 mots avec des fautes"):    
            self.player_health -= 1
            self.choice_active = False 
            self.cut = 80
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()
            
        elif choices == "Risposte":
            if self.cut == 49 :
                self.choice_active = False
                self.choices = self.choices6
                self.active_phrase_text = ("Ce soir, le rôle d'Ali sera joué par eune grante ténébreusse, sinistri et moche !")
                self.choice_active = True
                self.choice_index = 0
                self.current_char = 0
                self.last_update = pygame.time.get_ticks()
            elif self.cut == 54 :
                self.choice_active = False
                self.choices = self.choices6
                self.active_phrase_text = ("Siouplé, c'est pas exactement lu progénituro que j'ai commandéë ! J'ai dis eune grante gaillardi aux biceps en béton armé. Et là ce que j'ai, c'est rien qu'une crevette qui parle!")
                self.choice_active = True
                self.choice_index = 0
                self.current_char = 0
                self.last_update = pygame.time.get_ticks()
            elif self.cut == 59 :
                self.choice_active = False
                self.choices = self.choices6
                self.active_phrase_text = ("C’est la cata ! Comment tu dois être mal. Tu viens de perdre la totale ! Tan père, touttos ceulles de tan village, tan meilleurë amix...")
                self.choice_active = True
                self.choice_index = 0
                self.current_char = 0
                self.last_update = pygame.time.get_ticks()
            elif self.cut == 64 :
                self.choice_active = False
                self.choices = self.choices6
                self.active_phrase_text = ("Comme eune humaime, sois plus violende que lea cours du torrent")
                self.choice_active = True
                self.choice_index = 0
                self.current_char = 0
                self.last_update = pygame.time.get_ticks()
            elif self.cut == 69 :
                self.choice_active = False
                self.choices = self.choices6
                self.active_phrase_text = ("C'est Izma lea conseillèle de l'Empereuri. Iel est la preuve que li dinosaures ont vécu sur Terre")
                self.choice_active = True
                self.choice_index = 0
                self.current_char = 0
                self.last_update = pygame.time.get_ticks()
            elif self.cut == 74 :
                self.choice_active = False
                self.choices = self.choices6
                self.active_phrase_text = ("Bon, d'accord. On en appellera eune Nemo, mais les autres, j'aimerais qu'on les appelle Marin Junior")
                self.choice_active = True
                self.choice_index = 0
                self.current_char = 0
                self.last_update = pygame.time.get_ticks()
            elif self.cut == 79 :
                self.choice_active = False
                self.choices = self.choices6
                self.active_phrase_text = ("Tiens, tiens, tiens, des visiteurzes... Transgresseurx ! Espiomes ! Pas des espiomes !")
                self.choice_active = True
                self.choice_index = 0
                self.current_char = 0
                self.last_update = pygame.time.get_ticks()
                
        elif choices == "Fuir":
            self.choice_active = False
            self.goodbye = True
            self.current_char = 0
            self.last_update = pygame.time.get_ticks()
                

#SCENE ZERO
    def render_scene_0(self):
        self._render_dialogue_box("Salut ! Tu as besoin de quelque chose, étrangèle ?")
        self.screen.blit(self.charlie_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_1(self):
        self._render_dialogue_box_Answer("Euh, oui, j’aimerais passer la porte pour voir un ami.")
        self.screen.blit(self.charlie, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_2(self):
        self._render_dialogue_box("Et c’est qui tan pote ? ")
        self.screen.blit(self.charlie_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        
    def render_scene_3(self):
        self._render_dialogue_box("Ah oui, lea prof remplacande ?")
        self.screen.blit(self.charlie_penaud_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        
    def render_scene_4(self):
        self._render_dialogue_box_Answer("ça doit être lui, oui... Je peux le voir ? ")
        self.screen.blit(self.charlie, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        
    def render_scene_5(self):
        self._render_dialogue_box("C’est marrant ton accent, ça vient d’où ? ")
        self.screen.blit(self.charlie_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        
    def render_scene_6(self):
        self._render_dialogue_box_Answer("De quoi ?")
        self.screen.blit(self.charlie_surpris, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        
    def render_scene_7(self):
        self._render_dialogue_box("Oui, ton accent. Tu parles toujours comme ça, 'un ami', 'lui', 'le voir'. ça fait très provincial, de la campagne profonde !")
        self.screen.blit(self.charlie_surpris_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        
    def render_scene_8(self):
        self._render_dialogue_box_Answer("Ah, oui, c’est que je viens de... de loin. Chez moi on marque le genre des gens. On dit le ou la en fonction de si on parle à un homme ou une femme, et on accorde le tout. ")
        self.screen.blit(self.charlie_penaud, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        
    def render_scene_9(self):
        self._render_dialogue_box("Ouah, quoi ?! Tout le temps ?! Donc en fait la première chose que tu sais d’une personne c’est si c’est un homme ou une femme ? Mais c’est pas un peu... En fait tu es rapportéë TOUT LE TEMPS à ton genre ?")
        self.screen.blit(self.charlie_penaud_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        
    def render_scene_10(self):
        self._render_dialogue_box("C’est super complexe ! Attend je peux pas te laisser partir comme ça, je vais te montrer un peu ma langue à moi. ")
        self.screen.blit(self.charlie_penaud_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        
    def render_scene_11(self):
        self._render_dialogue_box("Dealons. On fait un petit tour du village, tu parles à quelques habitandes et ensuite je te laisse entrer.")
        self.screen.blit(self.charlie_penaud_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        
    def render_scene_12(self):
        self._render_dialogue_box_Answer("Bon, je suis plus à 10 minutes près.. Puis c'est pas comme si j'avais VRAIMENT le choix. Je marche. ")
        self.screen.blit(self.charlie_penaud, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        
    def render_scene_13(self):
        self._render_dialogue_box("Super !")
        self.screen.blit(self.charlie_penaud_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        
    def render_scene_14(self):
        self._render_dialogue_box("Parle aux gens en fusionnant les mots genrés. Pour actif/active, prends le « if » de actIF et le « ive » de actIVE. Puis colles-les. 'if' plus 'ive' ça fait 'ifive'. Donc ça donne « actIFIVE ». Compris ?")
        self.screen.blit(self.charlie_penaud_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        
    def render_scene_15(self):
        self._render_dialogue_box("Allez, je te laisse parler, reviens me raconter comment ça s'est passé !")
        self.screen.blit(self.charlie_penaud_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        self.game.unlock_pokedex_entry(3, "portier3.0")
        self.game.unlock_pokedex_entry(3, "portier3.1")
        self.game.unlock_pokedex_entry(3, "portier3.2")
        self.game.unlock_pokedex_entry(3, "portier3.exemple1")
        
    def render_scene_16(self):
        self._render_dialogue_box("")
        self.game.portier3_1_dialogue_done = True
                
#SCENE UN      
    def render_scene_17(self):
        self._render_dialogue_box("Tu as parlé à quelqu'eune ?")
        self.screen.blit(self.charlie_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_18(self):
        self._render_dialogue_box("")
        
#SCENE DEUX       
    def render_scene_19(self):
        self._render_dialogue_box("ça y es ? Tu as bien discuté ? Tu as un peu compris la règle ? C’est vraiment pas compliqué, tu fusionnes le masculin et le féminin !")
        self.screen.blit(self.charlie_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        
    def render_scene_20(self):
        self._render_dialogue_box("Allons parler à quelqu’eune d'autre. Allez, cette fois, tu vas te faire passer pour eune localë.")
        self.screen.blit(self.charlie_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        
    def render_scene_21(self):
        self._render_dialogue_box("Voyons une autre règle, le changement de voyelle. Tu vas voir c’est facile et logique. Par exemple, est-ce que tu as un synonyme de enfant ?")
        self.screen.blit(self.charlie_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        
    def render_scene_22(self):
        self._render_dialogue_box_Answer("Euh, mioche, gamin ?")
        self.screen.blit(self.charlie, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        
    def render_scene_23(self):
        self._render_dialogue_box("Gamin c’est très bien. Au féminin, gamin tu le dirais comment ?")
        self.screen.blit(self.charlie_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        
    def render_scene_24(self):
        self._render_dialogue_box_Answer("Ben, gamine.")
        self.screen.blit(self.charlie, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        
    def render_scene_25(self):
        self._render_dialogue_box("Gamin au masculin, gamine au féminin. Nous, ici, on dit gamaine.")
        self.screen.blit(self.charlie_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        
    def render_scene_26(self):
        self._render_dialogue_box_Answer("Gamaine ?")
        self.screen.blit(self.charlie_surpris, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        
    def render_scene_27(self):
        self._render_dialogue_box("Gamaine. Eune gamaine. C’est facile à prononcer. Tu transforme la voyelle. Allez, lance-toi.")
        self.screen.blit(self.charlie_surpris_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        self.game.unlock_pokedex_entry(3, "portier3.exemple2")
        
    def render_scene_28(self):
        self._render_dialogue_box_Answer("Ok, ok...")
        self.screen.blit(self.charlie_penaud, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        
    def render_scene_29(self):
        self._render_dialogue_box("")
        self.game.portier3_2_dialogue_done = True
        
#SCENE TROIS
    def render_scene_30(self):
        self._render_dialogue_box("Allez, vas-y, lance-toi !")
        self.screen.blit(self.charlie_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        
    def render_scene_31(self):
        self._render_dialogue_box("")
        
        
#SCENE QUATRE
    def render_scene_32(self):
        self._render_dialogue_box("Hé, tu te débrouilles pas mal du tout ! Allez, une dernière règle pour la route.")
        self.screen.blit(self.charlie_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        
    def render_scene_33(self):
        self._render_dialogue_box("Tu as un mot genré qui finit par une consonne ?")
        self.screen.blit(self.charlie_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        
    def render_scene_34(self):
        self._render_dialogue_box_Answer("Euh, cadet, comme dans fils cadet ?")
        self.screen.blit(self.charlie, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        
    def render_scene_35(self):
        self._render_dialogue_box("Très bien, très bien. Au féminin, c’est cadette c’est ça ? En fait c’est la même règle, tu remplaces la dernière consonne par une autre qui lui ressemble.")
        self.screen.blit(self.charlie_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_36(self):
        self._render_dialogue_box("Cadet, cadette, tu dois remplacer le T. Tu sais quel est la consonne la plus proche du T ? Le D. Donc ça va donner cadède. Compris ?")
        self.screen.blit(self.charlie_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_37(self):
        self._render_dialogue_box("Allez, vas essayer et reviens me raconter !")
        self.screen.blit(self.charlie_penaud_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        self.game.unlock_pokedex_entry(3, "portier3.exemple3")

    def render_scene_38(self):
        self._render_dialogue_box("")
        self.game.portier3_3_dialogue_done = True

#SCENE CINQ
    def render_scene_39(self):
        self._render_dialogue_box("Allez, vas parler, sois pas timide !")
        self.screen.blit(self.charlie_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        
    def render_scene_40(self):
        self._render_dialogue_box("")

#SCENE SIX
    def render_scene_41(self):
        self._render_dialogue_box("C’est bien, c’est très bien ! Tu te débrouilles vraiment bien ! Tu peux vraiment faire croire que tu es des nôtres maintenant ! Bon, normalement il y a une dernière règle, mais elle ne s’applique qu’à l’écrit.")
        self.screen.blit(self.charlie_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_42(self):
        self._render_dialogue_box("Il suffit de mettre un ë à la fin des mots qui ne sont genrés qu’à l’écrit : docteurë, inconnuë, exploitéë,... Enfin t’as compris ! Bon allez. Trève de bavardages. Es-tu prêtë pour ta dernière leçon ?")
        self.screen.blit(self.charlie_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        self.game.unlock_pokedex_entry(3, "portier3.exemple4")
        
    def render_scene_43(self):
        self._render_dialogue_box("Alors dans ce cas... Je te provoque en duel !")
        self.screen.blit(self.charlie_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))

    def render_scene_44(self):
        self.battle_portier3()
        self._render_dialogue_box_Battle("Portier 3 veut se battre avec vous !")
        if not self.pokemon_played:
            self.game.mondes123.set_volume(0)          # Pause la musique de fond
            self.pokemon_sound.play(-1)         # Joue le tonnerre
            self.pokemon_played = True

    def render_scene_45(self):
        self.battle_portier3()
        self._render_dialogue_box_Battle("Portier : Je t'explique les règles. Je vais prononcer une phrase, et tu devras dire combien il y a de mots qui ont une faute.")

    def render_scene_46(self):
        self.battle_portier3()
        self._render_dialogue_box_Battle("Portier : Si tu trouve la bonne réponse, je perd de la vie. Sinon, c'est toi. Le premier à arriver à 0 a perdu. Bonne chance !")

    def render_scene_47(self):
        self.battle_portier3()
        self._render_dialogue_box_Battle("Portier : Première phrase :")

    def render_scene_48(self):
        self.battle_portier3()
        self._render_dialogue_box_Battle("Ce soir, le rôle d'Ali sera joué par eune grante ténébreusse, sinistrë et moche !")

    def render_scene_49(self):
        self._render_dialogue_box_Battle_Phrase("Ce soir, le rôle d'Ali sera joué par eune grante ténébreusse, sinistrë et moche !")
        self.battle_portier3()

    def render_scene_50(self):
        self.battle_portier3()
        self._render_dialogue_box_Battle("Perdu ! Dommage ! Seconde phrase :")

    def render_scene_51(self):
        self._render_dialogue_box_Battle("")

    def render_scene_52(self):
        self.battle_portier3()
        self._render_dialogue_box_Battle("Gagné ! Seconde question :")

    def render_scene_53(self):
        self.battle_portier3()
        self._render_dialogue_box_Battle("Siouplé, c'est pas exactement lea progéniturë que j'ai commandéë ! J'ai dis eune grante gaillardi aux biceps en béton armé. Et là ce que j'ai, c'est rien qu'une crevette qui parle!")

    def render_scene_54(self):
        self._render_dialogue_box_Battle_Phrase("Siouplé, c'est pas exactement lea progéniturë que j'ai commandéë ! J'ai dis eune grante gaillardi aux biceps en béton armé. Et là ce que j'ai, c'est rien qu'une crevette qui parle!")
        self.battle_portier3()

    def render_scene_55(self):
        self.battle_portier3()
        self._render_dialogue_box_Battle("Perdu ! Dommage ! Troisième phrase :")

    def render_scene_56(self):
        self.battle_portier3()
        self._render_dialogue_box_Battle("")

    def render_scene_57(self):
        self.battle_portier3()
        self._render_dialogue_box_Battle("Gagné ! Moins un pour moi ! Question suivante :")

    def render_scene_58(self):
        self.battle_portier3()
        self._render_dialogue_box_Battle("C’est la cata ! Comment tu dois être mal. Tu viens de perdre la totale ! Tan père, toustes celleux de tan village, tan meilleurë amix...")

    def render_scene_59(self):
        self.battle_portier3()
        self._render_dialogue_box_Battle("C’est la cata ! Comment tu dois être mal. Tu viens de perdre la totale ! Tan père, toustes ceulles de tan village, tan meilleurë amix...")

    def render_scene_60(self):
        self.battle_portier3()
        self._render_dialogue_box_Battle("Perdu ! Phrase suivante :")

    def render_scene_61(self):
        self.battle_portier3()
        self._render_dialogue_box_Battle("")

    def render_scene_62(self):
        self.battle_portier3()
        self._render_dialogue_box_Battle("Bravo ! Phrase suivante :")

    def render_scene_63(self):
        self.battle_portier3()
        self._render_dialogue_box_Battle("Comme eune humaime, sois plus violende que lea cours du torrent")

    def render_scene_64(self):
        self.battle_portier3()
        self._render_dialogue_box_Battle("Comme eune humaime, sois plus violende que lea cours du torrent")

    def render_scene_65(self):
        self.battle_portier3()
        self._render_dialogue_box_Battle("Perdu ! Phrase suivante :")

    def render_scene_66(self):
        self.battle_portier3()
        self._render_dialogue_box_Battle("")

    def render_scene_67(self):
        self.battle_portier3()
        self._render_dialogue_box_Battle("Gagné ! suivant :")

    def render_scene_68(self):
        self.battle_portier3()
        self._render_dialogue_box_Battle("C'est Izma lea conseillèle de l'Empereurë. Iel est la preuve que li dinosauri ont vécu sur Terre.")

    def render_scene_69(self):
        self.battle_portier3()
        self._render_dialogue_box_Battle("C'est Izma lea conseillèle de l'Empereurë. Iel est la preuve que li dinosauri ont vécu sur Terre.")

    def render_scene_70(self):
        self.battle_portier3()
        self._render_dialogue_box_Battle("Perdu : Phrase suivante :")

    def render_scene_71(self):
        self.battle_portier3()
        self._render_dialogue_box_Battle("")

    def render_scene_72(self):
        self.battle_portier3()
        self._render_dialogue_box_Battle("Gagné ! Encore une :")

    def render_scene_73(self):
        self.battle_portier3()
        self._render_dialogue_box_Battle("Bon, d'accord. On en appellera eune Nemo, mais les autres, j'aimerais qu'on les appelle Marin Junior.")

    def render_scene_74(self):
        self.battle_portier3()
        self._render_dialogue_box_Battle("Bon, d'accord. On en appellera eune Nemo, mais les autres, j'aimerais qu'on les appelle Marin Junior.")

    def render_scene_75(self):
        self.battle_portier3()
        self._render_dialogue_box_Battle("Perdu ! Dernière question :")

    def render_scene_76(self):
        self.battle_portier3()
        self._render_dialogue_box_Battle("")

    def render_scene_77(self):
        self.battle_portier3()
        self._render_dialogue_box_Battle("Gagné ! Dernière question...")

    def render_scene_78(self):
        self.battle_portier3()
        self._render_dialogue_box_Battle("Tiens, tiens, tiens, des visiteurzes... Transgresseurx ! Espiomes ! Pas des espiomes !")

    def render_scene_79(self):
        self.battle_portier3()
        self._render_dialogue_box_Battle("Tiens, tiens, tiens, des visiteurzes... Transgresseurx ! Espiomes ! Pas des espiomes !")
    
    def render_scene_80(self):
        if self.pokemon_played:
            self.pokemon_sound.stop()
            self.game.mondes123.set_volume(0.8)
            self.pokemon_played = False
        self._render_dialogue_box("Ouah tu es vraiment devenu eune pro ! Bravo à toi, tu peux aller voir Gandalf, encore bravo hein !")
        self.screen.blit(self.charlie_content_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        self.game.portier3_4_dialogue_done = True
        
    def render_scene_81(self):
        self._render_dialogue_box("")
           
    def render_scene_82(self):
        self._render_dialogue_box("Tu as perdu... Mais tu peux recommencer ! Reviens me voir quand tu seras prêt !")
        self.screen.blit(self.charlie_mécontent_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        if self.pokemon_played:
            self.pokemon_sound.stop()
            self.game.mondes123.set_volume(0.8)
            self.pokemon_played = False
        
    def render_scene_83(self):
        self._render_dialogue_box("")
        
    def render_scene_84(self):
        self._render_dialogue_box("Encore bravo à toi, c'était pas facile !")
        self.screen.blit(self.charlie_gray, (config.SCREEN_WIDTH // 1.6, config.SCREEN_HEIGHT * 0.5))
        