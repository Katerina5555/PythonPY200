class Glass:
    def __init__(self, capacity_volume: int, occupied_volume: int):
        self.capacity_volume = capacity_volume
        self.occupied_volume = occupied_volume

    def __print_capacity(self):
        '''
        изолируем эту часть от пользователя
        :return:
        '''
        print(self.capacity_volume)


if __name__ == "__main__":
    glass = Glass(200, 0)
    print(glass.__dict__)       # пользовательские атрибуты
    print(dir(glass))    # возвращает все возможные атрибуты
