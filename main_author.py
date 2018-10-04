from packages.parser.parser import *;




myWorld = World();
myWorld.newArea("quarry", "There are many rocks in this place.")
myWorld.newArea("woods", "Many trees surround the area, wild animals can be heard")

myWorld.newTransition("path",["quarry", "west"], ["woods", "north"], True, "Its covered with giant boulders.")

myWorld.movePlayer("west")



print myWorld.trimDirectionString("      north east  ")
print myWorld.trimDirectionString(" south west ")
print myWorld.trimDirectionString("  north east  ")
print myWorld.trimDirectionString("      north east  ")
myWorld.printWorld()
