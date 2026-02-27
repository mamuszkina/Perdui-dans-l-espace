from enum import Enum
import pygame

class GameState(Enum):
    NONE = 0,
    RUNNING = 1,
    ENDED = 2

class CurrentGameState(Enum):
    MAP = 0,
    BATTLE = 1

def grayscale(surface: pygame.Surface) -> pygame.Surface:
    surf = surface.copy().convert_alpha()
    arr = pygame.surfarray.pixels3d(surf)
    lum = (0.299 * arr[:, :, 0] + 0.587 * arr[:, :, 1] + 0.114 * arr[:, :, 2]).astype(arr.dtype)
    arr[:, :, 0] = lum
    arr[:, :, 1] = lum
    arr[:, :, 2] = lum
    del arr
    return surf