# imports all necesary modules
import random
from maptraits import HealthRoom
from maptraits import CombatRoom
from maptraits import TreasureRoom
from maptraits import DragonRoom
from maptraits import Hallway

# Creates a list of places the player can go
locations = ["Treasure room", "Combat room", "Rest room"]

print(f"You start out in the hallways knowing that at the end of it the dragon lays")
print(f"You have to loot the dungeon to stand a chance against the beast")
print(f"Good luck")

# Creates a counter to when the player will be placed in dragon room
room_past = 0

# Creates a loop of rooms until the players has been in or past 9 rooms
while room_past < 10:
    """Asigns h to the hallway class"""
    h = Hallway()
    """Prints the hallway text"""
    h.scripts()
    print(f"Move or Enter")
    enter = input()
    try:
        if enter.lower() == "enter":
            play_location = random.choice(locations)
            """Prints text if player is in treasure room"""
            if play_location.lower() == "treasure room":
                """Asigns T to the treasure room class"""
                T = TreasureRoom()
                """Prints the treasure room text"""
                T.scripts()
                room_past = room_past + 1
            """Prints text if player is in treasure room"""
            if play_location.lower() == "combat room":
                """Asigns c to the combat room class"""
                c = CombatRoom()
                """Prints the combat room text"""
                c.scripts()
                room_past = room_past + 1
            """Prints text if player is in treasure room"""
            if play_location.lower() == "rest room":
                """Asigns H to the heath room class"""
                H = HealthRoom()
                """Prints the heath room text"""
                H.scripts()
                room_past = room_past + 1
        """Creates a skip room option """
        if enter.lower() == "move":
            print("You skip a room")
            room_past = room_past + 1
        """Creates an invalid input statement"""
        if enter.lower() not in ("move", "enter","quit"):
            raise Exception("")
        """Creates a quit option"""
        if enter.lower() == "quit":
            quit()
            pass
        """Handles exception created from invalid input"""
    except:
        print(f"Please type Move or Enter")

# Creates a prompt if the player enters or skips 10 rooms
if room_past == 10:
    d = DragonRoom()
    d.scripts()
