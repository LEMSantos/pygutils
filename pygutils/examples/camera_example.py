"""Use the directional keys to move the player around the map.
"""

import os
import sys

import pygame
from pygame.sprite import Sprite
from pygame.math import Vector2

from pygutils.camera import TopDownCamera

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
GAME_FPS = 60
BASE_PATH = os.path.join(os.path.dirname(__file__), "images", "camera")


class Player(Sprite):
    def __init__(self, position: tuple[int, int], *groups) -> None:
        super().__init__(*groups)

        self.image = pygame.image.load(
            os.path.join(BASE_PATH, "player.png")
        ).convert_alpha()
        self.rect = self.image.get_rect(center=position)

        self.direction = Vector2(0, 0)
        self.pos = Vector2(position)
        self.speed = 200

    def input(self) -> None:
        pressed_keys = pygame.key.get_pressed()
        keys_map = {
            pygame.K_UP: Vector2(0, -1),
            pygame.K_DOWN: Vector2(0, 1),
            pygame.K_LEFT: Vector2(-1, 0),
            pygame.K_RIGHT: Vector2(1, 0),
        }

        self.direction = Vector2(0, 0)

        for key, value in keys_map.items():
            if pressed_keys[key]:
                self.direction += value

    def move(self, delta_time: float) -> None:
        self.pos += self.direction * self.speed * delta_time
        self.rect.center = (round(self.pos.x), round(self.pos.y))

    def update(self, delta_time: float) -> None:
        self.input()
        self.move(delta_time)


pygame.init()
pygame.display.set_caption("Pygutils Camera Example")

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

bg_surface = pygame.image.load(os.path.join(BASE_PATH, "bg.png")).convert()

player = Player((WINDOW_WIDTH, WINDOW_HEIGHT))
all_sprites = TopDownCamera(bg_surface, player)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    delta_time = clock.tick(GAME_FPS) / 1000

    all_sprites.update(delta_time)

    screen.fill((0, 0, 0))
    all_sprites.draw(screen, player)

    pygame.display.update()
