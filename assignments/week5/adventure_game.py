#%%
#hours (and tears) spent fighting with this: 6

#imports
import os

#id like to give some text the typewriter effect so lets try to remember how that worked
import sys
import time

#and to be able to test this stuff without loosing my mind, lets add this
TEST_MODE = False

# Global variables
INVENTORY = []
INVENTORY_LIMIT = 5
DALEK = r"""
                              π∞∞≈√                           ∞∞
                              √√∞√√≈√√π∞∞√     π             √√≈∞
                               ∞√≠∞∞πππ≈∞√√π π√≠  √∞ √     √√πππ
                                     π∞≈≈ππ√∞≠≠=∞π≠  ∞π     √≈≈∞
                                             ∞π∞√∞√π  ≈
                                          √  ππ√∞∞∞≈∞√∞ π
                                          √√≠≠√π√∞≈≠∞=≠≈∞∞∞√√∞≈≈∞π
                                         π≠≈≠=≠≈∞∞√∞π≈√√√√√∞∞≠=≠∞≠≈
                                        √√√∞∞∞ππ  π∞π≈πππππ√∞∞∞ππ∞∞∞π
                                          √≈≠≠≠≠≠∞∞∞∞∞√∞∞∞≠≠≠=≠∞∞≠∞
                                        ∞∞∞∞≈∞     ∞ ∞      √∞≠π ∞≠≠√
                                           ≈≠√√∞∞≈≠=≠≠≈≈≈≈∞∞√≈≠ππ∞∞
                                        π∞∞∞∞∞√√√√√√√√√√∞√√∞√√∞∞∞∞√π
                                       √√∞ √  √∞≈≈≠√∞√≠≈∞π√∞ ππ∞π√∞π
            π≠∞                        ππ∞π∞√√∞√≠√≈∞√∞∞√∞ππ∞   ∞ ππ√
           √√√≠÷π                     π √ ππ√√ ≈√ ∞√ ∞π ∞√ ∞   ∞  π
            ≈π≈=∞≈π√                    ∞π ∞≈≠≠≠  ∞≈√≠π ≈∞∞≈∞π π√√π√
           π≈√=∞≠≈π≠∞ππ√πππ  π    π∞∞≠=≠≠∞≠≠≠≈≠=≠≠≈≈∞∞≠≠=∞≈∞≈ππ ≈√ ∞
           √≠≈∞           √ π∞≠≠∞√∞∞≈÷≈∞∞≠≠≠≠∞≈=≠≈≠×≈∞∞√×≠= ≈ ∞ ∞π√∞ππ
                                  √∞√÷≠∞≠∞∞≠≠≠  √≠×÷≠∞÷≈×≈≠ ∞ √ √π√π∞ππ
                                 √≈√≈∞∞≠=      π≠∞√∞∞≠π≠÷≠√√∞∞∞≈≠≈π√√√∞
                                    π  ππ ππ√∞∞∞∞√√√∞∞≠≈≈∞√∞  ∞∞π∞   π
                                   π≈∞∞√π π∞√πππ    ππ  π    √π∞∞ √  π √
                                        ∞∞    √∞∞=≠≠==÷=÷÷×≠≠∞√≈∞
                                  ππ∞∞√ ≠        ≈        =    π∞     ∞√
                                 π√√  ∞∞∞    ∞   ≈ π  √√  ≠ ∞  ∞≈∞  √∞  π
                                  √√∞π≠∞π√∞√∞∞∞ π∞√∞π∞ ≈ππ∞π≈√ππ≠≈∞∞√≠∞∞√
                                    √π ≈ π≠≠≠≈  ≈√π≠×÷×≠ √∞ ÷∞=≠≠√≠∞π ππ
                                 π     ≠        =   ∞≠∞  ∞√  ∞∞ ∞     ππ∞
                                πππ  π≈∞  π     =        ∞√   ππ√π∞π πππ π
                                √∞π π≠≠ √   ≠  ∞≈     ∞π ∞√ ≈π  ≈≠∞∞ ∞≠≈∞∞
                                 ∞∞∞≠∞∞π∞√∞≈≠√ ≈   ∞=√∞≠ ≈π =ππ∞≠∞≠∞∞√ ≠√π
                               π√π√√ ∞π √=≠×≠  ≈  ∞÷∞=∞≠ ≠  ∞≈≠√∞∞     √∞π
                              π π    ≠    π    ≠   π∞≈π  ≈       ∞ ∞π  π  π
                              π∞π ∞ ∞≈        π≈         ≈     π ≠≠∞  π√π√√
                              ∞π √≈√≠ √  √∞   ≠√  ππ∞≠∞  ≈  ≈∞  √≠=≈∞√∞π∞√
                              √∞≈∞≠π≈ππ √ ∞√  ×  ππ∞∞∞=∞ ≈  =≈≠≠≠≠π=≈≈  ∞∞π
                            √π√√≈∞ ∞∞√∞√≠≈≠  √÷  π=≠=≠÷√ ≠  π=≠≠√∞π    ∞π π∞
                            √√π    ≠  π∞≠∞   ∞∞   ≈≠≠≠π  ≠       √∞∞  √√√√π∞
                            π≠∞√∞ ∞≠         ≠π          ≠   ∞ πππ≠∞√≈≠ π√∞√ π
                          √ π∞ √∞∞=π √ π≠π   ÷   ππ√≈    ≠  ≠∞√∞≠√=∞==≠π∞ π    √
                         √  π≠≠∞÷√≠ ∞√π√π≠  π÷  ∞ππ√ =∞ π≠  ∞=≈=≠ =π≠∞  π  π π
                        ∞π  ∞√≈≈π∞≈ ∞=≈≈≠≠  ≈≠  ≠≈∞=××∞ √≠   √∞∞≠≠≈ π∞π π√ π
                       ππ∞π  √∞  ÷π  ∞≠≠≠   ×∞   ∞=≠=≠  ∞≠ √≈=≈π  ≠∞  √∞π∞   π
                      ∞π  ∞√   ≠==         π×√        π√≠≈π  ∞≠π  π∞ π≈≠  π   π
                      √∞   π≠≈   √∞≈≠÷××÷=≠≠+÷×××=∞√π  ∞∞≠∞π∞∞∞∞∞√ ≠≠∞ππ∞π  π
                      π ∞  ≠≈   π√∞∞∞≈≈≈≠≈≈≈∞≈∞∞∞∞√√√∞√ππ≠π√∞√π∞≈√ π≠π√  π√
                      ∞√π≈×≈   √π√π∞∞∞∞∞√∞√≠ππ∞∞∞∞∞∞√∞π π=≈∞≠∞  π√√ √√π∞∞
                      √π√≈×π√≈≈≠≠=≠≠≠≈≈∞∞∞∞÷√∞≠===≠≈√√√  ≠≈ππ√∞∞∞∞  π≈π
                        ∞√∞∞ π√  π√√∞√√√ √√π÷∞√π√√∞√∞∞∞√π √≠ √πππ∞≠π
                         ∞∞√π ππ√πππ∞π∞∞√π∞ ≠∞∞π∞≠∞∞≈π∞√∞  ≠√≠∞√
                           ∞∞√√√ππ√∞∞∞∞∞∞√π∞ ∞π√√√∞∞∞∞∞≈≈≈∞√π
                                         ππ

"""

