class Asteroid:
    def __init__(self, width, height):
        self.width = width
        self.height = height


class Robot:
    def __init__(self, x, y, asteroid, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.asteroid = asteroid
        if self.x > self.asteroid.width:
            raise MissAsteroidErro()
        if self.y > self.asteroid.height:
            raise MissAsteroidErro()

    def turn_left(self):
        turns = {"E": "N",
                 "N": "W",
                 "W": "S",
                 "S": "E",
                 }

        self.direction = turns[self.direction]

    def turn_right(self):
        turns = {"N": "E",
                 "E": "S",
                 "S": "W",
                 "W": "N",
                 }
        self.direction = turns[self.direction]

    def move_forwa(self):

        if self.direction == "E":
            self.x += 1
        elif self.direction == "N":
            self.y += 1
        elif self.direction == "S":
            self.y -= 1
        elif self.direction == "W":
            self.x -= 1
        else:
            raise MoveError("Choose direction")
        self.check_drop()

    def move_back(self):

        if self.direction == "E":
            self.x -= 1
        elif self.direction == "N":
            self.y -= 1
        elif self.direction == "S":
            self.y += 1
        elif self.direction == "W":
            self.x += 1
        else:
            raise MoveError("Вибери правильний напрямок")
        self.check_drop()
        self.check_obstacle(0, 0)

    def check_drop(self):
        if self.x > self.asteroid.width:
            raise MoveError("Drop from asteroid")
        if self.y > self.asteroid.height:
            raise MoveError("Drop from asteroid")

    def check_obstacle(self, obstacle_x, obstacle_y):

        if obstacle_x >= self.asteroid.width:
            raise MissAsteroidErro()
        if obstacle_y >= self.asteroid.height:
            raise MissAsteroidErro()
        if self.x == obstacle_x:
            raise MoveError("You have problem with obstacle")
        if self.y == obstacle_y:
            raise MoveError("You have problem with obstacle")


class MissAsteroidErro(Exception):
    pass


class MoveError(Exception):
    pass


""" if self.direction == "E":
            self.x += 1
            return self.x
        elif self.direction == "N":
            self.y += 1
        elif self.direction == "S":
            self.y -= 1
        elif self.direction == "W":
            self.x -= 1
        return self.x, self.y

        forward = {"N": (0, 1),
                   "E": (1, 0),
                   "S": (0, 1),
                   "W": (1, 0)
                   }

        self.direction = forward[self.direction]
        self.x += forward[self.x]


                try:
            self.x, self.y < self.width, self.height
            )
            raise MoveError
        except:
            pass
        """
