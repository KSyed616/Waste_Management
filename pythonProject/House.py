class House:
    def __init__(self, neighbourhood, occupied, residents):
        self.neighbourhood = neighbourhood
        self.occupied = occupied
        self.residents = residents
        # True = collected, else = not collected
        if occupied:  # occupied is boolean
            # blue = recycle, green = organics, black = garbage
            self.blue = False
            self.green = False
            self.black = False
        else:
            self.blue = True
            self.green = True
            self.black = True

        def occupy(self):  # making house un-vacant
            self.neighbourhood.append(self)
            self.blue = False
            self.green = False
            self.black = False

        def vacant(self):
            self.neighbourhood.remove(self)

        def isCollected(self):
            if self.blue and self.green and self.black:
                return True
            else:
                return False