#let's write the rooms and items :))
rooms = {
    "outside the tardis": [],
    "locked bunker": [],
    "library": [
        {"name": "book", "type": "tool", "description": "It's a book! The best weapon in the world!"},
        {"name": "intelligent glove", "type": "tool", "description": "Great to fend off gravity (oh, sorry, mavity), can help you hold on to anything without any strain."}
    ],
    "observatory": [
        {"name": "void stuff glasses", "type": "clothing", "description": "Ah! Useful to spot void particles. Not sure if I need it right now, but certainly looks stylish!"}
    ],
    "hallway": [
        {"name": "dust bunny", "type": "tool", "description": "Oh boy, I really need to clean this hall, don't I?!"}
    ],
    "console room": [
        {"name": "sonic screwdriver", "type": "tool", "description": "My trusty sonic. Multi-functional, great at opening door, except when it comes to wood..."},
        {"name": "psychic paper", "type": "tool", "description": "Can look like any type of identification you might need. Very handy indeed!"},
        {"name": "2Dis", "type": "tool", "description": "Used to defeat the Boneless, this wonderful technology can shift things between two- and three dimensions."}
    ],
    "storage room": [
        {"name": "timey-wimey-detector", "type": "tool", "description": "It goes Ding! when there is stuff!"},
        {"name": "dinosaur stun gun", "type": "tool", "description": "I used this to stun a dinosaur once. Wonder how she is doing..."},
        {"name": "Rassilon cube", "type": "tool", "description": "A mobile prison, created long ago by Rassilon himself. I trapped the Fractures inside. Maybe I should leave it here."}
    ],
    "kitchen": [
        {"name": "banana", "type": "food", "description": "Always bring a banana to a party. Bananas are good!", "uses": 1},
        {"name": "apple", "type": "food", "description": "Rubbish.", "uses": 1},
        {"name": "fish-fingers and custard", "type": "food", "description": "Now that is delicious!", "uses": 1}
    ],
    "doctor's room": [
        {"name": "mobile phone", "type": "tool", "description": "Oh, hey, my phone! thought I lost it on Raxacoricofallapatorius last week."},
        {"name": "fez", "type": "clothing", "description": "Stylish. Practical. Simply the best"},
        {"name": "coat", "type": "clothing", "description": "My trusty coat. I would never leave without it. Except when it's too warm... Or I forget it.... Or I don't feel like wearing it... Or..."}
    ]
}

