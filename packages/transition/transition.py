

class transition:

    def __init__(self, name, area, direction, destination , isPassable, description):
        self.name = name
        self.area = area
        self.direction = direction
        self.destination = destination
        self.isPassable = isPassable
        self.onSuccess = None
        self.onFailure = None
        self.description = description
        self.openedDescription = None
        self.detailedDescription = None
        self.onSuccessScripts = []
        self.onFailureScripts = []
        self.onOpenScripts = []
        self.requirements = []

    def printDescription(self):
        print( "You see a " + self.name + ". " + self.description + " It seems to lead "+ self.direction)

    #if a transition has no requirements, this is the description printed.
    def printOpenedDescription(self):
        print( "You see a " + self.name + ". " + self.openedDescription + " It seems to lead "+ self.direction)
