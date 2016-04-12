import sys
import time
import pygame
import math
import glob

class GameSpace:
    def main(self):
        # basic initialization
        pygame.init()

        self.size = self.width, self.height = (640, 1024)
        self.black = 0, 0, 0
        self.laser = []

        self.screen = pygame.display.set_mode(self.size)

        # set up game objects
        self.clock = pygame.time.Clock()

        self.player = Player(self)
        self.enemy = Enemy(self)
        self.explosion = Explosion(self)
        self.weapon_sound = pygame.mixer.Sound("media/screammachine.wav")

        # start game loop
        while 1:
            # clock tick regulation
            self.clock.tick(60)

            # handle user inputs
            pygame.event.pump()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                self.player.rect.y  = self.player.rect.y - self.player.speed
            if keys[pygame.K_s]:
                self.player.rect.y  = self.player.rect.y + self.player.speed
            if keys[pygame.K_d]:
                self.player.rect.x  = self.player.rect.x + self.player.speed
            if keys[pygame.K_a]:
                self.player.rect.x  = self.player.rect.x - self.player.speed
            if keys[pygame.K_SPACE]:
                self.player.tofire = True # should be able to delete this later
                self.laser.append(Weapon(self))
                self.weapon_sound.play()
            else:
                self.weapon_sound.stop()
                self.player.tofire = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # tick and display
            self.screen.fill(self.black)

            # player
            self.player.tick()
            self.screen.blit(self.player.image, self.player.rect)

            # enemy
            self.enemy.tick()
            if self.enemy.health > 0:
                # weapon
                for i in self.laser:
                    i.tick()
                    if i.fire == True:
                        self.screen.blit(i.image, i.rect)
                    elif i.fire == False:
                        del i
                self.screen.blit(self.enemy.image, self.enemy.rect)
            else:
                self.explosion.tick()
                if self.explosion.earth_disappears == False:
                    self.screen.blit(self.enemy.image, self.enemy.rect)
                else:
                    pass
                self.screen.blit(self.explosion.image, self.explosion.rect)
                self.enemy.sound.stop()
                pass

            pygame.display.flip()

class Player(pygame.sprite.Sprite):
    def __init__(self,gs=None):
        pygame.sprite.Sprite.__init__(self)

        self.gs = gs
        self.image = pygame.image.load("media/deathstar.png")
        self.rect = self.image.get_rect()
        self.angle = 0
        self.speed = 4

        # keep original image to limit resize errors
        self.orig_image = self.image

        # fire permissions/timing, other properties
        self.tofire = False

    def tick(self):
        # get mouse x and y position on the screen
        mx, my = pygame.mouse.get_pos()

        # prevents movement while firing
        if self.tofire == True:
            pass
        else:
            # compute angle between current direction and mouse position
            theta_mouse = math.atan2(my-self.rect.center[1],mx-self.rect.center[0])
            dtheta = (-(theta_mouse + self.angle)*180/math.pi)/2. - 45.
            self.angle = theta_mouse

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
        self.health = 100
        self.rect.x = self.gs.width/2.
        self.rect.y = self.gs.height/2.
        self.radius = self.rect.width/2.

    def tick(self):
        print self.health
        if self.health <= 0:
            self.image = pygame.image.load("media/globe_red100.png")
            self.sound.play()
        else:
            self.image = pygame.image.load("media/globe_red100.png")
            time.sleep(0.1)
            self.image = pygame.image.load("media/globe.png")


class Weapon(pygame.sprite.Sprite):
    def __init__(self,gs=None):
        pygame.sprite.Sprite.__init__(self)

        self.gs = gs
        self.image = pygame.image.load("media/laser.png")
        self.rect = self.image.get_rect()

        # geometry
        self.speed = 6
        self.rect.x = self.gs.player.rect.center[0] + math.cos(self.gs.player.angle)*self.gs.player.rect.width/4.
        self.rect.y = self.gs.player.rect.center[1] + math.sin(self.gs.player.angle)*self.gs.player.rect.height/4.
        self.dtheta = self.gs.player.angle - math.pi/2

        # other properties
        self.fire = True

    def tick(self):
        self.rect.x += self.speed*math.cos(self.dtheta+math.pi/2)
        self.rect.y += self.speed*math.sin(self.dtheta+math.pi/2)
        if pygame.sprite.collide_circle(self.gs.enemy, self) and self.fire==True:
            self.gs.enemy.health -= 1
            self.fire = False

class Explosion(pygame.sprite.Sprite):
    def __init__(self,gs=None):
        pygame.sprite.Sprite.__init__(self)

        self.gs = gs
        self.flist = sorted(glob.glob("media/explosion/*.png"))
        self.findex = 0
        self.image = pygame.image.load(self.flist[self.findex])
        self.size = self.image.get_size()
        self.image = pygame.transform.scale(self.image, (int(self.size[0]*2), int(self.size[1]*2)))
        self.rect = self.image.get_rect()
        self.rect.x = self.gs.width/2.
        self.rect.y = self.gs.height/2.
        self.earth_disappears = False

    def tick(self):
        if self.findex<len(self.flist)-1:
            self.image = pygame.image.load( self.flist[self.findex])
            self.size = self.image.get_size()
            self.image = pygame.transform.scale(self.image, (int(self.size[0]*2), int(self.size[1]*2)))
            time.sleep(0.25)
            self.findex += 1
            if self.findex>0.6*(len(self.flist)-1):
                self.earth_disappears = True
        else:
            pass

if __name__ == '__main__':
    gs = GameSpace()
    gs.main()
