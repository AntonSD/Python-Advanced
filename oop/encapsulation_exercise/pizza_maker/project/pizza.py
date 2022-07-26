from project.topping import Topping
from project.dough import Dough


class Pizza:
    def __init__(self, name, dough, topping_capacity):
        self.__name = name
        self.__dough = dough
        self.__topping_capacity = topping_capacity
        self.toppings = {}

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("The name cannot be an empty string")
        self.__name = value

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, value):
        if value is None:
            raise ValueError("You should add dough to the pizza")
        self.__dough = value

    @property
    def topping_capacity(self):
        return self.__topping_capacity

    @topping_capacity.setter
    def topping_capacity(self, value):
        if value <= 0:
            raise ValueError("The topping's capacity cannot be less or equal to zero")
        self.__topping_capacity = value

    def add_topping(self, topping: Topping):
        if len(self.toppings) == self.__topping_capacity:
            raise ValueError("Not enough space for another topping")
        if topping.topping_type in self.toppings:
            self.toppings[topping.topping_type] += topping.weight
        else:
            self.toppings[topping.topping_type] = topping.weight

    def calculate_total_weight(self):
        return self.dough.weight + sum(self.toppings.values())

