import random


class Customer:

   @classmethod
   def generate_customer(cls, probability_of_arrival, arrival_time):
      if probability_of_arrival > random.random():
         return Customer(arrival_time)

      # Customer did not arrive this clock tick
      return None


   def __init__(self, arrival_time):
      """ arrival_time represents which clock-tick this Customer arrived on """
      self._arrival_time = arrival_time
      self._transaction_time = random.randint(1, 3)

   @property
   def arrival_time(self):
      return self._arrival_time

   @property
   def transaction_time(self):
      return self._transaction_time

   def serve(self):
      """ Serve the customer for one unit of time. """
      self._transaction_time -= 1