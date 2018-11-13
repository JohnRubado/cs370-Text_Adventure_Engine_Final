class item:

    def __init__(self, name, description, area, moveable = True):
        self.name = name
        self.description = description
        self.detailedDescription = None
        self.area = area
        self.moveable = moveable
        self.onSuccess = None
        self.onFailure = None
        self.onSuccessScripts = []
        self.onFailureScripts = []
        self.onUseScripts = []
        self.onUse = None

    def printDescription(self):
        print( "You see a " + self.name + ". " + self.description)
