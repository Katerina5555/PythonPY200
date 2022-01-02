import random
import re
class Date:
    def __init__(self, day_: int, month_: int, year_: int):
        self.day_ = self.__check_day(day_)
        self.month_ = self.__check_month(month_)
        self.year_ = self.__check_year(year_)

    @staticmethod
    def __check_day(day_: int):
        if not isinstance(day_, int):
            raise TypeError
        if 0 >= day_ > 31:
            raise ValueError
        return "{0:0=2d}".format(day_)

    @staticmethod
    def __check_month(month_: int):
        if not isinstance(month_, int):
            raise TypeError
        if 0 >= month_ > 12:
            raise ValueError
        return "{0:0=2d}".format(month_)

    @staticmethod
    def __check_year(year_: int):
        if not isinstance(year_, int):
            raise TypeError
        return "{0:0=4d}".format(year_)

    def __str__(self) -> str:
        return f"{self.day_}/{self.month_}/{self.year_}"


if __name__ == "__main__":
    date = Date(1, 2, 991)
    print(date.__dict__)
    print(date)