# hours spent crying over this: currently 1,5 (wow, im actually getting better at this)
# for now, i will write the code structure in this file, once i dive in really deep to make this game,
# i will take some time to modularise everything, for example an asset directory with the art and such, also sound and co ofc
# a directory for the classes and the def functions and everything else, neatly seperated
# right now though, lets just write some code

# first imports

import pygame
import sys

# le global functions (currently 1)

TILE_SIZE = 64

# alright, onto classes, this should be well possible, looking at my classes from zombie survivor as guidance

class Player:
    def __init__(self, x, y):
        self.image = pygame.Surface((32, 32))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 3

    def handle_input(self, keys, obstacles):
        dx = dy = 0
        if keys[pygame.K_w]:
            dy = -self.speed
        if keys[pygame.K_s]:
            dy = self.speed
        if keys[pygame.K_a]:
            dx = -self.speed
        if keys[pygame.K_d]:
            dx = self.speed

        future_rect = self.rect.move(dx, 0)
        if not any(future_rect.colliderect(obj.rect if hasattr(obj, "rect") else obj) for obj in obstacles):
            self.rect.x += dx

        future_rect = self.rect.move(0, dy)
        if not any(future_rect.colliderect(obj.rect if hasattr(obj, "rect") else obj) for obj in obstacles):
            self.rect.y += dy

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class NPC:
    def __init__(self, x, y, message=None):
        self.image = pygame.Surface((32, 32))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.message = message
        self.interacted = False

    def interact(self):
        if self.message:
            print(f"{self.message}")
            self.interacted = True

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Enemy:
    def __init__(self, x, y):
        self.image = pygame.Surface((32, 32))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(topleft=(x, y))

    def draw(self, surface):
        surface.blit(self.image, self.rect)

# besides te characters, i want to implement rooms (in tiles), for this lets create a class and some placeholder tiles

class Room:
    def __init__(self, tilemap, npcs=None, enemies=None):
        self.tilemap = tilemap
        self.npcs = npcs if npcs else []
        self.enemies = enemies if enemies else []
        self.walls = self.generate_walls()

    def generate_walls(self):
        walls = []
        for row_index, row in enumerate(self.tilemap):
            for col_index, tile in enumerate(row):
                if tile == "#":
                    wall_rect = pygame.Rect(
                        col_index * TILE_SIZE,
                        row_index * TILE_SIZE,
                        TILE_SIZE,
                        TILE_SIZE
                    )
                    walls.append(wall_rect)
        return walls


class RoomManager:
    def __init__(self):
        self.rooms = {}
        self.current_coords = (0, 0)
        self.load_rooms()

    def load_rooms(self):
        room_0_npcs = []
        room_0_enemies = []
        tilemap_0 = [
            "################",
            "#..............#",
            "#..##..........#",
            "#..............#",
            "#......####....#",
            "#..............#",
            "################"
        ]

        # this is kinda testing but considering these maps will be changed once the graphics are added anyway, it hardly matters

        if tilemap_0[1][3] == '.':
            room_0_npcs.append(NPC(3 * TILE_SIZE, 1 * TILE_SIZE, "placeholder"))

        self.rooms[(0, 0)] = Room(tilemap_0, npcs=room_0_npcs, enemies=room_0_enemies)

        room_1_npcs = []
        room_1_enemies = []
        tilemap_1 = [
            "################",
            "...............#",
            ".....#####.....#",
            "...............#",
            "...####........#",
            "...............#",
            "################"
        ]

        if tilemap_1[1][2] == '.':
            room_1_npcs.append(NPC(2 * TILE_SIZE, 1 * TILE_SIZE, "placeholder"))
        if tilemap_1[2][1] == '.':
            room_1_enemies.append(Enemy(1 * TILE_SIZE, 2 * TILE_SIZE))

        self.rooms[(1, 0)] = Room(tilemap_1, npcs=room_1_npcs, enemies=room_1_enemies)

    def get_current_room(self):
        return self.rooms[self.current_coords]

    def transition(self, direction):
        x, y = self.current_coords
        if direction == "right":
            self.current_coords = (x + 1, y)
        elif direction == "left":
            self.current_coords = (x - 1, y)
        elif direction == "up":
            self.current_coords = (x, y - 1)
        elif direction == "down":
            self.current_coords = (x, y + 1)

# we need some general functions
# lets start with collision detection

def check_collision(a, b):
    return a.rect.colliderect(b.rect)

# something i want to implement is the player being able to walk out of one (or multiple) end(s) of the screen and move to the next part of the map/tile
# thanks to a youtube tutorial, i was able to write this

def handle_room_transition(player, room_manager, width, height):
    new_coords = list(room_manager.current_coords)
    if player.rect.right > width:
        new_coords[0] += 1
        player.rect.left = 0
    elif player.rect.left < 0:
        new_coords[0] -= 1
        player.rect.right = width
    elif player.rect.top < 0:
        new_coords[1] -= 1
        player.rect.bottom = height
    elif player.rect.bottom > height:
        new_coords[1] += 1
        player.rect.top = 0
    else:
        return

    new_coords = tuple(new_coords)
    if new_coords in room_manager.rooms:
        room_manager.current_coords = new_coords
    else:
        print("placeholder, exit game")
        pygame.quit()
        sys.exit()

# next, we move on to adding some npcs and the player onto the screen ofc, using coords

player = Player(100, 100)
npcs = [
    NPC(200, 150, message="placeholder"),
    NPC(300, 300, message="placeholder")
]
enemies = [
    Enemy(400, 200)
]

current_room = (0, 0)

# and ofc the main game loop

def main():
    pygame.init()
    WIDTH, HEIGHT = 640, 480
    TILE_SIZE = 64
    WHITE = (255, 255, 255)
    FPS = 60

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Story-Based Game")
    clock = pygame.time.Clock()

    room_manager = RoomManager()
    player = Player(100, 100)

    while True:
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    for npc in room_manager.get_current_room().npcs:
                        if player.rect.colliderect(npc.rect.inflate(10, 10)):
                            npc.interact()
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        current_room = room_manager.get_current_room()
        obstacles = current_room.walls + current_room.npcs + current_room.enemies
        player.handle_input(keys, obstacles)

        handle_room_transition(player, room_manager, WIDTH, HEIGHT)

        screen.fill(WHITE)

        for wall in current_room.walls:
            pygame.draw.rect(screen, (100, 100, 100), wall)
        for npc in current_room.npcs:
            npc.draw(screen)
        for enemy in current_room.enemies:
            enemy.draw(screen)

        player.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()


# this of course is still very very barebones, it will all come together once i thought about the game features
# i spent around 2 hours after this just planning some game features, like title screen, menu, esc menu, some different fonts, i looked at some libraries and github repos for inspo
# but for now, this is some good first reference for my final assignment, for now still a bit simple, but seeing as i will be greatly expanding this, it should turn out just fine