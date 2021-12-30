from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):

        self.capacity_volume = self.__check_capacity_volume(capacity_volume)      #  TODO инициализировать объект "Стакан"

        self.occupied_volume = self.__check_occupied_volume(occupied_volume)

    @staticmethod
    def __check_capacity_volume(value) -> Union[int, float]:
        if not isinstance(value, (int, float)):
            raise TypeError
        if value <= 0:
            raise ValueError
        return value

    @staticmethod
    def __check_occupied_volume(value) -> Union[int, float]:
        if not isinstance(value, (int, float)):
            raise TypeError
        if value < 0:
            raise ValueError
        return value

if __name__ == "__main__":
    glass_1 = Glass(300, 200)    # TODO инициализировать два объекта типа Glass
    print((glass_1.__dict__))
    glass_2 = Glass(200, 100)    # попытка ввести строковое значение или отрицательного

    # TODO попробовать инициализировать не корректные объекты
