from Pet import Pet

class Dog(Pet):
    def __init__(self, name, age, breed):
        self._breed = breed
        Pet.__init__(self, name, age)

    def fetch(self):
      print("{} runs and fetches the ball".format(self.name))

    def __str__(self):
      return'yyyooo dog'

    def eat(self):
      return f'{self.name} mofking dog is still eating man'

    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, breed):
        self._breed = breed

