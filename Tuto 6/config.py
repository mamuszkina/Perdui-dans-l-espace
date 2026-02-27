# colours
import config
import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (106, 229, 153)
YELLOW = (237, 208, 33)
RED = (251, 87, 60)
BLUE = (25,82,191)

SCALE = 70                                        #Zoom de l'image : 65 ou 75

SCREEN_HEIGHT = 700
SCREEN_WIDTH = 900

MAP_TILE_GRASS = "G"
MAP_TILE_GRASS2 = "O"
MAP_TILE_GRASS3 = "|"
MAP_TILE_FLOWER = "F"
MAP_TILE_WATER = "S"
MAP_TILE_ROAD = "R"
MAP_TILE_DOOR = "1"
MAP_TILE_DOORS = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]     #Dans quelle room les portes téléportent
MAP_TILE_LAB_FLOOR = "n"  #
MAP_TILE_LAB_WALL = "l"   #
MAP_TILE_ARMOIRE_BAS = "q"
MAP_TILE_ARMOIRE_HAUT = "a"
MAP_TILE_BIBLIOTHEQUE = "b"
MAP_TILE_CHAISE_DROITE = "d"
MAP_TILE_CHAISE_GAUCHE = "g"
MAP_TILE_PLANTE1_BAS = "r"
MAP_TILE_PLANTE1_HAUT = "f"
MAP_TILE_PLANTE2 = "m"
MAP_TILE_TABLE1 = "t"
MAP_TILE_FAUTEUIL1 = ","                               
MAP_TILE_FAUTEUIL2 = "?"                               
MAP_TILE_FAUTEUIL3 = ";"   
MAP_TILE_FAUTEUIL4 = "!" 
MAP_TILE_ARBRE1 = "$"
MAP_TILE_ARBRE2 = "%"
MAP_TILE_CHAMPI = "@"
MAP_TILE_TABLE2_GAUCHE = "u"
MAP_TILE_TABLE2_DROIT = "y"
MAP_TILE_ROOM_EXIT = "x"
MAP_TILE_BUILDING = "."
MAP_TILE_LARMOIRE = "v"
MAP_TILE_LSOL = "z"
MAP_TILE_LGE1 = "s"
MAP_TILE_LGE2 = "p"
MAP_TILE_LGE3 = "o"
MAP_TILE_LGE4 = "k"
MAP_TILE_LAB1 = "h"
MAP_TILE_LAB2 = "i"
MAP_TILE_LMACH = "e"
MAP_TILE_LMUR = "w"
MAP_TILE_FENCE = "X"
MAP_TILE_FENCE2 = "W"
MAP_TILE_FENCE3 = "Q"
MAP_TILE_FENCE4 = "D"
MAP_TILE_FENCE5 = "C"
MAP_TILE_FENCE6 = "E"
MAP_TILE_FENCE7 = "A"
MAP_TILE_FENCE8 = "Z"
MAP_TILE_TREE = "B"
MAP_TILE_TREE2 = "V"
MAP_TILE_CLOTURE = "M"
MAP_TILE_JPPDESTUILES = "*"
MAP_TILE_JPPDESTUILES2 = "="

IMPASSIBLE = [MAP_TILE_WATER, MAP_TILE_LAB_WALL, MAP_TILE_BUILDING, MAP_TILE_FENCE, MAP_TILE_FENCE2, MAP_TILE_FENCE3, MAP_TILE_FENCE4, MAP_TILE_FENCE5, MAP_TILE_FENCE6, MAP_TILE_FENCE7, MAP_TILE_FENCE8, MAP_TILE_TREE, MAP_TILE_TREE2, MAP_TILE_CLOTURE, MAP_TILE_ARMOIRE_HAUT, MAP_TILE_BIBLIOTHEQUE, MAP_TILE_PLANTE1_BAS, MAP_TILE_PLANTE1_HAUT, MAP_TILE_PLANTE2, MAP_TILE_TABLE1, MAP_TILE_LMUR, MAP_TILE_LMACH, MAP_TILE_LAB2, MAP_TILE_LAB1, MAP_TILE_LGE2, MAP_TILE_LGE1, MAP_TILE_LARMOIRE, MAP_TILE_ARBRE2, MAP_TILE_ARBRE1, MAP_TILE_JPPDESTUILES, MAP_TILE_JPPDESTUILES2]

