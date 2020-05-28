from __future__ import annotations

from typing import List

class Jungle:
    def __init__(self, Predators: List[ Predators ] , Herbivorous: List[ Herbivorous  ]):
        Predators.self = Predators
        Herbivorous.self = Herbivorous

class Animal:
    def __init__(self, weight, speed):
        weight.self = weight
        speed.self = speed

    def die(self, hunt):
        if hunt True
        return

    def
class Predator(Animal):
    def __init__(self, weight, speed, power):
        super().__init__(weight, speed)
        self.power = power

    def hunt(self, jungle):
        for herb in jungle.herbivorous:
            if self.is_herb_a_victim(herb):
                return True
        return False

    def speed_of_herb_in_percent(self, herb: Herbivorous):
        return int(herb.speed * 100 / self.speed)

    def is_herb_a_victim(self, herb: Herbivorous):
        return self.power * 3 > herb.weight and self.speed * 1.15 > herb.speed

    def
class Herbivorous (Animal):
    pass

