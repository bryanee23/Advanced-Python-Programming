import random


class Plane:

   @classmethod
   def generate_Plane(cls, status, arrival_time):
      return Plane(status, arrival_time)


   def __init__(self, status, arrival_time):
      """ arrival_time represents which clock-tick this Plane arrived on """
      self._status = status
      self._arrival_time = arrival_time
      self._transaction_time = random.randint(1, 3)
      self._fuel = random.randint(5, 15)

   @property
   def status(self):
      return self._status

   @property
   def arrival_time(self):
      return self._arrival_time

   @property
   def transaction_time(self):
      return self._transaction_time

   @property
   def fuel(self):
      return self._fuel

   def serve(self):
      """ Serve the Plane for one unit of time. """
      self._transaction_time -= 1

   def minus_fuel(self):
      """ Serve the Plane for one unit of time. """
      self._fuel -= 1