MAP_CONFIG = {
    "01" : {
        "start_position": [15, 12],                              #position de départ du joueur (x,y)
        "exits" : [
        {
            "map" : "02",
            "position" : [3, 0],
            "new_start_position": [1, 4],
        }],
        "buildings": [
            {
                "sprite": "02",
                "name": "Home",
                "position": [6, 26],
                "size" : [5, 3]
            },
            {
                "sprite": "09",
                "name": "Horloge",
                "position": [25, 9],
                "size" : [2, 4]
            },
            {
                "sprite": "10",
                "name": "Lampadaire",
                "position": [18, 9],
                "size" : [1, 3]
            },
            {
                "sprite": "10",
                "name": "Lampadaire",
                "position": [21, 9],
                "size" : [1, 3]
            },
            {
                "sprite": "10",
                "name": "Lampadaire",
                "position": [18, 15],
                "size" : [1, 3]
            },
            {
                "sprite": "10",
                "name": "Lampadaire",
                "position": [21, 15],
                "size" : [1, 3]
            },
            {
                "sprite": "10",
                "name": "Lampadaire",
                "position": [21, 21],
                "size" : [1, 3]
            },
            {
                "sprite": "10",
                "name": "Lampadaire",
                "position": [18, 21],
                "size" : [1, 3]
            },
            {
                "sprite": "10",
                "name": "Lampadaire",
                "position": [18, 26],
                "size" : [1, 3]
            },
            {
                "sprite": "10",
                "name": "Lampadaire",
                "position": [21, 26],
                "size" : [1, 3]
            },
            {
                "sprite": "11",
                "name": "Barils",
                "position": [1, 31],
                "size" : [4, 3]
            },
        ],
        "npcs" : [
            {
            "name" : "PNJ2",
            "image" : "prof2",
            "start_position" : [3,3]                    
            },
            {
            "name" : "Panneau0",
            "image" : "panneau",
            "start_position" : [4,5]                    
            },
            {
            "name" : "PNJ3",
            "image" : "enfant_un",
            "start_position" : [10,10]
            },
             {
            "name" : "figur1",    
            "image" : "prof5",
            "start_position" : [27,13]                    
            },
            {
            "name" : "figur2",
            "image" : "prof5",
            "start_position" : [1,12]                    
            },
            {
            "name" : "figur3",
            "image" : "prof3",
            "start_position" : [2,17]                    
            },
            {
            "name" : "figur4",
            "image" : "prof4",
            "start_position" : [3,19]                    
            },
        ],
    },
    "02" : {
        "start_position": [1, 4],
        "exits" : [{
            "map" : "01",
            "position" : [1, 5],
            "new_start_position" : [3, 1],
        }],
        "npcs" : [
        ],
        "buildings": [
        ],
    },
    "monde1" : {
        "start_position" : [8,29],
        "exits" : [{
            "map" :"monde1_N",
            "position" : [3,0],                          
            "new_start_position" : [3,27],
        }],
        "npcs" : [
            {
            "name" : "PNJ4",
            "image" : "prof2",
            "start_position" : [5,4]                    
            },
            {
            "name" : "PNJ5",
            "image" : "enfant_un",
            "start_position" : [10,10]
            },
            {
            "name" : "Panneau1_OffreEmploi",
            "image" : "panneau",
            "start_position" : [15,29]
            },
            {
            "name" : "Panneau2_Indice",
            "image" : "panneau",
            "start_position" : [2,6]
            },
            {
            "name" : "figur1",    
            "image" : "prof4",
            "start_position" : [27,13]                    
            },
            {
            "name" : "figur2",
            "image" : "prof5",
            "start_position" : [1,12]                    
            },
            {
            "name" : "figur3",
            "image" : "prof3",
            "start_position" : [2,17]                    
            },
            {
            "name" : "figur4",
            "image" : "prof4",
            "start_position" : [3,19]                    
            },
        ],
        "buildings": [
            {
                "sprite" : "02",
                "name" : "Home",
                "position" : [6,26],
                "size" : [5,3]
            },
            {
                "sprite": "09",
                "name": "Horloge",
                "position": [25, 9],
                "size" : [2, 4]
            },
            {
                "sprite": "10",
                "name": "Lampadaire",
                "position": [18, 9],
                "size" : [1, 3]
            },
            {
                "sprite": "10",
                "name": "Lampadaire",
                "position": [21, 9],
                "size" : [1, 3]
            },
            {
                "sprite": "10",
                "name": "Lampadaire",
                "position": [18, 15],
                "size" : [1, 3]
            },
            {
                "sprite": "10",
                "name": "Lampadaire",
                "position": [21, 15],
                "size" : [1, 3]
            },
            {
                "sprite": "10",
                "name": "Lampadaire",
                "position": [21, 21],
                "size" : [1, 3]
            },
            {
                "sprite": "10",
                "name": "Lampadaire",
                "position": [18, 21],
                "size" : [1, 3]
            },
            {
                "sprite": "10",
                "name": "Lampadaire",
                "position": [18, 26],
                "size" : [1, 3]
            },
            {
                "sprite": "10",
                "name": "Lampadaire",
                "position": [21, 26],
                "size" : [1, 3]
            },
            {
                "sprite": "11",
                "name": "Barils",
                "position": [1, 31],
                "size" : [4, 3]
            },
        ],
    },
    "monde1_N" : {
        "start_position" : [1,4],
        "exits" : [{
            "map" : "monde1",
            "position" : [3,27],                          #la position à avoir dans monde1_N pour aller à monde1 (x,y)
            "new_start_position" : [3,1]                  #la position de départ de la map monde1 après être sorti
        }],
        "npcs" : [
            {
            "name" : "portier",
            "image" : "portier",
            "start_position" : [23,19]
            },
            {
            "name" : "Panneau4_Scène_Errès",
            "image" : "panneau",
            "start_position" : [20,19]
            },
            {
            "name" : "Panneau3_Toilettes",
            "image" : "panneau",
            "start_position" : [3,13]
            }
        ],
        "buildings": [
{
                "sprite": "04",
                "name": "Scene_Erres",
                "position": [19, 14],
                "size" : [6, 5]
            },
            {
                "sprite": "03",
                "name": "Toilettes",
                "position" : [2,10],
                "size" : [4,3]
            }
        ],
    },
    "monde2" : {                                           #MONDE 2 A CONFIGURER ENTIEREMENT
        "start_position" : [8,29],
        "exits" : [{
            "map" : "monde2_N",
            "position" : [3,0],                          #la position à avoir dans monde1_N pour aller à monde1 (x,y)
            "new_start_position" : [3,27]                  #la position de départ de la map monde1 après être sorti
        }],
        "npcs" : [
            {
            "name" : "Panneau5_Indice",
            "image" : "panneau",
            "start_position" : [2,6]
            },
            {
            "name" : "figur1",    
            "image" : "prof4",
            "start_position" : [27,13]                    
            },
            {
            "name" : "figur2",
            "image" : "prof5",
            "start_position" : [1,12]                    
            },
            {
            "name" : "figur3",
            "image" : "prof3",
            "start_position" : [2,17]                    
            },
            {
            "name" : "figur4",
            "image" : "prof4",
            "start_position" : [3,19]                    
            },
        ],
        "buildings": [
{
                "sprite": "02",
                "name": "Boulangerie",
                "position": [6, 26],
                "size" : [5, 3]
            },
            {
                "sprite": "02",
                "name": "PNJ1_Home",
                "position" : [22, 16],
                "size" : [5, 3]
            },
            {
                "sprite": "09",
                "name": "Horloge",
                "position": [25, 9],
                "size" : [2, 4]
            },
            {
                "sprite": "10",
                "name": "Lampadaire",
                "position": [18, 9],
                "size" : [1, 3]
            },
            {
                "sprite": "10",
                "name": "Lampadaire",
                "position": [21, 9],
                "size" : [1, 3]
            },
            {
                "sprite": "10",
                "name": "Lampadaire",
                "position": [18, 15],
                "size" : [1, 3]
            },
            {
                "sprite": "10",
                "name": "Lampadaire",
                "position": [21, 15],
                "size" : [1, 3]
            },
            {
                "sprite": "10",
                "name": "Lampadaire",
                "position": [21, 21],
                "size" : [1, 3]
            },
            {
                "sprite": "10",
                "name": "Lampadaire",
                "position": [18, 21],
                "size" : [1, 3]
            },
            {
                "sprite": "10",
                "name": "Lampadaire",
                "position": [18, 26],
                "size" : [1, 3]
            },
            {
                "sprite": "10",
                "name": "Lampadaire",
                "position": [21, 26],
                "size" : [1, 3]
            },
            {
                "sprite": "11",
                "name": "Barils",
                "position": [1, 31],
                "size" : [4, 3]
            },
        ],
    },
    "monde2_N" : {                                          
        "start_position" : [1,4],
        "exits" : [{
            "map" : "monde2",
            "position" : [3,27],                          #la position à avoir dans monde1_N pour aller à monde1 (x,y)
            "new_start_position" : [3,1]                  #la position de départ de la map monde1 après être sorti
        }],
        "npcs" : [
            {
            "name" : "Panneau6_2_toilettes",
            "image" : "panneau",
            "start_position" : [3,13]
            },
            {
            "name" : "PNJ8",
            "image" : "prof2",
            "start_position" : [25,25]
            },
            {
            "name" : "Panneau6_Scene_Erres",
            "image" : "panneau",
            "start_position" : [20,19]
            },
            {
            "name" : "Fantome_du_lac",
            "image" : "water",
            "start_position" : [9,26]
            },
            {
            "name" : "Clef",
            "image" : "grass1",
            "start_position" : [6,11]
            },
            {
            "name" : "PNJ7",
            "image" : "enfant_deux",
            "start_position" : [30,17]
            },
        ],
        "buildings": [
{
                "sprite": "04",
                "name": "Home",
                "position": [19, 14],
                "size" : [6, 5]
            },
            {
                "sprite": "03",
                "name": "Toilettes",
                "position" : [2,10],
                "size" : [4,3]
            },
            {
                "sprite": "02",
                "name": "Maison_Vide",
                "position" : [2, 17],
                "size" : [5,3]
            }
        ],
    },
    "monde3" : {                                          
        "start_position" : [8,29],
        "exits" : [{
            "map" : "monde3_N",
            "position" : [3,0],                          #la position à avoir dans monde1_N pour aller à monde1 (x,y)
            "new_start_position" : [3,27]                  #la position de départ de la map monde1 après être sorti
        }],
        "npcs" : [
            {
            "name" : "PNJ12",
            "image" : "enfant_un",
            "start_position" : [16,25]
            },
            {
            "name" : "Panneau7",
            "image" : "panneau",
            "start_position" : [4,5]
            },
            {
            "name" : "PNJ14",
            "image" : "enfant_deux",
            "start_position" : [24,26]
            },
            {
            "name" : "figur1",    
            "image" : "prof4",
            "start_position" : [27,13]                    
            },
            {
            "name" : "figur2",
            "image" : "prof5",
            "start_position" : [1,12]                    
            },
            {
            "name" : "figur3",
            "image" : "prof3",
            "start_position" : [2,17]                    
            },
            {
            "name" : "figur4",
            "image" : "prof4",
            "start_position" : [3,19]                    
            },
        ],
        "buildings": [
{
                "sprite": "02",
                "name": "Boulangerie",
                "position": [6, 26],
                "size" : [5, 3]
            },
            {
                "sprite": "02",
                "name": "PNJ1_Home",
                "position" : [22, 16],
                "size" : [5, 3]
            },
            {
                "sprite": "09",
                "name": "Horloge",
                "position": [25, 9],
                "size" : [2, 4]
            },
            {
                "sprite": "10",
                "name": "Lampadaire",
                "position": [18, 9],
                "size" : [1, 3]
            },
            {
                "sprite": "10",
                "name": "Lampadaire",
                "position": [21, 9],
                "size" : [1, 3]
            },
            {
                "sprite": "10",
                "name": "Lampadaire",
                "position": [18, 15],
                "size" : [1, 3]
            },
            {
                "sprite": "10",
                "name": "Lampadaire",
                "position": [21, 15],
                "size" : [1, 3]
            },
            {
                "sprite": "10",
                "name": "Lampadaire",
                "position": [21, 21],
                "size" : [1, 3]
            },
            {
                "sprite": "10",
                "name": "Lampadaire",
                "position": [18, 21],
                "size" : [1, 3]
            },
            {
                "sprite": "10",
                "name": "Lampadaire",
                "position": [18, 26],
                "size" : [1, 3]
            },
            {
                "sprite": "10",
                "name": "Lampadaire",
                "position": [21, 26],
                "size" : [1, 3]
            },
            {
                "sprite": "11",
                "name": "Barils",
                "position": [1, 31],
                "size" : [4, 3]
            },
        ],
    },
    "monde3_N" : {                                          
        "start_position" : [1,4],
        "exits" : [{
            "map" : "monde3",
            "position" : [3,27],                          #la position à avoir dans monde1_N pour aller à monde1 (x,y)
            "new_start_position" : [3,1]                  #la position de départ de la map monde1 après être sorti
        }],
        "npcs" : [
            {
            "name" : "portier3",
            "image" : "portier",
            "start_position" : [23,19]
            },
            {
            "name" : "Panneau9",
            "image" : "panneau",
            "start_position" : [20,19]
            },
            {
            "name" : "Panneau10",
            "image" : "panneau",
            "start_position" : [3,13]
            },
        ],
        "buildings": [
{
                "sprite": "04",
                "name": "Home",
                "position": [19, 14],
                "size" : [6, 5]
            },
            {
                "sprite": "03",
                "name": "Toilettes",
                "position" : [2,10],
                "size" : [4,3]
            },
            {
                "sprite": "02",
                "name": "Maison_Vide",
                "position" : [2, 16],
                "size" : [5,3]
            }
        ],
    },
    "monde4" : {                                          
        "start_position" : [1,4],
        "exits" : [{
            "map" : "monde4_N",
            "position" : [3,0],                          #la position à avoir dans monde1_N pour aller à monde1 (x,y)
            "new_start_position" : [3,27]                  #la position de départ de la map monde1 après être sorti
        }],
        "npcs" : [
            {
            "name" : "panneau11",            
            "image" : "panneau",
            "start_position" : [13,14]
            },
            {
            "name" : "panneau12",            
            "image" : "panneau",
            "start_position" : [6,18]
            },
            {
            "name" : "panneau13",            
            "image" : "panneau",
            "start_position" : [7,18]
            },
            {
            "name" : "panneau14",            
            "image" : "panneau",
            "start_position" : [14,18]
            },
            {
            "name" : "panneau15",            
            "image" : "panneau",
            "start_position" : [13,18]
            },
            {
            "name" : "PNJ15",            
            "image" : "enfant_un",
            "start_position" : [8,30]
            },
            {
            "name" : "PNJ16",            
            "image" : "enfant_deux",
            "start_position" : [5,28]
            },
            {
            "name" : "PNJ17",            
            "image" : "prof4",
            "start_position" : [4,30]
            },
            {
            "name" : "fish",            
            "image" : "water",
            "start_position" : [1,1]
            },
        ],
        "buildings": [
            {
                "sprite": "05",
                "name": "Home",
                "position": [23, 6],
                "size" : [4, 3]
            },
            {
                "sprite": "05",
                "name": "Home",
                "position": [23, 13],
                "size" : [4, 3]
            },
            {
                "sprite": "05",
                "name": "Home",
                "position": [23, 20],
                "size" : [4, 3]
            },
            {
                "sprite": "05",
                "name": "Home",
                "position": [23, 27],
                "size" : [4, 3]
            },
            {
                "sprite": "06",
                "name": "Bibliothèque",
                "position": [9, 9],
                "size" : [5, 5]
            },
            {
                "sprite": "07",
                "name": "fontaine",
                "position": [7, 20],
                "size" : [2, 2]
            },
            {
                "sprite": "07",
                "name": "autrefontaine",
                "position": [12, 20],
                "size" : [2, 2]
            }
        ],
    },
    "monde4_N" : {                                          
        "start_position" : [1,4],
        "exits" : [{
            "map" : "monde4",
            "position" : [3,27],                          #la position à avoir dans monde1_N pour aller à monde1 (x,y)
            "new_start_position" : [3,1]                  #la position de départ de la map monde1 après être sorti
        }],
        "npcs" : [
            {
            "name" : "panneau16",            
            "image" : "panneau",
            "start_position" : [7,19]
            },
            {
            "name" : "PNJ18",            
            "image" : "prof5",
            "start_position" : [16,24]
            },
            {
            "name" : "PNJ19",            
            "image" : "prof3",
            "start_position" : [8,13]
            },
            {
            "name" : "portier4",            
            "image" : "prof3",
            "start_position" : [23,19]
            },
        ],
        "buildings": [
            {
                "sprite": "04",
                "name": "Home",
                "position": [19, 14],
                "size" : [6, 5]
            }
        ],
    },
    "monde5" :{                                          
        "start_position" : [1,4],
        "exits" : [{
            "map" : "monde5_N",
            "position" : [3,0],                          #la position à avoir dans monde1_N pour aller à monde1 (x,y)
            "new_start_position" : [3,27]                  #la position de départ de la map monde1 après être sorti
        }],
        "npcs" : [
            {
            "name" : "PNJ20",            #Bouteille de lait
            "image" : "prof4",
            "start_position" : [15,15]
            },
            {
            "name" : "Panneau_Place",     #       
            "image" : "panneau",
            "start_position" : [11,7]
            },
            {
            "name" : "PNJ22",            #petite fille boc notes
            "image" : "enfant_un",
            "start_position" : [22,5]
            },
            {
            "name" : "PNJ23",            #mère sur bloc notes
            "image" : "prof5",
            "start_position" : [23,5]
            },
            {
            "name" : "panneau17",            #pancarte sur bloc notes
            "image" : "panneau",
            "start_position" : [12,21]
            },
            {
            "name" : "tag_maison",            #tag maison sur bloc notes
            "image" : "graffiti",
            "start_position" : [21,17]
            },
            {
            "name" : "porte_close",            
            "image" : "water",
            "start_position" : [6,1]
            },
            {
            "name" : "panneau18",            
            "image" : "panneau",
            "start_position" : [27,6]
            },
        ],
        "buildings": [
            {
                "sprite": "08",
                "name": "Home",
                "position": [0, 13],
                "size" : [6, 5]
            },
            {
                "sprite": "08",
                "name": "Home",
                "position": [6, 13],
                "size" : [6, 5]
            },
            {
                "sprite": "08",
                "name": "Home",
                "position": [17, 13],
                "size" : [6, 5]
            },
            {
                "sprite": "08",
                "name": "Home",
                "position": [23, 13],
                "size" : [6, 5]
            },
            {
                "sprite": "08",
                "name": "Home",
                "position": [0, 20],
                "size" : [6, 5]
            },
            {
                "sprite": "08",
                "name": "Home",
                "position": [6, 20],
                "size" : [6, 5]
            },
            {
                "sprite": "08",
                "name": "Home",
                "position": [17, 20],
                "size" : [6, 5]
            },
            {
                "sprite": "08",
                "name": "Home",
                "position": [23, 20],
                "size" : [6, 5]
            },
            {
                "sprite": "08",
                "name": "Home",
                "position": [0, 27],
                "size" : [6, 5]
            },
            {
                "sprite": "08",
                "name": "Home",
                "position": [6, 27],
                "size" : [6, 5]
            },
            {
                "sprite": "08",
                "name": "Home",
                "position": [17, 27],
                "size" : [6, 5]
            },
            {
                "sprite": "08",
                "name": "Home",
                "position": [23, 27],
                "size" : [6, 5]
            },
            {
                "sprite": "10",
                "name": "Home",
                "position": [0, 16],
                "size" : [1, 3]
            },
            {
                "sprite": "10",
                "name": "Home",
                "position": [11, 16],
                "size" : [1, 3]
            },
            {
                "sprite": "10",
                "name": "Home",
                "position": [17, 16],
                "size" : [1, 3]
            },
            {
                "sprite": "10",
                "name": "Home",
                "position": [28, 16],
                "size" : [1, 3]
            },
            {
                "sprite": "10",
                "name": "Home",
                "position": [0, 23],
                "size" : [1, 3]
            },
            {
                "sprite": "10",
                "name": "Home",
                "position": [11, 23],
                "size" : [1, 3]
            },
            {
                "sprite": "10",
                "name": "Home",
                "position": [17, 23],
                "size" : [1, 3]
            },
            {
                "sprite": "10",
                "name": "Home",
                "position": [28, 23],
                "size" : [1, 3]
            },
            {
                "sprite": "10",
                "name": "Home",
                "position": [0, 30],
                "size" : [1, 3]
            },
            {
                "sprite": "10",
                "name": "Home",
                "position": [11, 30],
                "size" : [1, 3]
            },
            {
                "sprite": "10",
                "name": "Home",
                "position": [17, 30],
                "size" : [1, 3]
            },
            {
                "sprite": "10",
                "name": "Home",
                "position": [28, 30],
                "size" : [1, 3]
            },
            {
                "sprite": "09",
                "name": "Home",
                "position": [11, 1],
                "size" : [2, 4]
            },
            {
                "sprite": "07",
                "name": "Home",
                "position": [9, 4],
                "size" : [2, 2]
            },
            {
                "sprite": "07",
                "name": "Home",
                "position": [13, 4],
                "size" : [2, 2]
            },
            {
                "sprite": "07",
                "name": "Home",
                "position": [8, 7],
                "size" : [2, 2]
            },
            {
                "sprite": "07",
                "name": "Home",
                "position": [14, 7],
                "size" : [2, 2]
            }
        ],
    },
    "monde5_N" : {                                          
        "start_position" : [1,4],
        "exits" : [{
            "map" : "monde5",
            "position" : [3,27],                          #la position à avoir dans monde1_N pour aller à monde1 (x,y)
            "new_start_position" : [3,1]                  #la position de départ de la map monde1 après être sorti
        }],
        "npcs" : [
            {
            "name" : "portier5",            
            "image" : "portier",
            "start_position" : [23,19]
            },
            {
            "name" : "Gandalf5",            
            "image" : "prof",
            "start_position" : [24,20]
            },
            {
            "name" : "Event_Invisible",            
            "image" : "water",
            "start_position" : [24,12]
            },
            {
            "name" : "Event_Invisible2",            
            "image" : "water",
            "start_position" : [23,12]
            },
            {
            "name" : "PNJ21",            
            "image" : "prof3",
            "start_position" : [8,13]
            }
        ],
        "buildings": [
            {
                "sprite": "04",
                "name": "Home",
                "position": [19, 14],
                "size" : [6, 5]
            }
        ],
    },
    "monde6": {                                          
        "start_position" : [1,4],
        "exits" : [{
            "map" : "monde6_N",
            "position" : [3,0],                          #la position à avoir dans monde1_N pour aller à monde1 (x,y)
            "new_start_position" : [3,27]                  #la position de départ de la map monde1 après être sorti
        }],
        "npcs" : [
            {
            "name" : "Fig_Enfant",            
            "image" : "enfant",
            "start_position" : [12,20]
            },
            {
            "name" : "Fig_Arbre",            
            "image" : "arbre",
            "start_position" : [11,30]
            },
            {
            "name" : "PNJ24",            
            "image" : "prof5",
            "start_position" : [19,28]
            },
            {
            "name" : "PNJ26",            
            "image" : "enfant_deux",
            "start_position" : [18,30]
            },
            {
            "name" : "PNJ25",            
            "image" : "enfant_un",
            "start_position" : [23,4]
            },
            {
            "name" : "panneau19",            
            "image" : "panneau",
            "start_position" : [11,14]
            },
            {
            "name" : "panneau20",            
            "image" : "panneau",
            "start_position" : [8,14]
            },
        ],
        "buildings": [
            {
                "sprite": "05",
                "name": "Home",
                "position": [3, 16],
                "size" : [4, 3]
            },
            {
                "sprite": "05",
                "name": "Home",
                "position": [18, 23],
                "size" : [4, 3]
            },
        ],
    },
    "monde6_N": {                                          
        "start_position" : [1,4],
        "exits" : [{
            "map" : "monde6",
            "position" : [3,27],                          #la position à avoir dans monde1_N pour aller à monde1 (x,y)
            "new_start_position" : [3,1]                  #la position de départ de la map monde1 après être sorti
        }],
        "npcs" : [
            {
            "name" : "PNJ27",            
            "image" : "prof3",
            "start_position" : [6,21]
            },
            {
            "name" : "portier6",            
            "image" : "prof4",
            "start_position" : [23,19]
            },
            {
            "name" : "Fig_Lune",            
            "image" : "lune",
            "start_position" : [8,12]
            },
            {
            "name" : "Fig_Orange",            
            "image" : "orange",
            "start_position" : [26,16]
            },
            {
            "name" : "Fig_Voiture",            
            "image" : "voiture",
            "start_position" : [13,12]
            },
        ],
        "buildings": [
            {
                "sprite": "04",
                "name": "Home",
                "position": [19, 14],
                "size" : [6, 5]
            }
        ],
    },
    "monde7" : {
        "start_position": [1, 4],                              #position de départ du joueur (x,y)
        "exits" : [
        {
            "map" : "monde7_N",
            "position" : [3, 0],
            "new_start_position": [3, 27],
        }],
        "buildings": [
            {
                "sprite": "02",
                "name": "Home",
                "position": [6, 26],
                "size" : [5, 3]
            },
            {
                "sprite": "09",
                "name": "Horloge",
                "position": [25, 9],
                "size" : [2, 4]
            },
            {
                "sprite": "10",
                "name": "Lampadaire",
                "position": [18, 9],
                "size" : [1, 3]
            },
            {
                "sprite": "10",
                "name": "Lampadaire",
                "position": [21, 9],
                "size" : [1, 3]
            },
            {
                "sprite": "10",
                "name": "Lampadaire",
                "position": [18, 15],
                "size" : [1, 3]
            },
            {
                "sprite": "10",
                "name": "Lampadaire",
                "position": [21, 15],
                "size" : [1, 3]
            },
            {
                "sprite": "10",
                "name": "Lampadaire",
                "position": [21, 21],
                "size" : [1, 3]
            },
            {
                "sprite": "10",
                "name": "Lampadaire",
                "position": [18, 21],
                "size" : [1, 3]
            },
            {
                "sprite": "10",
                "name": "Lampadaire",
                "position": [18, 26],
                "size" : [1, 3]
            },
            {
                "sprite": "10",
                "name": "Lampadaire",
                "position": [21, 26],
                "size" : [1, 3]
            },
            {
                "sprite": "11",
                "name": "Barils",
                "position": [1, 31],
                "size" : [4, 3]
            },
        ],
        "npcs" : [
            {
            "name" : "PNJ28",
            "image" : "prof2",
            "start_position" : [3,3]                    
            },
            {
            "name" : "Panneau0",
            "image" : "panneau",
            "start_position" : [4,5]                    
            },
            {
            "name" : "PNJ29",
            "image" : "prof3",
            "start_position" : [10,10]
            },
             {
            "name" : "figur1",    
            "image" : "prof4",
            "start_position" : [27,13]                    
            },
            {
            "name" : "figur2",
            "image" : "prof5",
            "start_position" : [1,12]                    
            },
            {
            "name" : "figur3",
            "image" : "prof1",
            "start_position" : [2,17]                    
            },
            {
            "name" : "figur4",
            "image" : "prof2",
            "start_position" : [3,19]                    
            },
        ],
    },
    "monde7_N" : {
        "start_position" : [1,4],
        "exits" : [{
            "map" : "monde7",
            "position" : [3,27],                          #la position à avoir dans monde1_N pour aller à monde1 (x,y)
            "new_start_position" : [3,1]                  #la position de départ de la map monde1 après être sorti
        }],
        "npcs" : [
        ],
        "buildings": [
            {
                "sprite": "13",
                "name": "Tour Eiffel",
                "position" : [2,10],
                "size" : [5,12]
            }
        ],
    },
}

