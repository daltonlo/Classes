# imports base hp, treasuer chest function and hp
from charactertraits import basehp
from inventorytraits import treasurechest
from character import char_choice


# Creates a room class
class Room(object):
    def __init__(self):
        pass

# Creates a child class of room called Health room
class HealthRoom(Room):
    def scripts(self):
        """text that prints when player enters the health room"""
        print("You find a place where you can rest + 30 hp")

# Creates a child class of room called Combat Room
class CombatRoom(Room):
    def scripts(self):
        """text that prints when player enters the combat room"""
        print("You enter the room and get attacked - 50 hp")

# Creates a child class of room called Treasure Room
class TreasureRoom(Room):
    def scripts(self):
        """text that prints when player enters the treasure room"""
        print("You find a chest and open it")
        """Treasure chest function that gives people a random item"""
        treasurechest()

# Creates a child class of room called Dragon Room
class DragonRoom(Room):
    def scripts(self):
        """text that prints when player enters the dragon room"""
        print("You find the room where the Dragon lives")

# Creates a child class of room called Hallway
class Hallway(Room):
    def scripts(self):
        """text that prints when player enters the hallway"""
        print("You are in the hallway")
