import os
import sys

import pygame
from pygame.sprite import Sprite
from pygame.surface import Surface

from pygutils.animation import Animation

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400
GAME_FPS = 60


def get_surfaces() -> list[Surface]:
    path = os.path.join(os.path.dirname(__file__), "images", "animation")

    return [
        pygame.image.load(os.path.join(path, image)).convert_alpha()
        for image in sorted(os.listdir(path))
    ]


class AnimatedSprite(Sprite):
    def __init__(
        self, frames_sequence: list[Surface], position: tuple[int, int], *groups
    ) -> None:
        super().__init__(*groups)

        self.image = frames_sequence[0]
        self.rect = self.image.get_rect(center=position)

        self.animation = Animation(frames_sequence, 8)

    def update(self, delta_time: float) -> None:
        self.animation.update(delta_time)

        self.image = self.animation.next()
        self.rect = self.image.get_rect(center=self.rect.center)


pygame.init()
pygame.display.set_caption("Pygutils Animation Example")

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

animated_sprite = AnimatedSprite(
    frames_sequence=get_surfaces(),
    position=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2),
)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    delta_time = clock.tick(GAME_FPS) / 1000

    screen.fill((255, 255, 255))

    animated_sprite.update(delta_time)
    screen.blit(animated_sprite.image, animated_sprite.rect)

    pygame.display.update()
