class Device:
    def __init__(self, display, battery, brand, model_name):
        self._display = display  # display size(in inches)
        self.battery = battery  # battery capacity(mAh)
        self.brand = brand  # brand of device
        self.model_name = model_name  # modelname of device

    def is_portable(self):
        pass


class Laptop(Device):
    def __init__(self, display, battery, brand, model_name, cpu_power):
        super().__init__(display, battery, brand, model_name)
        self.cpu_power = cpu_power

    def is_portable(self):
        print("Laptops are pretty portable, but something feels off")


class Phone(Device):
    def __init__(self, display, battery, brand, model_name, antutu_score):
        super().__init__(display, battery, brand, model_name)
        self.antutu_score = antutu_score

    def is_portable(self):
        print(
            "Oh yeah, phones are REALLY portable compared to a laptop. Imagine u had 15 inch lol"
        )


my_laptop = Laptop(
    13, 19000, "Apple", "MacBook", 3
)  # i wish i ACTUALLY had macbook. even m1
my_laptop.is_portable()
my_phone = Phone(6.1, 4000, "Apple", "16e", 1450000)
my_phone.is_portable()
