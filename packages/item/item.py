

class item:

    def __init__(self, name, description, area, moveable):
        self.name = name
        self.description = description
        self.area = area
        self.moveable = moveable

    def printItem(self, name):

        if self.moveable == True:
            print( "You see a " + self.name + ". " + self.description + ". I think I can pick it up.")
        else:
            print( "You see a " + self.name + ". " + self.description)

    