#now lets connect the rooms

room_connections = {
    "doctor's room": ["hallway"],
    "hallway": ["doctor's room", "console room", "kitchen", "library", "observatory", "storage room"],
    "console room": ["hallway", "outside the tardis"],
    "kitchen": ["hallway"],
    "library": ["hallway"],
    "observatory": ["hallway"],
    "storage room": ["hallway"],
    "outside the tardis": ["console room", "locked bunker"],
    "locked bunker": []
}

#lets give the rooms some descriptions
room_descriptions = {
    "hallway": "Some nice, long corridors, leading anywhere and everywhere. Great for running.",
    "console room": "This must be my absolute favourite room. It holds all the controls one might long for.",
    "kitchen": "Ah, maybe it's time for a snack!",
    "library": "I wonder if the swimming pool is somewhere in here and I just haven't found it yet...",
    "observatory": "Admittedly, I rarely use this one. I can visit the star systems instead of just watching them after all.",
    "storage room": "Wow, I might have to do some spring cleaning soon.",
    "doctor's room": "Time to sleep? Nah, never! Time for an adventure!",
    "outside the tardis": "Oh, Earth! Great! Hmm. 2013? No, 14! Some sort of underground station.... Interesting!",
    "locked bunker": "Wait! Is that..."
}

current_room = "doctor's room"

#lets define some functions
def typewriter(text, delay=0.03):
    if TEST_MODE:
        print(text)
    else:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

def show_room_items():
    connections = room_connections.get(current_room, [])
    if connections:
        typewriter("From here, you can go to:")
        for room in connections:
            typewriter(f"- {room.title()}")
    else:
        typewriter("There are no visible exits from here.")

    if current_room in ["outside the tardis", "locked bunker"]:
        return
    items = rooms.get(current_room, [])
    if items:
        typewriter("You see the following items:")
        for item in items:
            typewriter(f"- {item['name'].title()} ({item['type']})")
    else:
        typewriter("There are no items here.")


def show_inventory():
    if not INVENTORY:
        typewriter("Your inventory is empty.")
    else:
        typewriter("Your inventory contains:")
        for item in INVENTORY:
            if item["type"] == "clothing":
                typewriter(f"- {item['name'].title()} ({item['type']}) [Worn]")
            else:
                typewriter(f"- {item['name'].title()} ({item['type']})")

        used_slots = len([item for item in INVENTORY if item["type"] != "clothing"])
        typewriter(f"Inventory slots used (excluding clothing): {used_slots}/{INVENTORY_LIMIT}")

#lets define the pick up function but make clothing not count into the inventory, you wear it, after all
def pick_up(item_name_raw):
    item_name = item_name_raw.strip().lower()
    non_clothing_items = [item for item in INVENTORY if item["type"] != "clothing"]
    if len(non_clothing_items) >= INVENTORY_LIMIT:
        for item in rooms[current_room]:
            if item["name"].lower() == item_name.lower() and item["type"] != "clothing":
                typewriter("Your inventory is full!")
                return

    for item in rooms[current_room]:
        if item["name"].lower() == item_name.lower():
            INVENTORY.append(item)
            rooms[current_room].remove(item)
            typewriter(f"You picked up the {item_name}.")
            return

    typewriter(f"There is no {item_name} here.")

