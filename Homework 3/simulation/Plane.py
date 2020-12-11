import random


class Plane:

   @classmethod
   def generate_Plane(cls, probability_of_arrival, arrival_time):
      if probability_of_arrival > random.random():
         return Plane(arrival_time)

      # Plane did not arrive this clock tick
      return None


   def __init__(self, arrival_time):
      """ arrival_time represents which clock-tick this Plane arrived on """
      self._arrival_time = arrival_time
      self._transaction_time = random.randint(1, 3)

   @property
   def arrival_time(self):
      return self._arrival_time

   @property
   def transaction_time(self):
      return self._transaction_time

   def serve(self):
      """ Serve the Plane for one unit of time. """
      self._transaction_time -= 1