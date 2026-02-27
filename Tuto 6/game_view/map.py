import pygame
import config
import math
import utilities
from building import Building
from npc import Npc


class Map:
    def __init__(self, screen):
        self.screen = screen
        self.map_array = []
        self.camera = [0, 0]
        self.file_name = None
        self.player_exit_position = None
        self.objects = []
        self.exit_positions = []

    def load(self, file_name, player):
        self.file_name = file_name

        self.player = player
        self.objects = [player]

        with open('maps/' + file_name + ".txt") as map_file:
            for line in map_file:
                tiles = []
                for i in range(0, len(line) - 1, 2):
                    tiles.append(line[i])
                self.map_array.append(tiles)
            print(self.map_array)

        map_config = config.MAP_CONFIG[file_name]

        player.position = map_config['start_position'][:]

        for building_data in map_config["buildings"]:
            building = Building(building_data['sprite'], building_data['position'], building_data['size'],building_data.get('name'))
            self.objects.append(building)

        for npc_data in map_config['npcs']:                                               
            npc = Npc(npc_data['name'], npc_data['image'], npc_data['start_position'][0], npc_data['start_position'][1])
            self.objects.append(npc)

        for exit_position in map_config['exits']:
            self.exit_positions.append(exit_position)
            
    def load_room(self, map_name, room_name, player): 
        self.file_name = map_name                              
        self.room_name = str(room_name).zfill(2)               
        self.player = player
        self.objects = [player]

        room_config = config.ROOM_CONFIG[map_name][str(room_name).zfill(2)]
        self.player.position = room_config['start_position'][:]
        self.player.player_exit_position = room_config['exit_position'][:]
        self.player_exit_position = room_config['exit_position'][:]

        # create our npcs
        for npc_data in room_config['npcs']:                                               
            npc = Npc(npc_data['name'], npc_data['image'], npc_data['start_position'][0], npc_data['start_position'][1])
            self.objects.append(npc)

        with open('rooms/' + map_name + '/' + str(room_name).zfill(2) + ".txt") as room_file:
            for line in room_file:
                tiles = []
                for i in range(0, len(line) - 1, 2):
                    tiles.append(line[i])
                self.map_array.append(tiles)
            print(self.map_array)

        pass

    def render(self, screen, player):
        self.determine_camera(player)
        cam_x = int(round(self.camera[0] * config.SCALE))
        cam_y = int(round(self.camera[1] * config.SCALE))

        y_pos = 0
        for line in self.map_array:
            x_pos = 0
            for tile in line:
                if tile not in map_tile_image:
                    x_pos = x_pos + 1
                    continue
                
                # Base tiles (default for every map)
                image = map_tile_image[tile]

                # Per-world overrides (only ROAD changes)
                if tile == config.MAP_TILE_ROAD:
                    if self.file_name in {"monde1", "monde1_N"}:
                        image = map_tile_road_monde1
                    elif self.file_name in {"monde2", "monde2_N"}:
                        image = map_tile_road_monde2
                    elif self.file_name in {"monde3", "monde3_N"}:
                        image = map_tile_road_monde3
                
                rect = pygame.Rect(
                    x_pos * config.SCALE - cam_x,
                    y_pos * config.SCALE - cam_y,
                    config.SCALE, config.SCALE
                )
                screen.blit(image, rect)
                x_pos = x_pos + 1

            y_pos = y_pos + 1

        # draw all objects on map
        for object in self.objects:
            object.render(self.screen, self.camera)

    def determine_camera(self, player):
        
        map_height = len(self.map_array)
        map_width = len(self.map_array[0])

        screen_tiles_x = config.SCREEN_WIDTH / config.SCALE
        screen_tiles_y = config.SCREEN_HEIGHT / config.SCALE

        # ----- Y AXIS -----
        if map_height <= screen_tiles_y:
            # Centre verticalement la room
            self.camera[1] = -(screen_tiles_y - map_height) / 2
        else:
            max_y_position = map_height - screen_tiles_y
            y_position = player.position[1] - math.ceil(screen_tiles_y / 2)

            if y_position < 0:
                self.camera[1] = 0
            elif y_position > max_y_position:
                self.camera[1] = max_y_position
            else:
                self.camera[1] = y_position

        # ----- X AXIS -----
        if map_width <= screen_tiles_x:
            # Centre horizontalement la room
            self.camera[0] = -(screen_tiles_x - map_width) / 2
        else:
            max_x_position = map_width - screen_tiles_x
            x_position = player.position[0] - math.ceil(screen_tiles_x / 2)

            if x_position < 0:
                self.camera[0] = 0
            elif x_position > max_x_position:
                self.camera[0] = max_x_position
            else:
                self.camera[0] = x_position

