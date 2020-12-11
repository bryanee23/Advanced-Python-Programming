from Tower import Tower
from Plane import Plane


class TowerSimulator:
   def __init__(self, length, odds_to_takeoff_arrival, odds_to_land_arrival):
      self._length = length
      self._odds_to_takeoff_arrival = odds_to_takeoff_arrival
      self._odds_to_land_arrival = odds_to_land_arrival
      self._Tower = Tower()
      self._Plane = Plane()




   def run_simulation(self):
      """ The following loop controls our entire simulation
      Each iteration represents a single clock tick (i.e. a minute) """

      #generates planes and places them into queues
      for i in range(self._length):
         self._Plane.generate_Plane(i, self._odds_to_takeoff_arrival, self._odds_to_land_arrival)


      self._Tower.serve_Plane(i)

      print(self._Tower)
      print(self._Tower2)