class House:

    def __init__(self, neighbourhood, occupied, residents):  # occupied is boolean
        self.neighbourhood = neighbourhood
        self.occupied = occupied
        self.residents = residents
        # blue = recycle, green = organics, black = garbage
        # True = collected
        blue = False
        green = False
        black = False

        def occupy(self):  # making house unvacant
            self.neighbourhood.append(self)

        def vacant(self):
            self.neighbourhood.remove(self)
