#time: surprisingly only like 2 hours         tears: countless at this point lmao
#what do you mean 3.13 is not supported by pygame, imma loose my----- time to install a new version fml
#ive been troubleshootin this bs for like half an hour now, and NOW i figured that out, are you serious?! T-T
#bro this is bs, it runs in the terminal but not here, imma cry
#FINALLY omg

import pygame
import sys
import random
import math

#time for some youtube tutorials as i was sick and couldnt come to class
#watch me, i can do this (while crying maybe but we shall see)
pygame.init()

#lets create a nice big screen to have a nice view of the incoming chaos
SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 900
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pygame Animated Image")

#the guy in the vid made his image jitter and rotate but my eyes hated that so instead i decided to attempt an impression of my beloved dvd idle screen
class AnimatedImage:
    def __init__(self, path, x, y, speed_x, speed_y):
        original = pygame.image.load(path)
        original = pygame.transform.scale(original, (400, 400))
        self.original_image = original
        self.color = (255, 255, 255)
        self.image = self.tint_image(self.original_image, self.color)
        self.rect = self.image.get_rect(center=(x, y))
        self.speed_x = speed_x
        self.speed_y = speed_y

        self.scale_factor = 1.0
        self.scale_direction = 1

        self.bounced_x = False
        self.bounced_y = False

    def tint_image(self, image, color):
        tinted = image.copy()
        tinted.fill(color + (0,), special_flags=pygame.BLEND_RGB_MULT)
        return tinted

    def randomize_color(self):
        self.color = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
        self.image = self.tint_image(self.original_image, self.color)

    def chaotic_movement(self):
        self.speed_x += random.uniform(-0.5, 0.5)
        self.speed_y += random.uniform(-0.5, 0.5)

        self.speed_x = max(min(self.speed_x, 10), -10)
        self.speed_y = max(min(self.speed_y, 10), -10)

        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        bounced_this_frame = False

        #for this following block i used chatgpt (bc i had a plan but no idea how to code it (or rather my attempts continued to break the code yippie....))
        #the following blocks ensure that the colour change only happens when the image ACTUALLY hits the borders and not vaguely touches it
        if self.rect.left <= 0:
            if not self.bounced_x:
                self.speed_x *= -1
                self.speed_x += random.uniform(-2, 2)
                bounced_this_frame = True
            self.bounced_x = True
            self.rect.left = 0

        elif self.rect.right >= SCREEN_WIDTH:
            if not self.bounced_x:
                self.speed_x *= -1
                self.speed_x += random.uniform(-2, 2)
                bounced_this_frame = True
            self.bounced_x = True
            self.rect.right = SCREEN_WIDTH

        else:
            self.bounced_x = False

        if self.rect.top <= 0:
            if not self.bounced_y:
                self.speed_y *= -1
                self.speed_y += random.uniform(-2, 2)
                bounced_this_frame = True
            self.bounced_y = True
            self.rect.top = 0

        elif self.rect.bottom >= SCREEN_HEIGHT:
            if not self.bounced_y:
                self.speed_y *= -1
                self.speed_y += random.uniform(-2, 2)
                bounced_this_frame = True
            self.bounced_y = True
            self.rect.bottom = SCREEN_HEIGHT

        else:
            self.bounced_y = False

        if bounced_this_frame:
            self.randomize_color()

    #this is something the guy in the vid explained but i disliked the size caps he chose and decided to make it more subtle
    def chaotic_transform(self):
        self.scale_factor += 0.01 * self.scale_direction
        if self.scale_factor > 1.05 or self.scale_factor < 0.95:
            self.scale_direction *= -1

        scaled = pygame.transform.rotozoom(self.original_image, 0, self.scale_factor)
        self.image = self.tint_image(scaled, self.color)
        center = self.rect.center
        self.rect = self.image.get_rect(center=center)

    def update(self):
        self.chaotic_movement()
        self.chaotic_transform()

    def draw(self, surface):
        surface.blit(self.image, self.rect)

#framerate (my enemy in every video game setting screen jk jk xD)
clock = pygame.time.Clock()

#from a different youtube tutorial, the youtuber created like 20 copies of their image which was funny but too much for me, so i went with 6 instead
sprites = []
for _ in range(6):
    x = random.randint(200, SCREEN_WIDTH - 200)
    y = random.randint(200, SCREEN_HEIGHT - 200)
    speed_x = random.uniform(1, 4) * random.choice([-1, 1])
    speed_y = random.uniform(1, 4) * random.choice([-1, 1])
    sprites.append(AnimatedImage("Marcid.png", x, y, speed_x, speed_y))

#looooooooooop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((30, 30, 30))  # dark grey, my favourite colour (jk) (did i google 'dark grey background colour most often used on digital interfaces'? yes. did i feel stupid cuz its literally just 30, 30, 30? also yes.)

    for sprite in sprites:
        sprite.update()
        sprite.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
#did i stare at this for like 10 mins without blinking like my child self did with the dvd idle screen? yes. yes i did. do i regret it? no. no i dont