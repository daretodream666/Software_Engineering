from datetime import datetime, time


class ShabbatShalomException(Exception):
    pass


def drive_car():
    try:
        today = datetime.now().weekday()
        if today == 5:
            raise ShabbatShalomException
        else:
            return "vroom vroom"
    except ShabbatShalomException:
        return "Oy vey! You cant do that on Shabbat"


def cook_lunch():
    try:
        today = datetime.now().weekday()
        if today == 5:
            raise ShabbatShalomException
        else:
            return "yay u made delicious shakshuka"
    except ShabbatShalomException:
        return "Oy vey! You cant do that on Shabbat"


print(cook_lunch())
print(drive_car())
