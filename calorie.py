from temperature import Temperature

class Calorie:
    """ Represent amount of calories calculated with
       BMR = 18*weight + 6.25*height - 5*age + 5 - 18*temperature
       """

    def __init__(self, weight, height, age, temperature):
        self.temperature = temperature
        self.age = age
        self.height = height
        self.weight = weight


    def calculate(self):
        result = 18 * self.weight + 6.25 * self.height - 5 * self.age + 5 - 18 * self.temperature
        return result

if __name__ == "__main__":
    temperature = Temperature(country="italy", city="rome").get()
    calorie = Calorie(weight=70, height=175, age=32, temperature=temperature)
    print(calorie.calculate())


