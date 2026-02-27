import random
import os

import pygame
import config
import math
import utilities
from events import game_event_handler

from player import Player
from game_state import GameState, CurrentGameState
from game_view.map import Map
from game_view.Pokédex_design import PokedexUI

pygame.mixer.init()

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.game_state = GameState.NONE
        self.current_game_state = CurrentGameState.MAP
        self.player_has_moved = False
        self.map = Map(screen)
        self.maps = [self.map]
        self.player = None
        self.event = None
        # --- Compagnons / followers ---
        # Gandalf5 suit le joueur après le dialogue, uniquement sur monde5 et monde5_N (hors rooms)
        self.gandalf5_following = False
        self.gandalf5_follower = None  # instance de npc.Npc marquée is_gandalf5_follower
        # --- Quit confirmation overlay ---
        self.confirm_quit = False
        self.quit_choices = ['Oui', 'Non']
        self.quit_choice_index = 0
        self._prev_esc_pressed = False

        #musiques
        self.intro = pygame.mixer.Sound("sons/a_druidesa.mp3")
        self.intro_played = False
        self.intro.set_volume(0.8)   # entre 0.0 et 1.0
        self.mondes123 = pygame.mixer.Sound("sons/monde123.mp3")
        self.mondes123_played = False
        self.mondes123.set_volume(0.8)   # entre 0.0 et 1.0
        self.mondes456 = pygame.mixer.Sound("sons/monde456.mp3")
        self.mondes456_played = False
        self.mondes456.set_volume(0.4)   # entre 0.0 et 1.0


                # --- Pokedex (citations PNJ) ---
        self.pokedex_open = False
        self._prev_p_pressed = False
        self.pokedex_unlocks = set()  # set of tuples (world_id, entry_id)
        self.pokedex_ui = PokedexUI(screen, self)

        # Drapeau : est-ce que le dialogue de portier a déjà été joué au moins une fois ?
        #MONDE INTRO 
        self.PNJ3_dialogue_done = False
        self.tp_monde1 = False
        #MONDE UN
        self.portier_dialogue_done = False
        self.panneau2_Indice_dialogue_done = False
        self.code_portier = False
        self.tp_monde2 = False
        #MONDE DEUX
        self.PNJ7_dialogue_done = False
        self.PNJ7_2_dialogue_done = False
        self.PNJ8_dialogue_done = False
        self.PNJ9_dialogue_done = False
        self.PNJ10_dialogue_done = False
        self.Maison_papier_dialogue_done = False
        self.Fantome_du_lac_dialogue_done = False
        self.Clef = True
        self.tp_monde3 = False
        #MONDE TROIS
        self.portier3_1_dialogue_done = False
        self.portier3_2_dialogue_done = False
        self.portier3_3_dialogue_done = False
        self.portier3_4_dialogue_done = False
        self.PNJ11_dialogue_done = False
        self.PNJ12_dialogue_done = False
        self.PNJ13_dialogue_done = False
        self.Gandalf3_QuiEtesVous_dialogue_done = False
        self.Gandalf3_KABOOM_dialogue_done = False
        self.Gandalf3_UniversAvant_dialogue_done = False
        self.tp_monde4 = False
        #MONDE QUATRE
        self.fish_done = False
        self.panneaux_dialogue_done = False
        self.portier4_dialogue_done = False
        self.fish2_done = False
        self.portier4_2dialogue1_done = False
        self.portier4_2dialogue2_done = False
        self.portier4_2dialogue3_done = False
        self.grenouille = False
        self.lezard = False
        self.serpent = False
        self.portier4_2_cache = False
        self.bocal = False
        self.baton = False
        self.herbe = False
        self.inun = False
        self.amoka = False
        self.isi = False
        self.tp_monde5 = False
        #MONDE CINQ 
        self.Event_Invisible_done = False      #Charlie assiste à la dispute entre portier et gandalf
        self.Gandalf5_dialogue_done = False    # Gandalf nous a expliqué qu'il est coincé ici
        self.compris = False                   #Première ligne pour les ç, é, ù, etc. à ne lire qu'une fois
        self.go_gandalf = False               #On a compris qu'on est pas chez nous et qu'on doit aller voir Gandalf
        self.portier5 = False                #Gandalf a parlé au portier et notre mission est de réconforter l'enfant
        self.panneau_done = False            #Le moment où on arrête de remplir le panneau et on va réconforter la fille
        self.enfant5_dialogue_done = False    #On a réconforté la fille, on peut aller le dire au portier
        self.portier5_2_dialogue_done = False   #Portier quand on a réconforté sa fille
        self.PNJ20_parlé = False
        self.homme = False
        self.boue = False
        self.croccodile = False
        self.beau_frère = False
        self.femme = False
        self.belle_soeur = False
        self.têtard = False
        self.lait = False
        self.pigeon = False
        self.chauve_souris = False
        self.rat = False
        self.mari = False
        self.larmes = False
        self.salive = False
        self.corde = False
        self.serpent = False
        self.langue = False
        self.homme_finito = False
        self.boue_finito = False
        self.croccodile_finito = False
        self.beau_frère_finito = False
        self.femme_finito = False
        self.belle_soeur_finito = False
        self.têtard_finito = False
        self.lait_finito = False
        self.pigeon_finito = False
        self.chauve_souris_finito = False
        self.rat_finito = False
        self.mari_finito = False
        self.larmes_finito = False
        self.salive_finito = False
        self.corde_finito = False      
        self.serpent_finito = False
        self.langue_finito = False
        self.tp_monde6 = False
        #MONDE SIX
        self.compris6 = False # True quand on a compris qu'il faut aller voir Gandalf
        self.portier6 = False   #True quand on sait qu'on doit chercher les figurines
        self.portier6_2_dialogue_done = False #True quand on a résolu l'énigme
        self.Fig_Enfant = False
        self.Fig_Lune = False
        self.Fig_Voiture = False
        self.Fig_Ouragan = False
        self.Fig_Orange = False
        self.Fig_Arbre = False
        self.Enfant = False   #Quand le mot est compris
        self.Lune = False
        self.Voiture = False
        self.Ouragan = False
        self.Orange = False
        self.Arbre = False
        self.fin_de_jeu = False

        self.unlock_pokedex_entry(0, "Essai")
        
        # added for movement speed
        # the game is tile-based (player position is used directly as indices into 
        # map_array), we can’t safely use fractional speeds like 0.3 tiles per frame — 
        # that would make positions floats and crash when indexing the map. 
        # So instead, we slow the movement by only allowing one tile move every X milliseconds.
        # To make the player slower, increase self.move_delay (e.g. 150, 180, 200).
        self.move_delay = 120      # milliseconds between tile moves (higher = slower)
        self.last_move_time = 0    # timestamp of last movement

    def set_up(self):                     
        player = Player(1, 1)                    #Position du carré UNIQUEMENT si la position n'est pas indiquée dans la map (config)
        self.player = player
        print("do set up")
        self.game_state = GameState.RUNNING

        self.map.load("01", self.player)      

    # ---------------------------------------------------------------------
    # Gandalf5 follower helpers
    def _is_in_room(self):
        return getattr(self.map, "room_name", None) is not None

    def _should_show_gandalf5_follower(self):
        return (
            getattr(self, "gandalf5_following", False)
            and getattr(self.map, "file_name", None) in ("monde5", "monde5_N")
        )

    def _find_free_adjacent_tile_for_gandalf5(self, preferred_positions=None, max_radius=6):
        """Trouve une case libre (passable, dans la map, non occupée) proche du joueur.
        - preferred_positions: positions à tester d'abord (ex: last_position)
        - max_radius: rayon manhattan max si les cases proches sont toutes bloquées
        """
        if preferred_positions is None:
            preferred_positions = []

        # dimensions de la map
        w = len(self.map.map_array[0]) if getattr(self.map, 'map_array', None) else 0
        h = len(self.map.map_array) if getattr(self.map, 'map_array', None) else 0

        def in_bounds(pos):
            return (0 <= pos[0] < w) and (0 <= pos[1] < h)

        def is_passable(pos):
            try:
                return self.map.map_array[pos[1]][pos[0]] not in config.IMPASSIBLE
            except Exception:
                return False

        def is_occupied(pos):
            for o in getattr(self.map, 'objects', []):
                if o is self.player:
                    continue
                if getattr(o, 'is_gandalf5_follower', False):
                    continue
                if getattr(o, 'position', None) == pos:
                    return True
            return False

        def is_free(pos):
            return in_bounds(pos) and is_passable(pos) and (not is_occupied(pos))

        px, py = self.player.position
        player_pos = [px, py]

        # 1) Priorités (derrière, spawn, etc.)
        for pos in preferred_positions:
            if pos is None:
                continue
            p = pos[:]
            if p != player_pos and is_free(p):
                return p

        # 2) Cases adjacentes (4-voisins puis diagonales en fallback)
        adj = [[px-1, py], [px+1, py], [px, py-1], [px, py+1],
               [px-1, py-1], [px+1, py-1], [px-1, py+1], [px+1, py+1]]
        for p in adj:
            if p != player_pos and is_free(p):
                return p

        # 3) Recherche en anneaux (si entrée de room coincée par des objets)
        for r in range(2, max_radius + 1):
            for dx in range(-r, r + 1):
                dy = r - abs(dx)
                for sign in (-1, 1):
                    p = [px + dx, py + sign * dy]
                    if p != player_pos and is_free(p):
                        return p

        return None

    def sync_gandalf5_follower_on_current_map(self):
        """Ajoute/retire Gandalf5 des objets de la map selon l'état de follow.
        - présent uniquement sur monde5 / monde5_N
        - présent aussi dans les rooms (rooms de monde5/monde5_N)
        - ne doit pas déclencher d'événement en collision
        - ne doit jamais se placer sur la même case que le joueur
        """
        # Retire toute instance précédente du follower de la map
        if hasattr(self, "map") and getattr(self.map, "objects", None) is not None:
            self.map.objects = [o for o in self.map.objects if not getattr(o, "is_gandalf5_follower", False)]

        if not self._should_show_gandalf5_follower():
            return

        # Si la map config place encore un Gandalf5 "statique", on le retire quand il suit déjà.
        self.map.objects = [o for o in self.map.objects if getattr(o, "name", None) != "Gandalf5"]

        # Crée le follower (1 seule instance globale) si besoin
        if self.gandalf5_follower is None:
            from npc import Npc
            self.gandalf5_follower = Npc("Gandalf5_FOLLOWER", "prof", self.player.position[0], self.player.position[1])
            self.gandalf5_follower.is_gandalf5_follower = True

        # Position : on privilégie la case précédente du joueur, sinon une case adjacente libre.
        preferred = []
        if hasattr(self.player, "last_position"):
            preferred.append(self.player.last_position[:])
        if getattr(self, "gandalf5_follower_spawn", None):
            preferred.append(self.gandalf5_follower_spawn[:])
        if getattr(self.gandalf5_follower, "position", None):
            preferred.append(self.gandalf5_follower.position[:])

        pos = self._find_free_adjacent_tile_for_gandalf5(preferred_positions=preferred)

        # Sécurité anti-superposition : si on n'a rien trouvé (ou si on a fini sur le joueur),
        # on tente une recherche plus large. Et si vraiment impossible, on NE DESSINE PAS Gandalf
        # plutôt que de le superposer au joueur.
        if pos is None or pos == self.player.position:
            pos = self._find_free_adjacent_tile_for_gandalf5(preferred_positions=[], max_radius=12)

        if pos is None or pos == self.player.position:
            return

        self.gandalf5_follower.position = pos
        self.map.objects.append(self.gandalf5_follower)

    def _get_quit_dialog_rects(self):
        sw, sh = self.screen.get_size()
        box = pygame.Rect(0, 0, 520, 220)
        box.center = (sw // 2, sh // 2)

        yes_btn = pygame.Rect(box.left + 70, box.bottom - 70, 150, 45)
        no_btn  = pygame.Rect(box.right - 220, box.bottom - 70, 150, 45)
        return box, yes_btn, no_btn
    def _activate_quit_choice(self):
        self.confirm_quit = True
        self.quit_choice_index = 0

    def _handle_quit_choice_event(self, ev):
        if ev.type == pygame.KEYDOWN:
            if ev.key == pygame.K_ESCAPE:
                self.confirm_quit = False
                return
            if ev.key in (pygame.K_UP, pygame.K_w):
                self.quit_choice_index = (self.quit_choice_index - 1) % len(self.quit_choices)
                return
            if ev.key in (pygame.K_DOWN, pygame.K_s):
                self.quit_choice_index = (self.quit_choice_index + 1) % len(self.quit_choices)
                return
            if ev.key in (pygame.K_RETURN, pygame.K_SPACE):
                choice = self.quit_choices[self.quit_choice_index]
                if choice.lower().startswith("oui"):
                    self.game_state = GameState.ENDED
                else:
                    self.confirm_quit = False
                return

        if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
            _, yes_rect, no_rect = self._get_quit_choice_rects()
            if yes_rect.collidepoint(ev.pos):
                self.game_state = GameState.ENDED
            elif no_rect.collidepoint(ev.pos):
                self.confirm_quit = False

    def _get_quit_choice_rects(self):
        box, _, _ = self._get_quit_dialog_rects()
        font = pygame.font.Font("fonts/PokemonGb.ttf", 20) if os.path.exists("fonts/PokemonGb.ttf") else pygame.font.Font(None, 28)
        line_h = font.get_height() + 8
        x_text = box.left + 80
        y0 = box.top + 110
        yes_rect = pygame.Rect(x_text, y0, box.width - 120, line_h)
        no_rect  = pygame.Rect(x_text, y0 + line_h, box.width - 120, line_h)
        return box, yes_rect, no_rect

    def render_choice(self):
        overlay = pygame.Surface(self.screen.get_size(), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 180))
        self.screen.blit(overlay, (0, 0))

        box, _, _ = self._get_quit_choice_rects()
        pygame.draw.rect(self.screen, (240, 240, 240), box, border_radius=12)

        font = pygame.font.Font("fonts/PokemonGb.ttf", 20) if os.path.exists("fonts/PokemonGb.ttf") else pygame.font.Font(None, 28)
        color = (0, 0, 0)
        surf_q = font.render("Quitter le jeu ?", True, color)
        self.screen.blit(surf_q, (box.left + 40, box.top + 35))

        x_arrow = box.left + 55
        x_text  = box.left + 80
        y = box.top + 110
        for i, choice in enumerate(self.quit_choices):
            surf = font.render(choice, True, color)
            self.screen.blit(surf, (x_text, y))
            if i == self.quit_choice_index:
                arrow_points = [(x_arrow, y + 8), (x_arrow - 10, y + 2), (x_arrow - 10, y + 14)]
                pygame.draw.polygon(self.screen, (255, 0, 0), arrow_points)
            y += font.get_height() + 8

    
    def update(self):
        if self.fin_de_jeu == True:
            self.game_state = GameState.ENDED
        
        if getattr (self.map, "file_name", None) in {"01", "monde7", "monde7_N"} \
        and self.intro_played == False :
            self.intro.play(-1)
            self.intro_played = True
            self.mondes123.stop()
            self.mondes456.stop()
            self.mondes456_played = False
            self.mondes123_played = False
            
        if getattr (self.map, "file_name", None) in {"monde1", "monde1_N", "monde2", "monde2_N", "monde3", "monde3_N"} \
        and self.mondes123_played == False :
            self.mondes123.play(-1)
            self.mondes123_played = True
            self.intro.stop()
            self.mondes456.stop()
            self.intro_played = False
            self.mondes456_played = False

        if getattr (self.map, "file_name", None) in {"monde4", "monde4_N", "monde5", "monde5_N", "monde6", "monde6_N"} \
        and self.mondes456_played == False :
            self.mondes456.play(-1)
            self.mondes456_played = True
            self.intro.stop()
            self.mondes123.stop()
            self.intro_played = False
            self.mondes123_played = False
            
            
        # Toggle Pokedex with P (edge-detected, works even if an event consumes pygame events)
        keys = pygame.key.get_pressed()
        p_pressed = keys[pygame.K_p]
        if p_pressed and not self._prev_p_pressed:
            self.pokedex_open = not self.pokedex_open
            if self.pokedex_open:
                self.pokedex_ui.set_world(self._get_world_id_from_map())
        self._prev_p_pressed = p_pressed

        # If Pokedex is open, pause everything and only render the overlay
        if self.pokedex_open:
            # Background: map + player
            if self.current_game_state == CurrentGameState.MAP:
                self.screen.fill(config.BLACK)
                self.map.render(self.screen, self.player)

            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    self.game_state = GameState.ENDED
                else:
                    self.pokedex_ui.handle_event(ev)

            self.pokedex_ui.render()
            return

        # --- Quit confirmation (ESC) : edge-detected like Pokedex ---
        keys = pygame.key.get_pressed()
        esc_pressed = keys[pygame.K_ESCAPE]
        if esc_pressed and not self._prev_esc_pressed:
            self._activate_quit_choice()
        self._prev_esc_pressed = esc_pressed

        # If quit choice is open, pause the game and only handle quit UI
        if self.confirm_quit:
            if self.current_game_state == CurrentGameState.MAP:
                self.screen.fill(config.BLACK)
                self.map.render(self.screen, self.player)

            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    self.game_state = GameState.ENDED
                else:
                    self._handle_quit_choice_event(ev)

            self.render_choice()
            return

            
        if self.current_game_state == CurrentGameState.MAP:
            self.player_has_moved = False
            self.screen.fill(config.BLACK)

        # If a dialog / event is running (PNJ, pick-monster, etc.),
        # we don't want the player to keep moving. Let the event
        # handle input and drawing instead.
            if self.event is not None:
                # Draw the map & player in the background
                self.map.render(self.screen, self.player)
                
                # ---- Global overlays should work even during dialogues/cutscenes ----

                # We "tap" the event queue once, handle ESC, then re-post the remaining

                # events so the current event/dialogue can still read them normally.

                tapped_events = pygame.event.get()

                for ev in tapped_events:
                    if ev.type == pygame.QUIT:
                        self.game_state = GameState.ENDED
                        continue

                    # Toggle quit confirmation on ESC (consume it so dialogues don't advance)
                    if ev.type == pygame.KEYDOWN and ev.key == pygame.K_ESCAPE:
                        self._activate_quit_choice()
                        continue
                    
                    pygame.event.post(ev)

                # If an overlay was opened, pause the cutscene and only handle the overlay UI

                if self.pokedex_open:
                    for ev in pygame.event.get():
                        if ev.type == pygame.QUIT:
                            self.game_state = GameState.ENDED
                        else:
                            self.pokedex_ui.handle_event(ev)
                    self.pokedex_ui.render()
                    return

                if self.confirm_quit:
                    for ev in pygame.event.get():
                        if ev.type == pygame.QUIT:
                            self.game_state = GameState.ENDED
                        else:
                            self._handle_quit_choice_event(ev)
                    self.render_choice()
                    return

                # Update the current event (reads its own pygame events)
                self.event.update()

                # Draw the dialog box / cut-scene on top
                if hasattr(self.event, "render"):
                    self.event.render()

                return  # <-- IMPORTANT: skip normal movement

            # (Re)place Gandalf5 follower si besoin (monde5/monde5_N hors rooms)
            self.sync_gandalf5_follower_on_current_map()

            # handle quit / ESC / debug keys
            self.handle_events()

            # ---- continuous movement here ----
            keys = pygame.key.get_pressed()
            dx, dy = 0, 0

            if keys[pygame.K_UP]:
                dy = -1
                
            elif keys[pygame.K_DOWN]:
                dy = 1

            if keys[pygame.K_LEFT]:
                dx = -1
            elif keys[pygame.K_RIGHT]:
                dx = 1

            if dx != 0 or dy != 0:
                now = pygame.time.get_ticks()

                # Only move if enough time has passed since the last step
                if now - self.last_move_time >= self.move_delay:
                    self.last_move_time = now

                    # update sprite orientation if this is the player
                    if isinstance(self.player, Player):
                        self.player.set_direction(dx, dy)

                    self.move_unit(self.player, [dx, dy])

            if self.player_has_moved:
                self.determine_game_events()

            self.map.render(self.screen, self.player)

    
    # ---------------- Pokedex helpers ----------------
    def _get_world_id_from_map(self):
        fn = getattr(self.map, "file_name", "") or ""
        if fn.startswith("monde1"):
            return 1
        if fn.startswith("monde2"):
            return 2
        if fn.startswith("monde3"):
            return 3
        if fn.startswith("monde4"):
            return 4
        if fn.startswith("monde5"):
            return 5
        if fn.startswith("monde6"):
            return 6
        return 0

    def unlock_pokedex_entry(self, world_id: int, entry_id: str):
        if entry_id:
            self.pokedex_unlocks.add((int(world_id), str(entry_id)))

    def is_pokedex_unlocked(self, world_id: int, entry_id: str) -> bool:
        return (int(world_id), str(entry_id)) in self.pokedex_unlocks


    def determine_game_events(self):
        map_tile = self.map.map_array[self.player.position[1]][self.player.position[0]]
        print(map_tile)

        if map_tile == config.MAP_TILE_ROOM_EXIT:
            self.player.position = self.map.player_exit_position[:]
            self.maps.pop()
            self.map = self.maps[-1]
            return

        # if the map tile is a door, we need a room
        if utilities.test_if_int(map_tile):
            room = Map(self.screen)
            room.load_room(self.map.file_name, map_tile, self.player)
            self.map = room
            self.maps.append(room)
            return
        
        for npc in self.map.objects:
            if npc == self.map.player:
                continue
            if getattr(npc, "is_gandalf5_follower", False):
                continue
            
            if npc.position[:] == self.map.player.position[:]:
                game_event_handler.handle(self, self.player, npc)

        for exit_position in self.map.exit_positions:
            if self.player.position[:] == exit_position['position'][:]:
                map_file = exit_position['map']
                map = Map(self.screen)

                config.MAP_CONFIG[map_file]['start_position'] = exit_position['new_start_position'][:]

                map.load(map_file, self.player)
                self.maps.pop()
                self.map = map
                self.maps.append(map)

    def teleport_to_map(self, map_file, new_start_position=None):
        """
        Teleport the player to another overworld map, e.g. '02',
        from an event (PNJ, cutscene, etc.).
        """
        from game_view.map import Map  # already imported at top, but safe here if needed

        # If a start position is provided, override the config so the player
        # appears at that position on the new map
        if new_start_position is not None:
            config.MAP_CONFIG[map_file]['start_position'] = new_start_position[:]

        # Create and load the new map, using the same pattern as exits
        new_map = Map(self.screen)
        new_map.load(map_file, self.player)

        # Replace the current map on the stack with the new one
        if self.maps:
            self.maps.pop()
        self.map = new_map
        self.maps.append(new_map)

    def handle_events(self):
        if self.event is not None:
            return

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_state = GameState.ENDED

            # handle key events that should only trigger once
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self._activate_quit_choice()


    def move_unit(self, unit, position_change):
        new_position = [unit.position[0] + position_change[0], unit.position[1] + position_change[1]]

        # check if off map
        if new_position[0] < 0 or new_position[0] > (len(self.map.map_array[0]) - 1):
            return

        if new_position[1] < 0 or new_position[1] > (len(self.map.map_array) - 1):
            return

        # --- Déclencheur spécial PNJ3 sur la case [14,11] de la map "01" ---
        # (On bloque le mouvement tant que le dialogue n'a pas été fait une fois)
        from player import Player  # normalement déjà importé en haut, mais au cas où

        if isinstance(unit, Player) \
           and getattr(self.map, "file_name", None) == "monde1_N" \
           and new_position == [22, 18] \
           and not getattr(self, "portier_dialogue_done", False):

            # On cherche le PNJ3 dans la liste des objets de la map
            for npc in self.map.objects:
                if getattr(npc, "name", None) == "portier":
                    # On lance l'événement PNJ3 comme si on lui parlait
                    game_event_handler.handle(self, self.player, npc)
                    break

            return

        if isinstance(unit, Player) \
           and getattr(self.map, "file_name", None) == "monde2_N" \
           and new_position == [22, 18] \
           and not getattr(self, "Fantome_du_lac_dialogue_done", False):

            # On cherche le PNJ3 dans la liste des objets de la map
            for npc in self.map.objects:
                if getattr(npc, "name", None) == "Fantome_du_lac":
                    # On lance l'événement PNJ3 comme si on lui parlait
                    game_event_handler.handle(self, self.player, npc)
                    break

            return

        if isinstance(unit, Player) \
           and getattr(self.map, "file_name", None) == "monde3_N" \
           and new_position == [22, 18] \
           and not getattr(self, "portier3_4_dialogue_done", False):

            # On cherche le PNJ3 dans la liste des objets de la map
            for npc in self.map.objects:
                if getattr(npc, "name", None) == "portier3":
                    # On lance l'événement PNJ3 comme si on lui parlait
                    game_event_handler.handle(self, self.player, npc)
                    break

            return
        
        if isinstance(unit, Player) \
           and getattr(self.map, "file_name", None) == "monde4" \
           and new_position in ([9, 19], [10,19], [11,19], [9,20], [11,20], [9,21], [10,21], [11,21], [19,17]) \
           and not getattr(self, "fish_done", False):

            # On cherche le PNJ3 dans la liste des objets de la map
            for npc in self.map.objects:
                if getattr(npc, "name", None) == "fish":
                    # On lance l'événement PNJ3 comme si on lui parlait
                    game_event_handler.handle(self, self.player, npc, keep_player_position=True)
                    break

            return
        
        if isinstance(unit, Player) \
           and getattr(self.map, "file_name", None) == "monde4_N" \
           and new_position == [22, 18] \
           and not getattr(self, "portier4_dialogue_done", False):

            # On cherche le PNJ3 dans la liste des objets de la map
            for npc in self.map.objects:
                if getattr(npc, "name", None) == "portier4":
                    # On lance l'événement PNJ3 comme si on lui parlait
                    game_event_handler.handle(self, self.player, npc)
                    break

            return

        if isinstance(unit, Player) \
            and getattr(self.map, "file_name", None) == "monde4_N" \
            and getattr(self.map, "room_name", None) in (None, "01") \
            and new_position == [7, 32] \
            and not getattr(self, "fish2_done", False):

            for npc in self.map.objects:
                if getattr(npc, "name", None) == "fish2":
                    # On lance l'événement PNJ3 comme si on lui parlait
                    game_event_handler.handle(self, self.player, npc)
                    break

            return    

        if isinstance(unit, Player) \
            and getattr(self.map, "file_name", None) == "monde4_N" \
            and getattr(self.map, "room_name", None) in (None, "01") \
            and new_position == [7, 25] \
            and not getattr(self, "portier4_2_cache", False):

            for npc in self.map.objects:
                if getattr(npc, "name", None) == "portier4_2_cache":
                    # On lance l'événement PNJ3 comme si on lui parlait
                    game_event_handler.handle(self, self.player, npc)
                    break

            return 

        if isinstance(unit, Player) \
           and getattr(self.map, "file_name", None) == "monde5" \
           and new_position == [12, 7]:

            # On cherche le PNJ3 dans la liste des objets de la map
            for npc in self.map.objects:
                if getattr(npc, "name", None) == "Panneau_Place":
                    # On lance l'événement PNJ3 comme si on lui parlait
                    game_event_handler.handle(self, self.player, npc, keep_player_position=True)
                    break

            return

        if isinstance(unit, Player) \
           and getattr(self.map, "file_name", None) == "monde5" \
           and new_position in ([2, 17], [19,17], [25,24], [8,31], [19,31]):

            # On cherche le PNJ3 dans la liste des objets de la map
            for npc in self.map.objects:
                if getattr(npc, "name", None) == "porte_close":
                    # On lance l'événement PNJ3 comme si on lui parlait
                    game_event_handler.handle(self, self.player, npc, keep_player_position=True)
                    break

            return

        if isinstance(unit, Player) \
           and getattr(self.map, "file_name", None) == "monde5_N" \
           and new_position in ([19,18],[19, 19], [19,20], [19,21], [19,22], [19,23], [19,24], [19,25], [19,26]) \
           and not getattr(self, "Event_Invisible_done", False):

            # On cherche le PNJ3 dans la liste des objets de la map
            for npc in self.map.objects:
                if getattr(npc, "name", None) == "Event_Invisible":
                    # On lance l'événement PNJ3 comme si on lui parlait
                    game_event_handler.handle(self, self.player, npc, keep_player_position=True)
                    break

            return

        if isinstance(unit, Player) \
            and getattr(self.map, "file_name", None) == "monde5_N" \
            and getattr(self.map, "room_name", None) in (None, "01") \
            and new_position in ([1, 5], [2,5], [3,5], [4,5], [5,5], [6, 5], [7,5], [8,5], [9,5], [10,5], [11, 5], [12,5], [13,5]) :

            for npc in self.map.objects:
                if getattr(npc, "name", None) == "Gandalf5_1":
                    game_event_handler.handle(self, self.player, npc)
                    break

            return

        
        if isinstance(unit, Player) \
           and getattr(self.map, "file_name", None) == "monde5_N" \
           and new_position in ([20,18],[20,19],[20,20],[20,21],[20,22],[20,23],[20,24],[20,25],[20,26]) \
           and getattr(self, "Gandalf5_dialogue_done", False) \
           and not getattr(self, "portier5", False):

            for npc in self.map.objects:
                if getattr(npc, "name", None) == "Event_Invisible2":
                    game_event_handler.handle(self, self.player, npc, keep_player_position=True)
                    break
            
            return


        if isinstance(unit, Player) \
           and getattr(self.map, "file_name", None) == "monde5_N" \
           and new_position in ([22,18], [22,17]) \
           and not getattr(self, "portier5_2_dialogue_done", False):

            # On cherche le PNJ3 dans la liste des objets de la map
            for npc in self.map.objects:
                if getattr(npc, "name", None) == "portier5":
                    # On lance l'événement PNJ3 comme si on lui parlait
                    game_event_handler.handle(self, self.player, npc, keep_player_position=True)
                    break
            return

        if isinstance(unit, Player) \
           and getattr(self.map, "file_name", None) == "monde6_N" \
           and new_position == [22, 18] \
           and not getattr(self, "portier6_2_dialogue_done", False):

            # On cherche le PNJ3 dans la liste des objets de la map
            for npc in self.map.objects:
                if getattr(npc, "name", None) == "portier6":
                    # On lance l'événement PNJ3 comme si on lui parlait
                    game_event_handler.handle(self, self.player, npc)
                    break

            return

        
        # check for valid movement
        if self.map.map_array[new_position[1]][new_position[0]] in config.IMPASSIBLE:
            return

        self.player_has_moved = True

        unit.update_position(new_position)

        # Si Gandalf5 suit, on le fait avancer sur la case précédente du joueur
        if isinstance(unit, Player) and self._should_show_gandalf5_follower():
            self.sync_gandalf5_follower_on_current_map()
