

class transition:

    def __init__(self, name, area, direction, destination , isPassable, description):
        self.name = name
        self.area = area
        self.direction = direction
        self.destination = destination
        self.isPassable = isPassable
        self.imPassable = ""
        self.description = description
        self.requirements = []

    def printTrans(self, name):
        print(self.name + ": " + self.description)
