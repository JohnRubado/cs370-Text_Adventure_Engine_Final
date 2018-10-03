from packages.parser.parser import *;

def testPrint():
    for area in myWorld.areas:
        print area.name + " contains:"
        if myWorld.player.currentArea.name == area.name:
            print "Player"
        for transition in area.transitions:
            print transition.name + " in the " + transition.direction + "\n"


myWorld = World();
myWorld.newArea("quarry", "There are many rocks in this place.")
myWorld.newArea("woods", "Many trees surround the area, wild animals can be heard")

myWorld.newTransition("path",["quarry", "west"], ["woods", "north"], True, "Its covered with giant boulders.")



testPrint()
myWorld.movePlayer("west")

testPrint()
