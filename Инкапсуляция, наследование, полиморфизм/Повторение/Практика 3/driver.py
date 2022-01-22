class Driver:
    def __init__(self, name, experience: int):
        self.name = name
        self.experience = experience

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}), {self.__class__.__name__}({self.experience})"

    def __str__(self):
        return f"Водитель {self.name}, стаж вождения {self.experience} лет"

    def experience(self, experience: int):
        return self.experience


if __name__ == '__main__':


    driver_vasya = Driver("Василий", 5)
    driver_ivan = Driver("Иван", 11)

    print(driver_vasya)
    print(driver_ivan)