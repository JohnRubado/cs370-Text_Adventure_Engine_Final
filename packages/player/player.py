from packages.item.item import item
from packages.area.area import Area


class player:


    def __init__(self, name="Player", description="",inventory=[]):
        self.description = description
        self.currentArea = None;
        self.name = name
        self.inventory = inventory


    def printPlayer(self):
        print "You are " + self.name + ". " + self.description

    def addToInventory(self, targetItem):
        area1 = self.currentArea
        for item in area1.items:
            if targetItem == item.name and item.moveable == True:
                self.inventory.append(item)
                print("You picked up: " + targetItem)
                area1.removeItem(targetItem)
                return 0
        print("You could not pick up: " + targetItem)

    def dropFromInventory(self, item):
        for items in self.inventory:
            if item == items.name:
                self.inventory.remove(items)



    def printInventory(self):
        for item in self.inventory:
            print(item.name + ": " + item.description)
