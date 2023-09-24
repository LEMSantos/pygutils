import os
import sys

import pygame
from pygame.image import load as load_image

from pygutils.sprite import SpriteSheet
from pygutils.animation import Animation

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 400
GAME_FPS = 60
BASE_PATH = os.path.join(os.path.dirname(__file__), "images", "sprite")


def run_animation(screen, animations, delta_time, height):
    idle_surface = animations["idle"].next()
    run_surface = animations["run"].next()
    attack_surface = animations["attack"].next()

    idle_rect = idle_surface.get_rect(center=(quarter_width, height))
    run_rect = run_surface.get_rect(center=(quarter_width * 2, height))
    attack_rect = attack_surface.get_rect(center=(quarter_width * 3, height))

    for animation in animations.values():
        animation.update(delta_time)

    screen.blit(idle_surface, idle_rect)
    screen.blit(run_surface, run_rect)
    screen.blit(attack_surface, attack_rect)


pygame.init()
pygame.display.set_caption("Pygutils Sprite Sheet Example")

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

warrior_surface = load_image(os.path.join(BASE_PATH, "Warrior.png")).convert_alpha()
goblin_surface = load_image(os.path.join(BASE_PATH, "Goblin.png")).convert_alpha()

warrior_sheet = SpriteSheet(warrior_surface, 3, 6)
goblin_sheet = SpriteSheet(goblin_surface, 3, 7)

warrior_animations = {
    "idle": Animation(warrior_sheet.get_surfaces_row(0), 10),
    "run": Animation(warrior_sheet.get_surfaces_row(1), 10),
    "attack": Animation(warrior_sheet.get_surfaces_row(2), 10),
}

goblin_animations = {
    "idle": Animation(goblin_sheet.get_surfaces_row(0), 10),
    "run": Animation(goblin_sheet.get_surfaces_row(1), 10),
    "attack": Animation(goblin_sheet.get_surfaces_row(2), 10),
}

third_height = WINDOW_HEIGHT // 3
quarter_width = WINDOW_WIDTH // 4

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    delta_time = clock.tick(GAME_FPS) / 1000

    screen.fill((255, 255, 255))

    run_animation(screen, warrior_animations, delta_time, third_height)
    run_animation(screen, goblin_animations, delta_time, third_height * 2)

    pygame.display.update()
