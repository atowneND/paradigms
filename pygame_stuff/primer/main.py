import sys
import time
import pygame
import math

class GameSpace:
    def main(self):
        # basic initialization
        pygame.init()

        self.size = self.width, self.height = (640, 1024)
        self.black = 0, 0, 0
        self.speed = 4

        self.screen = pygame.display.set_mode(self.size)

        # set up game objects
        self.clock = pygame.time.Clock()

        self.player = Player(self)
        self.enemy = Enemy(self)
        self.laser = Weapon(self)

        # start game loop
        while 1:
            # clock tick regulation
            self.clock.tick(60)

            # handle user inputs
            pygame.event.pump()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                self.player.rect.y  = self.player.rect.y - 1
            if keys[pygame.K_s]:
                self.player.rect.y  = self.player.rect.y + 1
            if keys[pygame.K_d]:
                self.player.rect.x  = self.player.rect.x + 1
            if keys[pygame.K_a]:
                self.player.rect.x  = self.player.rect.x - 1
            if keys[pygame.K_SPACE]:
                self.player.tofire = True
                self.enemy.newhit = True
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # send a tick to every game object
            self.player.tick()
            self.enemy.tick()
            if self.laser.fire == True:
                self.laser.tick()

            # display game objects
            self.screen.fill(self.black)

            if self.enemy.health >= 0:
                self.screen.blit(self.enemy.image, self.enemy.rect)
            else:
                self.enemy.sound.stop()
            self.screen.blit(self.player.image, self.player.rect)
            if self.laser.fire == True:
                self.screen.blit(self.laser.image, self.laser.rect)

            pygame.display.flip()

class Player(pygame.sprite.Sprite):
    def __init__(self,gs=None):
        pygame.sprite.Sprite.__init__(self)

        self.gs = gs
        self.image = pygame.image.load("media/deathstar.png")
        self.rect = self.image.get_rect()
        self.angle = 0

        # keep original image to limit resize errors
        self.orig_image = self.image

        # fire permissions/timing, other properties
        self.tofire = False

    def tick(self):
        # get mouse x and y position on the screen
        mx, my = pygame.mouse.get_pos()

        # compute angle between current direction and mouse position
        theta_mouse = math.atan2(my-self.rect.center[1],mx-self.rect.center[0])
        dtheta = (-(theta_mouse + self.angle)*180/math.pi)/2.
        self.angle = theta_mouse

        # prevents movement while firing
        if self.tofire == True:
            self.gs.laser.fire = True
            self.gs.laser.rect.x = self.rect.center[0] + math.cos(self.angle - math.pi/2)*self.rect.width/4.
            self.gs.laser.rect.y = self.rect.center[1] + math.sin(self.angle - math.pi/2)*self.rect.height/4.
            self.gs.laser.dtheta = self.angle - math.pi/2
            self.tofire = False
        else:
            # rotate the image to face the mouse
            self.image = pygame.transform.rotate(self.orig_image, dtheta)
            self.rect = self.image.get_rect(center=self.rect.center)

class Enemy(pygame.sprite.Sprite):
    def __init__(self,gs=None):
        pygame.sprite.Sprite.__init__(self)

        self.gs = gs
        self.image = pygame.image.load("media/globe.png")
        self.rect = self.image.get_rect()

        self.sound = pygame.mixer.Sound("media/explode.wav")

        # properties
        self.health = 5
        self.rect.x = self.gs.width/2.
        self.rect.y = self.gs.height/2.
        self.radius = self.rect.width/2.
        self.newhit = True

    def tick(self):
        if pygame.sprite.collide_circle(self, self.gs.laser) and self.newhit==True:
            self.health -= 1
            self.newhit = False
            self.gs.laser.fire = False
            self.gs.laser.sound.stop()
            if self.health == 0:
                self.image = pygame.image.load("media/globe_red100.png")
                self.sound.play()

class Weapon(pygame.sprite.Sprite):
    def __init__(self,gs=None):
        pygame.sprite.Sprite.__init__(self)

        self.gs = gs
        self.image = pygame.image.load("media/laser.png")
        self.rect = self.image.get_rect()
        self.fire = False
        self.speed = 6

        self.sound = pygame.mixer.Sound("media/screammachine.wav")

    def tick(self):
        self.rect.x += self.speed*math.cos(self.dtheta+math.pi/2)
        self.rect.y += self.speed*math.sin(self.dtheta+math.pi/2)
        self.sound.play()

if __name__ == '__main__':
    gs = GameSpace()
    gs.main()
