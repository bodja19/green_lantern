import pytest
from robot import Robot, Asteroid, MissAsteroidErro


class TestRobotCreation:
    def test_parameters(self):
        x, y = 10, 15
        direction = "E"
        asteroid = Asteroid(x + 1, y + 1)
        robot = Robot(x, y, asteroid, direction)
        assert robot.direction == direction
        assert robot.x == 10
        assert robot.y == 15
        assert robot.asteroid == asteroid

    @pytest.mark.parametrize(
        "asteroid_size,robot_coordinates",
        (
                ((15, 25), (26, 30)),
                ((15, 25), (25, 24)),
                ((15, 25), (15, 27)),
        )
    )

    def test_check_if_robot_on_asteroid(self, asteroid_size, robot_coordinates):
        with pytest.raises(MissAsteroidErro):
            asteroid = Asteroid(*asteroid_size)
            Robot(*robot_coordinates, asteroid, "W")


class TestMove:
    def setup(self):
        self.x, self.y = 10, 15
        self.asteroid = Asteroid(self.x + 1, self.y + 1)
        self.direction = self.curent_direction
    @pytest.mark.parametrize(
        "curent_direction,expected_direction",
        (
        ("N", "W"),
        ("W", "S"),
        ("S", "E"),
        )
    )

    def test_turn_left(self, curent_direction, expected_direction):
        print(self.setup())
        print(self.asteroid)
        print(curent_direction)
        robot = Robot(self.setup, self.asteroid, curent_direction)
        robot.turn_left()
        assert robot.direction == expected_direction


    """def test_turn_right(self):
        x, y = 10, 15
        direction = "E"
        asteroid = Asteroid(x + 1, y + 1)
        robot = Robot(x, y, asteroid, direction)
        robot.turn_left()
        assert robot.direction == "S"""""


