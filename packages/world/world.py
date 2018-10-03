from packages.area.area import Area
from packages.transition.transition import transition;
from packages.player.player import player;
from packages.item.item import item;

class world:

    NORTH = 1
    SOUTH = 2
    EAST = 3
    WEST = 4
    UP = 5
    DOWN = 6
    NORTH_EAST = 7
    SOUTH_EAST = 8
    SOUTH_WEST = 9
    NORTH_WEST = 10


    #AUTHOR METHODS
    def __init__(self, description = "New World", player = "Player One"):
        self.description = description
        self.player = player
        self.areas = []

    #Creates a new area unless one with the given name already exists
    #Returns the area object to the author.
    def newArea(self, name, description):
        if not self.areaExists(name):
            area = Area.newArea(self, name, description)
            self.areas.append(area)

        return self.getArea(name)

    #Searches for existence of an area with given name
    #Returns true if found, false otherwise
    def areaExists(self, name):
        for area in self.areas:
            if area.name == name:
                return True
        return False


    def newTransition(self, name, area, direction, destination, description, isTwoWay):

        areaFound = False
        destinationFound = False
        targetArea = None
        targetDestination = None

        #ERROR CHECKING UP FRONT
        #checking for existence of target area
        areaFound = self.areaExists(area)
        if areaFound == False:
            raise Exception("Area " + area + " does not exist")
        targetArea = self.getArea(area)

        #checking for existence of target destination
        destination = self.areaExists(destination)
        if destinationFound == False:
            raise Exception("Destination " + destination + " does not exist")
        targetDestination = self.getArea(destination)

        if isTwoWay == False:
            newTransition = transition(name, targetArea, direction, targetDestination)
            targetArea.newTransition(newTransition)
        if isTwoWay == True:
            newTransition = transition(name, targetArea, direction, targetDestination)
            targetArea.newTransition(newTransition)

            if cardinalPosition == "east":
                self.newTransition(name, area, "west", destination, False)
            elif cardinalPosition == "west":
                self.newTransition(name, area, "east", destination, False)
            elif cardinalPosition == "north":
                self.newTransition(name, area, "south", destination, False)
            elif cardinalPosition == "south":
                self.newTransition(name, area, "north", destination, False)
            elif cardinalPosition == "northeast":
                self.newTransition(name, area, "southwest", destination, False)
            elif cardinalPosition == "southeast":
                self.newTransition(name, area, "northwest", destination, False)
            elif cardinalPosition == "southwest":
                self.newTransition(name, area, "northeast", destination, False)
            elif cardinalPosition == "northwest":
                self.newTransition(name, area, "southeast", destination, False)

    #Searches for the name of the area in the list of areas (self.areas) in the world.
    #Returns area object once found.
    def getArea(self,name):
        if self.areaExists(name):
            for area in self.areas:
                if name is area.name:
                    return area
        else:
            Throw Exception("Area " + name + "does not exist")
