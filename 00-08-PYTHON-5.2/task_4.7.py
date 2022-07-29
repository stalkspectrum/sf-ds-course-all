#!/usr/bin/python3

def check_date(day, month, year):
    def is_leap():
        if year % 400 == 0:
            return True
        elif year % 100 == 0:
            return False
        elif year % 4 == 0:
            return True
        else:
            return False

    if (type(day), type(month), type(year)) != (int, int, int):
        return False
    if year not in range(1900, 2023):
        return False
    if month not in range(1, 13):
        return False
    if day not in range(1, 32):
        return False
    if month in [4, 6, 9, 11] and day not in range(1, 31):
        return False
    if month == 2:
        if is_leap():
            if day not in range(1, 30):
                return False
        else:
            if day not in range(1, 29):
                return False
    return True
