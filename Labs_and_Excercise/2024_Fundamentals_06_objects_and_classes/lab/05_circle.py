class Circle:

    __pi = 3.14

    def __init__(self, diameter):
        self.diameter = diameter

    def calculate_circumference(self):
        circumference = 2 * self.__pi * self.diameter / 2
        return circumference

    def calculate_area(self):
        area = self.__pi * (self.diameter / 2) ** 2
        return area

    def calculate_area_of_sector(self, angle):
        area_sector = (angle / 360) * self.__pi * (self.diameter / 2) ** 2
        return area_sector


circle = Circle(5)
angle = 355

print(f"{circle.calculate_circumference():.2f}")
print(f"{circle.calculate_area():.2f}")
print(f"{circle.calculate_area_of_sector(angle):.2f}")
