class Flower:
    def __init__(self, name, requirement):
        self.name = name
        self.requirement = requirement
        self.is_happy = False

    def water(self, water):
        if water >= self.requirement:
            self.is_happy = True

        else:
            self.is_happy = False
            return f"{self.name} is not happy"

    def status(self):
        if self.is_happy == True:
            return f"{self.name} is happy"
        else:
            return f"{self.name} is not happy"


flower = Flower("Lilly", 100)
flower.water(50)
print(flower.status())
flower.water(60)
print(flower.status())
flower.water(100)
print(flower.status())
