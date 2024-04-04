import random


class WasteDept:
    def __init__(self, type):
        self.type = type
        self.capacity = 200
        self.current = 0

    def collect_waste(self, amount=1):
        self.current += amount
        if self.current > self.capacity:
            self.current = self.capacity
