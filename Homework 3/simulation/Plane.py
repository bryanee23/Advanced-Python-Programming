import random
from Tower import Tower

class Plane:
   def __init__(self, status=None, arrival_time=None):
      """ arrival_time represents which clock-tick this Plane arrived on """
      self._status = status
      self._arrival_time = arrival_time
      self._transaction_time = random.randint(1, 3)
      self._fuel = random.randint(5, 15)
      self._Tower = Tower()


   def generate_Plane(self, arrival_time, odds_to_takeoff_arrival, odds_to_land_arrival, status=None):
      """
      :param arraival_time: clock_tick (i)
      :param odds_to_takeoff_arrival: probability of a plane arriving to takeoff
      :param odds_to_land_arrival: probability of a plane needing to land
      :praam status: provides
      """

      random_gen = random.random()

      if  (random_gen > odds_to_takeoff_arrival) and (random_gen > odds_to_land_arrival):
         pass

      else:
         if  random_gen < odds_to_land_arrival:
            status = "to_land"
            new_plane = Plane(status,arrival_time)
            self._Tower.add_Plane_to_priorityQ(new_plane)

         if  random_gen < odds_to_takeoff_arrival:
            status = "to_takeoff"
            new_plane = Plane(status,arrival_time)
            self._Tower.add_Plane_to_queue(new_plane)





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