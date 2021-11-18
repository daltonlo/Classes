# Runs the character file and imports the character choice
from character import *
from character import char_choice

# Creates the player class
class Players(object):
    def __init__(self,health,items):
        self.health = health
        self.items = items
        pass
        
# Creates the wizard child class        
class Wizard(Players):
    health = 50
    items = "Magic wand"

# Creates the knight child class
class Knight(Players):
    health = 100
    items = "Sword","Shield"

# Creates the adventurer child class
class Adventurer(Players):
    health = 80
    items = "Map","Dagger"

# Sets the base tools and health for each of the character choices
if char_choice.lower() == "wizard":
    basehp = Wizard.health
    basetools = Wizard.items
if char_choice.lower() == "knight":
    basehp = Knight.health
    basetools = Knight.items
if char_choice.lower() == "adventurer":
    basehp = Knight.health
    basetools = Knight.items
