import sys

import pygame

from pygutils.timer import Timer

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400
GAME_FPS = 60

pygame.init()
pygame.display.set_caption("Pygutils Timer Example")

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 24)

increment_timer = Timer(1000)
call_count = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    clock.tick(GAME_FPS)

    screen.fill((255, 255, 255))

    if not increment_timer.active:
        call_count += 1
        increment_timer.activate()

    increment_timer.update()

    text_surface = font.render(
        f"O timer foi ativado {call_count} vezes", True, (0, 0, 0)
    )
    text_rect = text_surface.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))

    screen.blit(text_surface, text_rect)
    pygame.display.update()
