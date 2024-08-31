import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, spawnPosX: int, spawnPosY: int):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([30, 60])
        self.image.fill((200, 200, 200))
        self.rect = self.image.get_rect()
        self.rect.center = spawnPosX, spawnPosY
        self.rect.x, self.rect.y = self.rect.center

    def update(self, userInput):
        # PHYSICS

        # CONTROLS
        if userInput[pygame.K_w]:
            self.rect.y -= 4
        if userInput[pygame.K_s]:
            self.rect.y += 4
        if userInput[pygame.K_a]:
            self.rect.x -= 4
        if userInput[pygame.K_d]:
            self.rect.x += 4