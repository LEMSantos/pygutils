import sys

import pygame
from pygame.sprite import Sprite
from pygame.surface import Surface

from pygutils.event import EventManager

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400
GAME_FPS = 60


class PlayerMovimentObserver:
    def notify(self, event: str, *args, **kwargs) -> None:
        direction = kwargs.get("direction")
        print("Executa alguma ação quando o player se move na direção:", direction)


class Player(Sprite):
    def __init__(self, position: tuple[int, int], *groups) -> None:
        super().__init__(*groups)

        self.events = EventManager()
        self.font = pygame.font.SysFont("Arial", 20)

        self.image = Surface((100, 50))
        self.image.set_colorkey((0, 255, 0))
        self.rect = self.image.get_rect(center=position)
        self.direction = "up"

    def input(self) -> None:
        pressed_keys = pygame.key.get_pressed()
        keys_map = {
            pygame.K_UP: "up",
            pygame.K_DOWN: "down",
            pygame.K_LEFT: "left",
            pygame.K_RIGHT: "right",
        }

        for key, value in keys_map.items():
            if pressed_keys[key]:
                self.direction = value
                self.events.notify("player:move", direction=self.direction)

    def update(self) -> None:
        self.input()

        text = self.font.render(self.direction, True, (0, 0, 0))
        rect = text.get_rect(
            center=(self.image.get_width() // 2, self.image.get_height() // 2)
        )

        self.image.fill((0, 255, 0))
        self.image.blit(text, rect)


pygame.init()
pygame.display.set_caption("Pygutils Timer Example")

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

player = Player((WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
player.events.subscribe("player:move", PlayerMovimentObserver())

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    clock.tick(GAME_FPS)

    player.update()

    screen.fill((255, 255, 255))
    screen.blit(player.image, player.rect)

    pygame.display.update()
