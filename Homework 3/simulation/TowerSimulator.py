from Tower import Tower
from Plane import Plane
import random


class TowerSimulator:
   def __init__(self, length, odds_to_land_arrival, odds_to_takeoff_arrival):
      self._length = length
      self._odds_to_land_arrival = odds_to_land_arrival
      self._odds_to_takeoff_arrival = odds_to_takeoff_arrival
      self._Tower = Tower()

   def run_simulation(self):
      """ The following loop controls our entire simulation
      Each iteration represents a single clock tick (i.e. a minute) """
      for i in range(self._length):

         random_num = random.random()
         # new_plane = None
         if random_num > self._odds_to_takeoff_arrival and random_num > self._odds_to_land_arrival:
            pass

         else:
            if random_num < self._odds_to_land_arrival:
               status = "to_land"
               new_plane = Plane.generate_Plane(status,i)
               self._Tower.add_to_PriorityQ(new_plane)

            if random_num < self._odds_to_takeoff_arrival:
               status = "to_takeoff"
               new_plane = Plane.generate_Plane(status,i)
               self._Tower.add_to_Q(new_plane)

         self._Tower.serve_Plane(i)
         # self._Tower2.serve_Plane(i)

      print(self._Tower)
