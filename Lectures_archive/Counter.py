class Counter:
  @property
  def value(self):
    return self._value

  @value.setter
  def value(self, val):
    self._value = val

  def increment(self, amount = 1):
    self._value = amount