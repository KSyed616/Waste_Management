class House:

    def __init__(self, neighbourhood, occupied, residents):  # occupied is boolean
        self.neighbourhood = neighbourhood
        self.occupied = occupied
        self.residents = residents
        # blue = recycle, green = organics, black = garbage
        # True = collected
        if(occupied):
            self.blue = False
            self.green = False
            self.black = False
        else:
            self.blue = True
            self.green = True
            self.black = True

        def occupy(self):  # making house unvacant
            self.neighbourhood.append(self)
            self.blue = False
            self.green = False
            self.black = False

        def vacant(self):
            self.neighbourhood.remove(self)

        def isCollected(self):
            if blue and green and black:
                return true
            else:
                return false
