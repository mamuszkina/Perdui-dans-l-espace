import pygame
import config
from Pokédex import POKEDEX_QUOTES

class PokedexUI:
    """Overlay UI showing NPC quotes per world.

    - Toggle open/close with P (handled by Game).
    - Navigate worlds with LEFT/RIGHT.
    - Scroll entries with UP/DOWN if needed.
    """

    def __init__(self, screen, game):
        self.screen = screen
        self.game = game

        self.world_page = 0  # 0..4
        self.scroll = 0
        self.max_world = 4

        # Fonts (fallback to default if missing)
        try:
            self.font_title = pygame.font.Font("fonts/Pokédex.ttf", 18)
            self.font_text = pygame.font.Font("fonts/Pokédex.ttf", 14)
        except Exception:
            self.font_title = pygame.font.SysFont(None, 24)
            self.font_text = pygame.font.SysFont(None, 18)

        # Layout
        self.margin = 40
        self.box_w = config.SCREEN_WIDTH - 2 * self.margin
        self.box_h = config.SCREEN_HEIGHT - 2 * self.margin
        self.box_rect = pygame.Rect(self.margin, self.margin, self.box_w, self.box_h)

        self.entry_h = 46
        self.entry_gap = 10

    def set_world(self, world_id: int):
        self.world_page = max(0, min(self.max_world, int(world_id)))
        self.scroll = 0

    def handle_event(self, event):
        if event.type != pygame.KEYDOWN:
            return

        if event.key == pygame.K_LEFT:
            self.set_world(self.world_page - 1)
        elif event.key == pygame.K_RIGHT:
            self.set_world(self.world_page + 1)
        elif event.key == pygame.K_UP:
            self.scroll = max(0, self.scroll - 1)
        elif event.key == pygame.K_DOWN:
            self.scroll = self.scroll + 1

    def _wrap_text(self, text, font, max_width):
        # Simple greedy word-wrap
        words = text.split(" ")
        lines = []
        current = ""
        for w in words:
            test = (current + " " + w).strip()
            if font.size(test)[0] <= max_width:
                current = test
            else:
                if current:
                    lines.append(current)
                current = w
        if current:
            lines.append(current)
        return lines

    def render(self):
        # Dim background
        overlay = pygame.Surface((config.SCREEN_WIDTH, config.SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 150))
        self.screen.blit(overlay, (0, 0))

        # Main box
        pygame.draw.rect(self.screen, (255, 255, 255), self.box_rect, border_radius=18)
        pygame.draw.rect(self.screen, (25, 82, 191), self.box_rect, width=3, border_radius=18)

        # Title + page
        title = f"Carnet des PNJs — Monde {self.world_page}"
        title_surf = self.font_title.render(title, True, (0, 0, 0))
        self.screen.blit(title_surf, (self.box_rect.x + 20, self.box_rect.y + 16))

        hint = "(P: fermer • ←/→: mondes)"
        hint_surf = self.font_text.render(hint, True, (0, 0, 0))
        self.screen.blit(hint_surf, (self.box_rect.right - hint_surf.get_width() - 20, self.box_rect.y + 20))

        # Entries
        entries = POKEDEX_QUOTES.get(self.world_page, [])
        area_top = self.box_rect.y + 60
        area_left = self.box_rect.x + 20
        area_right = self.box_rect.right - 20
        area_w = area_right - area_left
        area_bottom = self.box_rect.bottom - 20
        area_h = area_bottom - area_top

        # How many entries can we show?
        per_page = max(1, area_h // (self.entry_h + self.entry_gap))
        max_scroll = max(0, len(entries) - per_page)
        if self.scroll > max_scroll:
            self.scroll = max_scroll

        visible = entries[self.scroll:self.scroll + per_page]

        y = area_top
        for e in visible:
            unlocked = self.game.is_pokedex_unlocked(self.world_page, e.get("id", ""))
            bar_rect = pygame.Rect(area_left, y, area_w, self.entry_h)

            if unlocked:
                pygame.draw.rect(self.screen, (230, 230, 230), bar_rect, border_radius=10)
                pygame.draw.rect(self.screen, (120, 120, 120), bar_rect, width=2, border_radius=10)
                text = e.get("text", "")
            else:
                pygame.draw.rect(self.screen, (160, 160, 160), bar_rect, border_radius=10)
                pygame.draw.rect(self.screen, (90, 90, 90), bar_rect, width=2, border_radius=10)
                text = "????????????????????????????????"

            # source label (small)
            source = e.get("source", "")
            if source:
                src_surf = self.font_text.render(source, True, (0, 0, 0))
                self.screen.blit(src_surf, (bar_rect.x + 12, bar_rect.y + 6))

            # quote text (wrapped)
            max_text_w = bar_rect.w - 24
            lines = self._wrap_text(text, self.font_text, max_text_w)
            # keep at most 2 lines to fit
            lines = lines[:2]
            for i, line in enumerate(lines):
                line_surf = self.font_text.render(line, True, (0, 0, 0))
                self.screen.blit(line_surf, (bar_rect.x + 12, bar_rect.y + 22 + i * 16))

            y += self.entry_h + self.entry_gap

        # Scroll indicator
        if len(entries) > per_page:
            info = f"{self.scroll + 1}-{min(self.scroll + per_page, len(entries))}/{len(entries)}"
            info_surf = self.font_text.render(info, True, (0, 0, 0))
            self.screen.blit(info_surf, (self.box_rect.x + 20, self.box_rect.bottom - 24))
