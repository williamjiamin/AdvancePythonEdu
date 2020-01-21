import math


class Soup:
    def __init__(self, ingredients, soup_radius):
        self.ingredients = ingredients
        self.soup_radius = soup_radius

    def __repr__(self):
        return f'soup which include({self.ingredients})'

    def area(self):
        return self._circle_area(self.soup_radius)

    @staticmethod
    def _circle_area(r):
        return r ** 2 * math.pi

    @classmethod
    def makeTouFuSoup(cls):
        return cls(['大白菜', '肉', '豆腐'])


# This is a class method
# print(Soup.makeTouFuSoup())

# This is a instance method
# print(Soup(['大白菜', '肉', '豆腐']))

# This is a static method
# print(Soup(['肉'],3).area())
print(Soup._circle_area(3))
