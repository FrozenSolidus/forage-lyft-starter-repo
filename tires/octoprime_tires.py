from abc import ABC

from tires.TiresInterface import Tires


class OctoprimeTires(Tires):
    def __init__(self, tires):
        self.tires = tires

    def needs_service(self):
        array_sum = sum(self.tires)
        return array_sum >= 3