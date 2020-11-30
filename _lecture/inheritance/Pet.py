class Pet:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def eat(self):
        return f'{self.name} thanks you for el meal'

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
      self._age = age