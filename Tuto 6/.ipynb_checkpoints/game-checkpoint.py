import random

import pygame
import config
import math
import utilities
from events import game_event_handler

from player import Player
from game_state import GameState, CurrentGameState
from game_view.map import Map

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
        # Drapeau : est-ce que le dialogue de portier a déjà été joué au moins une fois ?
        #MONDE UN
        self.portier_dialogue_done = False
        #MONDE DEUX
        self.PNJ7_dialogue_done = False
        self.PNJ8_dialogue_done = False
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
    
    def update(self):
        if self.current_game_state == CurrentGameState.MAP:
            self.player_has_moved = False
            self.screen.fill(config.BLACK)

        # If a dialog / event is running (PNJ, pick-monster, etc.),
        # we don't want the player to keep moving. Let the event
        # handle input and drawing instead.
            if self.event is not None:
                # Draw the map & player in the background
                self.map.render(self.screen, self.player)

                # Update the current event (reads its own pygame events)
                self.event.update()

                # Draw the dialog box / cut-scene on top
                if hasattr(self.event, "render"):
                    self.event.render()

                return  # <-- IMPORTANT: skip normal movement

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
                    self.game_state = GameState.NONE

                elif event.key == pygame.K_c:
                    self.teleport_to_map("monde1", [8,29])
                    return 
                elif event.key == pygame.K_v:
                    self.teleport_to_map("monde2", [8,29])
                    return

                # these are for debug (big jumps)
                elif event.key == pygame.K_z:  # up fast
                    self.move_unit(self.player, [0, -10])
                elif event.key == pygame.K_s:  # down fast
                    self.move_unit(self.player, [0, 10])
                elif event.key == pygame.K_q:  # left fast
                    self.move_unit(self.player, [-10, 0])
                elif event.key == pygame.K_d:  # right fast
                    self.move_unit(self.player, [10, 0])

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

        # check for valid movement
        if self.map.map_array[new_position[1]][new_position[0]] in config.IMPASSIBLE:
            return

        self.player_has_moved = True

        unit.update_position(new_position)
