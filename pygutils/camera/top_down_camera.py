from operator import attrgetter
from typing import Any, Iterable

from pygame.rect import Rect
from pygame.math import Vector2
from pygame.surface import Surface
from pygame.sprite import AbstractGroup, Group, Sprite


class TopDownCamera(Group):
    def __init__(
        self,
        window_width: int,
        window_height: int,
        bg_surface: Surface | None,
        *sprites: Any | AbstractGroup | Iterable
    ) -> None:
        super().__init__(*sprites)

        self.offset = Vector2(0, 0)
        self.window_width = window_width
        self.window_height = window_height

        self.bg_surface = bg_surface

    def draw(self, surface: Surface, target: Sprite) -> list[Rect]:
        self.offset.x = target.rect.centerx - self.window_width / 2
        self.offset.y = target.rect.centery - self.window_height / 2

        if self.bg_surf is not None:
            surface.blit(self.bg_surface, -self.offset)

        return surface.blits(self.get_visible_sprites(surface), True)

    def get_visible_sprites(self, surface: Surface) -> list[tuple[Surface, Sprite]]:
        surface_rect = surface.get_rect(topleft=self.offset)

        return [
            (sprite.image, sprite.rect.topleft - self.offset)
            for sprite in self.sprites()
            if surface_rect.colliderect(sprite.rect)
        ]

    def sprites(self) -> list[Sprite]:
        return sorted(super().sprites(), key=attrgetter("rect.centery"))
