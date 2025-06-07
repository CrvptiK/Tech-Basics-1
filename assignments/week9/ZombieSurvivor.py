#%%
#time: 4 hours
#found a great tutorial by coding with russ, which i will use as a support for this, i will change the code so my game is less of a platformer and more like vampire survivor

import pygame
import random

pygame.init()

#constants
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)
FPS = 60

WHITE = (255, 255, 255)
RED = (255, 0, 0)

#now we need a screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("ZombieSurvivor")
clock = pygame.time.Clock()

#adding a downloaded font for more spooky theme
font_path = "BloodCrow-GdXg.ttf"
font = pygame.font.Font(font_path, 36)
title_font = pygame.font.Font(font_path, 64)

#setting the bounds for the start button to later check if it is clicked
button_width, button_height = 200, 60

def get_start_button_rect():
    instructions = [
        "Escape from the Horde!",
        "Collect Diamonds to increase Speed",
        "W, A, S, D or arrow keys to move",
        "Click the Start Button to Begin"
    ]
    start_y = SCREEN_HEIGHT // 2 - 80
    line_height = font.get_height() + 5
    instructions_bottom = start_y + len(instructions) * line_height
    button_y = instructions_bottom + 20
    button_x = SCREEN_WIDTH // 2 - button_width // 2
    return pygame.Rect(button_x, button_y, button_width, button_height)

#sprites creation and putting it as a class

#general sprite class
class Character(pygame.sprite.Sprite):
    def __init__(self, x, y, scale, image_path):
        super().__init__()
        img = pygame.image.load(image_path)
        self.image = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
        self.rect = self.image.get_rect(center=(x, y))
        self.__health = 100

    def render(self, surface):
        surface.blit(self.image, self.rect)

    def get_health(self):
        return self.__health

    def set_health(self, new_health):
        self.__health = max(0, min(100, new_health))

#class for player
class Player(Character):
    def __init__(self, x, y, scale):
        super().__init__(x, y, scale, 'Zombie.png')
        self.speed = 5

    def move(self, keys):
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x = max(0, self.rect.x - self.speed)
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x = min(SCREEN_WIDTH - self.rect.width, self.rect.x + self.speed)
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.rect.y = max(0, self.rect.y - self.speed)
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.rect.y = min(SCREEN_HEIGHT - self.rect.height, self.rect.y + self.speed)

#class for enemy
class EnemyZombie(Character):
    def __init__(self, x, y, scale):
        super().__init__(x, y, scale, 'Enemy.png')
        self.speed = 2

#i had a few problems preventing the enemy from moving through the player, so i googled for some fixes)
    def follow(self, target):
        dx = target.rect.x - self.rect.x
        dy = target.rect.y - self.rect.y
        dist = max(1, (dx ** 2 + dy ** 2) ** 0.5)
        self.rect.x += int(self.speed * dx / dist)
        self.rect.y += int(self.speed * dy / dist)

class Diamond(pygame.sprite.Sprite):
    def __init__(self, x, y, scale=1):
        super().__init__()
        img = pygame.image.load('diamond.png')  # Make sure you have this image file!
        self.image = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
        self.rect = self.image.get_rect(center=(x, y))

    def render(self, surface):
        surface.blit(self.image, self.rect)

#player
player = Player(400, 300, 2)
#zombies and diamond groups
zombies = pygame.sprite.Group()
diamonds = pygame.sprite.Group()

#timers and counts
diamond_spawn_timer = 0
diamond_count = 0

damage_timer = 0

survival_time = 0
last_speed_increase = 0
highscore = 0

#enemy spawn, with buffer so it doesnt spawn on top of the character (suggestion by chatgpt while improving my code with its help)
def spawn_zombie():
    while True:
        x = random.randint(0, SCREEN_WIDTH)
        y = random.randint(0, SCREEN_HEIGHT)
        if abs(x - player.rect.x) > 100 and abs(y - player.rect.y) > 100:
            break
    zombies.add(EnemyZombie(x, y, 1.5))

def spawn_diamond():
    while True:
        x = random.randint(0, SCREEN_WIDTH)
        y = random.randint(0, SCREEN_HEIGHT)
        if abs(x - player.rect.x) > 50 and abs(y - player.rect.y) > 50:
            break
    diamonds.add(Diamond(x, y, 1))

game_active = False

