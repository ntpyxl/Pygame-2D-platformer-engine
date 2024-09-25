import pygame
from sys import exit

from classes import Player, Platform

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
    player = Player(100, 20)
    playerSprites = pygame.sprite.GroupSingle()
    playerSprites.add(player)

    platforms = pygame.sprite.Group()
    platforms.add(Platform(20, 400, 340, 40))
    platforms.add(Platform(380, 400, 340, 40))
    platforms.add(Platform(380, 270, 340, 40))
    #platforms.add(Platform(440, 100, 40, 400))

    while True:
        clock.tick(60)
        quitGame()

        userInput = pygame.key.get_pressed()

        window.fill((30, 30, 30))

        # DRAW OBJECTS
        playerSprites.draw(window)
        platforms.draw(window)

        # UPDATE OBJECTS
        player.update(userInput)

        platformCollision = pygame.sprite.spritecollide(playerSprites.sprites()[0], platforms, False)
        if platformCollision:
            player.inAir = False

            # top platform detection
            if player.rect.bottom > platformCollision[0].rect.top and player.rect.bottom < platformCollision[0].rect.top + 20 and player.rect.bottom < platformCollision[0].rect.bottom - 24:
                player.rect.y -= player.rect.bottom - platformCollision[0].rect.top
                player.jumped = False
                player.gravity = 4
            
            # bottom platform detection
            if player.rect.top < platformCollision[0].rect.bottom and player.rect.top > platformCollision[0].rect.bottom - 20 and player.rect.top > platformCollision[0].rect.top + 24:
                player.rect.y -= player.rect.top - platformCollision[0].rect.bottom
                player.jumpVelocity = 0
                player.gravity = 4

            # left platform detection
            if player.rect.right > platformCollision[0].rect.left and player.rect.right < platformCollision[0].rect.left + 20 and player.rect.left < platformCollision[0].rect.left - 24:
                player.rect.x -= player.rect.right - platformCollision[0].rect.left

            # right platform detection
            if player.rect.left < platformCollision[0].rect.right and player.rect.right > platformCollision[0].rect.right - 20 and player.rect.right > platformCollision[0].rect.right + 24:
                player.rect.x -= player.rect.left - platformCollision[0].rect.right
        else:
            player.inAir = True

        pygame.display.update()

main()