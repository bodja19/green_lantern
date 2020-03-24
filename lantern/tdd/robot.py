class Asteroid:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Robot:
    def __init__(self, x, y, asteroid, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.asteroid = asteroid
        if self.x > self.asteroid.x:
            raise MissAsteroidErro()
        if self.y > self.asteroid.y:
            raise MissAsteroidErro()

    def turn_left(self):
        turns = {"E": "N",
                 "N": "W",
                 "W": "S",
                 "S": "E"
         }
        self.direction = turns[self.direction]

    """def turn_right(self):
        turns = {"E": "S"}
        self.direction = turns[self.direction]"""

class MissAsteroidErro(Exception):
    pass
