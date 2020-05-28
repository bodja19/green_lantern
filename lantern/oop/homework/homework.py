import math


class Cat:
    """
    Write Class Cat which will receive age from user
    * Add to class average_speed variable which will get it's values
      from private method _set_average_speed()

    * Add to class saturation_level variable with value 50

    * Implement private methods _increase_saturation_level and _reduce_saturation_level
      that will receive value and add/subtract from saturation_level this value
      if saturation_level is less than 0, return 0
      if saturation_level is grosser than 100, return 100

    * Implement method eat which will receive from user product value
      if product eq fodder use _increase_saturation_level with value eq 10
      if product eq apple use _increase_saturation_level with value eq 5
      if product eq milk use _increase_saturation_level with value eq 2

    * Implement private method _set_average_speed
      if age less or eq 7 return 12
      if age between 7(not including) and 10(including) return 9
      if age grosser than 10(not including) return 6

    * Implement method run it receives hours value
      Calculate run km per hours remember that you have average_speed value
      Than if your cat run less or eq than 25 _reduce_saturation_level with value 2
      if it runs between 25(not including) and 50(including) than _reduce_saturation_level with value 5
      if it runs between 50(not including) and 100(including) than _reduce_saturation_level with value 15
      if it runs between 100(not including) and 200(including) than _reduce_saturation_level with value 25
      if it runs more than 200(not including) than _reduce_saturation_level with value 50

      return text like this: f"Your cat ran {ran_km} kilometers"

    * Implement get_saturation_level and return saturation_level
      if saturation_level eq 0 return text like this: "Your cat is dead :("

    * Implement get_average_speed and return average_speed
     _______________________________________
     Напишіть Cat Class, який отримає вік від користувача
    * Додайте до класу value_speed змінної класу, яка отримає її значення
      від приватного методу _set_average_speed ()

    * Додати до змінної saturation_level класу зі значенням 50

    * Реалізуйте приватні методи _increase_saturation_level та _reduce_saturation_level
      який отримає значення і додасть / відніме з saturation_level це значення
      якщо saturation_level менше 0, поверніть 0
      якщо saturation_level більше 100, поверніть 100

    * Реалізація методу харчування, який отримуватиме від продукту користувача значення
      якщо продукт eq корм використовують _increase_saturation_level зі значенням eq 10
      якщо продукт eq apple використовує _increase_saturation_level зі значенням eq 5
      якщо в еквівалентному молоці продукту використовується _increase_saturation_level зі значенням eq 2

    * Реалізувати приватний метод _set_average_speed
      якщо вік менший або екв. 7 повертаються 12
      якщо вік між 7 (не враховуючи) і 10 (включаючи) повертається 9
      якщо вік зростає за 10 (не враховуючи) повернення 6

    * Запуск методу виконання він отримує значення годин
      Обчисліть пробіг км на годину, пам’ятайте, що у вас є середнє значення швидкості
      Тоді, якщо ваша кішка працює менше або еквівалентно, ніж 25 _reduce_saturation_level зі значенням 2
      якщо він працює між 25 (не включаючи) і 50 (включаючи), ніж _reduce_saturation_level зі значенням 5
      якщо він працює від 50 (не включаючи) і 100 (включаючи), ніж _reduce_saturation_level зі значенням 15
      якщо він працює між 100 (не включаючи) і 200 (включаючи), ніж _reduce_saturation_level зі значенням 25
      якщо він працює більше 200 (не враховуючи), ніж _reduce_saturation_level зі значенням 50

      повернути такий текст: f "Ваша кішка пробігла {ran_km} кілометрів"

    * Реалізуйте get_saturation_level та поверніть saturation_level
      if saturation_level eq 0 повернути такий текст: "Ваша кішка мертва :("

    * Реалізуйте get_average_speed і поверніть середню швидкість
    """

    def __init__(self, age):
        self.age = age
        self.saturation_level = 50
        self.average_speed = self._set_average_speed()

    def eat(self, food):
        foods = {
            "fodder": 10,
            "apple": 5,
            "milk": 2
        }
        try:
            return self._increase_saturation_level(foods[food])
        except KeyError:
            return self._increase_saturation_level(0)

    def _reduce_saturation_level(self, value):
        self.saturation_level -= value
        if self.saturation_level <= 0:
            self.saturation_level = 0
        return self.saturation_level

    def _increase_saturation_level(self, value):
        self.saturation_level += value
        if self.saturation_level >= 100:
            self.saturation_level = 100
        return self.saturation_level

    def _set_average_speed(self):
        if self.age <= 7:
            return 12
        elif 7 < self.age <= 10:
            return 9
        else:
            return 6

    def run(self, hours):
        time_h = self._set_average_speed() * hours
        if time_h <= 25:
            self._reduce_saturation_level(2)
        elif 25 < time_h <= 50:
            self._reduce_saturation_level(5)
        elif 50 < time_h <= 100:
            self._reduce_saturation_level(15)
        elif 100 < time_h <= 200:
            self._reduce_saturation_level(25)
        else:
            self._reduce_saturation_level(50)
        return f"Your cat ran {time_h} kilometers"

    def get_saturation_level(self):
        if self.saturation_level <= 0:
            return "Your cat is died :("
        return self.saturation_level

    def get_average_speed(self):
        return self.average_speed


