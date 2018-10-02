from packages.area.area import Area
from packages.transition.transition import transition;
from packages.player.player import player;
from packages.item.item import item;

class world:


    #AUTHOR METHODS
    def __init__(self, description = "New World", player = "Player One"):
        self.description = description
        self.player = player
        self.areas = []

    def newArea(self, name, description):
        if not self.areaExists(name):
            area = Area.newArea(self, name, description)
            self.areas.append(area)

        

    def areaExists(self, name):
        for area in self.areas:
            if area.name == name:
                return True

        return False
