import random

class Customer:
    def __init__(self, arrival_time):
      """arrival time represents which clock-tick this customer has"""
      self._arrival_time = arrival_time
      self._transaction_time = random.randint(1,3)

    @classmethod
    def generate_customer(cls, probability_of_arrival, arrival_time):
      if probability_of_arrival > random.random():
        return Customer(arrival_time)

      return None

    @property
    def arrival_time(self):
      return self._arrival_time

    @property
    def transaction_time(self):
      return self._transaction_time

    def serve(self):
      self._transaction_time -= 1