class Cheetah(Cat):
    """
    * Inherit from class Cat

    * Redefine method eat from parent class it will receive product value
      if product eq gazelle use _increase_saturation_level from parent class with value 30
      if product eq rabbit use _increase_saturation_level from parent class with value 15

    * Redefine method _set_average_speed
      if age less or eq 5 return 90
      if age between 5 and 15(including) return 75
      if age grosser 15(not including) return 40
      ___________________________________
      Спадщина з класу Кіт

     * Перевизначення методу харчування з батьківського класу, воно отримає вартість продукту
       якщо продукт eq gazelle використовує _increase_saturation_level з батьківського класу зі значенням 30
       якщо кролик продукту eq використовують _increase_saturation_level з батьківського класу зі значенням 15

     * Перевизначити метод _set_average_speed
       якщо вік менший або еквівалент 5 повертається 90
       якщо вік між 5 і 15 (включаючи) поверне 75
       якщо вік зростає 15 (не враховуючи) повернення 40

    """

    def eat(self, food):
        foods = {
            'gazelle': 30,
            'rabbit': 15
        }
        try:
            return self._increase_saturation_level(foods[food])
        except KeyError:
            return self._increase_saturation_level(0)

    def _set_average_speed(self):

        if self.age <= 5:
            return 90
        elif 5 < self.age <= 15:
            return 75
        else:
            return 40


class Wall:
    """
    * Implement class Wall which receives such parameters: width and height

    * Implement method wall_square which return result of simple square formula of rectangle

    * Implement method number_of_rolls_of_wallpaper which receives such parameters: roll_width_m, roll_length_m
      (_m in the parameters name means meters) return number of rolls of wallpaper

      Example:
          count of lines in roll eq roll length in meters divide height of the wall (use rounding down)
          count of lines eq width of the wall divide roll width in meters
          number of rolls of wallpaper eq count of lines divide  count of lines in roll
    _________________________________________________________________
    * Стіна класу реалізації, яка отримує такі параметри: ширину та висоту

     * Реалізувати метод wall_square, який повертає результат простої квадратної формули прямокутника

     * Спосіб реалізації number_of_rolls_of_wallpaper, який отримує такі параметри: roll_width_m, roll_length_m
       (_m в назві параметрів означає метри) повернути кількість рулонів шпалер

       Приклад:
           кількість ліній в еквіваленті довжини рулону в метрах розділити висоту стіни (використовуйте округлення вниз)
           кількість ліній eq ширина стіни розділити ширину рулону в метрах
           кількість рулонів шпалер еквівалентна кількість ліній ділити кількість ліній у рулоні
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def wall_square(self):
        return self.width * self.height

    def number_of_rolls_of_wallpaper(self, roll_width_m, roll_length_m):
        return round(round(self.width / roll_width_m) / math.floor(roll_length_m / self.height))


class Roof:
    """
        * Implement class Roof which receives such parameters: width, height and roof_type

        * Implement method roof_square that returns square of the roof
          if roof_type eq "gable" the roof square if simple rectangle square formula multiplied 2
          if roof_type eq "single-pitch" the roof square if simple rectangle square formula
          if other roof_type raise ValueError like this "Sorry there is only two types of roofs"
