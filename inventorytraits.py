# imports base tools hp and base hp from charactertraits
from charactertraits import *
from charactertraits import basetools
from charactertraits import basehp
import random

# Creates a list of possible tools the player can use
possible_items = ["Torch","Food","Health Potion","Ladder"]

# Creates the heals class for items that heal
class Heals(object):
    def __init__(self,name):
        self.healamount = healamount
        self.name = name
        print(f"You recieved {name}")
        print("You use it and heal")

# Creates a class of heals called food
class Food(Heals):
    name = "Food"

# Creates a class of heals called health potion
class HealthPotion(Heals):
    name = "a Health Potion"

# Creates the tools class
class Tools(object):
    def __init__(self,name):
        self.name = name
        print(f"You recieved a {name}")

class Torch(Tools):
    name = "Torch"

class Ladder(Tools):
    name = "Ladder"

def treasurechest():
    treasure = random.choice(possible_items)
    if treasure == "Torch":
        t = Torch("Torch")
    if treasure == "Food":
        t = Food("Food")
    if treasure == "Health Potion":
        t = HealthPotion("Health Potion")
    if treasure == "Ladder":
        t = Ladder("Ladder")