def draw_start_screen():
    screen.fill((0, 0, 0))

    #why is the title causing such problems wtf)
    title = title_font.render("ZombieSurvivor", True, RED)
    title_pos = (SCREEN_WIDTH // 2 - title.get_width() // 2, SCREEN_HEIGHT // 3 - 140)
    screen.blit(title, title_pos)

    #game tutorial
    instructions = [
        "Escape from the Horde!",
        "Collect Diamonds to increase Speed",
        "W, A, S, D or arrow keys to move",
        "Click the Start Button to Begin"
    ]
    start_y = SCREEN_HEIGHT // 2 - 80
    line_height = font.get_height() + 5
    for i, line in enumerate(instructions):
        text_surface = font.render(line, True, WHITE)
        screen.blit(text_surface, (SCREEN_WIDTH // 2 - text_surface.get_width() // 2, start_y + i * line_height))

    # button shenanigans
    button_rect = get_start_button_rect()
    mouse_pos = pygame.mouse.get_pos()
    if button_rect.collidepoint(mouse_pos):
        button_color = (170, 170, 170)
    else:
        button_color = (100, 100, 100)
    pygame.draw.rect(screen, button_color, button_rect)

    start_text = font.render("START", True, WHITE)
    screen.blit(start_text, (button_rect.x + button_rect.width // 2 - start_text.get_width() // 2,
                             button_rect.y + button_rect.height // 2 - start_text.get_height() // 2))

    pygame.display.update()

#variables as global, thus outside the def
button_width, button_height = 200, 60
button_x = SCREEN_WIDTH//2 - button_width//2

#of course we need a game over screen
def draw_game_over():
    screen.fill((10, 0, 0))
    game_over_text = font.render("GAME OVER", True, RED)
    restart_text = font.render("Press [R] to Restart or [ESC] to Quit", True, WHITE)
    survival_text = font.render(f"Survived: {int(survival_time)} seconds", True, WHITE)
    highscore_text = font.render(f"Highscore: {int(highscore)} seconds", True, WHITE)

    screen.blit(game_over_text, (SCREEN_WIDTH//2 - game_over_text.get_width()//2, SCREEN_HEIGHT//2 - 80))
    screen.blit(survival_text, (SCREEN_WIDTH//2 - survival_text.get_width()//2, SCREEN_HEIGHT//2 - 30))
    screen.blit(highscore_text, (SCREEN_WIDTH//2 - highscore_text.get_width()//2, SCREEN_HEIGHT//2 + 10))
    screen.blit(restart_text, (SCREEN_WIDTH//2 - restart_text.get_width()//2, SCREEN_HEIGHT//2 + 50))
    pygame.display.update()

game_state = "start"

#main loop
spawn_timer = 0
run = True
while run:
    clock.tick(FPS)
    events = pygame.event.get()

    if game_state == "start":
        draw_start_screen()
        for event in events:
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left click
                mouse_pos = event.pos
                if get_start_button_rect().collidepoint(mouse_pos):
                    pygame.time.wait(100)
                    game_state = "playing"
                    pygame.event.clear()

#the following block was a bit of a pain honestly
    elif game_state == "playing":
        screen.fill((30, 30, 30))
        for event in events:
            if event.type == pygame.QUIT:
                run = False
        damage_timer += 1
        survival_time += clock.get_time() / 1000
        if survival_time - last_speed_increase >= 30:
            for zombie in zombies:
                zombie.speed += 0.8
            last_speed_increase = survival_time

        #id like to move it move it
        keys = pygame.key.get_pressed()
        player.move(keys)
        player.render(screen)

        #diamond spawning logic
        diamond_spawn_timer += 1
        if diamond_spawn_timer >= 180:
            spawn_diamond()
            diamond_spawn_timer = 0

        for diamond in diamonds:
            diamond.render(screen)

        #diamond collection counter
        collected = pygame.sprite.spritecollide(player, diamonds, True)
        if collected:
            diamond_count += len(collected)
            #speed increase when enough diamonds are collected
            if diamond_count % 10 == 0:
                player.speed += 1

        #zombie spawning logic
        spawn_timer += 1
        if spawn_timer >= 120:
            spawn_zombie()
            spawn_timer = 0

        for zombie in zombies:
            zombie.follow(player)
            zombie.render(screen)

            if zombie.rect.colliderect(player.rect) and damage_timer >= 30:
                player.set_health(player.get_health() - 10)
                damage_timer = 0

        #game end and highscore
        if player.get_health() <= 0:
            if survival_time > highscore:
                highscore = survival_time
            game_state = "game_over"

        #health bar :))
        health_text = font.render(f'Health: {player.get_health()}', True, RED)
        screen.blit(health_text, (10, 10))

        #diamond count and speed count display
        diamond_text = font.render(f'Diamonds: {diamond_count}', True, WHITE)
        speed_text = font.render(f'Speed: {player.speed}', True, WHITE)
        screen.blit(diamond_text, (10, 40))
        screen.blit(speed_text, (10, 70))

        pygame.display.update()

    elif game_state == "game_over":
        draw_game_over()
        for event in events:
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    player = Player(400, 300, 2)
                    zombies.empty()
                    survival_time = 0
                    diamond_count = 0
                    player.speed = 5
                    diamonds.empty()
                    game_state = "playing"
                elif event.key == pygame.K_ESCAPE:
                    run = False

pygame.quit()



#the game is based on vampire survivor
#you as the player try and survive a horde of monsters, while collecting points to power up
#this is a much simpler version