________________________________________________________________________
Реалізуємо клас Дах, який отримує такі параметри: ширина, висота та тип даху

         * Реалізувати метод roof_square, який повертає квадрат даху
           якщо roof_type eq "франтон" квадрат даху, якщо проста формула прямокутника квадрат помножена на 2
           якщо roof_type eq "односхилий" квадрат даху, якщо проста формула прямокутника квадрат
           якщо інший тип даху підвищує ValueError, подібний до цього "Вибачте, що дах існує лише два типи"
    """

    def __init__(self, width, height, roof_type):
        self.width = width
        self.height = height
        self.roof_type = roof_type

    def roof_square(self):
        if self.roof_type == "gable":
            return self.width * self.height * 2
        elif self.roof_type == "single-pitch":
            return self.width * self.height
        else:
            raise ValueError("Sorry there is only two types of roofs")


class Window:
    """
       * Implement class Window which receives such parameters: width and height

       * Implement method window_square which return result of simple square formula of rectangle
       ______________________________________________________
       Клас реалізації Вікно, яке отримує такі параметри: ширину та висоту

        * Реалізувати метод window_square, який повертає результат простої квадратної формули прямокутника
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def window_square(self):
        return self.width * self.height


class Door:
    """
     * Implement class Door which receives such parameters: width and height
      add variables wood_price eq 10, metal_price eq 3

     * Implement method door_square which return result of simple square formula of rectangle

     * Implement method door_square which receives material value as a parameter
       if material eq wood return door_square multiplied on wood_price
       if material eq metal return door_square multiplied on metal_price
       if material value is another one (not metal or wood) raise ValueError "Sorry we don't have such material"

     *  Implement method update_wood_price which receives new_price value and updates your old price

     *  Implement method update_metal_price which receives new_price value and updates your old price
     ________________________________________________________________________________________
     Клас реалізації дверей, який приймає такі параметри: ширина і висота
       додати змінні wood_price eq 10, metal_price eq 3

      * Реалізуйте метод door_square, який повертає результат простої квадратної формули прямокутника

      * Реалізуйте метод door_square, який отримує матеріальну цінність як параметр
        якщо матеріал еквівалентної деревини повертається door_square помножений на wood_price
        якщо матеріал еквівалентний металевий зворотний двері_квадрату помножився на метал_ціна
        якщо матеріальна цінність є іншою (а не металом чи деревом), підвищити ValueError Вибачте у настакого матеріалу

         немає"

      * Реалізуйте метод update_wood_price, який отримує значення new_price та оновлює стару ціну

      * Реалізуйте метод update_metal_price, який отримує значення new_price та оновлює стару ціну

    """

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.price_wood = 10
        self.price_metal = 3

    def door_square(self):
        return self.width * self.height

    def door_price(self, material):
        if material == "wood":
            return self.door_square() * self.price_wood
        elif material == "metal":
            return self.door_square() * self.price_metal
        else:
            raise ValueError("Sorry we don't have such material")

    def update_wood_price(self, new_price):
        self.price_wood = new_price

    def update_metal_price(self, new_price):
        self.price_metal = new_price


