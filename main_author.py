from packages.parser.parser import *;
myWorld = World("yes");
# myWorld.newArea("yep", "yeppers")
# myWorld.newArea("Nope", "Noperino")
print myWorld.trimDirectionString("      north east  ")
print myWorld.trimDirectionString(" south west ")
print myWorld.trimDirectionString("  north east  ")
print myWorld.trimDirectionString("      north east  ")
myWorld.printWorld()
