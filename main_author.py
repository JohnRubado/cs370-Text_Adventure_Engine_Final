from packages.world.world import *;


mixer.init()

def onLoadScript():
    birds = mixer.Sound("birds.wav")
    birds.play()

script = onLoadScript

player = player("Johnny", "A brolic young lad")
myWorld = World("A vast land of wonders",player, script);
myWorld.newArea("quarry", "There are many rocks in this place.")
myWorld.newArea("woods", "Many trees surround the area, wild animals can be heard")

myWorld.newTransition("path",["quarry", "west"], ["woods", "north"], True, "Its covered with giant boulders.")

myWorld.movePlayer("path")
myWorld.printWorld()

myWorld.movePlayer("west")
myWorld.movePlayer("east")
myWorld.movePlayer("south")
myWorld.movePlayer("north")
myWorld.printWorld()
time.sleep(20)
