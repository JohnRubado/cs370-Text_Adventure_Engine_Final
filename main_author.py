from packages.world.world import *;
from packages.parser.parser import parser

mixer.init()

# def onLoadScript():
#     birds = mixer.Sound("birds.wav")
#     birds.play()
#
# script = onLoadScript


player = player("Johnny", "A brolic young lad")
myWorld = World("The Deep","A vast land of wonders",player);


myWorld.newArea("quarry", "There are many rocks in this place.")
myWorld.newArea("woods", "Many trees surround the area, wild animals can be heard")

myWorld.newTransition("path",["quarry", "west"], ["woods", "north"], True, "Its covered with giant boulders.")
parser = parser(myWorld)
parser.start()