def drop(item_name_raw):
    item_name = item_name_raw.strip().lower()
    for item in INVENTORY:
        if item["name"].lower() == item_name.lower():
            INVENTORY.remove(item)
            rooms[current_room].append(item)
            typewriter(f"You dropped the {item_name}.")
            return
    typewriter(f"You don't have the {item_name}.")

def use(item_name_raw):
    item_name = item_name_raw.strip().lower()
    for item in INVENTORY:
        if item["name"].lower() == item_name.lower():
            if item["type"] == "food":
                typewriter("Delightful, I feel ready to take on a Judoon upon the Moon now!")
                item["uses"] -= 1
                if item["uses"] <= 0:
                    INVENTORY.remove(item)
            elif item["type"] == "tool":
                typewriter(f"You use the {item_name}, but nothing happens yet.")
            else:
                typewriter(f"You used the {item_name}.")
            return
    typewriter(f"You don't have a {item_name}.")

def examine(item_name_raw):
    item_name = item_name_raw.strip().lower()
    for item in INVENTORY:
        if item["name"].lower() == item_name.lower():
            typewriter(f"You inspect the {item['name']}.")
            typewriter(f"{item['description']}.")
            return
    typewriter(f"You don't have the {item_name}.")

def move_to_room(room_name):
    global current_room

    if room_name == "locked bunker":
        has_sonic = any(item["name"].lower() == "sonic screwdriver" for item in INVENTORY)
        if not has_sonic:
            typewriter("The bunker door is sealed shut. Maybe if I had my sonic screwdriver...")
            return False  # Prevent move

    if room_name in room_connections.get(current_room, []):
        current_room = room_name
        typewriter(f"{room_name}")
        typewriter(room_descriptions.get(room_name, ""))
        show_room_items()
        if room_name == "locked bunker":
            os.system('cls' if os.name == 'nt' else 'clear')
            time.sleep(1)
            print(DALEK)
            time.sleep(1)
            typewriter(f"It can't be! How did it get here?!")
            typewriter("You turn around, slamming the bunker door shut behind you and returning to the TARDIS. Time to make a plan.")
            typewriter("Congratulations, you finished the game!")
            return True
    else:
        typewriter("I don't think I can go there from here.")
    return False

#how about all the possible commands one can use
def help_menu():
    print("""Available commands:
- inventory
- pickup [item]
- drop [item]
- use [item]
- examine [item]
- look
- go [room]
- help
- quit/exit
""")


#game loop go brr
def game_loop():
    global current_room

    current_room = "doctor's room"
    help_menu()

    while True:
        command = input("> ").strip().lower()
        if command == "help":
            help_menu()
        elif command == "look":
            show_room_items()
        elif command.startswith("pickup"):
            parts = command.split(maxsplit=1)
            if len(parts) > 1:
                pick_up(parts[1])
            else:
                typewriter("Please specify what you want to pick up.")
        elif command.startswith("drop"):
            parts = command.split(maxsplit=1)
            if len(parts) > 1:
                drop(parts[1])
            else:
                typewriter("Please specify what you want to drop.")
        elif command.startswith("use"):
            parts = command.split(maxsplit=1)
            if len(parts) > 1:
                use(parts[1])
            else:
                typewriter("Please specify what you want to use.")
        elif command.startswith("examine"):
            parts = command.split(maxsplit=1)
            if len(parts) > 1:
                examine(parts[1])
            else:
                typewriter("Please specify what you want to examine.")
        elif command == "inventory":
            show_inventory()
        elif command.startswith("go "):
            room_name = command[3:].strip().lower()
            if room_name in room_connections.get(current_room, []):
                game_over = move_to_room(room_name)
                if game_over:
                    break
            else:
                typewriter("You can't go there from here.")
        elif command == "quit":
            typewriter("Thanks for playing!")
            break
        else:
            typewriter("Unknown command. Type 'help' to see available commands.")
#brother, the amount of googling this took


if __name__ == "__main__":
    typewriter("Welcome, Doctor! Please choose your own adventure!")
    game_loop()
