class Man():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def inCar(self):
        return "In car"

    def atHome(self):
        return "At home"


class Car():
    def __init__(self, color, brand, price):
        self.color = color
        self.brand = brand
        self.price = price

    def stop(self):
        return "Stop"

    def drive(self):
        return "Drive"


if __name__ == "__main__":
    car = Car("blue", "BMW", 5000)
    driver = Man("Bob", 30)
    n = driver.atHome()
    # n = driver.inCar()
    print("У " + driver.name + " (" + str(driver.age),
          " лет) есть " + car.brand + " (" + car.color,
          " цвета). Она стоит " + str(car.price) + "   $ ")
    if n == driver.atHome():
        print("Сейчас она " + car.stop())
    if n == driver.inCar():
        print("Сейчас она " + car.drive())
