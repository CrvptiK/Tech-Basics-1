#%%
#i have decided to give some comments so i can understand my process in the future, and ofc make all this plausible hopefully...
#first things first, and admittedly one of the hardest process steps was finding an idea
#i had some vague ideas but none of them really involved randomness, so i was at a bit of a loss there
#i did a lot of googling and in the end asked chatgpt for some suggestions, giving it the task and asking for a general idea involving a game or dnd theme, as that is something that interests me
#chatgpt suggested an arcane glyph/ summoning circle design and i rolled with it

#now its time for me to sit down and figure out the code with knowledge from the session and probably asking google a lot xD

#first lets get our user inputs and validate them

#first the size/radius and validate it
while True:
    try:
        size = int(input("Enter circle size (5-30): "))
        if 5 <= size <= 30:
            break
        else:
            print("Size must be between 5 and 30")
    except ValueError:
        print("Please enter a valid number in format: integer.")

#now the complexity of the design, again with validation
while True:
    try:
        level = int(input("Enter spell level (0-10): "))
        if 0 <= level <= 10:
            break
        else:
            print("Level must be between 0 and 10")
    except ValueError:
        print("Please enter a valid number in format: integer.")

#and lastly the theme
#validate wahoo (this requires a different format (let's hope i figure this out))
#ok one google search later
valid_elements = ["fire", "cold", "lightning", "necrotic", "radiant", "poison"]
while True:
    element = input("Enter a magic type: fire, cold, lightning, necrotic, radiant, poison: ").lower()
    if element in valid_elements:
        break
    else:
        print("Invalid magic type. Please choose one of the following: fire, cold, lightning, necrotic, radiant, poison. ")

#now the input should be saved and validated, so we can move to the lists of symbols for each elemental type
import random

element_themes = {
    "fire": ["*", "+", "#", "-"],
    "cold": ["<", ">", "^", "/"],
    "lightning": ["/", "|", "_", "'"],
    "necrotic": ["$", "&", "%", "§"],
    "radiant": ["(", ")", "|", "*"],
    "poison": ["°", "0", ".", "~"]
}
symbols = element_themes[element]

#after trying for 15 minutes to set up a fricking circle (end me pls), lets ask google
diameter = size * 2 + 1
center = size
grid = [[" " for _ in range(diameter)] for _ in range(diameter)]
#please work omg

#time to use some nested loops and give the glyph circle some complexity based on the level
#easier said than done, boi, time to google again
#i saw a cool suggestion of havin the layers be one symbol each, so i ran with that suggestion here:
for layer in range(1, level + 1):
    r = int((layer / (level + 1)) * size)

    layer_symbols = random.sample(symbols, k=len(symbols))
    symbol = layer_symbols[layer % len(layer_symbols)]

    for y in range(diameter):
        for x in range(diameter):
            dist = int(((x - center) ** 2 + (y - center) ** 2) ** 0.5)
            if abs(dist - r) <= 1:
                grid[y][x] = symbol

#after staring at the tutorial for another eternity and getting an explanation from chatgpt i think i understood it now, boi o boi
#side note: i hope using google, tutorials and ai is alright in this case and in my progression, if not, please inform me (and maybe the others idk how they do this) so i can refrain from using it in the future, as you can hopefully tell, im trying to learn with it, rather than blindly copy-pasting anything from it

#now let's print the glyph and add the time sleep effect that we learned about previously
import time
for row in grid:
    print("".join(row))
    time.sleep(0.05)

#ok technically i could leave it here, but i want to have a special easter egg, so i asked google, how to replace singular glyphs at random with a magic sparkle effect
#after some tweaking to make it work for my code (i hope it works lmao) i can present this:
if random.random() < 0.05:
    grid[random.randint(0, diameter-1)][random.randint(0, diameter-1)] = "✨"
#it hasnt yet come up while testing so i hope it actually works and im just unlucky xD