class House:
    """
    !!!! DON'T WRITE NEW METHODS TO THIS CLASS EXCEPT FOR THOSE LISTED BELOW !!!

    * Add super private variable __walls and its value will be empty list
    * Add super private variable __windows and its value will be empty list
    * Add super private variable __roof and its value will be None
    * Add super private variable __door and its value will be None

    * Implement method create_wall which will create new wall using class Wall and add it to the __walls list
      it receives parameters width and height
      if width or height eq 0 raise ValueError "Value must be not 0"
      if user have more than 4 walls raise ValueError "Our house can not have more than 4 walls"

    * Implement method create_roof which will create new roof using class Roof and assign it to the __roof variable
      it receives parameters width, height and roof_type
      if width or height eq 0 raise ValueError "Value must be not 0"
      Check that we won't have another roof if we already have another one,
              otherwise raise ValueError "The house can not have two roofs"

    * Implement method create_window which will create new window using class Window and add it to the __windows list
      it receives parameters width and height
      if width or height eq 0 raise ValueError "Value must be not 0"

    * Implement method create_door which will create new door using class Door and assign it to the __door variable
      it receives parameters width and height
      if width or height eq 0 raise ValueError "Value must be not 0"
      Check that we won't have another door if we already have another one,
              otherwise raise ValueError "The house can not have two doors"

    * Implement method get_count_of_walls that returns count of walls

    * Implement method get_count_of_windows that returns count of windows

    * Implement method get_door_price that receives material value and returns price of the door

    * Implement method update_wood_price that receives new_wood_price and updates old one

    * Implement method update_metal_price that receives new_metal_price and updates old one

    * Implement method get_roof_square that returns the roof square

    * Implement method get_walls_square that returns sum of all walls square that we have

    * Implement method get_windows_square that returns sum of all windows square that we have

    * Implement method get_door_square that returns the square of the door

    * Implement method get_number_of_rolls_of_wallpapers that returns sum of the number of rolls of wallpapers
      needed for all our walls
      it receives roll_width_m, roll_length_m parameters
      Check if roll_width_m or roll_length_m eq 0 raise ValueError "Sorry length must be not 0"

    * Implement method get_room_square that returns the square of our room
      (from walls_square divide windows and door square)
________________________________________________________________________________
!!!! НЕ ЗАПИСАЙТЕ НОВІ МЕТОДИ ДО ЦЬОГО КЛАСУ, ОКРЕМИ ДЛЯ ЦІХ СПИСОК НИЖЕ !!!

    * Додати супер приватну змінну __walls, і її значення буде порожнім списком
    * Додати супер приватну змінну __windows, і її значення буде порожнім списком
    * Додати супер приватну змінну __roof і її значення буде None
    * Додати супер приватну змінну __door, і її значення буде None

    * Реалізувати метод create_wall, який створить нову стіну за допомогою класу Wall та додасть її до списку __walls
      він отримує параметри ширини та висоти
      якщо ширина або висота eq 0 підвищують ValueError "Значення не повинно бути 0"
      якщо у користувача більше 4 стін піднімають ValueError "У нашому будинку не може бути більше 4 стін"

    * Реалізувати метод create_roof, який створить новий дах за допомогою класу Roof та призначить його змінної __roof
      він отримує параметри ширина, висота та тип даху
      якщо ширина або висота eq 0 підвищують ValueError "Значення не повинно бути 0"
      Перевірте, чи не буде у нас іншого даху, якщо у нас вже є інший,
              інакше підняти ValueError "У будинку не може бути двох дахів"

    * Реалізує метод create_window, який створить нове вікно за допомог класу Window та додасть його до списку __windows
      він отримує параметри ширини та висоти
      якщо ширина або висота eq 0 підвищують ValueError "Значення не повинно бути 0"

    * Реалізувати метод create_door, який створить нові двері за допомогою класу Door та призначить її змінної __door
      він отримує параметри ширини та висоти
      якщо ширина або висота eq 0 підвищують ValueError "Значення не повинно бути 0"
      Переконайтесь, що у нас не буде іншої двері, якщо у нас вже є інша,
              інакше підняти ValueError "У будинку не може бути двох дверей"

    * Метод реалізації get_count_of_walls, який повертає кількість стін

    * Метод реалізації get_count_of_windows, який повертає кількість вікон

    * Метод реалізації get_door_price, який отримує матеріальну цінність і повертає ціну дверей

    * Реалізувати метод update_wood_price, який отримує new_wood_price та оновлює старий

    * Реалізувати метод update_metal_price, який отримує new_metal_price та оновлює старий

    * Метод реалізації get_roof_square, який повертає квадрат даху

    * Метод реалізації get_walls_square, який повертає суму всіх квадратних стін у нас

    * Метод реалізації get_windows_square, який повертає суму всіх вікон квадратних у нас

    * Метод реалізації get_door_square, який повертає квадрат дверей

    * Спосіб реалізації get_number_of_rolls_of_wallpapers, який повертає суму кількості рулонів шпалер
      необхідні для всіх наших стін
      він отримує параметри roll_width_m, roll_length_m
      Перевірте, чи roll_width_m або roll_length_m eq 0 підвищити ValueError "Вибачте, довжина не повинна бути 0"

    * Метод реалізації get_room_square, який повертає площу нашої кімнати
      (від стін-квадратів розділіть вікна та двері)
    """

    def __init__(self):
        self.__walls = []
        self.__windows = []
        self.__door = None
        self.__roof = None

    def create_wall(self, width, height):
        if width == 0 or height == 0:
            raise ValueError("Value must be not 0")
        else:
            if len(self.__walls) >= 4:
                raise ValueError("Our house can not have more than 4 walls")
            else:
                self.__walls.append(Wall(width, height))

    def create_roof(self, width, height, roof_type):
        if width == 0 or height == 0:
            raise ValueError("Value must be not 0")
        if self.__roof:
            raise ValueError("The house can not have two roofs")
        self.__roof = Roof(width, height, roof_type)

    def create_window(self, width, height):
        if width == 0 or height == 0:
            raise ValueError("Value must be not 0")
        else:
            self.__windows.append(Window(width, height))

    def create_door(self, width, height):
        if width == 0 or height == 0:
            raise ValueError("Value must be not 0")
        if self.__door:
            raise ValueError("The house can not have two doors")
        self.__door = Door(width, height)

    def get_count_of_walls(self):
        return len(self.__walls)

    def get_count_of_windows(self):
        return len(self.__windows)

    def get_door_price(self, material):
        return self.__door.door_price(material)

    def update_wood_price(self, new_price):
        return self.__door.update_wood_price(new_price)

    def update_metal_price(self, new_price):
        return self.__door.update_metal_price(new_price)

    def get_roof_square(self):
        return self.__roof.roof_square()

    def get_walls_square(self):
        return sum(i.wall_square() for i in self.__walls)

    def get_windows_square(self):
        return sum(i.window_square() for i in self.__windows)

    def get_door_square(self):
        return self.__door.door_square()

    def get_number_of_rolls_of_wallpapers(self, roll_width_m, roll_length_m):
        if roll_width_m == 0 or roll_length_m == 0:
            raise ValueError("Sorry length must be not 0")
        else:
            return sum(i.number_of_rolls_of_wallpaper(roll_width_m, roll_length_m) for i in self.__walls)

    """number_of_rolls_of_wallpaper(self, roll_width_m, roll_length_m):
        return round(round(self.width / roll_width_m) / math.floor(roll_length_m / self.height))
        Спосіб реалізації get_number_of_rolls_of_wallpapers, який повертає суму кількості рулонів шпалер
      необхідні для всіх наших стін
      він отримує параметри roll_width_m, roll_length_m
      Перевірте, чи roll_width_m або roll_length_m eq 0 підвищити ValueError "Вибачте, довжина не повинна бути 0"""

    def get_room_square(self):
        return int(self.get_walls_square() - self.get_windows_square() - self.get_door_square())
