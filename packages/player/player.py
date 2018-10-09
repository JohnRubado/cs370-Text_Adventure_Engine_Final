
class player:


    def __init__(self, name="Player", description="",inventory=[]):
        self.description = description
        self.currentArea = None;
        self.name = name


    def printPlayer(self):
        print "You are " + self.name + ". " + self.description
