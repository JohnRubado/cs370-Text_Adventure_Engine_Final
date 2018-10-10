from packages.world.world import *;
from packages.parser.parser import parser

mixer.init()

def onLoadScript():
    birds = mixer.Sound("birds.wav")
    birds.play()

script = onLoadScript

#CREATE THE WORLD AND THE PLAYER
player = player("Johnny", "A young man")
myWorld = World("The Narrows","An uncharted territory. Good Luck.",player, script);

#CREATE SOME AREAS
quarry = myWorld.newArea("quarry", "Placeholder description")
quarry.setDescription("There are many rocks around here")
woods = myWorld.newArea("woods", "Many trees surround the area, wild animals can be heard")
lake = myWorld.newArea("cavern", "Its dark and wet")

myWorld.newTransition("path",["quarry", "west"], ["woods", "north"], True, "Its covered with giant boulders.")

parser = parser(myWorld)
parser.start()