ROOM_CONFIG = {
    "01" : {                                             #RF nom de map du dossier "01" dans "rooms" (donc créer les maps dans le bon dossier)
        "02" : {                                         #RF room 02
            "start_position" : [7,10],
            "exit_position" : [8,29],
            "npcs" : [
                {
                    "name" : "PNJ1",
                    "image" : "prof1",
                    "start_position" : [8,3]
                },
                {
                    "name" : "TV",
                    "image" : "TV",
                    "start_position" : [4,6]
                },
                {
                    "name" : "Save",
                    "image" : "screen",
                    "start_position" : [3,6]
                },
            ]
        }
    },
    "monde1" : {       
        "02" : {
            "start_position" : [7,10],
            "exit_position" : [8,29],
            "npcs" : [
                {
                    "name" : "PNJ6",
                    "image" : "prof1",
                    "start_position" : [8,3]
                },
                {
                    "name" : "TV",
                    "image" : "TV",
                    "start_position" : [4,6]
                },
                {
                    "name" : "Screen1",
                    "image" : "screen",
                    "start_position" : [11,1]
                },
                {
                    "name" : "Save",
                    "image" : "screen",
                    "start_position" : [3,6]
                },
            ]
        }
    },
    "monde1_N" : {
        "01" : {
            "start_position" : [7,10],
            "exit_position" : [22,19],
            "npcs" : [
                {
                    "name" : "Gandalf1",
                    "image" : "prof",
                    "start_position" : [8,3]
                }
            ]
        }
    },
    "monde2" : {                                         #nom de la map (s'appelle comme je veux)
        "01" : {                                         #nom de la room (uniquement un chiffre 01,02,03 etc. Attention nom map = nom sortie dans map
            "start_position" : [7,10],
            "exit_position" : [8,29],
            "npcs" : [
                {
                    "name" : "PNJ9",
                    "image" : "prof1",
                    "start_position" : [8,3]
                },
                {
                    "name" : "Save",
                    "image" : "screen",
                    "start_position" : [3,6]
                },
            ]
        },
        "02" : {
            "start_position" : [7,10],
            "exit_position" : [24,19],
            "npcs" : [
                {
                    "name" : "PNJ10",
                    "image" : "enfant_un",
                    "start_position" : [8,3]
                },
            ]
        }
    },
    "monde2_N" : {
        "01" : {
            "start_position" : [7,10],
            "exit_position" : [4,20],
            "npcs" : [
                {
                    "name" : "Maison_papier",
                    "image" : "Table2gauche",
                    "start_position" : [10,7]
                },
                {                                       #handle et event pnj
                    "name" : "un",
                    "image" : "Table2gauche",
                    "start_position" : [9,6]
                },
                {
                    "name" : "deux",
                    "image" : "Table2gauche",
                    "start_position" : [4,9]
                },                                      
                {
                    "name" : "trois",                  
                    "image" : "Bibliotheque",
                    "start_position" : [2,3]
                },
                {
                    "name" : "quatre",
                    "image" : "Bibliotheque",
                    "start_position" : [1,1]
                },
                {
                    "name" : "cinq",
                    "image" : "Bibliotheque",
                    "start_position" : [2,1]
                },
                {
                    "name" : "six",
                    "image" : "Bibliotheque",
                    "start_position" : [3,1]
                },
                {
                    "name" : "sept",
                    "image" : "Bibliotheque",
                    "start_position" : [6,1]
                },
                {
                    "name" : "huit",
                    "image" : "Bibliotheque",
                    "start_position" : [7,1]
                },
                {
                    "name" : "neuf",
                    "image" : "Bibliotheque",
                    "start_position" : [13,6]
                },
                {
                    "name" : "dix",
                    "image" : "Plante2",
                    "start_position" : [5,6]
                },
                {
                    "name" : "onze",
                    "image" : "Table1",
                    "start_position" : [12,7]
                },
                {
                    "name" : "douze",
                    "image" : "Table1",
                    "start_position" : [4,5]
                },
                {
                    "name" : "treize",
                    "image" : "ArmoireHaut",
                    "start_position" : [11,1]
                },
                {
                    "name" : "quatorze",
                    "image" : "ArmoireHaut",
                    "start_position" : [12,1]
                },
                {
                    "name" : "quinze",
                    "image" : "ArmoireHaut",
                    "start_position" : [13,1]
                },
            ]
        },
        "02" : {
            "start_position" : [7,10],
            "exit_position" : [22,19],
            "npcs" : [
                {
                    "name" : "Gandalf2",
                    "image" : "prof",
                    "start_position" : [8,3]
                },
            ]
        }
    },
    "monde3" : {                                         #nom de la map (s'appelle comme je veux)
        "01" : {                                         #nom de la room (uniquement un chiffre 01,02,03 etc. Attention nom map = nom sortie dans map
            "start_position" : [7,10],
            "exit_position" : [8,29],
            "npcs" : [
                {
                    "name" : "Save",
                    "image" : "screen",
                    "start_position" : [3,6]
                },
            ]
        },
        "02" : {
            "start_position" : [7,10],
            "exit_position" : [24,19],
            "npcs" : [
                {
            "name" : "PNJ11",
            "image" : "prof3",
            "start_position" : [5,5]
            },
            ]
        }
    },
    "monde3_N" : {                                         #nom de la map (s'appelle comme je veux)
        "01" : {                                         #nom de la room (uniquement un chiffre 01,02,03 etc. Attention nom map = nom sortie dans map
            "start_position" : [7,10],
            "exit_position" : [4,20],
            "npcs" : [
                {
            "name" : "PNJ13",
            "image" : "prof3",
            "start_position" : [4,5]
            },
            ]
        },
        "02" : {
            "start_position" : [7,10],
            "exit_position" : [24,20],
            "npcs" : [
                {
                    "name" : "Gandalf3",
                    "image" : "prof",
                    "start_position" : [8,3]
                },
            ]
        }
    },
    "monde4" : {                                         #nom de la map (s'appelle comme je veux)
        "01" : {                                         #nom de la room (uniquement un chiffre 01,02,03 etc. Attention nom map = nom sortie dans map
            "start_position" : [7,13],
            "exit_position" : [12,14],
            "npcs" : [
                {
                    "name" : "Save",
                    "image" : "screen",
                    "start_position" : [1,11]
                },
                {
                    "name" : "bibliothèque",
                    "image" : "Bibliotheque",
                    "start_position" : [9,9]
                },
                {
                    "name" : "bibliothèque",
                    "image" : "Bibliotheque",
                    "start_position" : [8,9]
                },
                {
                    "name" : "bibliothèque",
                    "image" : "Bibliotheque",
                    "start_position" : [1,1]
                },
                {
                    "name" : "bibliothèque",
                    "image" : "Bibliotheque",
                    "start_position" : [2,1]
                },
                {
                    "name" : "bibliothèque",
                    "image" : "Bibliotheque",
                    "start_position" : [3,1]
                },
                {
                    "name" : "bibliothèque",
                    "image" : "Bibliotheque",
                    "start_position" : [4,1]
                },
                {
                    "name" : "bibliothèque",
                    "image" : "Bibliotheque",
                    "start_position" : [5,1]
                },
                {
                    "name" : "bibliothèque",
                    "image" : "Bibliotheque",
                    "start_position" : [6,1]
                },
                {
                    "name" : "bibliothèque",
                    "image" : "Bibliotheque",
                    "start_position" : [7,1]
                },
                {
                    "name" : "bibliothèque",
                    "image" : "Bibliotheque",
                    "start_position" : [8,1]
                },
                {
                    "name" : "bibliothèque",
                    "image" : "Bibliotheque",
                    "start_position" : [9,1]
                },
                {
                    "name" : "bibliothèque",
                    "image" : "Bibliotheque",
                    "start_position" : [10,1]
                },
                {
                    "name" : "bibliothèque",
                    "image" : "Bibliotheque",
                    "start_position" : [11,1]
                },
                {
                    "name" : "bibliothèque",
                    "image" : "Bibliotheque",
                    "start_position" : [12,1]
                },
                {
                    "name" : "bibliothèque",
                    "image" : "Bibliotheque",
                    "start_position" : [13,1]
                },
                {
                    "name" : "bibliothèque",
                    "image" : "Bibliotheque",
                    "start_position" : [1,3]
                },
                {
                    "name" : "bibliothèque",
                    "image" : "Bibliotheque",
                    "start_position" : [2,3]
                },
                {
                    "name" : "bibliothèque",
                    "image" : "Bibliotheque",
                    "start_position" : [3,3]
                },
                {
                    "name" : "bibliothèque",
                    "image" : "Bibliotheque",
                    "start_position" : [4,3]
                },
                {
                    "name" : "bibliothèque",
                    "image" : "Bibliotheque",
                    "start_position" : [5,3]
                },
                {
                    "name" : "bibliothèque",
                    "image" : "Bibliotheque",
                    "start_position" : [7,3]
                },
                {
                    "name" : "bibliothèque",
                    "image" : "Bibliotheque",
                    "start_position" : [8,3]
                },
                {
                    "name" : "bibliothèque",
                    "image" : "Bibliotheque",
                    "start_position" : [1,5]
                },
                {
                    "name" : "bibliothèque",
                    "image" : "Bibliotheque",
                    "start_position" : [2,5]
                },
                {
                    "name" : "bibliothèque",
                    "image" : "Bibliotheque",
                    "start_position" : [3,5]
                },
                {
                    "name" : "bibliothèque",
                    "image" : "Bibliotheque",
                    "start_position" : [4,5]
                },
                {
                    "name" : "bibliothèque",
                    "image" : "Bibliotheque",
                    "start_position" : [5,5]
                },
                {
                    "name" : "bibliothèque",
                    "image" : "Bibliotheque",
                    "start_position" : [1,7]
                },
                {
                    "name" : "bibliothèque",
                    "image" : "Bibliotheque",
                    "start_position" : [2,7]
                },
                {
                    "name" : "bibliothèque",
                    "image" : "Bibliotheque",
                    "start_position" : [3,7]
                },
                {
                    "name" : "bibliothèque",
                    "image" : "Bibliotheque",
                    "start_position" : [4,7]
                },
                {
                    "name" : "bibliothèque",
                    "image" : "Bibliotheque",
                    "start_position" : [5,7]
                },
                {
                    "name" : "bibliothèque",
                    "image" : "Bibliotheque",
                    "start_position" : [1,9]
                },
                {
                    "name" : "bibliothèque",
                    "image" : "Bibliotheque",
                    "start_position" : [2,9]
                },
                {
                    "name" : "bibliothèque",
                    "image" : "Bibliotheque",
                    "start_position" : [3,9]
                },
                {
                    "name" : "bibliothèque",
                    "image" : "Bibliotheque",
                    "start_position" : [4,9]
                },
                {
                    "name" : "bibliothèque",
                    "image" : "Bibliotheque",
                    "start_position" : [5,9]

                    
                },
                {
                    "name" : "bibliothèque",
                    "image" : "Bibliotheque",
                    "start_position" : [13,8]
                },
                {
                    "name" : "bibliothèque",
                    "image" : "Bibliotheque",
                    "start_position" : [8,7]
                },
                {
                    "name" : "bibliothèque",
                    "image" : "Bibliotheque",
                    "start_position" : [11,10]
                },
            ]
        },
    },
    "monde4_N" : {                                         #nom de la map (s'appelle comme je veux)
        "01" : {                                         #nom de la room (uniquement un chiffre 01,02,03 etc. Attention nom map = nom sortie dans map
            "start_position" : [7,34],
            "exit_position" : [22,19],
            "npcs" : [
                {
                    "name" : "Gandalf4",
                    "image" : "prof",
                    "start_position" : [8,3]
                },
                {
                    "name" : "grenouille",
                    "image" : "grenouille",
                    "start_position" : [12,27]
                },
                {
                    "name" : "serpent",
                    "image" : "serpent",
                    "start_position" : [12,31]
                },
                {
                    "name" : "lezard",
                    "image" : "lezard",
                    "start_position" : [5,26]
                },
                {
                    "name" : "bocal",
                    "image" : "bocal",
                    "start_position" : [6,28]
                },
                {
                    "name" : "baton",
                    "image" : "baton",
                    "start_position" : [7,28]
                },
                {
                    "name" : "herbe",
                    "image" : "herbe",
                    "start_position" : [8,28]
                },
                {
                    "name" : "portier4_2",
                    "image" : "portier",
                    "start_position" : [7,30]
                },
                {
                    "name" : "portier4_2_cache",
                    "image" : "Table1",
                    "start_position" : [12,33]
                },
                {
                    "name" : "farine",
                    "image" : "Armoirehaut",
                    "start_position" : [1,30]
                },
                {
                    "name" : "fish2",
                    "image" : "Table1",
                    "start_position" : [13,33]
                },
            ]
        },
    },
    "monde5" : {                                       
        "01" : {                                  
            "start_position" : [7,10],
            "exit_position" : [8,18],
            "npcs" : [
            ]
        },
        "02" : {
            "start_position" : [7,10],
            "exit_position" : [25,18],
            "npcs" : [
                {
                    "name" : "Save",
                    "image" : "screen",
                    "start_position" : [3,6]
                },
            ]
        },
        "03" : {                                  
            "start_position" : [7,10],
            "exit_position" : [2,25],
            "npcs" : [
            ]
        },
        "04" : {                                  
            "start_position" : [7,10],
            "exit_position" : [8,25],
            "npcs" : [
                {
                    "name" : "PNJ24_1",
                    "image" : "prof1",
                    "start_position" : [8,3]
                },
            ]
        },
        "05" : {                                  
            "start_position" : [7,10],
            "exit_position" : [19,25],
            "npcs" : [
            ]
        },
        "06" : {                                  
            "start_position" : [7,10],
            "exit_position" : [2,32],
            "npcs" : [
            {
            "name" : "enfant5",            
            "image" : "enfant_deux",
            "start_position" : [5,6]
            },
            ]
        },
        "07" : {                                  
            "start_position" : [7,10],
            "exit_position" : [25,32],
            "npcs" : [
            ]
        }
    },
    "monde5_N" : {                                         #nom de la map (s'appelle comme je veux)
        "01" : {                                         #nom de la room (uniquement un chiffre 01,02,03 etc. Attention nom map = nom sortie dans map
            "start_position" : [7,10],
            "exit_position" : [22,20],
            "npcs" : [
                {
                    "name" : "Gandalf5_1",
                    "image" : "sol",
                    "start_position" : [3,4]
                },
            ]
        },
    },
    "monde6" : {                                         #nom de la map (s'appelle comme je veux)
        "01" : {                                         #nom de la room (uniquement un chiffre 01,02,03 etc. Attention nom map = nom sortie dans map
            "start_position" : [7,10],
            "exit_position" : [20,26],
            "npcs" : [
                {
            "name" : "TV6",            
            "image" : "TV",
            "start_position" : [5,6]
            },
                
            ]
        },
        "02" : {                                         #nom de la room (uniquement un chiffre 01,02,03 etc. Attention nom map = nom sortie dans map
            "start_position" : [7,10],
            "exit_position" : [5,19],
            "npcs" : [
                {
            "name" : "Fig_Ouragan",            
            "image" : "ouragan",
            "start_position" : [2,6]
            },
            {
            "name" : "Save",
            "image" : "screen",
            "start_position" : [3,6]
            },
            ]
        },
    },
    "monde6_N" : {                                         #nom de la map (s'appelle comme je veux)
        "01" : {                                         #nom de la room (uniquement un chiffre 01,02,03 etc. Attention nom map = nom sortie dans map
            "start_position" : [7,10],
            "exit_position" : [22,19],
            "npcs" : [
                {
                    "name" : "Gandalf6",
                    "image" : "prof",
                    "start_position" : [8,3]
                },
            ]
        },
    },
}
