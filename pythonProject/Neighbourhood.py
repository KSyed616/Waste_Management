from House import House
import random


# no roads under the idea that ONE garbage truck goes through a whole neighbourhood
# with road implementation may need to pass a couple or array of strings as param
# split total amongst strings
class Neighbourhood:
    # create neighbourhood and give it parameters such as total, green, black, blue, etc.
    def __init__(self, total):
        self.total = total
        self.houses = []
        for num in range(total):
            self.houses.append(House(self, True, random.randint(1, 5)))
        self.blue = False
        self.green = False
        self.black = False

    # calculates number of residents in neighbourhood
    def residents(self):
        res = 0
        for house in self.houses:
            res += house.residents
        return res

    # sets blue, green, and black parameters of house to true.
    def collect(self):
        for house in self.houses:
            house.blue = True
            house.green = True
            house.black = True

    # checks if the isCollected() method for all houses gives true
    def complete(self):
        for house in self.houses:
            if not house.isCollected():
                return False
        return True