map_tile_image = {
    config.MAP_TILE_GRASS : pygame.transform.scale(pygame.image.load("imgs/grass1.png"), (config.SCALE, config.SCALE)),
    config.MAP_TILE_GRASS2 : pygame.transform.scale(pygame.image.load("imgs/grass2.png"), (config.SCALE, config.SCALE)),
    config.MAP_TILE_FLOWER : pygame.transform.scale(pygame.image.load("imgs/flower.png"), (config.SCALE, config.SCALE)),
    config.MAP_TILE_TREE : pygame.transform.scale(pygame.image.load("imgs/tree.png"), (config.SCALE, config.SCALE)),
    config.MAP_TILE_TREE2 : pygame.transform.scale(pygame.image.load("imgs/tree2.png"), (config.SCALE, config.SCALE)),
    config.MAP_TILE_WATER: pygame.transform.scale(pygame.image.load("imgs/water.png"), (config.SCALE, config.SCALE)),
    config.MAP_TILE_ROAD: pygame.transform.scale(pygame.image.load("imgs/road.png"), (config.SCALE, config.SCALE)),
    config.MAP_TILE_FENCE: pygame.transform.scale(pygame.image.load("imgs/fence.png"), (config.SCALE, config.SCALE)),
    config.MAP_TILE_FENCE2: pygame.transform.scale(pygame.image.load("imgs/fence2.png"), (config.SCALE, config.SCALE)),
    config.MAP_TILE_FENCE3: pygame.transform.scale(pygame.image.load("imgs/fence3.png"), (config.SCALE, config.SCALE)),
    config.MAP_TILE_FENCE4: pygame.transform.scale(pygame.image.load("imgs/fence4.png"), (config.SCALE, config.SCALE)),
    config.MAP_TILE_FENCE5: pygame.transform.scale(pygame.image.load("imgs/fence5.png"), (config.SCALE, config.SCALE)),
    config.MAP_TILE_FENCE6: pygame.transform.scale(pygame.image.load("imgs/fence6.png"), (config.SCALE, config.SCALE)),
    config.MAP_TILE_FENCE7: pygame.transform.scale(pygame.image.load("imgs/fence7.png"), (config.SCALE, config.SCALE)),
    config.MAP_TILE_FENCE8: pygame.transform.scale(pygame.image.load("imgs/fence8.png"), (config.SCALE, config.SCALE)),
    config.MAP_TILE_LAB_FLOOR: pygame.transform.scale(pygame.image.load("imgs/lab_tile.png"), (config.SCALE, config.SCALE)),
    config.MAP_TILE_LAB_WALL: pygame.transform.scale(pygame.image.load("imgs/lab_wall.png"), (config.SCALE, config.SCALE)),
    config.MAP_TILE_ARMOIRE_BAS: pygame.transform.scale(pygame.image.load("imgs/Intérieur/Armoirebas.png"), (config.SCALE, config.SCALE)),
    config.MAP_TILE_ARMOIRE_HAUT: pygame.transform.scale(pygame.image.load("imgs/Intérieur/Armoirehaut.png"), (config.SCALE, config.SCALE)),
    config.MAP_TILE_BIBLIOTHEQUE: pygame.transform.scale(pygame.image.load("imgs/Intérieur/Bibliotheque.png"), (config.SCALE, config.SCALE)),
    config.MAP_TILE_CHAISE_DROITE: pygame.transform.scale(pygame.image.load("imgs/Intérieur/Chaise_droite.png"), (config.SCALE, config.SCALE)),
    config.MAP_TILE_CHAISE_GAUCHE: pygame.transform.scale(pygame.image.load("imgs/Intérieur/Chaise_gauche.png"), (config.SCALE, config.SCALE)),
    config.MAP_TILE_PLANTE1_BAS: pygame.transform.scale(pygame.image.load("imgs/Intérieur/Plante1_bas.png"), (config.SCALE, config.SCALE)),
    config.MAP_TILE_PLANTE1_HAUT: pygame.transform.scale(pygame.image.load("imgs/Intérieur/Plante1_haut.png"), (config.SCALE, config.SCALE)),
    config.MAP_TILE_PLANTE2: pygame.transform.scale(pygame.image.load("imgs/Intérieur/Plante2.png"), (config.SCALE, config.SCALE)),
    config.MAP_TILE_TABLE1: pygame.transform.scale(pygame.image.load("imgs/Intérieur/Table1.png"), (config.SCALE, config.SCALE)),
    config.MAP_TILE_TABLE2_GAUCHE: pygame.transform.scale(pygame.image.load("imgs/Intérieur/Table2gauche.png"), (config.SCALE, config.SCALE)),
    config.MAP_TILE_TABLE2_DROIT: pygame.transform.scale(pygame.image.load("imgs/Intérieur/Table2droit.png"), (config.SCALE, config.SCALE)),
    config.MAP_TILE_LARMOIRE: pygame.transform.scale(pygame.image.load("imgs/laboratoire/armoire.png"), (config.SCALE, config.SCALE)),
    config.MAP_TILE_LSOL: pygame.transform.scale(pygame.image.load("imgs/laboratoire/sol.png"), (config.SCALE, config.SCALE)),
    config.MAP_TILE_LGE1: pygame.transform.scale(pygame.image.load("imgs/laboratoire/GE1.png"), (config.SCALE, config.SCALE)),
    config.MAP_TILE_LGE2: pygame.transform.scale(pygame.image.load("imgs/laboratoire/GE2.png"), (config.SCALE, config.SCALE)),
    config.MAP_TILE_LGE3: pygame.transform.scale(pygame.image.load("imgs/laboratoire/GE3.png"), (config.SCALE, config.SCALE)),
    config.MAP_TILE_LGE4: pygame.transform.scale(pygame.image.load("imgs/laboratoire/GE4.png"), (config.SCALE, config.SCALE)),
    config.MAP_TILE_LAB1: pygame.transform.scale(pygame.image.load("imgs/laboratoire/lab_bas.png"), (config.SCALE, config.SCALE)),
    config.MAP_TILE_LAB2: pygame.transform.scale(pygame.image.load("imgs/laboratoire/lab_haut.png"), (config.SCALE, config.SCALE)),
    config.MAP_TILE_LMACH: pygame.transform.scale(pygame.image.load("imgs/laboratoire/Machine-droit.png"), (config.SCALE, config.SCALE)),
    config.MAP_TILE_LMUR: pygame.transform.scale(pygame.image.load("imgs/laboratoire/Mur.png"), (config.SCALE, config.SCALE)),
    config.MAP_TILE_ROOM_EXIT: pygame.transform.scale(pygame.image.load("imgs/floor_mat.png"), (config.SCALE, config.SCALE)), 
    config.MAP_TILE_CLOTURE: pygame.transform.scale(pygame.image.load("imgs/cloture.png"), (config.SCALE, config.SCALE)),
    config.MAP_TILE_FAUTEUIL1: pygame.transform.scale(pygame.image.load("imgs/Intérieur/fauteuil1.png"), (config.SCALE, config.SCALE)), 
    config.MAP_TILE_FAUTEUIL2: pygame.transform.scale(pygame.image.load("imgs/Intérieur/fauteuil2.png"), (config.SCALE, config.SCALE)),
    config.MAP_TILE_FAUTEUIL3: pygame.transform.scale(pygame.image.load("imgs/Intérieur/fauteuil3.png"), (config.SCALE, config.SCALE)),
    config.MAP_TILE_FAUTEUIL4: pygame.transform.scale(pygame.image.load("imgs/Intérieur/fauteuil4.png"), (config.SCALE, config.SCALE)),
    config.MAP_TILE_ARBRE1: pygame.transform.scale(pygame.image.load("imgs/arbre1.png"), (config.SCALE, config.SCALE)),
    config.MAP_TILE_ARBRE2: pygame.transform.scale(pygame.image.load("imgs/arbre2.png"), (config.SCALE, config.SCALE)),
    config.MAP_TILE_CHAMPI: pygame.transform.scale(pygame.image.load("imgs/champis.png"), (config.SCALE, config.SCALE)),
    config.MAP_TILE_GRASS3: pygame.transform.scale(pygame.image.load("imgs/grass3.png"), (config.SCALE, config.SCALE)),
    config.MAP_TILE_JPPDESTUILES: pygame.transform.scale(pygame.image.load("imgs/road.png"), (config.SCALE, config.SCALE)),
    config.MAP_TILE_JPPDESTUILES2: pygame.transform.scale(pygame.image.load("imgs/grass1.png"), (config.SCALE, config.SCALE)),
}

# ROAD overrides by world (everything else uses map_tile_image)
map_tile_road_monde1 = pygame.transform.scale(
    pygame.image.load("imgs/Monde1/road.png"), (config.SCALE, config.SCALE)
)
map_tile_road_monde2 = pygame.transform.scale(
    pygame.image.load("imgs/Monde2/road.png"), (config.SCALE, config.SCALE)
)
map_tile_road_monde3 = pygame.transform.scale(
    pygame.image.load("imgs/Monde2/road.png"), (config.SCALE, config.SCALE)
)