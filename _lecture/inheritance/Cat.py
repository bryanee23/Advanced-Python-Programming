from Pet import Pet

class Cat(Pet):
    def __init__(self, name, age):
      Pet.__init__(self, name, age)

    def sleep(self):
      print("{} continues to sleep".format(self.name))