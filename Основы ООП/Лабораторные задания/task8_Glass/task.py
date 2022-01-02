from typing import Union

class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        self.capacity_volume = None
        self.occupied_volume = None
        self.__capacity_volume(capacity_volume)
        self.__occupied_volume(occupied_volume)

    def __capacity_volume(self, capacity_volume: Union[int, float]):
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError
        if capacity_volume <= 0:
            raise ValueError
        self.capacity_volume = capacity_volume

    def __occupied_volume(self, occupied_volume: Union[int, float]):
        if not isinstance(occupied_volume, (int, float)):
            raise TypeError
        if occupied_volume < 0:
            raise ValueError
        self.occupied_volume = occupied_volume

    def add_water(self, value: Union[int, float]):
        if not isinstance(value, (int, float)):
            raise TypeError
        if value <= 0:
            raise ValueError
        self.occupied_volume += value

    def remove_water(self, value: Union[int, float]):
        if not isinstance(value, (int, float)):
            raise TypeError
        if value < 0:
            raise ValueError
        value_after_all = self.occupied_volume-value
        if value_after_all < 0:
            raise ValueError("В стакане недостаточно воды для данной операции")
        self.occupied_volume -= value


if __name__ == "__main__":

    glass = Glass(200, 100)  # экземпляр класса
    print(glass.capacity_volume, glass.occupied_volume)

    glass.add_water(50)
    print(glass.capacity_volume, glass.occupied_volume)

    glass.remove_water(200)
    print(glass.capacity_volume, glass.occupied_volume)




