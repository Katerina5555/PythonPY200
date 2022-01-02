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
        return day_

    @staticmethod
    def __check_month(month_: int):
        if not isinstance(month_, int):
            raise TypeError
        if 0 >= month_ > 12:
            raise ValueError
        return month_

    @staticmethod
    def __check_year(year_: int):
        if not isinstance(year_, int):
            raise TypeError
        return year_

    def __repr__(self):
        print(f"Date ({self.day_},{self.month_},{self.year_})")

    def __str__(self) -> str:
        day_ = "{0:0=2d}".format(self.day_)
        month_ = "{0:0=2d}".format(self.month_)
        year_ = "{0:0=4d}".format(self.year_)

        return f"{day_}/{month_}/{year_}"


if __name__ == "__main__":
    date = Date(1, 2, 991)
    print(date.__dict__)
    print(date)
