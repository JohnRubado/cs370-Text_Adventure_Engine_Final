from packages.item import item;
from packages.direction.direction import direction;


class Area:


    def __init__(self,name, description = "A vast land of wonders, maybe I should take a look around?"):
        self.name = name
        self.items = []
        self.transitions = []
        

    def newItem(self, item):
        self.items.append(item)
