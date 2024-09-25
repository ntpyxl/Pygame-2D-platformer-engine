import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, spawnPosX: int, spawnPosY: int):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([30, 60])
        self.image.fill((200, 200, 200))
        self.rect = self.image.get_rect()
        self.rect.center = spawnPosX, spawnPosY
        self.rect.x, self.rect.y = self.rect.center

        self.inAir = True
        self.maxGravity = 10
        self.gravity = 4
        self.jumpVelocity = 0
        self.jumped = True

    def update(self, userInput):
        # PHYSICS
        if not self.jumped and self.inAir:
            self.rect.y += self.gravity
            if self.gravity != 10:
                self.gravity += 0.5
        if self.jumped:
            self.rect.y += self.jumpVelocity
            if self.jumpVelocity < self.maxGravity:
                self.jumpVelocity += 0.5

        # CONTROLS
        if userInput[pygame.K_w] and not self.jumped and self.gravity == 4:
                self.jumpVelocity = -12
                self.jumped = True
        if userInput[pygame.K_a]:
            self.rect.x -= 4
        if userInput[pygame.K_d]:
            self.rect.x += 4

class Platform(pygame.sprite.Sprite):
    def __init__(self, posX: int, posY: int, width: int, length: int):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, length])
        self.image.fill((90, 200, 120))
        self.rect = self.image.get_rect()
        self.rect.center = posX, posY
        self.rect.x, self.rect.y = self.rect.center