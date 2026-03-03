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
    """
    Grayscale robuste (pygbag/web-friendly).
    - Essaie d'abord pygame.transform.grayscale si dispo
    - Sinon utilise surfarray.array3d/array_alpha (copies -> pas de surface lock)
    """
    # 1) Pygame-ce a parfois pygame.transform.grayscale (selon version)
    try:
        g = pygame.transform.grayscale(surface)
        # preserve alpha if needed
        if surface.get_masks()[3] != 0:
            g = g.convert_alpha()
        return g
    except Exception:
        pass

    # 2) Fallback numpy/surfarray sans pixels3d (évite les verrous)
    surf = surface.convert_alpha() if surface.get_masks()[3] != 0 else surface.convert()

    arr = pygame.surfarray.array3d(surf)  # copie (w, h, 3) -> pas de lock
    # luminance en entier (rapide, stable)
    # approx Rec.601: 0.299, 0.587, 0.114
    lum = (arr[:, :, 0].astype("uint16") * 77 +
           arr[:, :, 1].astype("uint16") * 150 +
           arr[:, :, 2].astype("uint16") * 29) >> 8
    gray = lum.astype("uint8")
    gray3 = pygame.surfarray.make_surface(gray.repeat(3).reshape(gray.shape[0], gray.shape[1], 3))

    # Réappliquer l'alpha si présent
    if surface.get_masks()[3] != 0:
        gray3 = gray3.convert_alpha()
        alpha = pygame.surfarray.array_alpha(surf)  # copie
        pygame.surfarray.pixels_alpha(gray3)[:, :] = alpha

    return gray3