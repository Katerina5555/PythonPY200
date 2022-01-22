import time
import uuid
from driver import Driver

class DriverTypeError(Exception):
    pass

class EngineIsNotRunning(Exception):
    pass

class DriverNotFoundError(Exception):
    pass

class Car:
    brand = None   # публичный, на случай продажи компании
    _max_speed = 180    #защищенный
    __created_car = 0   #приватный

    def __init__(self, engine_type=None, body_type=None, gear_type=None, drive_type=None,
                 configuration=None, color=None):
        """создание атрибутов класса"""
        self.__body_type = body_type
        self._engine_type = engine_type
        self._gear_type = gear_type
        self._drive_type = drive_type
        self.configuration = configuration
        self.color = color

        self.__vin_number = uuid.uuid4()
        self.__created_time = time.time()
        self.__mileage = 0

        self.__status_engine = False
        self.__driver = None

    def __new__(cls, *args, **kwargs):
        cls.__append_new_car_counter()
        print(f"Создано {cls.__created_car} класса {cls.__name__}")
        return super().__new__(cls)

    #метод класса
    @classmethod
    def change_brand(cls, new_brand):
        cls.brand = new_brand

    @classmethod
    def set_max_speed(cls, max_speed):
        if not isinstance(max_speed, (int, float)):
            raise TypeError
        cls._max_speed = max_speed

    @classmethod
    def __append_new_car_counter(cls):
        cls.__created_car += 1


    def start_engine(self):
        self.__status_engine = True

    def __is_ready_to_move(self):

        if not self.__status_engine:
            raise EngineIsNotRunning("Двигатель не запущен")

        if self.__driver is None:
            raise DriverNotFoundError("Водитель не найден")
        return True

    def time_to_stop(self, start_mile):

        """расчет максимального времени в пути для конкретного водителя"""
        max_on_the_way = int((self.max_time_on_the_way() / 60) * self.speed_limit())
        """предупреждение о предстоящей остановке и инфо после"""
        if (self.__mileage - start_mile) % max_on_the_way - (max_on_the_way // 4 * 3) == 0 and self.__mileage != 0:     #поставлено из длины пути. каждый километр повторять - отвлекает
                b = max_on_the_way - (self.__mileage -start_mile) % max_on_the_way
                print(f'Через {b} км машина вынужденно остановится. '
                f'Необходимо найти место для остановки')

        elif (self.__mileage - start_mile) % max_on_the_way == 0 and self.__mileage != start_mile:
                a = 2
                print(f'Вам необходимо отдохнуть. '
                    f'Вы можете продолжить движение через {a} минут(ы). '
                      f'Согласно регламента Вы можете двигаться без остановки {self.max_time_on_the_way()} минут, '
                      f'при текущей скорости ({self.speed_limit()} км/ч) - это {max_on_the_way} км.')
                time.sleep(a)


    def move(self, distance):
        try:
            start_mile = self.get_mileage()
            if self.__is_ready_to_move():

                for i in range(distance):
                    self.time_to_stop(start_mile)

                    print(f"Машина проехала {start_mile + i + 1} км")
                    self.__mileage += 1
                    time.sleep(0.3)

            print("Машина проехала указанный путь")
            print(f"Вы начали свой путь с пробегом {start_mile} км")
        except(EngineIsNotRunning, DriverNotFoundError) as e:
            print(f"Машина не может ехать, т.к. {e}")

    def max_time_on_the_way(self) -> int:
        """вспомогательный расчет максимального времени в пути для водителя"""
        if self.driver.experience < 10:
            max_no_sleep = 5    # установлено 10 минут, чтобы долго не жждать результата

        else:
            max_no_sleep = 9

        return max_no_sleep

    def speed_limit(self) -> int:
        """вспомогательный расчет максимальной скорости для водителя"""
        if self.driver.experience < 10:
            max_speed = 100
        else:
            max_speed = self._max_speed
        return max_speed

    #  вывод и добалвение через геттер и сеттер
    # def set_driver(self, driver: Driver):
    #     if not isinstance(driver, Driver):
    #         raise DriverTypeError(f"Ожидается тип {Driver}, "
    #                               f"получен {type(driver)}")
    #     self.__driver = driver
    #
    # def get_driver(self):
    #     return self.__driver

    """получение и установка через свойства. вместо геттера и сеттера"""
    @property
    def driver(self):
        return self.__driver

    @driver.setter
    def driver(self, driver: Driver):

        if not isinstance(driver, Driver):
            raise DriverTypeError(f"Ожидается тип {Driver}, "
                              f"получен {type(driver)}")
        self.__driver = driver

    def get_mileage(self):
        return self.__mileage

    def _set_mileage(self, mileage):
        if not isinstance(mileage, (int, float)):
            raise TypeError(f"Ожидается тип данных {int} или {float}, получен {type(mileage)}")
        self.__mileage = mileage

    @staticmethod
    def miles_to_km(mile_count):
        return mile_count * 1.609




class Honda(Car):
    brand = "Honda"
    __created_car = 0
    def __init__(self, engine_type, body_type, gear_type, drive_type, configuration, color):
        super().__init__()



if __name__ == '__main__':
    # print(Car().miles_to_km(40))
    #
    #
    car = Car("бензин", "седан", "автомат", "полный", "люкс", "белый")
    # car_2 = Car("бензин", "седан", "автомат", "полный", "люкс", "черный")
    # honda = Honda("бензин", "седан", "автомат", "полный", "люкс", "белый")
    # honda_2 = Honda("бензин", "седан", "автомат", "полный", "люкс", "черный")


    # print(car.brand)
    # print(car_2.brand)
    # Car.change_brand("Mitsubishi")
    # print(car.brand)
    # print(car_2.brand)
    #
    # print(car._max_speed)
    # print(car_2._max_speed)
    # Car.set_max_speed(200)
    # print(car._max_speed)
    # print(car_2._max_speed)
    #
    #блок работы с защищенными методами
    car.start_engine()
    car.driver = Driver("Иван", 10)
    print(car.driver)

    # блок методов экземпляра

    car._set_mileage(5)
    car.move(30)
    print(car.get_mileage())
    # car.move()
    # print(car)
    # print(car.get_mileage())

    # car._set_mileage(30)
    # print(car.get_mileage())
    # car.move()
    # print(car.get_mileage())
    # car._set_mileage(10)

    #блок сеттеров
    # для чистого геттера и сеттера
    # car.set_driver(Driver("Иван"))
    # print(car.get_driver())





