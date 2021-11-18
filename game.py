# Runs the program and prints an error message if it messes up
try:
    print("Quit at any time by typing QUIT")
    from charactertraits import *
    from map import *
except:
    print("Game ran into an error")
else:
    print("Game ran into no errors")