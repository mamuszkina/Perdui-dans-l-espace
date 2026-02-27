import pygame
import config

class Player:
    def __init__(self, x_postition, y_position):
        print("player created")
        self.position = [x_postition, y_position]
        self.last_position = [x_postition, y_position]    #nouveau tuto 6
        # Load directional sprites
        self.image_up = pygame.transform.scale(
            pygame.image.load("imgs/player.png"), (config.SCALE, config.SCALE)
        )
        self.image_down = pygame.transform.scale(
            pygame.image.load("imgs/player2.png"), (config.SCALE, config.SCALE)
        )
        self.image_left = pygame.transform.scale(
            pygame.image.load("imgs/player3.png"), (config.SCALE, config.SCALE)
        )
        self.image_right = pygame.transform.flip(self.image_left, True, False)

        # default orientation (e.g., facing down or up as you prefer)
        self.image = self.image_down
        self.rect = pygame.Rect(self.position[0] * config.SCALE, self.position[1] * config.SCALE, config.SCALE, config.SCALE)
        self.monster = None
        self.monsters = []

    def set_direction(self, dx, dy):
        # dy first so vertical movement has priority when moving diagonally
        if dy > 0:
            self.image = self.image_down
        elif dy < 0:
            self.image = self.image_up
        elif dx > 0:
            self.image = self.image_right
        elif dx < 0:
            self.image = self.image_left

    def update(self):
        print("player updated")

    def update_position(self, new_position):
        self.last_position = self.position[:]
        self.position[0] = new_position[0]
        self.position[1] = new_position[1]


    def render(self, screen, camera):
        self.rect = pygame.Rect(self.position[0] * config.SCALE - (camera[0] * config.SCALE), self.position[1] * config.SCALE - (camera[1] * config.SCALE), config.SCALE, config.SCALE)
        screen.blit(self.image, self.rect)
