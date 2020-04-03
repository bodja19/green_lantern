import pytest

from robot import Robot, Asteroid, MissAsteroidErro, MoveError

"""Порядок денний:
Створіть робота з положенням і напрямком
Перевірте, чи робот пропустив астероїд під час посадки
Створіть і випробуйте функції turn_left і turn_right
Додайте функції move_forward, move_backward
Перевірте, чи падає він від астероїда під час руху
Додайте астероїдні перешкоди
Оновіть рух робота, щоб дотримуватися перешкод
... Ваші ідеї

Домашня роботаmove_direction
Закінчіть тестування оборотів
Логіка руху коду move_forward, move_backward
Перевірте, чи не падає робот з астероїду
Для сміливих людей
Додайте перешкоди астероїду
Створіть роботу почесні перешкоди
"""


class TestRobotCreation:
    def test_parameters(self):
        x, y = 10, 15
        direction = "E"
        asteroid = Asteroid(15, 25)
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

    @pytest.mark.parametrize(
        "curent_direction,expected_direction",
        (
                ("N", "W"),
                ("W", "S"),
                ("S", "E"),
        )
    )
    def test_turn_left(self, curent_direction, expected_direction):
        robot = Robot(self.x, self.y, self.asteroid, curent_direction)
        robot.turn_left()
        assert robot.direction == expected_direction

    @pytest.mark.parametrize(
        "curent_direction,expected_direction",
        (
                ("N", "E"),
                ("W", "N"),
                ("S", "W"),
        )
    )
    def test_turn_right(self, curent_direction, expected_direction):
        robot = Robot(self.x, self.y, self.asteroid, curent_direction)
        robot.turn_right()
        assert robot.direction == expected_direction

    @pytest.mark.parametrize(
        "move_forward_x, move_forward_y,expected_move_x,expected_move_y,move_direction",
        [(10, 15, 10, 14, "S"),
         (10, 15, 11, 15, "E"),
         (10, 15, 9, 15, "W"),
         (10, 24, 10, 25, "B"),
         ]
    )
    def test_move_forward(self, move_forward_x, move_forward_y, expected_move_x, expected_move_y, move_direction):
        print(self.asteroid.height)
        robot = Robot(move_forward_x, move_forward_y, self.asteroid, move_direction)
        robot.move_forwa()
        assert robot.x == expected_move_x
        assert robot.y == expected_move_y

    @pytest.mark.parametrize(
        "move_back_x, move_back_y,expected_move_x,expected_move_y,move_direction",
        [(10, 15, 10, 16, "S"),
         (10, 15, 9, 15, "E"),
         (10, 15, 11, 15, "W"),
         ]
    )
    def test_move_backward(self, move_back_x, move_back_y,expected_move_x,expected_move_y,move_direction):
        robot = Robot(move_back_x, move_back_y, self.asteroid, move_direction)
        robot.move_back()
        assert robot.x == expected_move_x
        assert robot.y == expected_move_y


    def test__error_backward(self):
        with pytest.raises(MoveError):
            asteroid = Asteroid(14, 25)
            robot = Robot(14, 25, asteroid, "W")
            robot.move_back()


    def test_drop_robot_asteroid(self):
        asteroid = Asteroid(14, 25)
        robot = Robot(10, 20, asteroid, "W")
        robot.check_drop()
        assert robot.x == 10
        assert MoveError

    @pytest.mark.parametrize(
        "obstacle_X,obstacle_Y",
        (
                (1, 2),
                (15, 2),
                (30, 30),
        )
    )
    def test_obstacle_robot_on_asteroid(self, obstacle_X, obstacle_Y):
        with pytest.raises(MoveError):
            asteroid = Asteroid(20, 25)
            robot = Robot(15, 20, asteroid, "W")
            robot.check_obstacle(obstacle_X, obstacle_Y)




        """
        (self, asteroid_size, robot_coordinates):
        with pytest.raises(MissAsteroidErro):
            asteroid = Asteroid(*asteroid_size)
            Robot(*robot_coordinates, asteroid, "W")
    @pytest.mark.parametrize(
        "expected_move,move_direction",
        [(15, 16, "S"),
         (10, 9, "E"),
         (10, 11, "W"),
         ]
    )
         self.asteroid = Asteroid(20, 35)
        robot = Robot(self.x, self.y, self.asteroid, move_direction)
        robot.check_drop()
        assert robot.check_drop == expected_move


        x, y = 10, 15 
        direction = "E"
        asteroid = Asteroid(x + 1, y + 1)
        robot = Robot(x, y, asteroid, direction)
        assert robot.direction == direction
        assert robot.x == 10
        assert robot.y == 15
        assert robot.asteroid == asteroid
        assert robot."""
