from packages.parser.parser import *;
myWorld = World();
print myWorld.trimDirectionString("      north east  ")
print myWorld.trimDirectionString(" south west ")
print myWorld.trimDirectionString("  north east  ")
print myWorld.trimDirectionString("      north east  ")
