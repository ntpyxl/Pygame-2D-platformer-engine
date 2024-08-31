import pygame
from sys import exit

from classes import Player

pygame.init()
clock = pygame.time.Clock()

windowSize = (800, 600)
window = pygame.display.set_mode(windowSize)
pygame.display.set_caption("Pygame 2D Platformer")

def quitGame():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

def main():
    player = pygame.sprite.GroupSingle()
    player.add(Player(100, 250))

    while True:
        clock.tick(60)
        quitGame()

        userInput = pygame.key.get_pressed()

        window.fill((30, 30, 30))

        # DRAW OBJECTS
        player.draw(window)

        # UPDATE OBJECTS
        player.update(userInput)

        pygame.display.update()

main()